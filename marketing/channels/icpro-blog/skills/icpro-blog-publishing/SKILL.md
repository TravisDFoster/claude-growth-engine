---
name: icpro-blog-publishing
description: Use after `icpro-blog-editing` finishes a post — takes the `_live.md`, uploads it to Google Drive as a Doc with the `ICP` naming segment, then inserts the Drive URL into the target week's Jira CSV row matching the synthesized slug. This is the final step before Travis imports the CSV to Jira. Triggers on phrases like "publish the [slug] ICP post", "run publishing on the [slug] ICPro draft", "upload [slug] to Drive and wire into Jira CSV". Prerequisite: a `_live.md` in `blog-posts-live/` AND a Jira CSV scaffold at `content-plan/jira/imports/YYYY-Www.csv` for the target week. Output: Drive Doc URL + updated CSV row.
metadata:
  version: 0.1.0
---

# ICPro Blog Publishing

Bridges the editing skill and Jira import for internalcommspro.com posts. Takes a publication-ready `_live.md`, uploads it to Drive with the `ICP` filename segment that distinguishes it from cerkl.com posts, and threads the Drive URL into the right row of the week's Jira CSV scaffold (created during Monday reconcile per [`../../../../content-plan/content-lifecycle-process.md`](/Users/travisfoster/claude-code/cerkl/marketing/content-plan/content-lifecycle-process.md)).

## Inputs

1. **Live file:** `/Users/travisfoster/claude-code/cerkl/marketing/channels/icpro-blog/blog-posts-live/YYYY-MM-DD_[slug]_live.md`
2. **Slug:** the synthesized slug for this post. ICPro has no brief queue, so the slug is derived from the deliverable title in [`../../../../content-plan/rolling-4week.md`](/Users/travisfoster/claude-code/cerkl/marketing/content-plan/rolling-4week.md) using the rule in [`../../../../content-plan/jira/CONTEXT.md`](/Users/travisfoster/claude-code/cerkl/marketing/content-plan/jira/CONTEXT.md#slug-threading-the-canonical-identity). The orchestrator should compute the slug once and pass it forward; the scaffold creator uses the same rule independently.
3. **Target CSV path:** `/Users/travisfoster/claude-code/cerkl/marketing/content-plan/jira/imports/YYYY-Www.csv`. Compute the ISO week from the publish date in rolling-4week if not provided.

## Pre-flight checks

Stop and surface an error if any fail:

- **Live file exists** at the given path. If not: editing hasn't finished.
- **Target CSV exists.** If not: Monday reconcile didn't create the scaffold — flag this back to the user, do not create the CSV from this skill.
- **CSV has a row for this slug.** Look for a row where `Issue Type = Task` AND `Summary` starts with `Content - Blog (ICP) -` AND `Description` contains `Slug: <slug>`. (The `Channel` column is `Blog Posts` for both Cerkl and ICP rows; the `(ICP)` marker in `Summary` is what differentiates them — see [`../../CONTEXT.md`](../../CONTEXT.md#source-of-truth-for-what-to-write).) If no match: the row was scheduled but the scaffold synthesized a different slug — surface the row's actual slug so the orchestrator/scaffold-creator divergence can be diagnosed.
- **The matched row's Description contains `[DRIVE_URL_PLACEHOLDER]`.** If already filled: this post has been published before — confirm with the user before overwriting.

## Steps

### 1. Upload to Drive

Load and follow [`/Users/travisfoster/claude-code/cerkl/skills/md-to-drive/SKILL.md`](/Users/travisfoster/claude-code/cerkl/skills/md-to-drive/SKILL.md) with:
- **Source file:** the `_live.md` from input #1
- **Cleanup:** apply the Edit-log strip recipe — the trailing `---\n**Edit log**...` block is QA metadata, not customer-facing content
- **Destination:** default (Claude-Uploads folder)
- **Naming:** `YYYY-MM-DD — ICP — <H1 title>` (the `ICP` segment between date and title distinguishes ICPro posts from Cerkl posts in the shared Drive folder)

Capture the returned Drive Doc URL.

### 2. Insert URL into Jira CSV

- Open the target CSV at the path from input #3
- Find the Task row (`Issue Type = Task`, `Summary` starts with `Content - Blog (ICP) -`) whose `Description` contains `Slug: <slug>`. The `Channel` column is `Blog Posts` for both Cerkl and ICP rows — match on the `Summary` prefix, not on `Channel`.
- In that row's Description, replace `[DRIVE_URL_PLACEHOLDER]` with the actual Drive URL
- Preserve all other fields, all other rows, and the CSV header
- Save the CSV in place

CSV escaping: the Description field typically contains newlines and may be quoted. Use a real CSV library — do not regex the raw file unless you've verified field content has no embedded commas or quotes.

### 3. Verify

Re-read the CSV and confirm:
- The target row's Description now contains the Drive URL (not the placeholder)
- All other rows are byte-identical to the pre-edit state
- The CSV still parses cleanly

### 4. Return

Report back to the orchestrator:
- Drive Doc URL
- CSV path + row index (or Task summary) of the row updated
- Final score line and brand-mention check result from editing (passed through for the orchestrator's roll-up)

## What this skill does NOT do

- Create the Jira CSV — that's done at Monday reconcile per [`../../../../content-plan/content-lifecycle-process.md`](/Users/travisfoster/claude-code/cerkl/marketing/content-plan/content-lifecycle-process.md). If the scaffold doesn't exist, fail with a clear error.
- Synthesize a slug from scratch — the slug is computed upstream (by the orchestrator at write time and the scaffold creator at Monday reconcile). Publishing only matches.
- Modify rolling-4week.md — content-plan owns that file; publishing is downstream.
- Import to Jira — Travis runs the manual import after all rows in the week's CSV have their URLs filled in.

## Error modes

| Error | Cause | Fix |
|---|---|---|
| `live file not found` | Editing didn't run or wrote to wrong path | Confirm editing produced `_live.md` at the expected path |
| `CSV scaffold not found` | Monday reconcile didn't create `jira/imports/YYYY-Www.csv` | Travis creates the scaffold; re-run |
| `no CSV row for slug` | Slug synthesis at scaffold time and at write time produced different strings | Diagnose the divergence; align both to the rule in `content-plan/jira/CONTEXT.md` |
| `placeholder already replaced` | This post was already published — possible re-publish | Confirm with user before overwriting |
| `Drive upload failed` | md-to-drive skill error | Surface md-to-drive's error; do not touch CSV |
