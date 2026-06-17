# Jira Scaffold

> Generate the Jira CSV scaffold for a target week. Output: one `imports/YYYY-Www.csv` per week, every row present, every blog Task Description carrying a `Slug: <slug>` line and a `[DRIVE_URL_PLACEHOLDER]` token. The downstream publishing skill replaces the placeholders. Travis imports the completed CSV to Jira.

## Trigger

- "Create the Jira CSV scaffold for [week]"
- "Generate the scaffold for [ISO week]"
- "Build the Jira import for week of [YYYY-MM-DD]"
- "Run the Monday scaffold for [week]"
- "Scaffold next week's Jira import"

## Inputs

1. **Target week** — ISO week (`2026-W26`) or the Monday date of the publish week.
2. **The slate** — the list of deliverables for the week: `{deliverable, channel, publish_date, owner, source_brief}` per row. Normally this comes straight from Phase 1 of the [weekly content session](../weekly-content-process.md); when run standalone, ask for it (or reconstruct from scheduled briefs + `../inputs.md` Upcoming and confirm).

## Context to load

- /Users/travisfoster/claude-code/cerkl/marketing/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/content-plan/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/content-plan/jira/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/content-plan/jira-csv-guidelines.md

(Per [PRINCIPLES.md #4](/Users/travisfoster/claude-code/cerkl/PRINCIPLES.md), this list is authoritative for this scope — parent loads do not apply unless re-listed here.)

---

## Steps

### Step 1 — Resolve the target week

- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** —
- **Inputs:** the target week argument from the user
- **Produces:** `{iso_week, monday_date, sunday_date, csv_path}`
- **What to do:** From the target week argument, compute the Monday and Sunday dates of the ISO week. The CSV path is `imports/YYYY-Www.csv`. If the file already exists, ask the user whether to overwrite (re-run) or stop (avoid clobbering a partially populated CSV from the publishing skill).

### Step 2 — Confirm the slate

- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** —
- **Inputs:** the slate from input #2, the target week's date range from Step 1
- **Produces:** an in-memory list of slate rows `{deliverable, channel, publish_date, owner, source_brief}`
- **What to do:** Verify every row's `publish_date` falls inside the target week and every blog row's `source_brief` resolves (for cerkl.com rows). Echo the slate back as a table for a final eyeball before generating.

### Step 3 — Derive slugs and brief metadata

- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** [`CONTEXT.md`](CONTEXT.md) (slug threading + synthesis rule)
- **Inputs:** the row list from Step 2 + [`../../seo/briefs/`](../../seo/briefs/)
- **Produces:** each row enriched with `{slug, brief_path, brief_metadata}` (the last two are blank for non-SEO rows)
- **What to do:** For each row:
  - If the `Source brief` column links to `../../seo/briefs/<slug>.md`: read the brief, extract `slug`, primary keyword, secondary keywords, target_pillar, primary_solution, all_categories. `slug = brief.slug`.
  - If the row is a cerkl.com blog whose brief doesn't exist yet (just-in-time — written in Wave 1 of the weekly session): the slug was decided in the session conversation (brief filename = slug). Render the Description with `Slug:`, the topic, and `[BRIEF_PENDING]` on the keyword/CMS lines — the orchestrator backfills them after Wave 1 returns.
  - If the row is `Blog — internalcommspro.com` (no brief): synthesize the slug from the deliverable title using the rule in [`CONTEXT.md`](CONTEXT.md#slug-threading-the-canonical-identity). No brief metadata.
  - If the row is a LinkedIn post: no slug needed in the Description — instead, derive the `Post type` slug from the slate row's `Channel` string using the mapping below, and capture the wrapped blog as `Wraps: <blog-slug>`. The LinkedIn drafting process at [`../../channels/linkedin/linkedin-process.md`](../../channels/linkedin/linkedin-process.md) uses the same mapping to load the right template.

    | `Channel` string | Type slug |
    |---|---|
    | LinkedIn carousel | `carousel` |
    | LinkedIn static/theme | `static-theme` |
    | LinkedIn static/blog | `static-blog` |
    | LinkedIn poll | `poll` |
    | LinkedIn short video | `short-video` |

  - If the row is another non-blog channel: no slug needed in the Description — render a minimal block per channel.

### Step 4 — Compute Work Item IDs and Subtask layout

- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** [`../jira-csv-guidelines.md`](../jira-csv-guidelines.md) (channel subtask templates, ownership table, capacity limits)
- **Inputs:** the enriched row list from Step 3
- **Produces:** a flat list of Task + Subtask rows with `Work Item ID` and `Parent ID` assigned, ready for CSV output
- **What to do:**
  - Assign Task IDs: first Task in the CSV is `T001`, second is `T002`, etc. Tasks ordered by `publish_date` then by channel within a date.
  - For each Task, look up the channel's subtask template from `../jira-csv-guidelines.md`. Assign Subtask IDs continuing the sequence: `S001`, `S002`, etc. Subtask `Parent ID` = the parent Task's `Work Item ID`.
  - Compute Task `Start Date` (typically 5–7 days before publish) and Subtask date ranges (Copy starts at Task Start; Approval is the day before publish; Implementation/Publishing spans the last 1–4 days).

### Step 5 — Generate the CSV

- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** [`_template.csv`](_template.csv) (column order + cell shape reference), [`../jira-csv-guidelines.md`](../jira-csv-guidelines.md) (field rules)
- **Inputs:** the row list from Step 4
- **Produces:** `imports/YYYY-Www.csv`
- **What to do:** Write the CSV per the canonical column order in `../jira-csv-guidelines.md`. For each Task, render the Description block per channel:
  - **SEO blog (cerkl.com):** `Topic`, `Slug`, `Brief link`, `Primary keyword`, `Secondary keywords`, `Webflow CMS properties` (Primary Category, Primary Solution, All Categories), `Draft (Google Doc): [DRIVE_URL_PLACEHOLDER]`
  - **ICPro blog (internalcommspro.com):** `Topic`, `Slug`, `Note: ICPro has no brief queue — slug synthesized at scaffold time`, `Draft (Google Doc): [DRIVE_URL_PLACEHOLDER]`
  - **LinkedIn:** `Topic`, `Post type: <type-slug>` (`carousel`, `static-theme`, `static-blog`, `poll`, or `short-video` — derived from the slate row's `Channel` string per Step 3), `Wraps: <blog-slug>` (the blog brief this LinkedIn post pairs with), then a final `Copy:` line with a `[COPY_PLACEHOLDER]` token on the next line. The LinkedIn drafting process replaces that token **in the Task Description** with the drafted caption + asset spec + hashtags — the copy lives on the parent Task card, not in a subtask. Every LinkedIn Task still gets the standard 4 social-media subtasks per [`../jira-csv-guidelines.md`](../jira-csv-guidelines.md): `LinkedIn – Copy`, `LinkedIn – Asset Creation`, `LinkedIn – Approval`, `LinkedIn – Implementation / Publishing`. The `LinkedIn – Copy` subtask keeps its plain action description (`Draft the post copy.`) — it is the production step, not the storage location for copy. For `poll` rows, the `LinkedIn – Asset Creation` subtask Description uses the explicit skip note from `../jira-csv-guidelines.md` (native poll widget — no asset needed).
  - **Other non-blog channels:** minimal block with `Topic` and any channel-specific notes

  Use standard CSV quoting for multi-line Description cells (double-quote the field, embed newlines literally). **Pre-fill `Epic Link`** on every Task with the current campaign Epic key (ask Travis once if unknown; it's long-lived). **Pre-fill subtask `Owner`** with the channel owner's Jira ID from the ownership table — Travis overrides at import only when a subtask owner varies.

### Step 6 — Verify and report

- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** —
- **Inputs:** the generated CSV
- **Produces:** chat-printed summary
- **What to do:** Re-read the CSV and confirm:
  - It parses cleanly via standard CSV library (no malformed quoting)
  - Every Task has a `Slug: <slug>` line and a `[DRIVE_URL_PLACEHOLDER]` token (where applicable)
  - Every Subtask's `Parent ID` matches a Task `Work Item ID` in the same file
  - Date math is sane (Subtask Due ≤ Task Due, Subtask Start ≥ Task Start)

  Print a summary: total Tasks, total Subtasks, distinct channels represented, brief slugs scaffolded, ICPro slugs synthesized, and a one-line note of which Tasks have `[DRIVE_URL_PLACEHOLDER]` waiting on the publishing skill.

---

## Output

- `imports/YYYY-Www.csv` — the scaffold for the target week, ready for the writing+publishing pipeline to populate Drive URLs into
- A chat-printed summary

## Future work

- Promote to a skill if scaffold generation becomes Tuesday-morning routine and we want auto-trigger (currently invoked manually each Monday).
- Pull subtask date offsets out of this file into a config block in `../jira-csv-guidelines.md` once we see what real-world cadence wants.
- Add a `--dry-run` mode that prints the planned CSV to chat without writing the file (useful when iterating on the slug synthesis rule).
