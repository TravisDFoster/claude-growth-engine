#!/usr/bin/env python3
"""Refresh canonical-{templates,assets}.json from the Canva curation sheet.

Source: Google Sheet "Canva Catalog — Templates & Assets" in Drive's Claude-Uploads.
Output:
  ../_cache/canonical-templates.json — {use_case_or_id -> [{template_id, use_case, ...}]}
  ../_cache/canonical-assets.json    — {asset_id -> {category, subject, tags, ...}}

Re-runnable. Run after Furqan/Travis update the curation sheet.
"""

from __future__ import annotations

import json
import subprocess
from collections import defaultdict
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
SKILL_DIR = SCRIPT_DIR.parent
CACHE_DIR = SKILL_DIR / "_cache"

SPREADSHEET_ID = "1uUFXBnyDE0_3oecC1SRgi24HfstoKVfnB86Am5RfLss"
TEMPLATES_RANGE = "Templates!A2:L"
ASSETS_RANGE = "Assets!A2:I"


def gws_values_get(range_: str) -> list[list[str]]:
    """Read a sheet range via the gws CLI. Returns rows; right-pads missing trailing cells with empty strings."""
    params = json.dumps({"spreadsheetId": SPREADSHEET_ID, "range": range_})
    result = subprocess.run(
        ["gws", "sheets", "spreadsheets", "values", "get", "--params", params],
        capture_output=True,
        text=True,
        check=True,
    )
    # gws prints a backend banner on stderr — JSON is on stdout.
    data = json.loads(result.stdout)
    return data.get("values", [])


def cell(row: list[str], idx: int) -> str:
    return row[idx].strip() if idx < len(row) and row[idx] is not None else ""


def is_yes(value: str) -> bool:
    return value.strip().lower() in {"y", "yes", "true", "1", "approved"}


def refresh_templates() -> dict[str, Any]:
    rows = gws_values_get(TEMPLATES_RANGE)
    approved: list[dict[str, Any]] = []
    by_use_case: dict[str, list[dict[str, Any]]] = defaultdict(list)
    total = 0
    for row in rows:
        template_id = cell(row, 1)
        if not template_id:
            continue
        total += 1
        record = {
            "template_id": template_id,
            "name": cell(row, 0),
            "canva_link": cell(row, 2),
            "aspect": cell(row, 3),
            "shape_category": cell(row, 4),
            "use_case": cell(row, 5),
            "pages": cell(row, 6),
            "autofill_ready": cell(row, 7),
            "element_map_status": cell(row, 8),
            "approved": is_yes(cell(row, 9)),
            "priority": cell(row, 10),
            "notes": cell(row, 11),
        }
        if record["approved"]:
            approved.append(record)
            if record["use_case"]:
                by_use_case[record["use_case"]].append(record)
    return {
        "_meta": {
            "spreadsheet_id": SPREADSHEET_ID,
            "total_rows": total,
            "approved_count": len(approved),
        },
        "approved": approved,
        "by_use_case": dict(by_use_case),
    }


def refresh_assets() -> dict[str, Any]:
    rows = gws_values_get(ASSETS_RANGE)
    by_id: dict[str, dict[str, Any]] = {}
    by_category: dict[str, list[str]] = defaultdict(list)
    by_subject: dict[str, list[str]] = defaultdict(list)
    total = 0
    approved_count = 0
    for row in rows:
        asset_id = cell(row, 1)
        if not asset_id:
            continue
        total += 1
        canonical = is_yes(cell(row, 6))
        approved = is_yes(cell(row, 7))
        if not (canonical and approved):
            continue
        approved_count += 1
        record = {
            "asset_id": asset_id,
            "name": cell(row, 0),
            "category": cell(row, 2),
            "subject": cell(row, 3),
            "tags": [t.strip() for t in cell(row, 4).split(",") if t.strip()],
            "aspect": cell(row, 5),
            "canonical": canonical,
            "approved": approved,
            "notes": cell(row, 8),
        }
        by_id[asset_id] = record
        if record["category"]:
            by_category[record["category"]].append(asset_id)
        if record["subject"]:
            by_subject[record["subject"]].append(asset_id)
    return {
        "_meta": {
            "spreadsheet_id": SPREADSHEET_ID,
            "total_rows": total,
            "approved_canonical_count": approved_count,
        },
        "by_id": by_id,
        "by_category": dict(by_category),
        "by_subject": dict(by_subject),
    }


def main() -> None:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    templates = refresh_templates()
    assets = refresh_assets()
    (CACHE_DIR / "canonical-templates.json").write_text(json.dumps(templates, indent=2) + "\n")
    (CACHE_DIR / "canonical-assets.json").write_text(json.dumps(assets, indent=2) + "\n")
    print(
        f"Templates: {templates['_meta']['approved_count']}/{templates['_meta']['total_rows']} approved.\n"
        f"Assets: {assets['_meta']['approved_canonical_count']}/{assets['_meta']['total_rows']} approved+canonical.\n"
        f"Cache written to {CACHE_DIR}"
    )


if __name__ == "__main__":
    main()
