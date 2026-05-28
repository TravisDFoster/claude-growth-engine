---
name: seo-blog-publishing
description: Use after `seo-blog-editing` finishes a post — takes the `_live.md`, uploads it to Google Drive as a Doc, then inserts the Drive URL into the target week's Jira CSV row matching the brief slug. This is the final step before Travis imports the CSV to Jira. Triggers on phrases like "publish the [slug] post", "run publishing on the [slug] draft", "upload [slug] to Drive and wire into Jira CSV". Prerequisite: a `_live.md` in `blog-posts-live/` AND a Jira CSV scaffold at `content-plan/jira/imports/YYYY-Www.csv` for the target week. Output: Drive Doc URL + updated CSV row.
metadata:
  version: 0.1.0
---

# SEO Blog Publishing

Bridges the editing skill and Jira import. Takes a publication-ready `_live.md`, uploads it to Drive, and threads the Drive URL into the right row of the week's Jira CSV scaffold (which was created during the Monday reconcile per [`../../../../content-plan/content-lifecycle-process.md`](/Users/travisfoster/claude-code/cerkl/marketing/content-plan/content-lifecycle-process.md)).

## Inputs

1. **Live file:** `/Users/travisfoster/claude-code/cerkl/marketing/channels/seo-blog/blog-posts-live/YYYY-MM-DD_[slug]_live.md`
2. **Brief slug:** the SEO brief slug (e.g., `internal-communications-in-manufacturing`). Match against the brief in [`../../../../seo/briefs/`](/Users/travisfoster/claude-code/cerkl/marketing/seo/briefs/) — slug equals the brief filename without `.md`, equals the Webflow URL slug.
3. **Target CSV path:** `/Users/travisfoster/claude-code/cerkl/marketing/content-plan/jira/imports/YYYY-Www.csv`. Compute the ISO week from the brief's `scheduled_for:` date in its frontmatter if not provided.

## Pre-flight checks

Stop and surface an error if any fail:

- **Live file exists** at the given path. If not: editing hasn't finished.
- **Target CSV exists.** If not: Monday reconcile didn't create the scaffold — flag this back to the user, do not create the CSV from this skill.
- **CSV has a row for this brief slug.** Look for `Slug: <slug>` in the Description column of a Task row. If no match: the brief was scheduled but the scaffold didn't pick it up — flag this back to the user, do not invent a row.
- **The matched row's Description contains the `[DRIVE_URL_PLACEHOLDER]` token.** If already filled with a URL: this brief has already been published once — confirm with the user before overwriting (re-publish scenario).

## Steps

### 1. Upload to Drive

Load and follow [`/Users/travisfoster/claude-code/cerkl/skills/md-to-drive/SKILL.md`](/Users/travisfoster/claude-code/cerkl/skills/md-to-drive/SKILL.md) with:
- **Source file:** the `_live.md` from input #1
- **Cleanup:** apply the Edit-log strip recipe — the trailing `---\n**Edit log**...` block is QA metadata, not customer-facing content
- **Destination:** default (Claude-Uploads folder)
- **Naming:** default convention (`YYYY-MM-DD — <H1 title>` with em-dash)

Capture the returned Drive Doc URL.

**What Furqan sees in the Doc:** the five bold-bracket body markers from editing (`[Top CTA — variant]`, `[Content 1]`, `[Middle CTA — variant]`, `[Content 2]`, `[Bottom CTA — variant]`) render as visible bold text in the Drive Doc. They tell Furqan exactly which Webflow CTA component to insert at each spot and where the Content 1 → Content 2 Rich Text field split happens. The block between `[Content 1]` and `[Middle CTA]` pastes into Webflow's Content 1 field; the block between `[Content 2]` and `[Bottom CTA]` pastes into Content 2. Do not use HTML comments (`<!-- ... -->`) — Drive's markdown→Doc converter strips them and Furqan would see no markers at all.

### 2. Insert URL into Jira CSV

- Open the target CSV at the path from input #3
- Find the Task row (Issue Type = `Task`) whose Description column contains `Slug: <slug>` (for SEO blog rows, this slug is also the brief slug and the Webflow URL slug)
- In that row's Description, replace `[DRIVE_URL_PLACEHOLDER]` with the actual Drive URL
- Preserve all other fields, all other rows, and the CSV header
- Save the CSV in place

CSV escaping: the Description field typically contains newlines and may be quoted. Use a real CSV library (Python `csv`, or equivalent) — do not regex the raw file unless you've verified the Description field has no embedded commas or quotes.

### 3. Verify

Re-read the CSV and confirm:
- The target row's Description now contains the Drive URL (not the placeholder)
- All other rows are byte-identical to the pre-edit state
- The CSV still parses cleanly

### 4. Return

Report back to the orchestrator:
- Drive Doc URL
- CSV path + row index (or Task summary) of the row updated
- Final score line from editing (passed through for the orchestrator's roll-up)

## What this skill does NOT do

- Flip brief `status:` — stays `in-progress` from editing through Webflow publish. The brief flips to `shipped` only when Furqan reports the post live in Webflow.
- Create the Jira CSV — that's done at Monday reconcile per [`../../../../content-plan/content-lifecycle-process.md`](/Users/travisfoster/claude-code/cerkl/marketing/content-plan/content-lifecycle-process.md). If the scaffold doesn't exist, fail with a clear error.
- Modify rolling-4week.md — content-plan owns that file; publishing is downstream.
- Import to Jira — Travis runs the manual import after all rows in the week's CSV have their URLs filled in.

## Error modes

| Error | Cause | Fix |
|---|---|---|
| `live file not found` | Editing didn't run or wrote to wrong path | Confirm editing produced `_live.md` at the expected path |
| `CSV scaffold not found` | Monday reconcile didn't create `jira/imports/YYYY-Www.csv` | Travis creates the scaffold; re-run |
| `no CSV row for slug` | Brief was scheduled in rolling-4week but scaffold-generation missed it | Travis adds the row to the CSV; re-run |
| `placeholder already replaced` | This brief was already published — possible re-publish | Confirm with user before overwriting |
| `Drive upload failed` | md-to-drive skill error | Surface md-to-drive's error; do not touch CSV |
