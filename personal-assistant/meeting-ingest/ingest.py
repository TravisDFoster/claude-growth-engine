#!/usr/bin/env python3
"""Ingest Google Meet meeting notes from Drive into local markdown — no inference, no Claude tokens.

Lists the "Meet Recordings" Drive folder via the `gws` CLI (reusing the existing
keyring OAuth), exports each Gemini/transcript Google Doc to markdown, and writes
it under meetings/drive-sync/, grouped by meeting series. Idempotent: a manifest
keyed by Drive file id + modifiedTime means unchanged files are skipped and edited
notes are re-exported.

Videos (mp4) and chat logs (text/plain) are intentionally ignored — notes only.

Usage:
    python3 ingest.py            # sync
    python3 ingest.py --dry-run  # show what would change, write nothing
"""

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone

# ── Config ────────────────────────────────────────────────────────────────────
FOLDER_ID = "1PLp6glPHlDgH1v-uc8MuNDA4kiCI9_DJ"  # "Meet Recordings"
HERE = os.path.dirname(os.path.abspath(__file__))
OUTPUT_DIR = os.path.normpath(os.path.join(HERE, "..", "meetings", "drive-sync"))
MANIFEST_PATH = os.path.join(OUTPUT_DIR, ".ingest-state.json")

DOC_MIME = "application/vnd.google-apps.document"
EXPORT_MIME = "text/markdown"

# Recurring meetings get their own series subfolder; everything else → one-offs/.
RECURRING_SERIES = {"marketing-weekly", "cerkl-sem-sync"}

DATE_RE = re.compile(r"(\d{4})[/-](\d{2})[/-](\d{2})")
DRY_RUN = "--dry-run" in sys.argv


# ── gws helpers ───────────────────────────────────────────────────────────────
def run_gws(args, cwd=None):
    """Run a gws command, returning (returncode, stdout). stderr is surfaced on error."""
    proc = subprocess.run(
        ["gws", *args], cwd=cwd, capture_output=True, text=True
    )
    if proc.returncode != 0:
        sys.stderr.write(proc.stderr)
    return proc.returncode, proc.stdout


def list_folder():
    """Return all non-trashed files in the folder (paginated)."""
    files = []
    page_token = None
    while True:
        params = {
            "q": f"'{FOLDER_ID}' in parents and trashed = false",
            "fields": "nextPageToken,files(id,name,mimeType,modifiedTime,webViewLink)",
            "pageSize": 1000,
        }
        if page_token:
            params["pageToken"] = page_token
        rc, out = run_gws(
            ["drive", "files", "list", "--params", json.dumps(params), "--format", "json"]
        )
        if rc != 0:
            raise SystemExit("gws drive files list failed — try `gws auth login`.")
        data = json.loads(out)
        files.extend(data.get("files", []))
        page_token = data.get("nextPageToken")
        if not page_token:
            break
    return files


# ── Naming ────────────────────────────────────────────────────────────────────
def slugify(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s or "untitled"


def parse_meeting(name, modified_iso):
    """(title, date YYYY-MM-DD, kind) from a Meet/Gemini file name.

    Pattern: "<Title> - YYYY/MM/DD HH:MM TZ - <Notes by Gemini|Transcript|Chat>".
    Falls back to modifiedTime date and the whole name when it doesn't match.
    """
    m = DATE_RE.search(name)
    if m:
        date = f"{m.group(1)}-{m.group(2)}-{m.group(3)}"
        title = name[: m.start()].rstrip(" -").strip()
    else:
        date = modified_iso[:10]
        title = name

    low = name.lower()
    if "notes by gemini" in low:
        kind = "notes"
    elif "transcript" in low:
        kind = "transcript"
    else:
        kind = "doc"

    if not title or title.lower().startswith("meeting started"):
        title = "ad-hoc"
    return title, date, kind


def target_for(f):
    """(dest_dir, filename, series_slug) for a file."""
    title, date, kind = parse_meeting(f["name"], f["modifiedTime"])
    series = slugify(title)
    if series in RECURRING_SERIES:
        dest_dir = os.path.join(OUTPUT_DIR, series)
        filename = f"{date}-{kind}.md"
    else:
        dest_dir = os.path.join(OUTPUT_DIR, "one-offs")
        filename = f"{date}-{series}-{kind}.md"
    return dest_dir, filename, series, date, kind


# ── Export ────────────────────────────────────────────────────────────────────
def export_doc(file_id, dest_dir, filename):
    """Export a Google Doc to markdown at dest_dir/filename. gws -o must be relative to cwd."""
    os.makedirs(dest_dir, exist_ok=True)
    params = {"fileId": file_id, "mimeType": EXPORT_MIME}
    rc, _ = run_gws(
        ["drive", "files", "export", "--params", json.dumps(params), "-o", filename],
        cwd=dest_dir,
    )
    return rc == 0


def write_frontmatter(path, f, series, date, kind):
    """Prepend YAML frontmatter to the exported markdown so downstream skills have metadata."""
    with open(path, "r", encoding="utf-8") as fh:
        body = fh.read()
    fm = (
        "---\n"
        f"source_id: {f['id']}\n"
        f"meeting: {series}\n"
        f"date: {date}\n"
        f"kind: {kind}\n"
        f"drive_name: {json.dumps(f['name'])}\n"
        f"drive_link: {f.get('webViewLink', '')}\n"
        f"drive_modified: {f['modifiedTime']}\n"
        f"ingested_at: {datetime.now(timezone.utc).isoformat()}\n"
        "---\n\n"
    )
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(fm + body)


# ── Main ──────────────────────────────────────────────────────────────────────
def load_manifest():
    if os.path.exists(MANIFEST_PATH):
        with open(MANIFEST_PATH, encoding="utf-8") as fh:
            return json.load(fh)
    return {}


def save_manifest(manifest):
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(MANIFEST_PATH, "w", encoding="utf-8") as fh:
        json.dump(manifest, fh, indent=2, sort_keys=True)


def main():
    files = list_folder()
    manifest = load_manifest()

    new, updated, skipped, ignored = [], [], 0, 0

    for f in files:
        if f["mimeType"] != DOC_MIME:
            ignored += 1  # videos, chat logs, plain-text recaps
            continue

        dest_dir, filename, series, date, kind = target_for(f)
        path = os.path.join(dest_dir, filename)
        rel = os.path.relpath(path, OUTPUT_DIR)

        prev = manifest.get(f["id"])
        unchanged = (
            prev
            and prev.get("drive_modified") == f["modifiedTime"]
            and os.path.exists(path)
        )
        if unchanged:
            skipped += 1
            continue

        bucket = updated if prev else new
        bucket.append(rel)
        if DRY_RUN:
            continue

        if not export_doc(f["id"], dest_dir, filename):
            sys.stderr.write(f"  ! export failed: {f['name']}\n")
            continue
        write_frontmatter(path, f, series, date, kind)
        manifest[f["id"]] = {
            "drive_name": f["name"],
            "drive_modified": f["modifiedTime"],
            "path": rel,
        }

    if not DRY_RUN:
        save_manifest(manifest)

    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    tag = "[dry-run] " if DRY_RUN else ""
    print(
        f"{stamp} {tag}meeting-ingest: "
        f"{len(new)} new, {len(updated)} updated, {skipped} unchanged, {ignored} ignored (video/chat)"
    )
    for label, items in (("new", new), ("updated", updated)):
        for rel in items:
            print(f"  + {label}: {rel}")


if __name__ == "__main__":
    main()
