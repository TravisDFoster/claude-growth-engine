# Monthly Plan Generation

> Generate the week-by-week deliverable plan for a target month. Output: `monthly-content-plans/[month-year].md`. Downstream consumer is [`plan-reconcile-process.md`](plan-reconcile-process.md), which pulls rows from the monthly plan into [`rolling-4week.md`](rolling-4week.md) each Monday.

## Trigger

- "Generate the [Month YYYY] content plan"
- "Build out [Month] plan"
- "Plan [Month YYYY]"

Default cadence: ~2 weeks before the target month begins, so the first Monday reconcile of the new month has material to pull from.

## Inputs

I'll confirm before generating:

1. **Target month** (e.g., `2026-07` or "July 2026")
2. **Month-specific context** — product launches, events, capacity changes, calendar constraints not already in the annual plan or [`inputs.md`](inputs.md)

## Context to load

- /Users/travisfoster/claude-code/cerkl/marketing/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/content-plan/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/content-plan/2026-content-plan.md
- /Users/travisfoster/claude-code/cerkl/marketing/content-plan/jira-csv-guidelines.md
- /Users/travisfoster/claude-code/cerkl/marketing/content-plan/inputs.md

(Per [PRINCIPLES.md #4](/Users/travisfoster/claude-code/cerkl/PRINCIPLES.md), this list is authoritative for this scope — parent loads do not apply unless re-listed here. Brief files and prior monthly plans are read on-demand during steps.)

---

## Steps

### Step 1 — Pull the month's strategic context

- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** —
- **Inputs:** [`2026-content-plan.md`](2026-content-plan.md) (target month section), Travis's month-specific context from the kickoff
- **Produces:** in-memory summary of theme, campaign Epic, anchor, ICP pain points, key topics, important dates
- **What to do:** Read the target month's section in the annual plan. Capture: monthly theme, campaign Epic name, narrative anchor, ICP pain points, suggested topics, federal holidays in-month, and any awareness moments (Pride, Juneteenth, mental health, etc.).

### Step 2 — Compute week structure

- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** [`jira-csv-guidelines.md`](jira-csv-guidelines.md) (weekly capacity limits, channel rules)
- **Inputs:** target month, calendar context from Step 1
- **Produces:** week-by-week skeleton — for each ISO week falling in the month: `{week_number, date_range, narrative_label, holiday_constraints, working_capacity}`
- **What to do:**
  - Carve the month into ISO weeks (use the Monday of each week).
  - Assign a narrative arc across the weeks. Default pattern: **Build the Problem → Show the Solution → [theme-specific anchor moment] → Reinforce/Push**. Adapt to the month's actual anchor — e.g., June 2026 used Build the Problem → Show the Solution → Juneteenth Anchor → Reinforce + Foundations Push.
  - Flag holiday weeks: federal holiday on Monday → reconcile/writing in lead week compresses; Friday holiday (Juneteenth, July 4) → no Friday sends; full-week shutdown (Thanksgiving, Christmas) → publishing gap.
  - Apply weekly capacity limits per `jira-csv-guidelines.md`: 1 cerkl.com blog, 1 ICPro blog, 4 LinkedIn (1 static/theme + 1 static/link + 1 poll + 1 short video), 1 marketing email, 1 SEM review.

### Step 3 — Triage briefs into the month's slots

- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** [`CONTEXT.md`](CONTEXT.md) (brief lifecycle rules)
- **Inputs:** [`../seo/briefs/`](../seo/briefs/) (`status: queued`), the week skeleton from Step 2
- **Produces:** assignment of each fitting brief to a week + publish date; brief frontmatter updates (`status: scheduled`, `scheduled_for: YYYY-MM-DD`)
- **What to do:**
  - List queued briefs from `../seo/briefs/`. Read frontmatter (title, slug, target_pillar, primary keyword, any seasonality).
  - Match briefs to weeks by theme fit, narrative arc position, and any in-brief constraints (e.g., a refresh brief tied to an old post's anniversary).
  - For each match: update brief frontmatter `status: scheduled` and `scheduled_for: YYYY-MM-DD`.
  - If a week has open cerkl.com blog slots but no fitting queued brief, mark the row as TBD with `**needs brief from SEO by [date]**` (deadline = publish date − 10 days).

### Step 4 — Draft ICPro and LinkedIn rows

- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** —
- **Inputs:** each week's cerkl.com blog (anchors the week), [`inputs.md`](inputs.md), the annual plan's topic list for the month
- **Produces:** in-memory list of ICPro blog topics + LinkedIn wrap posts per week
- **What to do:**
  - For each week, draft one ICPro blog topic that fits the week's theme + the month's awareness-month angle (typically the DEI/inclusion lens of the annual plan).
  - For each cerkl.com blog, draft the 3 LinkedIn wrap rows (theme, link, poll) using the blog as anchor. Use a `wraps <blog-shorthand> blog` annotation in the `Source brief` column.
  - Add one **barebones** LinkedIn short video row per week (Deliverable: `— (planned out-of-band)`, Source brief: `— (out-of-band, barebones Jira row)`). Short videos are planned outside the content-plan system as of 2026-06-01 — the row exists for Jira capacity tracking; the topic/wrap/copy is owned by Furqan at publish time. See [`jira-csv-guidelines.md` §Short video — out-of-band](jira-csv-guidelines.md#short-video--out-of-band).
  - Check `inputs.md` for anything that fits the month — promote any timely items into draft rows.

### Step 5 — Write the plan file

- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** [`monthly-content-plans/june-2026.md`](monthly-content-plans/june-2026.md) (reference shape)
- **Inputs:** outputs of Steps 2–4
- **Produces:** `monthly-content-plans/[month-year].md`
- **What to do:** Write the file matching the structure of `june-2026.md`:
  - H1: `# [Month YYYY] — [Theme]`
  - Header block: `**Epic:**`, `**Anchor:**`, `**Notes:**` (holiday/lead-week constraints, special context like Insights launch)
  - One H2 per week: `## Week N — Mon DD–DD: [Narrative label]`
  - Italic note line under each week H2 for any week-specific constraint (e.g., `*Juneteenth Friday June 19 — federal holiday, no Friday sends.*`)
  - Table per week: `Deliverable | Channel | Publish Date | Owner | Source brief`
  - Use absolute `YYYY-MM-DD` dates everywhere.
  - Flag gaps explicitly with `> **Gap:** ...` quote blocks (see june-2026.md Week 3 example).

### Step 6 — Report

- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** —
- **Inputs:** outputs of all prior steps
- **Produces:** chat-printed summary
- **What to do:** Print:
  - **File written:** `monthly-content-plans/[month-year].md`
  - **Brief queue status:** X scheduled out of Y queued, listed by slug
  - **Open gaps:** TBD slots with brief-from-SEO deadlines
  - **Calendar friction:** holidays in lead weeks, capacity overruns, lead-week compression for Week 1 of the new month
  - **Heads-up for Monday reconcile:** the first reconcile after this plan lands will pull rows from this file

---

## Output

- `monthly-content-plans/[month-year].md`
- Updated brief frontmatter in [`../seo/briefs/`](../seo/briefs/) (`status: scheduled`, `scheduled_for`)
- Chat-printed summary

## Future work

- Pull recurring brief patterns (refresh cadence, versus-page cycle) from a config rather than restating per month.
- Add a cross-month check: no brief gets double-booked across two monthly plans.
- Auto-generate the brief request list (with deadlines) as a markdown handoff for SEO.

## Learnings

Append "what broke / what we changed" notes here as the process matures.
