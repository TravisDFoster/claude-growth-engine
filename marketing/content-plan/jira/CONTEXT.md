# Jira Imports — Context

> Stable knowledge about the weekly Jira CSV imports: cadence, naming, contents, slug threading, lifecycle. Procedural how-to (generate a scaffold for week X) lives in [`jira-scaffold-process.md`](jira-scaffold-process.md). Field mappings live in [`../jira-csv-guidelines.md`](../jira-csv-guidelines.md).

---

## Cadence

| Day | What happens to the CSV |
|---|---|
| **Mon** | Travis runs the [plan reconcile](../plan-reconcile-process.md) (per [`../content-lifecycle-process.md`](../content-lifecycle-process.md#weekly-cadence)) and generates the scaffold at `imports/YYYY-Www.csv`. Every row is filled in EXCEPT each blog Task's Description has a `[DRIVE_URL_PLACEHOLDER]` token. |
| **Mon–Tue** | Writing pipeline runs (pre-write → draft → edit). |
| **Tue** | Publishing skill runs per post (one per scheduled blog) — uploads `_live.md` to Drive, then finds the matching row in `imports/YYYY-Www.csv` by `Slug: <slug>` and replaces `[DRIVE_URL_PLACEHOLDER]` with the actual Drive URL. |
| **Tue** | All placeholders replaced; CSV is complete. Travis imports it to Jira (manual fills at import: Epic ID + subtask owner IDs). |
| **Wed** | Furqan reviews drafts in Drive (linked from each Jira task). |
| **Thu–Fri** | Furqan does publishing prep in Webflow/Wix. |
| **Mon–Fri (week N)** | Content publishes on its scheduled dates. |

---

## Naming

`imports/YYYY-Www.csv` — ISO week of the **publish week**, not the lead week.

Examples:
- `imports/2026-W22.csv` → scaffold created Mon 2026-05-25 (Memorial Day shifts work to Tue), filled + imported by Wed 2026-05-27, content publishes week of Mon 2026-06-01
- `imports/2026-W23.csv` → scaffold created Mon 2026-06-01, filled + imported Tue 2026-06-02, content publishes week of Mon 2026-06-08

Use [ISO week numbers](https://en.wikipedia.org/wiki/ISO_week_date). When in doubt, the `YYYY-MM-DD` of the Monday of the publish week is unambiguous.

---

## Scaffold contents

Generated per [`../jira-csv-guidelines.md`](../jira-csv-guidelines.md). The shape and column order come from there; this section describes the per-row content at scaffold time.

Each blog Task row has:
- **Work Item ID:** `T001`, `T002`, … (CSV-local placeholder Jira uses to stitch subtasks to parents at import)
- **Issue Type:** `Task`
- **Parent ID:** blank (Tasks have no parent)
- **Epic Link:** blank — filled at import time
- **Summary:** `Lever - Channel - Deliverable Name` (e.g., `Content - Blog (Cerkl.com) - Internal Communications in Manufacturing`)
- **Description:** structured block containing:
  - `Slug: <slug>` — the canonical match key for publishing. For SEO-blog rows this equals the brief slug + Webflow URL slug. For ICPro rows it's synthesized from the deliverable title at scaffold time (see [slug threading](#slug-threading-the-canonical-identity) below).
  - `Brief link: ../seo/briefs/<slug>.md` — SEO-blog only; ICPro rows omit this line
  - Primary keyword + secondary keywords (from brief frontmatter; SEO-blog only)
  - Webflow CMS properties: Primary Category, Primary Solution, All Categories (SEO-blog only; ICPro has its own CMS metadata)
  - `Draft (Google Doc): [DRIVE_URL_PLACEHOLDER]` — replaced by the publishing skill
- **Owner:** channel owner Jira ID (from ownership table in `../jira-csv-guidelines.md`)
- **Channel:** custom Channel field value (e.g., `Blog Posts`)
- **Start Date / Due Date:** from rolling-4week row

Subtask rows reference their parent Task via `Parent ID = T###`. Subtask names follow the channel templates in `../jira-csv-guidelines.md`. Subtask owner IDs are blank at scaffold time — filled at import.

**LinkedIn short video — barebones rows (as of 2026-06-01):** the weekly short-video Task is a single row with a generic Summary (`Social Media - LinkedIn - Short Video (out-of-band)`), a one-line Description, and **no subtasks**. Videos are planned and produced outside the content-plan system; the Task exists for capacity tracking only. See [`../jira-csv-guidelines.md` §Short video — out-of-band](../jira-csv-guidelines.md#short-video--out-of-band).

A complete shape with placeholders for one cerkl blog + one icpro blog + one LinkedIn lives at [`_template.csv`](_template.csv).

---

## Slug threading (the canonical identity)

The slug is the same string everywhere it appears. That's the key to making this whole flow work without a database. Two sources of slugs:

**SEO-blog (cerkl.com):** slug comes from the brief filename — the brief is authored once with a slug, every downstream step inherits it.

| Location | Form |
|---|---|
| Brief filename | `../seo/briefs/<slug>.md` |
| Brief frontmatter | `slug: <slug>` |
| Rolling-4week row | `Source brief` column linking the brief file |
| Jira CSV scaffold | `Slug: <slug>` line in the Task Description |
| Publishing skill | matches CSV row by this exact string |
| Webflow CMS | URL slug = same string |
| File names through the writing pipeline | `_pre-writing.md`, `_draft.md`, `_live.md` all carry `<slug>` |

**ICPro (internalcommspro.com):** no brief queue — slug is synthesized from the deliverable title at scaffold time using a deterministic rule (below). Both the scaffold creator (Monday reconcile) and the ICPro orchestrator apply the same rule so they land on the same slug independently.

**Slug synthesis rule** (used by ICPro at scaffold time and any other channel without an upstream brief):
1. Lowercase the deliverable title
2. Strip common English articles before slugifying: `a`, `an`, `the`, `for`, `of`, `to`, `in`, `and` (matches the hand-curated convention used in pre-existing SEO blog filenames; without this, mechanical slugs like `building-a-case-for-comms-investment-using-data` diverge from real Webflow URLs like `building-case-comms-investment-using-data`)
3. Replace every run of non-alphanumeric characters with a single hyphen
4. Strip leading and trailing hyphens
5. Truncate to 60 characters; if truncation lands mid-word, trim back to the previous hyphen
6. If the result collides with another slug in the same week's scaffold, append `-2`, `-3`, etc.

Example: `"Pride Month internal comms: communicating inclusion all year, not just June"` → `pride-month-internal-comms-communicating-inclusion-all`

If anywhere along the chain a slug drifts (typo, hand-edit, divergent synthesis), the publishing skill fails loudly when it can't find a CSV row by `Slug: <slug>` — that's the first signal something is wrong.

---

## Lifecycle

- **`imports/`** — current and recent weekly CSVs (rolling, ~3 months)
- **`archive/`** — CSVs older than ~3 months. Manual move at quarter close.
- **`_template.csv`** — the canonical shape, always kept current with `../jira-csv-guidelines.md`
- Never edit a CSV after import. If a row is wrong, fix it in Jira directly and note the correction for the next week's scaffold generation.

---

## Open items

- **Real-world column-order parity:** when the first scaffold is imported into Jira, confirm the header order in this CONTEXT and in `../jira-csv-guidelines.md` matches what Jira accepts cleanly. Adjust both if Jira's importer expects a different order.
- **Slug-rule edge cases:** the article-stripping step (rule #2) is a recent addition (2026-05-19) after the W21 test surfaced the divergence with hand-curated historical slugs. Watch for cases where stripping articles produces an awkward slug, and refine the rule if needed.
