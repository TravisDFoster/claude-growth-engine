#!/usr/bin/env python3
"""Bulk rename/retag uploaded Canva assets from the curation sheet.

Reads the Canva Catalog — Templates & Assets spreadsheet's Assets tab, finds rows
where Canonical=Y and Approved=Y, and PATCHes each asset's name + tags via the
Canva Connect REST API. This is the *only* path that can rename uploads — the
MCP has no rename tool.

Auth: requires a Canva Connect API access token in env var CANVA_CONNECT_TOKEN.
   - Create an integration: https://www.canva.com/developers/integrations
   - Grant scope: asset:write (and asset:read if you want pre-PATCH GETs)
   - Export the token: export CANVA_CONNECT_TOKEN=...

Usage:
   python3 rename_canva_assets.py            # dry-run (prints diffs)
   python3 rename_canva_assets.py --apply    # live PATCH

Endpoint: PATCH https://api.canva.com/rest/v1/assets/{assetId}
   Body: {"name": "...", "tags": ["..."]}
   Docs: https://www.canva.dev/docs/connect/api-reference/assets/update-asset/
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

SPREADSHEET_ID = "1uUFXBnyDE0_3oecC1SRgi24HfstoKVfnB86Am5RfLss"
ASSETS_RANGE = "Assets!A2:I"
API_BASE = "https://api.canva.com/rest/v1"


def gws_values_get(range_: str) -> list[list[str]]:
    params = json.dumps({"spreadsheetId": SPREADSHEET_ID, "range": range_})
    result = subprocess.run(
        ["gws", "sheets", "spreadsheets", "values", "get", "--params", params],
        capture_output=True,
        text=True,
        check=True,
    )
    return json.loads(result.stdout).get("values", [])


def cell(row: list[str], idx: int) -> str:
    return row[idx].strip() if idx < len(row) and row[idx] is not None else ""


def is_yes(value: str) -> bool:
    return value.strip().lower() in {"y", "yes", "true", "1", "approved"}


def patch_asset(token: str, asset_id: str, payload: dict[str, Any]) -> tuple[int, str]:
    req = urllib.request.Request(
        f"{API_BASE}/assets/{asset_id}",
        data=json.dumps(payload).encode("utf-8"),
        method="PATCH",
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(req) as resp:
            return resp.status, resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        return e.code, e.read().decode("utf-8", errors="replace")


def build_payloads() -> list[dict[str, Any]]:
    rows = gws_values_get(ASSETS_RANGE)
    payloads: list[dict[str, Any]] = []
    for row in rows:
        asset_id = cell(row, 1)
        if not asset_id:
            continue
        if not (is_yes(cell(row, 6)) and is_yes(cell(row, 7))):
            continue
        new_name = cell(row, 0)
        tags = [t.strip() for t in cell(row, 4).split(",") if t.strip()]
        payload: dict[str, Any] = {}
        if new_name:
            payload["name"] = new_name
        if tags:
            payload["tags"] = tags
        if not payload:
            continue
        payloads.append({"asset_id": asset_id, "payload": payload, "subject": cell(row, 3)})
    return payloads


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true", help="Actually PATCH (default: dry-run)")
    args = parser.parse_args()

    token = os.environ.get("CANVA_CONNECT_TOKEN", "").strip()
    if args.apply and not token:
        print("ERROR: CANVA_CONNECT_TOKEN is not set. Mint a token at https://www.canva.com/developers/integrations and export it.", file=sys.stderr)
        sys.exit(2)

    payloads = build_payloads()
    if not payloads:
        print("No approved+canonical assets in the sheet yet. Nothing to PATCH.")
        return

    print(f"{len(payloads)} approved+canonical asset(s) ready to PATCH.")
    if not args.apply:
        for p in payloads[:10]:
            print(f"  {p['asset_id']}  name='{p['payload'].get('name','')}'  tags={p['payload'].get('tags', [])}")
        if len(payloads) > 10:
            print(f"  … (+{len(payloads) - 10} more)")
        print("\nDry-run only. Re-run with --apply to PATCH live.")
        return

    ok = 0
    fail = 0
    for p in payloads:
        status, body = patch_asset(token, p["asset_id"], p["payload"])
        if 200 <= status < 300:
            ok += 1
            print(f"  ✓ {p['asset_id']}  → name='{p['payload'].get('name','')}'")
        else:
            fail += 1
            print(f"  ✗ {p['asset_id']}  HTTP {status}: {body[:200]}")
    print(f"\nDone: {ok} updated, {fail} failed.")


if __name__ == "__main__":
    main()
