---
name: md-to-drive
description: User-invoked skill to upload one or more local Markdown files to Travis's Google Drive as native Google Docs (not as .md attachments) using the gws CLI. Default destination is the "Claude-Uploads" folder at Drive root. Trigger phrases include "upload to drive", "convert to google doc", "send this to claude-uploads", "publish these to drive", "drop these markdown files into drive", "make google docs from these". For batches of 2+ files, dispatch one parallel subagent per file.
metadata:
  version: 0.1.0
---

# Markdown → Google Drive (as Docs)

Convert one or more local Markdown files into native Google Docs in Travis's Drive, using the `gws` CLI. The Drive API converts markdown to Doc format on the fly when the request body specifies `mimeType: application/vnd.google-apps.document`, so the result is a real Doc — not a `.md` attachment.

## Default destination

**Folder:** `Claude-Uploads` at Travis's My Drive root
**Folder ID:** `1L4GEISXbi9sbqOKDCwbFuD1F6MF-JI5g`

Override only if the user explicitly names a different folder. To find another folder ID, run:
```
gws drive files list --params '{"q":"name=\"<FOLDER_NAME>\" and mimeType=\"application/vnd.google-apps.folder\" and trashed=false","fields":"files(id,name,parents)"}'
```

## Inputs to gather

Before running, confirm or ask for:

1. **File path(s)** — one or more absolute paths to local `.md` files.
2. **Doc naming convention** — defaults below; ask only if the user signals they want something different.
3. **Content cleanup** — defaults to none. Ask if the user wants any trailing block stripped (e.g., the `--- **Edit log**` QA block on Cerkl SEO blog files; see "Optional cleanup recipes" below).
4. **Destination override** — assume Claude-Uploads unless the user names another folder.

## Default naming convention

`<YYYY-MM-DD> — <H1 title>` with a real em-dash (U+2014) and single spaces around it.

- **Date:** the `YYYY-MM-DD` prefix in the filename (before the first underscore). If the filename has no date prefix, ask the user before defaulting to today.
- **H1 title:** the text after `# ` on the first heading line of the file (drop the leading `# `).

Example: `2026-05-14_hidden-cost-benefits-communication_live.md` with H1 `# The Hidden Cost of Benefits Communication` becomes `2026-05-14 — The Hidden Cost of Benefits Communication`.

If the file has no H1, fall back to the filename slug (humanized: replace `-` with spaces, title-case). Ask the user if uncertain.

## The recipe

### Step 1 — Set up the temp directory

The gws CLI requires upload paths to live **inside the current working directory**. Always stage uploads in `/tmp/md-to-drive/`:

```
mkdir -p /tmp/md-to-drive
```

### Step 2 — Stage the file (with optional cleanup)

For each source file, write a cleaned copy to `/tmp/md-to-drive/<base>.md`. The base filename should drop any trailing `_live` / `_draft` / `_pre-writing` suffix and the `.md` extension before re-adding `.md`.

**No cleanup (default):**
```bash
cp "<source>" "/tmp/md-to-drive/<base>.md"
```

**With Edit-log strip** (Cerkl SEO blog `_live.md` files have a trailing `--- **Edit log** ...` QA block — use this if the user asks):
```bash
python3 -c "import re; c=open('<source>').read(); open('/tmp/md-to-drive/<base>.md','w').write(re.sub(r'\n---\n\*\*Edit log\*\*.*\$','',c,flags=re.DOTALL).rstrip()+'\n')"
```

### Step 3 — Upload as a Google Doc

Build the Doc name per the naming convention above. Then run, **from inside `/tmp/md-to-drive/`** (use the bare filename, not the absolute path):

```bash
cd /tmp/md-to-drive && gws drive files create \
  --upload "<base>.md" \
  --upload-content-type "text/markdown" \
  --json '{"name":"<DOC NAME>","mimeType":"application/vnd.google-apps.document","parents":["1L4GEISXbi9sbqOKDCwbFuD1F6MF-JI5g"]}' \
  --format json
```

The response includes the new file's `id`. Build the Doc URL as:
```
https://docs.google.com/document/d/<id>/edit
```

### Step 4 — Report back

For each file uploaded, report:
- Source filename
- Doc name
- File ID
- Doc URL
- Any errors

For batch uploads, present results as a table sorted by date prefix.

## Single file vs. batch

- **1 file:** run the recipe inline. ~5 seconds end-to-end.
- **2–10 files:** dispatch one parallel subagent per file (general-purpose subagent type). Each subagent gets a self-contained prompt with: the source path, the destination folder ID, the naming rule, the cleanup rule (if any), the exact gws command shape, and instructions to return file ID + URL in under 80 words. Send all subagent calls in a single message for true parallel execution.
- **10+ files:** still use parallel subagents but consider batching in groups of ~10 to keep the response manageable.

For the subagent prompt template, see the worked example in this skill's git history (or the Matt Frost recap-blog upload run from 2026-05-07).

## Common gotchas

1. **gws cwd restriction.** The CLI rejects upload paths outside the current working directory with a `validationError`. Always `cd /tmp/md-to-drive/` before running `gws drive files create`, and use the bare filename in `--upload`.
2. **The mimeType in --json is the *target* format.** `application/vnd.google-apps.document` triggers Drive's markdown-to-Doc conversion. If you forget it, the file uploads as a `.md` attachment that opens in a text viewer, not as an editable Doc.
3. **`--upload-content-type` is the *source* format.** Always `text/markdown` for our use case. Skipping it sometimes works (Drive auto-detects), but specifying it is safer.
4. **Em-dash in Doc names.** Use a real em-dash character (U+2014, "—"), not two hyphens. Drive titles render fine with em-dashes and they sort correctly. The ban on em-dashes in editing applies to *blog body content*, not to Doc filenames.
5. **Auth.** First-run will hit a keyring prompt. After that, gws caches credentials. If `gws drive files list ...` returns auth errors, run any `gws drive` command interactively in a terminal to re-auth.

## Optional cleanup recipes

Document any source-specific patterns here as they emerge. Each entry should be a 1-line description + the Python or bash one-liner.

- **Strip Cerkl SEO blog Edit log block** (trailing `\n---\n**Edit log**...`):
  ```python
  re.sub(r'\n---\n\*\*Edit log\*\*.*$', '', content, flags=re.DOTALL)
  ```

## Permissions / sharing

This skill does not set permissions. Uploaded Docs are private to Travis's Drive account by default. To make a Doc shareable, run `gws drive permissions create` after upload (out of scope here). If the user asks for sharing as part of the upload, ask whether they want anyone-with-link access or an explicit email list, then add that as a follow-up step.

## Worked example

The first run of this recipe was the bulk upload of Cerkl SEO blog `_live.md` files on 2026-05-07 — 9 files in parallel via subagents, plus one inline test. See [cerkl/marketing/channels/seo-blog/blog-posts-live/](../../marketing/channels/seo-blog/blog-posts-live/) for the source files.
