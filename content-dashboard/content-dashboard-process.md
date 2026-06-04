# Content Dashboard — Refresh Process

> Regenerate `data.json` so `index.html` reflects: the state of recent Jira import CSVs (the end-goal artifact), this-week's locked plan, 4-week pipeline, briefs in staging by status, blog swim-lanes (pre-writing → draft → live) for both channels, a derived LinkedIn view, and an `actions[]` list of "what's the next thing to launch from here."

Browse at: **http://127.0.0.1:3000/cerkl/content-dashboard/**

Output: [`/Users/travisfoster/claude-code/cerkl/content-dashboard/data.json`](data.json)

## Trigger

Routes here from `cerkl/CLAUDE.md`:

- "Refresh my content dashboard" / "Refresh the content dashboard"
- "Update my content dashboard" / "Update the content dashboard"
- "Sync the content dashboard"
- "Rebuild the content dashboard"

## Inputs

None to ask. Reads [`sources.md`](sources.md) and parses the sources it declares.

## Context to load

- [`sources.md`](sources.md) — source registry

## Execution

Steps 1–9 are mechanized in [`refresh.py`](refresh.py). Run it, then do Step 10 in chat.

```bash
python3 /Users/travisfoster/claude-code/cerkl/content-dashboard/refresh.py
```

The script writes `data.json` and copies the prior file to `data.previous.json` so Step 10 can diff. The Steps 1–9 below are the contract the script implements — keep them in sync when changing parsing logic.

## Steps

### Step 1 — Read the registry
Parse the `## Sources` section of `sources.md`. Six sources: `jira-imports`, `rolling-4week`, `briefs`, `seo-blog-posts`, `icpro-blog-posts`, `linkedin` (derived).

### Step 2 — Parse rolling-4week.md
Read [`marketing/content-plan/rolling-4week.md`](../marketing/content-plan/rolling-4week.md).

- Capture `last_reconciled` from `**Last reconciled:** YYYY-MM-DD`.
- For each H2 section that starts with `## Carryover` or `## Week N — `, parse the markdown table beneath it. Tables follow the convention: `| Deliverable | Channel | Publish | Owner | Status | Source brief |`.
- Skip note/aside paragraphs between heading and table — start at the first `| ---` separator line.
- For each data row:
  - **deliverable**: column 1, trim whitespace, strip leading/trailing `*`
  - **channel**: column 2
  - **publish**: column 3 (`YYYY-MM-DD` or `—`)
  - **owner**: column 4
  - **status**: column 5 (`planned` / `in-progress` / `shipped` / `pulled` / `blocked`)
  - **source_brief**: column 6. If contains a markdown link `[slug](path)`, extract `slug` and rewrite URL to `/cerkl/marketing/seo/briefs/<slug>.md` (path-strip the workspace prefix). Otherwise keep as raw text.
- Stash results: `carryover[]`, `weeks[0..3]` (each with `label`, `range`, `rows[]`). The first week is also surfaced as `this_week` since the convention is "Week 1 is locked, in Jira."

### Step 3 — Scan briefs and read frontmatter
For each `*.md` in [`marketing/seo/briefs/`](../marketing/seo/briefs/) (excluding `_template.md` and global excludes):
- Read **only the YAML frontmatter** (between the two `---` delimiters at the top).
- Capture: `title`, `status`, `scheduled_for`, `slug`, `target_channel`.
- Compute **url** = `/cerkl/marketing/seo/briefs/<filename>`.

Bucket by `status` value into: `queued`, `scheduled`, `in-progress`, `shipped`. Sort `scheduled` by `scheduled_for` ascending (soonest first); sort other buckets by filename mtime descending.

The dashboard renders only `queued` · `scheduled` · `in-progress`. Shipped briefs are excluded from the rendered view but counted in `stats.briefs_shipped`.

### Step 4 — Scan blog channel state folders
For each blog channel (`seo-blog-posts`, `icpro-blog-posts`), scan its three state folders:

- `pre_writing/*_pre-writing.md`
- `draft/*_draft.md` (skip any `archive/` subfolder)
- `live/*_live.md`

For each file:
- **date**: parse `YYYY-MM-DD_` prefix. If prefix is `TBD_`, set `date: "TBD"`.
- **title**: strip leading date or `TBD_`, strip trailing `_state`, replace `-` with space, title-case.
- **slug**: the middle part (between the date prefix and `_state` suffix).
- **url**: server-relative path.
- **state**: `pre-writing` / `draft` / `live` (from folder).

Sort each bucket newest-first (TBD items go last). Compute `posts_in_flight` per channel = pre-writing + draft (live is shipped state).

