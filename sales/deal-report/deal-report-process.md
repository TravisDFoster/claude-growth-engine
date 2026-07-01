# Deal Report — Health Drilldown

> Per-deal health board over the **active open Sales Pipeline + RFP Process** deals (owner trio: Josh / Marc / Tarek). Companion to the weekly Sales Pipeline Report: that one is the rep scoreboard, this one drills into individual deal **trajectory, velocity, and health**. On-demand / ad hoc — not a weekly cadence. Output: `reports/deal-report.html`, rendered deterministically.
>
> **Two layers, by design.** The 99% is deterministic Python (pull → metrics → rules-based score → render). The 1% is inference: a `deal-health-analyst` sub-agent that runs **only on deals the rules flag** (`watch`/`at_risk`) or a deal you name, to explain *why* and pull next-steps from cleaned email threads. **Rules flag; inference explains — inference never sets the band.**

## Trigger
- "Run the deal report" / "Deal health report"
- "Deal report for Marc" (single rep)
- "What's the health of <deal>?" (calls out a specific deal → goes straight to the inference pass)

## Inputs
- **Owner** — defaults to all three AEs. `--owner Marc` filters to one (substring match on name).
- No timeframe: the report is a **live snapshot** of current active open pipeline (history/recency are computed relative to now).

## Context to load
- `/Users/travisfoster/claude-code/cerkl/sales/CONTEXT.md`
- (Phase 2 inference only) `skills/deal-health-analyst/SKILL.md` — the sub-agent's self-contained brief.

