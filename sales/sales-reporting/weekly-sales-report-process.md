# Weekly Sales Report

> HubSpot pipeline report for the sales operating cadence (Josh Mandelman, Marc Fregoe, Tarek Kamil). Default cadence is weekly, but the same process renders ANY timeframe. Output: `reports/<label>.html` (dashboard), rendered deterministically — no LLM in the render path. V1 = pipeline metrics only.

## Trigger

- "Run the weekly sales report"
- "Weekly sales report"
- "Generate this week's sales report"
- "Sales report for the last 4 weeks" / "4-week sales report"
- "Sales report for <date> to <date>"

## Inputs

- **Timeframe** — defaults to the current ISO week (Mon–Sun). Flexible:
  - `--weeks N` → trailing N ISO weeks (e.g. `--weeks 4` = last 4 weeks), labeled like `2026-W19-W22`.
  - `--week-start YYYY-MM-DD --week-end YYYY-MM-DD` → an explicit range (e.g. to re-run a prior complete week).
  - "New / closed" counts cover the whole window; the open-pipeline snapshot is always current live state (period-independent).

## Context to load

- /Users/travisfoster/claude-code/cerkl/sales/CONTEXT.md

(Per [PRINCIPLES.md #4](../../PRINCIPLES.md), this list is authoritative for this scope — parent loads do not apply unless re-listed here. The feature-request classifier reads `shared/broadcast.md` itself inside a sub-agent (Step 4), so it stays out of the main process context.)

**Deterministic core + one bounded inference step.** The pipeline / activity / feature-gaps data → HTML path is fully deterministic: `pull_pipeline.py` pulls, aggregates, and calls `render_report.py` (byte-identical styling every run, no styling sub-agent). The *only* inference is the feature-request classifier (Step 4) — a sub-agent that turns unstructured notes into a small structured JSON, which the render then merges deterministically.

---

## Steps

### Step 1 — Resolve the timeframe
- **Owner:** Joint
- **Needs:** —
- **Inputs:** today's date, or an explicit override from the user (a number of weeks, or a date range)
- **Produces:** the args to pass the script (none / `--weeks N` / `--week-start … --week-end …`)
- **What to do:** Default to the current ISO week (Mon–Sun) — run with no args. If the user asked for a lookback ("last 4 weeks") pass `--weeks 4`; explicit dates → `--week-start/--week-end`. The script derives `label`, `period_label`, and `num_weeks` itself.

### Step 2 — Pull + render (one command)
- **Owner:** Claude
- **Needs:** [`scripts/pull_pipeline.py`](scripts/pull_pipeline.py), [`scripts/render_report.py`](scripts/render_report.py), [`reference-weekly-sales-report.html`](reference-weekly-sales-report.html) (CSS source)
- **Inputs:** the Step 1 args (or none, for the current-week default)
- **Produces:** `tmp/pipeline-<label>.json` (data record) + `reports/<label>.html` (deliverable). A compact at-a-glance prints to stdout.
- **What to do:** Run the command below. `pull_pipeline.py` fetches stage metadata + deal searches (new / closed / open / Foundations), per-rep **activity** counts (meetings/notes/tasks — calls read 0, emails scope-blocked), **demo-request form submissions** in the window (no owner filter; forms configured in `DEMO_FORMS` at the top of the script), and the structured **`feature_gaps` roll-up**, aggregates in Python, writes the JSON, then calls `render_report.py` to emit the HTML deterministically (reusing the reference's CSS verbatim — no sub-agent, no styling drift). **Two gotchas, both handled below:** `.env` must be exported with `set -a` (plain `source` won't reach the `uv` child); use absolute paths (the scripts resolve their own output paths from `__file__`).

  ```bash
  set -a && source /Users/travisfoster/claude-code/cerkl/.env 2>/dev/null && set +a
  uv run /Users/travisfoster/claude-code/cerkl/sales/sales-reporting/scripts/pull_pipeline.py
  # last 4 weeks:    … pull_pipeline.py --weeks 4
  # explicit range:  … pull_pipeline.py --week-start 2026-05-18 --week-end 2026-05-24
  ```

  Read the printed at-a-glance — you don't need to open the JSON. **This step's report is complete on its own** (pipeline, activity, structured feature_gaps); Steps 3–5 enrich the Feature-gaps section with the notes-classified product/positioning signal. For a fast metrics-only run, stop here. To re-render after a CSS tweak (no re-pull): `uv run scripts/render_report.py tmp/pipeline-<label>.json`.

### Step 3 — Pull notes (for feature extraction)
- **Owner:** Claude
- **Needs:** [`scripts/pull_notes.py`](scripts/pull_notes.py)
- **Inputs:** the same timeframe args as Step 2
- **Produces:** `tmp/notes-<label>.json` — note bodies + owner/date + deal/company associations + each associated deal's `feature_gaps`; `assoc_type` flags contact/company-only notes.
- **What to do:** `uv run .../scripts/pull_notes.py [same args]` (same `set -a` + absolute-path rules as Step 2). Deterministic. Pulls **all** AE notes in the window — feature signal shows up in both deal- and company-associated notes, so don't pre-filter (the `assoc_type` flag is captured for possible future filtering).

### Step 4 — Classify notes → feature requests (the one inference step)
- **Owner:** Claude (sub-agent)
- **Needs:** [`feature-extraction-rubric.md`](feature-extraction-rubric.md) + `tmp/notes-<label>.json` + `/Users/travisfoster/claude-code/cerkl/shared/broadcast.md`
- **Produces:** `tmp/feature-requests-<label>.json`
- **What to do:** Dispatch a sub-agent with a self-contained brief: *"Read `feature-extraction-rubric.md` and follow it exactly. Input notes: `tmp/notes-<label>.json`. Product truth for the already_ships call: `shared/broadcast.md`. Write `tmp/feature-requests-<label>.json`."* The rubric carries the signal/noise rules (excludes praise), the product-vs-positioning `already_ships` split, taxonomy mapping, the verbatim-quote rule, and the output schema. The sub-agent inherits no context — the rubric file IS the brief.

### Step 5 — Re-render with the feature signal
- **Owner:** Claude
- **Needs:** [`scripts/render_report.py`](scripts/render_report.py)
- **Produces:** `reports/<label>.html` (now with the notes-classified gaps in section 05)
- **What to do:** `uv run scripts/render_report.py tmp/pipeline-<label>.json`. `render_report` auto-detects `tmp/feature-requests-<label>.json` and merges the **product gaps** (roadmap) + **positioning gaps** (enablement) into the Feature-gaps section, alongside the structured roll-up. Deterministic.

### Step 6 — Open + relay
- **Owner:** Claude
- **Needs:** —
- **Inputs:** the printed summary + `reports/<label>.html`
- **What to do:** `open <abs path to .html>` and relay the "at a glance" block with the path, so Travis can forward it to Josh + Marc.

## Output

- `reports/<label>.html` — the dashboard deliverable, rendered deterministically by `render_report.py`. `label` is `YYYY-WNN` for a single week, `YYYY-WNN-WNN` for a multi-week lookback.
- `tmp/pipeline-<label>.json` — the aggregated data record (kept for week-over-week deltas later).
- `tmp/notes-<label>.json` + `tmp/feature-requests-<label>.json` — intermediate inputs/outputs for the feature-extraction step. ([`feature-extraction-rubric.md`](feature-extraction-rubric.md) is the classifier's brief.)
- No `.md` intermediate (retired with the deterministic render), no Drive upload, no Chat post — Travis reads/forwards the HTML directly.
- **Surfaced on Mission Control** (the ops dashboard) — the `sales-reporting` Launch/Run category scans `reports/*.html`, so each new weekly `.html` shows up automatically with a weekly freshness badge and a "Run new" launcher. No manual registration needed; just produce the `.html`.

## Future work

- **Email activity (blocked):** the current HubSpot token lacks the email-read scope, so email engagements can't be pulled. Grant the app the `sales-email-read` / engagements email scope in HubSpot, then add emails to the activity roll-up. (Calls currently read 0 — AEs don't log call engagements — so the activity section covers meetings/notes/tasks for now.)
- **"Most-requested capabilities we ship" view (NEW — 2026-05-29):** the classifier's `already_ships: true` rows are AE-recorded *prospect priorities* for features Cerkl already has — NOT gaps. They're extracted and kept in the feature-requests JSON but excluded from the Feature-gaps section. Spin up a dedicated section/roll-up of the most sought-after capabilities we ship (marketing + enablement signal — "lead with what prospects keep asking for that we already do"). Tie it to a **new HubSpot deal property** (e.g. a `sought_after_features` checkbox mirroring the `feature_gaps` taxonomy) for discrete, structured data pulls — same dual-source pattern (structured property + notes-extracted).
- **Property write-back from notes (write-skill):** the classifier could *suggest* values to backfill both `feature_gaps` (real gaps) and the future `sought_after_features` property from note insights — closing the loop on the sparse (~10%) manual tagging. This is a CRM mutation (`hubspot/` write-skill territory), out of scope for this read-only report — would live as a separate hubspot/ skill the AEs run to confirm suggestions.
- **More note-signal sources for the classifier:** fold `closed_lost_reason` free-text and (if a scope/transcript tier is added) call transcripts into the Step-4 input.
- **Stage-movement deltas:** per-transition movement needs deal-stage history (`propertiesWithHistory=dealstage`); deferred for simplicity.
- **Week-over-week deltas:** read the prior `tmp/pipeline-*.json` and show ▲/▼ vs. last week.
- **Stalled-deals callout:** open deals with no activity / no stage change in N days.
- **`/schedule` wiring:** auto-run Friday morning once scheduling is set up.
- **Optional push:** Chat or email delivery if pull-from-file stops being enough.
- **Stage-meta caching:** `pull_pipeline.py` re-fetches pipeline metadata each run (one GET); fine for now.

## Learnings

_Append "what broke / what we changed" notes here as the process matures._

- **2026-06-01 — Added "Demos requested" (top-of-funnel demand signal).** New `DEMO_FORMS` map at the top of `pull_pipeline.py` (initially: `Schedule a Chat (Webflow)` — the form on `cerkl.com/broadcast/demo`). Pulls submissions in the window via `/form-integrations/v1/submissions/forms/{guid}` (newest-first, stops paging once the page's oldest entry is below `start_ms`). No owner filter — pure demand signal, mirroring how Foundations is reported. Renders as a new stat card in the hero strip + a dedicated section 07 (table: date · name · company · company size · email). To add another demo form, append a `{guid: name}` entry to `DEMO_FORMS`. **Gotcha:** the form-submissions endpoint uses cursor-based paging with `after` (offset in the query string), not the deal-search `after` body field — kept separate from `search()`.
- **2026-05-29 — Render lost all CSS (extract_style comment collision).** Editing the reference's header comment to mention the literal string `<style>` broke `render_report.extract_style()`, which did a naive `txt.index("<style>")` and matched the *comment* instead of the real tag — injecting comment prose + duplicate HTML as "CSS," so the browser discarded it and the report rendered unstyled. Fixed by stripping `<!-- -->` comments before locating the tag. **Verification lesson:** grepping for content strings ("header.hero", numbers) passed even though the CSS was malformed — to verify a render, confirm exactly one well-formed `<style>`/`</style>` pair and that the block *starts* with real CSS (`<style>\n :root`), not just that strings exist.
- **2026-05-29 — Activity roll-up + feature extraction.** Spiked engagements: calls read 0 (AEs don't log them), emails are scope-blocked (Future work) → activity section covers meetings/notes/tasks per rep. `feature_gaps` is a 28-option checkbox set on only 72/738 AE deals (~10%) — so notes are the fuller source; built the structured roll-up anyway as a complement. Built `pull_notes.py` (all AE notes + v4 batch associations + each deal's feature_gaps; **gotcha:** v4 `toObjectId` is an int while v3 batch-read keys are strings — coerce to str or lookups silently miss). The classifier (sub-agent driven by `feature-extraction-rubric.md`) maps note mentions onto the taxonomy and splits **product gaps** (roadmap) vs **positioning gaps** (Cerkl already ships it — enablement). Spike finding: 8 of 9 "requests" were *positioning* gaps — the more actionable signal for AEs. Tightened the rubric after the first run mis-tagged praise ("Loved retargeting") as a gap. Render merges the classifier JSON deterministically into section 05. Watch: classification quality depends on `broadcast.md` being current; signal is sparse (~3 signal notes / 65) so prefer multi-week windows. **Also caught a variable clobber** — a loop reused `label` (the period-label var in `main`), renaming the output file to a feature-gap option; renamed the loop var.
- **2026-05-28 — Build.** `.env` must be exported with `set -a` for the `uv` child to see the token (plain `source` failed). Script writes its output path from `__file__`, so cwd-independence is built in. Nurture stage (Sales Pipeline, win-prob 0.1) holds ~$22.6M and would swamp the "open pipeline" headline — split into an active total + a separate Nurture holding line. `closed_lost_reason` is the populated lost-reason field (`loss_reason` is dead).
- **2026-05-28 — Deterministic render (Steps 3+4 → code).** The LLM template-fill + md-to-html sub-agent render were the only inference in the pipeline (~50k tokens/run + styling-drift risk). Replaced with `render_report.py`, which builds the body from the JSON and reuses the reference's `<style>` block verbatim (md5-confirmed identical). Now `pull_pipeline.py` pulls → JSON → HTML in one zero-inference command. Retired the `report-template.md` intermediate and the `.md` output. Also merged the won+lost searches into one "closed-in-period" query (classify in Python) — 6 API calls → 5.
- **2026-05-28 — Foundations decoupled.** Foundations is a free/PLG funnel that's mostly unowned, so owner-filtering it (as the AE pipelines are) undercounted it badly — a 4-week window showed 4 owned vs. 25 actual new deals. Now queried separately with NO owner filter, count-only, and excluded from the AE new-deals / by-owner / by-pipeline breakdowns (which cover only Sales + RFP). Owner scope for AE metrics confirmed as Marc + Josh + Tarek.
- **2026-05-28 — Styling locked.** First render improvised a light adaptation of the workspace's *dark* `reference-dashboard.html`, leaving a saturated cobalt gradient hero with white text that clashed with the light body. Fixed to a white-panel light hero; switched the stat strip to `auto-fit minmax(150px,1fr)` (was cramming at narrow widths); fixed `.bar-row` label column to 150px so bars start at the same x (per-row `max-content` grids don't align). Locked the corrected render as `reference-weekly-sales-report.html` and pointed Step 4 at it so future weeks don't regress.