### Step 5 — Derive LinkedIn view
From `rolling-4week` parsed rows: filter where `channel` starts with `LinkedIn`. Bucket by `status`:
- `planned`
- `in-progress` (also include rows from `carryover[]`)
- `shipped`
- `blocked` and `pulled` are counted in `stats.linkedin_blocked` and `stats.linkedin_pulled` but not rendered.

Within each bucket, sort by `publish` ascending.

### Step 6 — Scan Jira import CSVs
Read every `*.csv` in [`marketing/content-plan/jira/imports/`](../marketing/content-plan/jira/imports/).

For each CSV file:

- **Filename → ISO week**: `YYYY-Www.csv` → parse `week_iso`. Compute `week_monday` (Monday date of that ISO week) and `week_range` (Mon→Fri as `YYYY-MM-DD → YYYY-MM-DD`).
- **Parse rows** (CSV with quoted multi-line cells — Description spans lines inside quotes):
  - Tasks (Issue Type = `Task`): classify by Summary prefix
    - `Content - Blog (Cerkl.com) -` → `cerkl_blog`
    - `Content - Blog (ICP) -` → `icpro_blog`
    - `Social Media - LinkedIn -` → `linkedin`
  - Subtasks (Issue Type = `Subtask`) are *not* used for readiness — they're Jira workflow steps. Both signals below read **Task** Descriptions.
- **Drive URL fill** (blog Tasks only): for each blog Task Description, check the `Draft (Google Doc):` line — `[DRIVE_URL_PLACEHOLDER]` = unfilled, `https://docs.google.com/...` = filled.
- **LinkedIn copy fill** (LinkedIn Tasks only): the drafted post copy lives in the LinkedIn **Task** Description under a `Copy:` section (a line that is exactly `Copy:`, followed by `[CAPTION]` / `[POLL]`, `[ASSET SPEC]`, `[HASHTAGS]`). A LinkedIn Task counts as **copy-drafted** when its Description contains a `Copy:` line AND no remaining `[COPY_PLACEHOLDER]` token. Count filled vs. total LinkedIn Tasks.
  - Note: a `[BLOG URL — populate after Furqan publishes…]` placeholder *inside* a finished `Copy:` block does **not** make it unfilled — the copy is drafted; only the live blog URL is pending downstream. Only `[COPY_PLACEHOLDER]` (or the absence of a `Copy:` block) means copy isn't written yet.
- **Status inference** (date-based):
  - `imported` if today ≥ `week_monday`
  - `ready-to-import` if today < `week_monday` AND `drive_urls.filled == total` AND `linkedin_copy.filled == total`
  - `in-prep` otherwise
- **import_ready**: `drive_urls.filled == total && linkedin_copy.filled == total`