(Per [PRINCIPLES.md #4](../../PRINCIPLES.md), this list is authoritative for this scope.)

---

## Scope decisions (locked 2026-06-22)
- **Pipelines:** Sales Pipeline + RFP Process only. **Active open only** — the Nurture holding stage (win-prob ≤ 0.1) is excluded so "active" matches the weekly report. Active deals that *should* move to Nurture are caught by the `nurture_candidate` flag, not dropped (Travis: surface them, don't act on them yet).
- **Scoring:** rules-based and transparent (`score.py` is the single tuning surface). Qualitative inference runs only when a deal is flagged or explicitly called out.
- **Grouping:** by owner, sorted worst-health-first within each owner. Marc's aged pile is real (most of his deals flag at-risk) — the band/recency model keeps that from burying the genuinely-actionable deals; raw age is *not* the sort key.
- **Cadence:** ad hoc / on-demand. When fresh, it can enrich the weekly Sales Pipeline Report.

## Signals (Phase 1 — structural, no email bodies)
Per deal, from HubSpot structured fields + engagement **metadata** (not bodies):
| Signal | Source | Feeds |
|---|---|---|
| Age | `createdate` | context |
| Stage age (velocity) | `dealstage` history (most recent entry) | score |
| Close-date slippage | `closedate` history (# pushes outward) | score |
| Last-touch recency | max timestamp across meetings/notes/emails | score |
| Reply ratio | email `hs_email_direction` (sent vs received) | score |
| Tracked vs untracked email | `hs_email_tracker_key` present | data-quality note |
| Opens / clicks | `hs_email_open_count` / `_click_count` | context |
| Task aging | tasks `hs_task_status` + due date | score |
| Multithreading | # associated contacts | score |
| No-recap meetings | meetings present, zero notes | context (nudge) |

`score.py` turns these into a **risk-point total → Healthy / Watch / At-risk band**, with a plain-English `reasons[]` audit trail rendered under each deal.

---

## Steps

### Step 1 — Pull + score + render (one command)
- **Owner:** Claude
- **Needs:** [`scripts/pull_deals.py`](scripts/pull_deals.py), [`scripts/score.py`](scripts/score.py), [`scripts/render_deal_report.py`](scripts/render_deal_report.py)
- **Produces:** `tmp/deal-report.json` (data record) + `reports/deal-report.html` (deliverable). At-a-glance prints to stdout.
- **What to do:** same `set -a` + absolute-path rules as the weekly report (`.env` must be exported for the `uv` child). The script reuses the weekly report's data layer (`pull_pipeline` / `pull_notes`) via a `sys.path` insert, so it shares owners/pipelines/HubSpot helpers — keep those in sync.

  ```bash
  set -a && source /Users/travisfoster/claude-code/cerkl/.env 2>/dev/null && set +a
  uv run /Users/travisfoster/claude-code/cerkl/sales/deal-report/scripts/pull_deals.py
  # one rep:  … pull_deals.py --owner Marc
  ```

  Read the at-a-glance. **This step is complete on its own** — a full rules-based health board. Stop here for a fast structural run. To re-render after a CSS/score tweak without re-pulling: `uv run scripts/render_deal_report.py tmp/deal-report.json`.

### Step 2 — Inference pass on flagged deals (Phase 2 — NOT BUILT YET)
- **Owner:** Claude (sub-agent, per flagged deal or small batch)
- **Needs:** `skills/deal-health-analyst/SKILL.md` + cleaned email threads for the flagged deals
- **What to do:** for deals banded `watch`/`at_risk` (or one Travis names), dispatch the `deal-health-analyst` sub-agent against the **cleaned** thread text (never raw HTML — the orchestrator never loads bodies). It returns sentiment, the open next-step (or its absence), and a short risk narrative. The render merges these into the flagged deals' rows. See "Phase 2" below for what's required to switch this on.

### Step 3 — Render to shareable PDF (optional)
- **Owner:** Claude
- **Needs:** [`html-to-pdf` skill](../../skills/html-to-pdf/SKILL.md) (Chrome headless)
- **Inputs:** `reports/deal-report.html` from Step 1 — independent of the Step 2 inference pass; run it whenever you want a forwardable copy.
- **Produces:** `reports/deal-report.pdf` — a print-format sibling, gitignored alongside the HTML (deal-level PII; local-only, no Drive/Chat).
- **What to do:** when Travis wants something to forward (the HTML is a local `file://` dashboard not everyone can open), render the PDF with the workspace `html-to-pdf` skill in **`--single-page`** mode. The deal report is a digital, zoomable artifact, not a printout — `--single-page` measures the rendered content height and emits **one continuous page sized to the content**, so no deal row is ever sliced across a page boundary (the failure US-Letter pagination caused). It's a single-flow dashboard (`hero` + `wrap`) with no `.page` divs, so `--single-page` skips the overflow gate automatically — no separate `--skip-verify` needed. No `.env` / `set -a` needed (Chrome only, no HubSpot call).

  ```bash
  bash /Users/travisfoster/claude-code/cerkl/skills/html-to-pdf/run.sh \
    /Users/travisfoster/claude-code/cerkl/sales/deal-report/reports/deal-report.html \
    /Users/travisfoster/claude-code/cerkl/sales/deal-report/reports/deal-report.pdf \
    --single-page
  ```

  The skill prints the content dimensions and confirms `1 page` (e.g. `12.3×130.5in` for the full trio — taller with more deals, shorter for a single-rep `--owner` run). Density matches the on-screen dashboard; the reader zooms. `open <pdf>` to eyeball before sending. (If the pipeline ever needs a paper-printable version instead, drop `--single-page` for the default US-Letter mode — `tr`-level `break-inside` rules in the shared print CSS keep rows whole there too.)

---

## Output
- `reports/deal-report.html` — the deliverable (gitignored — deal-level PII). Rendered deterministically; reuses the weekly report's CSS verbatim (single styling source) plus a small band-badge block.
- `reports/deal-report.pdf` — optional print-format sibling for sharing (Step 3); gitignored alongside the HTML.
- `tmp/deal-report.json` — the scored data record (gitignored).
- No Drive upload, no Chat post — read/forward the HTML or PDF locally (PII).

## Phase 2 — email-conversation ingestion (planned, not built)
The big enrichment. What it takes:
- **Pull bodies** — scope already granted; `hs_email_text` / `hs_email_html` (the preview fields are truncated). Associate to deals with the same v4 batch pattern Phase 1 uses.
- **Clean in Python (the 99%)** — strip HTML, drop signatures / quoted reply chains / legal footers / auto-replies, reconstruct threads (`hs_in_reply_to_engagement_id`), and **redact PII** in any artifact that could travel. Raw + cleaned bodies stay in gitignored `tmp/` only.
- **Infer on flagged deals only (the 1%)** — `deal-health-analyst` reads cleaned threads → sentiment / next-step / risk narrative. Bounded: a handful of flagged deals, never the whole pipeline.

### PII handling (design rule, applies now and in Phase 2)
- Raw and cleaned email bodies live **only** in gitignored `tmp/`. Never upload to Drive/Chat.
- The cleaning pass redacts obvious PII (emails, phone numbers) from any summary artifact; full cleaned text is read by the sub-agent locally and not persisted to a shared surface.
- `reports/` (HTML + PDF) and `tmp/` are both gitignored for this folder.

## Future work
- **Velocity benchmarks:** derive "normal" stage durations from closed-won history so stage-age risk is relative, not absolute thresholds.
- **Engaged-contact multithreading:** count contacts with *activity*, not just associated contacts.
- **Tracked-ratio surfacing:** the JSON already carries tracked/untracked per deal — roll up a per-rep tracked-ratio (data-quality + a nudge) into the HTML.
- **Meeting outcomes from notes:** once reps log post-meeting notes, infer held/no-show + outcome (no transcripts in v1).
- **Mission Control surfacing:** add a Launch/Run tile like the weekly report.
- **Weekly enrichment hook:** when fresh, fold the at-risk list into the weekly Sales Pipeline Report.
- **Score calibration:** first run skews heavily at-risk (the pipeline is genuinely stale, esp. Marc) — revisit weights/thresholds in `score.py` once the nurture cleanup happens.

## Learnings
- **2026-06-30 — Added the shareable-PDF step (Step 3), single-page mode.** First cut used the skill's default US-Letter pagination, which **sliced deal rows across page breaks** (a 55-deal owner table is taller than a page, so the existing `section { page-break-inside: avoid }` rule can't hold and Chrome falls back to slicing — that's what cut "Lees Famous"). Since the deliverable is digital + zoomable, not printed, the fix was a new **`--single-page`** mode on the shared `html-to-pdf` skill: it measures the rendered content height and emits **one content-sized page** (e.g. 12.3×130.5in for the trio) — zero internal breaks, nothing can be sliced. **Why a new mode, not a new skill:** PDF-export of a scrolling dashboard is reusable across every report (weekly, mission-control, content-dashboard), so it's a capability of the existing skill, not a wrapper around it. **Implementation note:** CSS alone can't size `@page` to content height, and no crop tools (`gs`/`pdfcrop`) are installed — so `single_page.mjs` drives the installed Chrome over the DevTools Protocol using **Node's built-in `WebSocket`/`fetch` (Node ≥22), zero npm installs**: measure `scrollHeight` → `Page.printToPDF` at that exact paper size, `pageRanges:'1'`. Also hardened the shared print CSS with `tr { break-inside: avoid }` + `thead { display: table-header-group }` so the Letter *fallback* keeps rows whole too. PDF lands in the already-gitignored `reports/`, so PII stays local with no new ignore rule.
- **2026-06-22 — Built Phase 1.** Reuses the weekly report's `pull_pipeline`/`pull_notes` via a `sys.path` insert (shared owners/pipelines/HubSpot helpers). **Gotchas:** (1) batch reads requesting `propertiesWithHistory` cap at **50 inputs**, not 100 — a 78-deal chunk 400s; chunk at 50. (2) HubSpot count props (`hs_email_open_count`) come back as float strings (`"5.0"`) — parse via `float()` (`pp._int`) or they silently zero. (3) Must exclude the `is_holding` Nurture stage or the set balloons (359 → 77) and drowns the active pipeline. First run: 77 active deals, 57 at-risk (Marc 44/55), 42 nurture candidates, 282 nurture-stage deals excluded — the stale-pipeline reality the report exists to surface.
