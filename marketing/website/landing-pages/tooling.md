# Landing Page A/B Testing — Tooling & Conventions

> Source of truth for how Cerkl runs landing-page experiments. Read before designing a test.

## Stack

| Layer | Tool | Purpose |
|---|---|---|
| Site builder | Webflow | cerkl.com — pages live here |
| Experimentation | **PostHog** | A/B test platform + analytics + session replay + heatmaps + feature flags |
| Analytics (existing) | Google Analytics 4 | Top-of-funnel traffic, retained alongside PostHog until sunset decision |

## Why PostHog (decision recorded 2026-05-11)
- Bayesian stats engine — calls winners on smaller samples (critical at ~500 uniques/wk per page)
- Free tier covers cerkl.com volume many times over
- A/B + session replay + heatmaps in one tool — qualitative fills the gap when statistical significance is slow at our traffic
- Open source backstop if data residency ever matters
- Plays naturally with the `analytics-tracking` skill since events are unified in one platform

## Installation
- PostHog JS snippet lives in Webflow Project Settings → Custom Code → Head
- Snippet + project API key tracked in 1Password (entry: "PostHog — cerkl.com")
- Verify on every page with `posthog._isIdentified()` in browser console (returns true once a user is identified)

## Event naming convention
| Event | When it fires | Properties to capture |
|---|---|---|
| `lp_view` | Landing page loads (auto via `$pageview`) | page_slug, traffic_source |
| `lp_cta_click` | Primary CTA on a landing page is clicked | page_slug, cta_label, cta_position |
| `lp_secondary_cta_click` | Any non-primary CTA click | page_slug, cta_label |
| `signup_started` | Foundations signup form opens | source_page_slug |
| `signup_completed` | Foundations account created | source_page_slug, plan |

Custom per-page events: prefix with `lp_<page-slug>_` to keep page-specific tagging clean (e.g. `lp_why-pay_pricing_anchor_view`).

## Metric framework (locked)
- **Primary metric (per test):** CTA click-through — `lp_view` → `lp_cta_click`
- **Guardrail metric (per test):** Foundations signup direction — `lp_view` → `signup_completed`. Watch direction; do **not** gate test calls on signup significance.
- **Quarterly aggregate:** total Foundations signups attributed to landing pages, all tests rolled up. This is where signup impact actually gets evaluated.

**Why this split:** at ~500 uniques/wk per page, signup-as-primary needs ~30+ weeks per test to reach significance (see [ab-test-setup sample tables](../../skills/ab-test-setup/SKILL.md#sample-size)). CTA click-through reaches significance in ~2–3 weeks at 50% MDE. Signup is the real KPI, but we measure it on the quarter, not the test.

## Test design defaults
- One hypothesis per test
- 50/50 split unless risk-mitigating (then 80/20 control-heavy)
- **Minimum Detectable Effect: 50% relative lift** (anything smaller exceeds our traffic budget)
- Run duration: 3-week fixed commit minimum, longer if sample math demands
- No peeking-to-stop, but PostHog's Bayesian view is fine for monitoring direction
- Variant changes mid-test = test invalid, restart

## Webflow + PostHog implementation patterns

**Copy-only variants (most common):** PostHog Feature Flags drive text swaps via inline JS. Element selectors target Webflow class names. No new pages needed.

**Layout/structural variants:** build the challenger as `/broadcast/<slug>-v2` in Webflow, use PostHog "split URL" experiment to redirect % of traffic.

**Element-level variants (CTA copy, button color, hero image):** PostHog Feature Flag + conditional in Custom Code embed at page level.

Default to copy-only — fastest to ship and matches our hypothesis bias (messaging, not design).

## Roles
- **Travis:** hypothesis approval, Webflow build, PostHog experiment configuration & launch, results readout from PostHog
- **Claude:** audit, hypothesis generation, variant copy drafts, test design doc, results synthesis from PostHog screenshots/exports Travis shares

## Future tooling work
- Decide whether GA4 stays alongside PostHog or sunsets
- Evaluate PostHog's `Web Analytics` product as GA4 replacement
- Add Microsoft Clarity if PostHog session replay quota becomes a constraint
- Schedule monthly backlog re-score (wire to /schedule when available)
