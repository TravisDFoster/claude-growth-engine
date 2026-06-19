# Meeting Ingest

> Pull Gemini meeting notes from the Drive "Meet Recordings" folder into local markdown. Output: `personal-assistant/meetings/drive-sync/`. **No Claude tokens / no inference** — pure `gws` CLI download + markdown export.

## Trigger
- Scheduled: launchd job `com.travisfoster.meeting-ingest`, daily at 17:00 local.
- Manual: `python3 meeting-ingest/ingest.py` (add `--dry-run` to preview).

## What it does
1. Lists the "Meet Recordings" Drive folder (`gws drive files list`).
2. Diffs every Google Doc against the manifest (`meetings/drive-sync/.ingest-state.json`), keyed by Drive **file id** + `modifiedTime`.
3. Exports new/edited docs to markdown (`gws drive files export`, `mimeType=text/markdown`), prepends YAML frontmatter, writes to disk.

Idempotent: unchanged docs are skipped; edited notes (Gemini touches them up post-meeting) are re-exported. Videos (mp4) and chat logs (text/plain) are **ignored** — notes only.

## Output layout
```
meetings/drive-sync/
├── .ingest-state.json          ← manifest (idempotency key store)
├── .ingest.log                 ← launchd run log
├── marketing-weekly/           ← recurring series → own folder
│   └── YYYY-MM-DD-notes.md
├── cerkl-sem-sync/
│   └── YYYY-MM-DD-notes.md
└── one-offs/                   ← non-recurring meetings
    └── YYYY-MM-DD-<slug>-<kind>.md
```
Each `.md` carries frontmatter: `source_id`, `meeting`, `date`, `kind`, `drive_name`, `drive_link`, `drive_modified`, `ingested_at`.

Recurring series live in `RECURRING_SERIES` in `ingest.py` — add a slug there to give a meeting its own folder.

## Ad-hoc import (one-off doc outside Meet Recordings)
When Travis hands over a Drive doc link to pull on demand, **no script change** — these are
ad-hoc and the link changes each time. Pull it directly:
```bash
# file id = the part between /d/ and /edit in the share URL
# gws -o is sandboxed to cwd, so cd into the destination folder first
cd meetings/drive-sync/<folder> && \
gws drive files export --params '{"fileId":"<ID>","mimeType":"text/markdown"}' -o <YYYY-MM-DD>-notes.md
```
- Pick `<folder>` to match the content — an existing series folder, a new descriptive one, or `one-offs/`.
- Date the filename from the doc's `modifiedTime` (`gws drive files get … --fields modifiedTime`) or just today.
- Frontmatter is **optional** for ad-hoc pulls — only add the drive-sync schema fields if a downstream skill (e.g. `process-meeting`) will consume the file.
- Don't add it to the manifest; these aren't tracked, so a later `ingest.py` run leaves them alone.

## Relationship to other PA skills
- `meetings/drive-sync/` is machine-generated and **separate** from the hand-written notes in `growth-meeting-notes/`, `sales-meeting-notes/`, etc. The script never touches those.
- To turn an ingested note into project `## Log` entries, run `skills/process-meeting.md` against the file — that step is the only one that uses inference, and only when you ask for it.

## Git
`meetings/` is gitignored, so the synced notes, manifest, and log stay local-only (each device re-syncs from Drive independently). The script, plist, and this doc are tracked.

## launchd management
```bash
# Install / reload
cp meeting-ingest/com.travisfoster.meeting-ingest.plist ~/Library/LaunchAgents/
launchctl bootout  gui/$(id -u)/com.travisfoster.meeting-ingest 2>/dev/null
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.travisfoster.meeting-ingest.plist
# Run now
launchctl kickstart -k gui/$(id -u)/com.travisfoster.meeting-ingest
# Status / disable
launchctl print gui/$(id -u)/com.travisfoster.meeting-ingest | head
launchctl bootout gui/$(id -u)/com.travisfoster.meeting-ingest
```

## Future work
- Opt-in `--with-video <id>` flag to pull a specific recording on demand (videos are 160–580 MB; index-only by default).
- If OAuth ever lapses, the run exits non-zero and logs to `.ingest.log` — a `gws auth login` re-auth fixes it. Could add a desktop notification on failure.

## Learnings
- `gws drive files export -o` is sandboxed to the cwd, so the script runs `gws` with `cwd=<dest folder>` and a relative `-o`.
- Meet file names use either `/` or `-` date separators; the parser accepts both.
