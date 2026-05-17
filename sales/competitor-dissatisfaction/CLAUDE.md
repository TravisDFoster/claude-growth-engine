# Identity

You are helping Travis Foster mine dissatisfied users of internal-comms competitors from public review sites, forums, and communities — enrich them to contact + account level, and hand off targeted rows to Marc Fregoe + Josh Mandelman.

## Context to load

- /Users/travisfoster/claude-code/cerkl/shared/company-info.md
- /Users/travisfoster/claude-code/cerkl/shared/icp.md
- /Users/travisfoster/claude-code/cerkl/shared/competitors.md
- /Users/travisfoster/claude-code/cerkl/shared/broadcast.md
- /Users/travisfoster/claude-code/cerkl/sales/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/sales/competitor-dissatisfaction/methodology.md

(Per [PRINCIPLES.md #4](../../PRINCIPLES.md), this list replaces the parent `sales/` load. The methodology is the central artifact — always loaded.)

**Referenced (not loaded):** [customer-research](../../marketing/skills/customer-research/SKILL.md) (Mode 2 is the primary engine), [competitor-profiling](../../marketing/skills/competitor-profiling/SKILL.md), [cold-email](../../marketing/skills/cold-email/SKILL.md). Invoke when the task matches their description.

## Scope

- **Signal source:** public reviews, forums, communities — *not* corporate pressure events (that's [Pressure Prospecting](../pressure-prospecting/CLAUDE.md)).
- **Competitors:** anchor on [`shared/competitors.md`](../../shared/competitors.md); breadth over narrowing per Travis's call.
- **Sizes:** match `shared/icp.md` — enterprise/midmarket primary, Foundations-tier secondary.
- **Consumers:** Marc Fregoe + Josh Mandelman (AEs). They run outbound; this folder produces the enriched list.

## Phase status (as of 2026-05-14)

| Phase | State | Notes |
|---|---|---|
| Phase 1 — Methodology | **Scaffolded** | [methodology.md](methodology.md) drafted; needs Travis sign-off on bucket names, filter thresholds, enrichment schema. |
| Phase 2 — Sample run | Not started | 1 competitor × 2 source surfaces (likely G2 + Reddit) to tune the dissatisfaction filter. |
| Phase 3 — First full run | Target Fri 2026-05-22 | Top 3 competitors across locked source surfaces; full enrichment + HubSpot dedupe; handoff to AEs. |
| Phase 4 — Operationalize | Not started | Decide cadence (weekly/biweekly), automate where viable. |

## File structure

```
sales/competitor-dissatisfaction/
├── CLAUDE.md           ← this file (router + decisions)
├── methodology.md      ← signal taxonomy, filter, schema, buckets, handoff (always loaded)
├── competitor-dissatisfaction-mining-process.md  ← orchestrator
├── handoffs/           ← created at runtime; YYYY-MM-DD.md master per run
└── raw/                ← created at runtime; <competitor-slug>/YYYY-MM-DD/ per scrape
```

## Key decisions and rationale (preserve across sessions)

### Sibling to pressure-prospecting, not folded under it
Pressure Prospecting's CLAUDE.md scopes vendor dissatisfaction out and points here. Signal source is mechanically different (public review mining vs. corporate pressure events) even though both feed the same AEs. Same consumers + parallel handoff schema = Marc/Josh can consume both without context-switching.

### Scraping tool is a Step-1-at-runtime decision
The methodology is tool-agnostic. Apify vs. BrightData vs. ScrapingBee vs. custom Python is decided at the start of each run — keeps the methodology stable across tool churn.

### Confidence framework borrowed from Pressure Prospecting
High / Medium / Low (per `customer-research` Mode 2 and pressure-prospecting methodology §1). Tier-S dissatisfaction signals require **High** source confidence — verifiable reviewer identity (real name + company OR named role at named company). An unverified 1-star review is a *lead to verify*, not a Tier-S row.

### Bucket = outbound posture, not user state
Parallel to pressure-prospecting. The bucket tells Marc/Josh how to pitch:
- **Active Switcher** → pitch now (explicit "looking for alternative to X")
- **Vocal Critic** → tactical (specific feature/measurement angle)
- **Frustrated User** → warm sequence (general dissatisfaction, no clear angle)
- **Vendor Burnout** → strategic (long-tenured user complaining about platform overall)

Final bucket names + thresholds pending Travis review of [methodology.md](methodology.md).

## What's still hypothetical — validate in sample run

- Whether 4 buckets survive contact with the data, or one collapses
- Recency window (12-month default per `customer-research`) — may need tightening for SaaS where vendor pivots happen fast
- Whether the dissatisfaction filter catches signal without drowning in false positives (Travis's stated risk in the PA brief)

## Open calls for Travis before sample run

- Confirm bucket names + outbound posture per bucket (methodology §5)
- Confirm dissatisfaction filter thresholds (methodology §3) — star rating, recency, keyword categories
- Confirm enrichment schema fields and HubSpot dedupe policy (methodology §4)
- Pick sample-run competitor (1 × 2 surfaces)

## Rules

- Tier-S signals require High source confidence — verified reviewer identity. No exceptions.
- All mined evidence goes in dated `raw/<slug>/YYYY-MM-DD/` folders — never overwrite a prior date.
- Methodology is the source of truth for signal taxonomy + handoff schema; CLAUDE.md carries decisions only.

## Personal Assistant — Push-Update Protocol

When work in this folder advances the project tracked at [`personal-assistant/projects/competitor-dissatisfaction-mining.md`](../../personal-assistant/projects/competitor-dissatisfaction-mining.md), append an update block at the bottom of that file before ending the session:

```
## Update — YYYY-MM-DD (from sales/)
- Completed: <task>
- Status change: <if any>
- New blocker: <if any>
- Proposed next step: <one line>
```

Use absolute dates (YYYY-MM-DD). Do not edit `personal-assistant/INDEX.md` directly — PA's `refresh` skill reconciles update blocks into INDEX.
