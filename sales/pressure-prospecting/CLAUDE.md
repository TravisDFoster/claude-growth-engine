# Identity

You are helping Travis Foster build and run the Pressure Prospecting outbound motion — identifying Tech/SaaS + Healthcare companies (enterprise/midmarket) under organizational pressure where internal comms is operating under stress, and producing handoff rows for Marc Fregoe + Josh Mandelman.

## Context to load

- /Users/travisfoster/claude-code/cerkl/shared/company-info.md
- /Users/travisfoster/claude-code/cerkl/shared/icp.md
- /Users/travisfoster/claude-code/cerkl/shared/competitors.md
- /Users/travisfoster/claude-code/cerkl/shared/broadcast.md
- /Users/travisfoster/claude-code/cerkl/sales/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/sales/pressure-prospecting/methodology.md

(Per [PRINCIPLES.md #4](../../PRINCIPLES.md), this list replaces the parent `sales/` load. The Pressure Prospecting methodology is the central artifact — always loaded.)

**Referenced (not loaded):** [cold-email](../../marketing/skills/cold-email/SKILL.md), [customer-research](../../marketing/skills/customer-research/SKILL.md), [competitor-profiling](../../marketing/skills/competitor-profiling/SKILL.md), [sales-enablement](../../marketing/skills/sales-enablement/SKILL.md). Invoke when the task matches their description.

## Scope

- **Verticals:** Tech/SaaS + Healthcare only (Phase 1 + Phase 3 pilot).
- **Sizes:** Enterprise/midmarket only — 501–12k+ employees per `shared/icp.md`.
- **Out of scope:** SMB (separate Foundations growth motion), vendor dissatisfaction (that's [Competitor Dissatisfaction Mining](../../personal-assistant/projects/competitor-dissatisfaction-mining.md)).
- **Consumers:** Marc Fregoe + Josh Mandelman (AEs). They run the outbound; this folder produces the list.

## Phase status (as of 2026-05-14)

| Phase | State | Notes |
|---|---|---|
| Phase 1 — Methodology | **Done** | [methodology.md](methodology.md) covers signal taxonomy, source confidence, bucket model, emotional read, voice rules, handoff schema, evidence storage. |
| Phase 2 — Sources + tooling | Not started | Owner TBD. Decide: manual vs. semi-automated; HubSpot import vs. shared Google Sheet vs. Doc. |
| Phase 3 — Pilot (20–40 accounts) | Not started | Success criterion for the whole project. |
| Phase 4 — Post-pilot retro | Not started | Decide future cadence; update methodology Learnings section. |

## File structure

```
sales/pressure-prospecting/
├── CLAUDE.md           ← this file (router + decisions)
├── methodology.md      ← the methodology (always loaded)
└── raw/                ← dated source archives (per account); created during Phase 3
    └── <account-slug>/
        └── YYYY-MM-DD/
            ├── articles/
            ├── filings/
            └── notes.md
```

## Key decisions and rationale (preserve across sessions)

### Tier ≠ bucket — the trap to avoid
Tier (S/A/B) = how hot the *signal* is. Bucket = how to *talk to* the company. A Tier-S CHRO exit puts an account in Transition Shock (pitch now). A Tier-S layoff puts the same-sized company in Acute Crisis (hold). Future sessions will get this wrong without re-reading methodology §2. If a row's `signal_tier` and `bucket` feel mismatched, that's usually the trap, not a real mismatch.

### Why we kept 4 buckets (not 3)
Considered collapsing Acute Crisis into Aftermath since the action is "hold, don't pitch." Kept it so Marc/Josh can plan the +60-day re-entry without losing the account from view. If the Phase 3 pilot shows Acute Crisis rows are noise (AEs never re-pursue), the call is to move them to a separate "watch" tab — not delete them.

### Source confidence is the bouncer — do not relax under pilot pressure
Tier-S signals require **High** source confidence (official filing or ≥2 independent reputable outlets). This is the rule most likely to break when we're hunting volume: "but Layoffs.fyi says…" An unverified single-source Tier-S is a *lead to verify*, not a row to ship. Padding the list with Medium-confidence Tier-S rows ruins the list's reputation with sales fast.

### Bucket = outbound posture, not company state
The methodology's central insight. Each bucket maps to a playbook:
- **Acute Crisis** → don't pitch; warm-touch only; revisit +60d
- **Aftermath** → prime window; lead with measurement/retention
- **Transition Shock** → audit-window; lead with consolidation
- **Sustained Strain** → tactical; lead with "prove the message is landing"

If a bucket assignment isn't clearly mapped to one of these postures, the row isn't ready.

### Bucket naming evolved from Travis's working hypothesis
- "Sustained pressure" → **Aftermath** (the most consequential rename — captures the *post-crisis reflection window*, which is our best pursuit moment, not just "things are bad")
- "Quiet stress" → **Sustained Strain**
- Acute Crisis + Transition Shock kept as-is

### Vendored skills are referenced, not moved
`marketing/skills/` is vendored from `coreyhaines31/marketingskills`. Cold-email, sales-enablement, customer-research, and competitor-profiling are routed from sales by absolute path — see parent [sales/CLAUDE.md](../CLAUDE.md#vendored-skills-referenced-from-sales). Do not fork or move. The physical location under `marketing/` is a vendoring artifact, not a claim about ownership.

### Methodology was refined from a vendored-skill review (2026-05-14)
The methodology's §1 source-confidence framework, §4 voice rules, and §5 dated-snapshot storage were pulled from reading `cold-email`, `customer-research`, and `competitor-profiling` SKILLs. Reading more vendored skills (e.g., `sales-enablement`'s objection categories) may surface more refinements. Especially worth a pass after Phase 3 pilot.

## What's still hypothetical — validate in Phase 3 pilot

- The 60-day Acute → Aftermath transition window. May be too short for healthcare regulatory crises (FDA letters often resolve over 6+ months internally).
- Whether 4 buckets survive contact with the pilot, or one collapses.
- Bucket-specific reply-rate hypothesis: Aftermath > Transition Shock > Sustained Strain >> Acute.
- Whether the sales-craft bucket framing translates into copy that gets replies — Marc/Josh are the final validators.
- Whether `contact-first` (de-prioritize accounts without a findable comms/HR contact) is the right pilot filter, or whether logo-strong accounts without a contact still belong.

## Open calls for Travis before pilot

- Confirm the signal taxonomy default tiers and modifiers (methodology §1).
- Confirm voice/format rules (methodology §4 voice block).
- Confirm angle direction per bucket (methodology §4 bucket angles).
- Pick Phase 2 owner — `sales/` to drive sources + tooling, or hand off?
- Set target pilot date.
- Confirm 20–40 is still the pilot volume target.

## Rules

- Tier-S signals require High source confidence. No exceptions.
- Bucket = posture (what to do), not company state (what's happening). If unclear, re-read methodology §2.
- All Phase 2/3 evidence goes in dated `raw/<slug>/YYYY-MM-DD/` folders — never overwrite a prior date.

## Personal Assistant — Push-Update Protocol

When work in this folder advances the project tracked at [`personal-assistant/projects/pressure-prospecting.md`](../../personal-assistant/projects/pressure-prospecting.md), append an update block at the bottom of that file before ending the session:

```
## Update — YYYY-MM-DD (from sales/)
- Completed: <task>
- Status change: <if any>
- New blocker: <if any>
- Proposed next step: <one line>
```

Use absolute dates (YYYY-MM-DD). Do not edit `personal-assistant/INDEX.md` directly — PA's `refresh` skill reconciles update blocks into INDEX.