Stash as `csvs[]` array, sorted by `week_monday` ascending. Compute `current_csv_file` = the file with the smallest `week_monday >= today`; if none in the future, use the largest `week_monday` (today's or most recent).

### Step 7 — Compute stats
- `briefs_total`, `briefs_queued`, `briefs_scheduled`, `briefs_in_progress`, `briefs_shipped`
- `seo_blog_in_flight`, `seo_blog_live_count`
- `icpro_blog_in_flight`, `icpro_blog_live_count`
- `linkedin_planned`, `linkedin_in_progress`, `linkedin_shipped`, `linkedin_blocked`
- `weeks_planned` (count of weeks with ≥1 row that isn't all-TBD)
- `csvs_in_prep`, `csvs_ready`, `csvs_imported` (counts from `csvs[]`)
- `current_csv_drive_fill` (e.g., `"3/4"`), `current_csv_copy_fill` (e.g., `"0/4"`) — string ratios for the current CSV

### Step 8 — Compute `actions[]`
The dashboard exposes a flat list of named actions Travis can launch by copying the prompt. Each entry declares the action's identity, whether it's ready to run *right now* (computed from current state), why, and the exact prompt to paste into Claude.

**Action catalogue** (id → label, when_ready rule, prompt template). Compute `ready` and `reason` from state; render prompts verbatim.

| id | label | ready when | prompt routes to |
|---|---|---|---|
| `reconcile` | Run Monday reconcile | always available; `reason` notes last reconcile date + next publish week to lock | [`plan-reconcile-process.md`](../marketing/content-plan/plan-reconcile-process.md) |
| `generate-csv-scaffold` | Generate Jira CSV scaffold for next week | the next ISO week after the most recent locked week has no CSV in `jira/imports/` | [`jira-scaffold-process.md`](../marketing/content-plan/jira/jira-scaffold-process.md) |
| `bulk-write-cerkl-blog` | Bulk-write cerkl.com blog drafts for the current CSV | the current CSV has ≥1 `cerkl_blog` Task with `[DRIVE_URL_PLACEHOLDER]` | [`seo-blog-process.md`](../marketing/channels/seo-blog/seo-blog-process.md) |
| `bulk-write-icpro-blog` | Bulk-write Internal Comms Pro blog drafts for the current CSV | the current CSV has ≥1 `icpro_blog` Task with `[DRIVE_URL_PLACEHOLDER]` | [`icpro-blog-process.md`](../marketing/channels/icpro-blog/icpro-blog-process.md) |
| `bulk-write-linkedin` | Bulk-write LinkedIn copy for the current CSV | the current CSV has ≥1 `LinkedIn – Copy` subtask with `[COPY_PLACEHOLDER]` | [`linkedin-process.md`](../marketing/channels/linkedin/linkedin-process.md) |
| `fill-brief-gaps` | Fill SEO brief gaps in rolling-4week | any `rolling-4week` row's `source_brief` contains `needs brief from SEO` | SEO brief writing process |
| `refresh-dashboard` | Refresh this dashboard | always available | this process |

Each action's `prompt` should be self-contained (no follow-up clarification needed). Include the relevant week / CSV / file paths inline. Examples:

```jsonc
{
  "id": "bulk-write-cerkl-blog",
  "label": "Bulk-write cerkl.com blog drafts for 2026-W23",
  "ready": true,
  "reason": "2 cerkl.com blog Task(s) in 2026-W23.csv still have [DRIVE_URL_PLACEHOLDER]",
  "prompt": "Bulk-write this week's planned cerkl.com blog post(s).\n\nJira CSV: /Users/.../jira/imports/2026-W23.csv\nProcess: /Users/.../seo-blog-process.md"
}
```

Sort `actions[]` so ready actions come first; within ready, sort by the order in the catalogue above (reconcile → CSV scaffold → bulk writes → brief gaps → refresh).

### Step 9 — Write `data.json`
Path: [`data.json`](data.json). Overwrite in place. Schema reference below.

### Step 10 — Summarize in chat
Diff `data.json` against `data.previous.json` (written by the script) to identify what changed. Narrate:
- CSV state changes (placeholders filled since last refresh; new CSVs in `jira/imports/`)
- New briefs since prior refresh; status changes
- Blog posts that moved between states (e.g., draft → live)
- Carryover items still in flight (haven't shipped)
- New rolling-4week reconcile date
- The top-priority `actions[]` entry surfaced ("next thing to do")

One paragraph; no file dump.

## Output

- [`content-dashboard/data.json`](data.json) — overwritten in place
- Chat summary of what changed

## `data.json` schema

```jsonc
{
  "generated_at": "YYYY-MM-DD",
  "last_reconciled": "YYYY-MM-DD",
  "current_csv_file": "YYYY-Www.csv",  // pointer into csvs[]
  "stats": {
    "briefs_total": <int>, "briefs_queued": <int>, "briefs_scheduled": <int>,
    "briefs_in_progress": <int>, "briefs_shipped": <int>,
    "seo_blog_in_flight": <int>, "seo_blog_live_count": <int>,
    "icpro_blog_in_flight": <int>, "icpro_blog_live_count": <int>,
    "linkedin_planned": <int>, "linkedin_in_progress": <int>,
    "linkedin_shipped": <int>, "linkedin_blocked": <int>,
    "weeks_planned": <int>,
    "csvs_in_prep": <int>, "csvs_ready": <int>, "csvs_imported": <int>,
    "current_csv_drive_fill": "X/Y",      // e.g., "3/4"
    "current_csv_copy_fill":  "X/Y"       // e.g., "0/4"
  },
  "csvs": [
    {
      "file": "2026-W23.csv",
      "path": "/cerkl/marketing/content-plan/jira/imports/2026-W23.csv",
      "week_iso": "2026-W23",
      "week_monday": "2026-06-01",
      "week_range": "2026-06-01 → 2026-06-05",
      "status": "in-prep",                 // "in-prep" | "ready-to-import" | "imported"
      "counts": {
        "tasks_total": <int>,
        "cerkl_blog_tasks": <int>,
        "icpro_blog_tasks": <int>,
        "linkedin_tasks": <int>,
        "subtasks_total": <int>
      },
      "readiness": {
        "drive_urls":    { "filled": <int>, "total": <int> },
        "linkedin_copy": { "filled": <int>, "total": <int> }
      },
      "import_ready": <bool>
    }
  ],
  "actions": [
    {
      "id": "reconcile",
      "label": "Run Monday reconcile",
      "ready": <bool>,
      "reason": "...one-line context, e.g. 'Last reconciled 2026-05-21; next week to lock is 2026-W24'...",
      "prompt": "...full prompt the user copies into Claude..."
    }
    // ...one entry per action in the catalogue (Step 8)
  ],
  "carryover": [
    { "deliverable": "...", "channel": "LinkedIn poll", "publish": "YYYY-MM-DD",
      "owner": "...", "status": "in-progress", "source_brief": "...", "source_brief_url": "..." }
  ],
  "this_week": {
    "label": "Week 1 — May 25–29: Reinforce and Extend",
    "range": "2026-05-25 → 2026-05-29",
    "locked": true,
    "in_jira": true,
    "rows": [ /* same row shape as carryover */ ]
  },
  "weeks": [
    { "n": 1, "label": "Week 1 — …", "range": "…", "locked": true, "rows": [...] },
    { "n": 2, "label": "Week 2 — …", "range": "…", "locked": false, "rows": [...] },
    { "n": 3, "label": "Week 3 — …", "range": "…", "locked": false, "rows": [...] },
    { "n": 4, "label": "Week 4 — …", "range": "…", "locked": false, "rows": [...] }
  ],
  "briefs": {
    "queued":      [ { "title": "...", "slug": "...", "url": "...", "target_channel": "seo-blog" } ],
    "scheduled":   [ { "title": "...", "slug": "...", "url": "...", "scheduled_for": "YYYY-MM-DD", "target_channel": "..." } ],
    "in_progress": [ { ... } ]
  },
  "blog_swimlanes": [
    {
      "slug": "seo-blog",
      "label": "Cerkl Blog (cerkl.com)",
      "subtitle": "Webflow · primary growth channel",
      "new_run_prompt": "...",
      "buckets": {
        "pre_writing": [ { "title": "...", "date": "YYYY-MM-DD", "slug": "...", "url": "..." } ],
        "draft":       [ { ... } ],
        "live":        [ { ... } ]
      }
    },
    { "slug": "icpro-blog", ... }
  ],
  "linkedin": {
    "planned":     [ /* row shape */ ],
    "in_progress": [ /* row shape */ ],
    "shipped":     [ /* row shape */ ]
  }
}
```

## How to add a new source

1. Add a `### <slug>` section under `## Sources` in [`sources.md`](sources.md).
2. Document its parser convention (filename / frontmatter / table).
3. Update Step 2/3/4 in this process file with the parser logic.
4. Update the `data.json` schema above.
5. Update [`index.html`](index.html) to render the new section.
6. Refresh.

## How to add a new blog channel

1. Mirror the `seo-blog-posts` / `icpro-blog-posts` shape in `sources.md` with a new slug.
2. Confirm the channel uses the `blog-posts-{pre-writing,draft,live}/` folder convention.
3. Refresh — the new channel will appear as a third swim-lane row.

## Future work

- **Diff against previous refresh** — persist `data.previous.json` for a real "what's new" Step 8 summary.
- **Brief tier / target_channel filters** — surface as facets in the Briefs Kanban.
- **LinkedIn posts-{state} folders** — when adopted, register as own source; rolling-4week becomes fallback for scheduled rows without draft files.
- **Wraps-blog backlinks** — resolve `wraps X blog` source-brief text in LinkedIn rows back to the parent blog's slug so LinkedIn rows can cluster under their parent blog.
- **Schedule** — wire to `/schedule` if a daily/weekly auto-refresh stabilizes.

## Learnings

- **2026-06-02 — mechanized Steps 1–9 into `refresh.py`.** Hand-refreshes were burning ~3k output tokens writing `data.json` and were error-prone on long CSV Description cells (a manual scan miscounted W24 LinkedIn copy as 0/4 filled when it was actually 3/4; the script parsed the same file correctly). Script also persists `data.previous.json` so Step 10 has a real diff to narrate.
- **2026-06-02 — out-of-band LinkedIn rows skip copy-fill totals.** Rows with `(out-of-band)` in the Summary are placeholders for Jira capacity tracking; copy is filled at publish time outside the content-plan system. Counting them as unfilled meant CSVs could never flip to `ready-to-import`. Now `copy.total` excludes them.
- **2026-06-02 — `fill-brief-gaps` reason notes candidate queued briefs.** When a rolling-4week row says `needs brief from SEO`, the script checks the queued-briefs bucket for slug-tokens that overlap the deliverable text (≥2 tokens of length ≥4). If a candidate is found, the action prompt tells the next agent to confirm fit + schedule rather than write a duplicate brief.
