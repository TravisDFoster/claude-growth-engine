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

(Per [PRINCIPLES.md #4](../../PRINCIPLES.md), this list is authoritative for this scope — parent loads do not apply unless re-listed here. V1 is pipeline metrics only, so `shared/broadcast.md` is **not** loaded; add it when the V2 feature-request scan lands — see Future work.)

**Fully deterministic:** there is no LLM or sub-agent in the data→report path. `pull_pipeline.py` pulls, aggregates, and calls `render_report.py` to emit the HTML in one run — byte-identical styling every time. The only place inference returns is the V2 feature-request scan (see Future work).

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
- **What to do:** Run the command below. `pull_pipeline.py` fetches stage metadata + 4 deal searches (new / closed / open / Foundations), aggregates in Python, writes the JSON, then calls `render_report.py` to emit the HTML deterministically (reusing the reference's CSS verbatim — no sub-agent, no styling drift). **Two gotchas, both handled below:** `.env` must be exported with `set -a` (plain `source` won't reach the `uv` child); use absolute paths (the scripts resolve their own output paths from `__file__`).

  ```bash
  set -a && source /Users/travisfoster/claude-code/cerkl/.env 2>/dev/null && set +a
  uv run /Users/travisfoster/claude-code/cerkl/sales/sales-reporting/scripts/pull_pipeline.py
  # last 4 weeks:    … pull_pipeline.py --weeks 4
  # explicit range:  … pull_pipeline.py --week-start 2026-05-18 --week-end 2026-05-24
  ```

  Read the printed at-a-glance — you don't need to open the JSON. To re-render after a CSS tweak in the reference (no re-pull): `uv run scripts/render_report.py tmp/pipeline-<label>.json`.

### Step 3 — Open + relay
- **Owner:** Claude
- **Needs:** —
- **Inputs:** the printed summary + `reports/<label>.html`
- **What to do:** `open <abs path to .html>` and relay the printed "at a glance" block with the path, so Travis can forward it to Josh + Marc.

## Output

- `reports/<label>.html` — the dashboard deliverable, rendered deterministically by `render_report.py`. `label` is `YYYY-WNN` for a single week, `YYYY-WNN-WNN` for a multi-week lookback.
- `tmp/pipeline-<label>.json` — the aggregated data record (kept for week-over-week deltas later).
- No `.md` intermediate (retired with the deterministic render), no Drive upload, no Chat post — Travis reads/forwards the HTML directly.
- **Surfaced on Mission Control** (the ops dashboard) — the `sales-reporting` Launch/Run category scans `reports/*.html`, so each new weekly `.html` shows up automatically with a weekly freshness badge and a "Run new" launcher. No manual registration needed; just produce the `.html`.

## Future work

- **V2 — Activity metrics:** calls / emails / meetings logged per rep (Engagements API). New script section + template block.
- **V2 — Feature-request scan:** mine the week's deal/call notes for product asks, triage against `shared/broadcast.md` (add it to Context to load then). The rich `closed_lost_reason` free-text is a starter signal source.
- **V2 — Stage-movement deltas:** per-transition movement needs deal-stage history (`propertiesWithHistory=dealstage`); deferred from V1 for simplicity.
- **Week-over-week deltas:** read the prior `tmp/pipeline-*.json` and show ▲/▼ vs. last week.
- **Stalled-deals callout:** open deals with no activity / no stage change in N days.
- **`/schedule` wiring:** auto-run Friday morning once scheduling is set up.
- **Optional push:** Chat or email delivery if pull-from-file stops being enough.
- **Stage-meta caching:** `pull_pipeline.py` re-fetches pipeline metadata each run (one GET); fine for now.

## Learnings

_Append "what broke / what we changed" notes here as the process matures._

- **2026-05-28 — Build.** `.env` must be exported with `set -a` for the `uv` child to see the token (plain `source` failed). Script writes its output path from `__file__`, so cwd-independence is built in. Nurture stage (Sales Pipeline, win-prob 0.1) holds ~$22.6M and would swamp the "open pipeline" headline — split into an active total + a separate Nurture holding line. `closed_lost_reason` is the populated lost-reason field (`loss_reason` is dead).
- **2026-05-28 — Deterministic render (Steps 3+4 → code).** The LLM template-fill + md-to-html sub-agent render were the only inference in the pipeline (~50k tokens/run + styling-drift risk). Replaced with `render_report.py`, which builds the body from the JSON and reuses the reference's `<style>` block verbatim (md5-confirmed identical). Now `pull_pipeline.py` pulls → JSON → HTML in one zero-inference command. Retired the `report-template.md` intermediate and the `.md` output. Also merged the won+lost searches into one "closed-in-period" query (classify in Python) — 6 API calls → 5.
- **2026-05-28 — Foundations decoupled.** Foundations is a free/PLG funnel that's mostly unowned, so owner-filtering it (as the AE pipelines are) undercounted it badly — a 4-week window showed 4 owned vs. 25 actual new deals. Now queried separately with NO owner filter, count-only, and excluded from the AE new-deals / by-owner / by-pipeline breakdowns (which cover only Sales + RFP). Owner scope for AE metrics confirmed as Marc + Josh + Tarek.
- **2026-05-28 — Styling locked.** First render improvised a light adaptation of the workspace's *dark* `reference-dashboard.html`, leaving a saturated cobalt gradient hero with white text that clashed with the light body. Fixed to a white-panel light hero; switched the stat strip to `auto-fit minmax(150px,1fr)` (was cramming at narrow widths); fixed `.bar-row` label column to 150px so bars start at the same x (per-row `max-content` grids don't align). Locked the corrected render as `reference-weekly-sales-report.html` and pointed Step 4 at it so future weeks don't regress.
