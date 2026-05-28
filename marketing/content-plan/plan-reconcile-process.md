# Plan Reconcile

> Weekly reconciliation of the content plan. Output: `rolling-4week.md` updated (next week locked), the SEO brief queue advanced and archived, [`inputs.md`](inputs.md) triaged, and a fresh Jira CSV scaffold at [`jira/imports/YYYY-Www.csv`](jira/imports/).

## Trigger

- "Run the Monday reconcile"
- "Reconcile the plan"
- "Plan reconcile for [week]"
- "Lock next week"

Default cadence: every Monday morning of the lead week (week N−1 for publish week N) or Friday of the week before. If Monday is a federal holiday, slide to Tuesday and compress per the [holiday gotcha](content-lifecycle-process.md#holiday-gotcha).

## Inputs

I'll confirm before reconciling:

1. **Target publish week** — defaults to next ISO week (the week to lock). Override as `2026-W23` or as the Monday date of the publish week (`2026-06-01`).
2. **Anything Travis wants me to know** — slipped launches, capacity changes, urgent insertions, briefs that should jump the queue.

## Context to load

- /Users/travisfoster/claude-code/cerkl/marketing/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/content-plan/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/content-plan/rolling-4week.md
- /Users/travisfoster/claude-code/cerkl/marketing/content-plan/inputs.md
- /Users/travisfoster/claude-code/cerkl/marketing/content-plan/2026-content-plan.md

(Per [PRINCIPLES.md #4](/Users/travisfoster/claude-code/cerkl/PRINCIPLES.md), this list is authoritative for this scope — parent loads do not apply unless re-listed here. Individual brief files and monthly plans are read on-demand during steps, not loaded upfront.)

---

## Steps

### Step 1 — Triage the brief queue

- **Owner:** Claude
- **Parallelizable with:** 2 (independent file reads/writes — Step 1 touches `../seo/briefs/` + monthly plan; Step 2 touches `inputs.md` + `rolling-4week.md`)
- **Needs:** —
- **Inputs:** [`../seo/briefs/`](../seo/briefs/), the target month's plan at [`monthly-content-plans/`](monthly-content-plans/), today's date, Travis's urgency input from the kickoff
- **Produces:** brief frontmatter updates (`status: scheduled`, `scheduled_for: YYYY-MM-DD`) + new rows in the matching monthly plan file
- **What to do:**
  - List briefs in `../seo/briefs/` with `status: queued`. Note their `target_pillar`, primary keyword, and any in-brief seasonality.
  - For each brief that fits an open slot in the next 2–4 weeks (the lead week being locked + nearby), schedule it: update frontmatter `status: scheduled` and `scheduled_for: YYYY-MM-DD` (the planned publish date), then add a row to the matching week section of `monthly-content-plans/[month-year].md`.
  - Urgency triage: if Travis flagged a brief as urgent and the target week is already full, swap — downgrade the displaced brief back to `status: queued`, schedule the urgent one in its place.
  - If a week has open `cerkl.com` slots but no fitting queued brief, leave the slot as TBD with a `**needs brief from SEO by [date]**` annotation (deadline = publish date − 10 days).

### Step 2 — Process the inputs mailbox

- **Owner:** Claude
- **Parallelizable with:** 1
- **Needs:** —
- **Inputs:** [`inputs.md`](inputs.md), [`rolling-4week.md`](rolling-4week.md)
- **Produces:** updated `inputs.md` (entries promoted, pruned, or parked), possible new rows in `rolling-4week.md` for non-SEO items, possible brief-request notes for SEO
- **What to do:**
  - Read every entry in `inputs.md`. For each, decide:
    - **Promote** — actionable for an upcoming week. Add a row to `rolling-4week.md` (use `Source brief` to link the input or upstream signal) and delete the entry from `inputs.md`.
    - **Convert** — needs an SEO brief to operationalize. Note as a brief request for SEO; keep the entry in `inputs.md` until the brief lands.
    - **Park** — still relevant but not this cycle. Leave in place.
    - **Prune** — expired, superseded, or no longer fits. Delete from `inputs.md`.
  - Stale items don't survive forever — pruning is the maintenance the mailbox needs.

### Step 3 — Archive shipped briefs

- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** —
- **Inputs:** [`../seo/briefs/`](../seo/briefs/) (any briefs with `status: shipped`)
- **Produces:** moved files in `../seo/briefs/archive/`
- **What to do:** List briefs with `status: shipped`. Move each to `../seo/briefs/archive/<slug>.md`. The active folder stays a clean queue + scheduled + in-progress view.

### Step 4 — Lock next week into rolling-4week.md

- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** —
- **Inputs:** the target month's plan, current `rolling-4week.md`, results of Steps 1–2
- **Produces:** updated `rolling-4week.md` with target week as "Week 1 — locked"
- **What to do:**
  - Pull the rows for the target publish week from `monthly-content-plans/[month-year].md`.
  - Replace the "Week 1 — locked" section with those rows. Shift Week 2 → Week 1's prior position, Week 3 → Week 2, and pull a new Week 4 from the monthly plan (or next month if we're at month boundary).
  - For each cerkl.com blog in the locked week, confirm the 4 LinkedIn wraps are present (theme, link, poll, short video). If missing, draft them using the blog as anchor.
  - Mark any previously-locked rows that shipped as `Status: shipped`. Move shipped rows out of `rolling-4week.md` and append them to the matching month's `monthly-content-plans/YYYY-MM-posted.md` (the living shipped-rows archive). Create `YYYY-MM-posted.md` if the file doesn't exist yet.
  - Bump `**Last reconciled:** YYYY-MM-DD` at the top of `rolling-4week.md` to today.

### Step 5 — Generate the Jira CSV scaffold

- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** [`jira/jira-scaffold-process.md`](jira/jira-scaffold-process.md)
- **Inputs:** the locked Week 1 from Step 4
- **Produces:** `jira/imports/YYYY-Www.csv` (scaffold form — every row present, blog Task Descriptions carry `Slug: <slug>` and `[DRIVE_URL_PLACEHOLDER]`)
- **What to do:** Invoke `jira-scaffold-process.md` with the target publish week. The scaffold process handles slug resolution, work-item-IDs, subtask layout, and column ordering.

  After the scaffold runs, verify the LinkedIn coverage explicitly: every LinkedIn row in the locked week must produce exactly 1 Task + 4 subtasks (`LinkedIn – Copy`, `LinkedIn – Asset Creation`, `LinkedIn – Approval`, `LinkedIn – Implementation / Publishing`), and each LinkedIn Task Description must carry the `[COPY_PLACEHOLDER]` token (on its `Copy:` line) that the LinkedIn drafting process fills. If any LinkedIn row is missing its Task, missing one of the 4 subtasks, or missing the placeholder, surface the gap in Step 6 so it can be patched before the LinkedIn drafting process runs.

### Step 6 — Report and trigger

- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** —
- **Inputs:** outputs of Steps 1–5
- **Produces:** chat-printed summary
- **What to do:** Print a concise summary:
  - **Scheduled this run:** briefs newly moved from queued → scheduled, with slug + publish date
  - **Archived:** briefs moved to `archive/`
  - **Inputs processed:** count promoted, converted, parked, pruned
  - **Locked week:** ISO week + row count + Jira CSV path
  - **Brief requests for SEO:** any TBD slots with deadlines
  - **LinkedIn scaffold gaps (if any):** LinkedIn rows missing a Task, missing subtasks, or missing the `[COPY_PLACEHOLDER]` token in the Task Description — must be patched before the LinkedIn drafting process runs
  - **Next action:** which writing+publishing pipeline runs next, with the channel + slug list

---

## Output

- Updated [`rolling-4week.md`](rolling-4week.md) (Week 1 locked, `Last reconciled` bumped)
- Updated brief frontmatter in [`../seo/briefs/`](../seo/briefs/) (status changes) + archived shipped briefs in [`../seo/briefs/archive/`](../seo/briefs/archive/)
- Updated rows in the relevant [`monthly-content-plans/`](monthly-content-plans/) file
- Updated [`inputs.md`](inputs.md) (entries promoted/pruned)
- New [`jira/imports/YYYY-Www.csv`](jira/imports/) scaffold
- Chat-printed summary

## Future work

- Wire to `/schedule` for automatic Monday cadence (with holiday slide built in).
- Add a "diff vs. last reconcile" report (briefs moved, rows added/removed, inputs delta).
- Once a few cycles have run, tighten the inputs triage rules into a sharper rubric.

## Learnings

Append "what broke / what we changed" notes here as the process matures.
