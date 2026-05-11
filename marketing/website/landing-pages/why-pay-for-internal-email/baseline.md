# Baseline — /broadcast/why-pay-for-internal-email

> First page workspace; this baseline is the template every future page will follow.
> Re-pull before each test design.

## Page
- **URL:** https://cerkl.com/broadcast/why-pay-for-internal-email
- **Slug:** `why-pay-for-internal-email`
- **Type:** Acquisition landing page (long-form / SEO-targeted)
- **Audience:** SMB internal comms teams and people leaders evaluating whether to pay for an internal email tool

## Traffic (as of 2026-05-11)
- **Unique visitors / week:** ~500 (per GA4)
- **Sessions / week:** ~2,000–3,000 (GA4 — includes returning visitors and bot/refresh inflation; PostHog should be reconciled)
- **Top traffic sources:** *(TBD — Travis to pull from GA4 acquisition report)*

## Current metrics
*All TBD until tracking precheck (Step 2) confirms PostHog events are live for this page.*

- **Primary CTA:** *(TBD — capture from current page on first audit)*
- **Primary CTA click rate (`lp_view` → `lp_cta_click`):** TBD
- **Foundations signup conversion (`lp_view` → `signup_completed`):** TBD

## Sample-size implications

Working back from `tooling.md` defaults (MDE = 50% relative lift, 50/50 split, 250 visitors/variant/week):

| Primary metric | Plausible baseline | Sample/variant | Weeks needed |
|---|---|---|---|
| CTA click-through | 10% | ~550 | ~2–3 weeks ✓ |
| CTA click-through | 5% | ~1,200 | ~5 weeks |
| Foundations signup | 2% | ~7,500 | ~30 weeks (not viable per-test) |

Primary metric for tests on this page = **CTA click-through**. Foundations signup is a guardrail + quarterly aggregate.

## Notes
- Baseline first pulled: 2026-05-11
- Re-pull cadence: before each new test design
- Workspace created as part of building out the landing-page CRO process
