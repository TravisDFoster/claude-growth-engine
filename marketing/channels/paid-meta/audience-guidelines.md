# Audience Guidelines

> Audience definitions, exclusion rules, and the system for adding / promoting audiences as test data accumulates.

**Last updated:** 2026-05-27

---

## HubSpot source lists (for Meta Custom Audience uploads)

Active lists in HubSpot that drive Meta audience CSV exports. Re-export each list when refreshing Meta audiences (cadence per Source data inventory below).

| HubSpot list | listId | Object | Type | Purpose | Count (2026-05-27) |
|---|---|---|---|---|---|
| Meta Seed — Foundations Sign-ups | *UI-built* | Contact | Dynamic | LAL seed (cell A) | ~115 expected |
| Meta Exclusion — Demo Requests | 1658 | Contact | Dynamic | Exclusion for cells A, B | 631 |

**Recommended export fields** (same set for both, for Meta match quality):
`email, firstname, lastname, phone, city, state, country, zip, company, jobtitle`

### Foundations seed — UI filter recipe

The public Lists v3 API doesn't expose cross-object filtering on contact lists (ASSOCIATION filter type is rejected; only PROPERTY / IN_LIST / FORM_SUBMISSION / EVENT / etc. are allowed). Build this list in the HubSpot UI:

1. Lists → Create list → **Active list** → Object: **Contacts**
2. Name: `Meta Seed — Foundations Sign-ups`
3. Filter group:
   - Associated deal → **Pipeline** is any of → `Email Foundations`
   - AND Associated deal → **Deal stage** is none of → `Abandoned Account`
4. Expected count: **~115 contacts** (113 deals across 4 non-Abandoned stages, ~115 unique associated contacts)
5. Paste this into the list description: `Used as Custom Audience SEED for Meta 1% US+CA Lookalike (cell A). Export fields: email, firstname, lastname, phone, city, state, country, zip, company, jobtitle.`

### Demo exclusion — definition (already built via API, listId 1658)

OR'd union of submissions on either demo form:
- `Schedule a Chat (Webflow)` (id `c0af68f9-b9e5-4222-bc09-c7552fafe13b`) — current form, 77 submissions
- `Schedule a Demo` (id `35ac2c2b-d2f5-440d-ac80-aa7a80102d62`) — legacy pre-Webflow, 904 historical submissions
- *Excluded:* `Schedule a Demo - NO EMAIL FOLLOW UP (Paycor)` — 4 records, partner-specific, stale

---

## Test 1 audiences (pre-launch — designed 2026-05-21)

| Cell | Audience | Definition | Hypothesis |
|---|---|---|---|
| **A** | 1% US + CA LAL | Lookalike (1%, US + CA), seeded from Foundations sign-up + demo-request emails (~115 records as of 2026-05-21) | Meta can extrapolate from existing-user shape to find similar internal-comms owners at scale |
| **B** | Cold interest stack | Title targets (Internal Communications, Employee Communications, Internal Comms Manager) **AND** interests (Employee engagement, Workplace from Meta, Slack as business interest, Microsoft Teams as business interest). US + CA. | Meta's title + interest graph is usable for cold acquisition of our buyer — independent of first-party seed |
| **C** | Retargeting (warm) | Pixel-fired Cerkl.com visitors past 180 days + IG/FB account engagers past 90 days. US + CA. | Warm audience sets the "hot floor" CPC / CPL benchmark to compare cold cells (A, B) against |

## Exclusion list (applies to all cold cells — A and B)

- Existing Foundations users (email list export from Foundations DB)
- Paid customers (email list export from CRM)

**Why:** don't pay to retarget current customers. Cell C is retargeting by design, so the exclusion applies to A and B only.

## System for adding new audiences

Each test cycle, new audiences enter via one of three paths:

1. **Variant of a winner** — narrow or broaden a cell that won test N. Example: if cell A (1% LAL) wins test 1, test 2 could compare 1% vs. 2% vs. 3% LAL. New audience block goes here with the parent winner referenced.
2. **Net-new hypothesis** — different angle, different data source. Example: lookalike seeded from email-engaged employees (if that data becomes available). New audience block lists the hypothesis explicitly so we know what we're learning.
3. **Promoted to production** — a cell that's won 2+ tests with stable CPC/CPL gets promoted to the "Production audiences" section below and runs as an always-on campaign.

**Every new audience must include:** definition, source data + freshness, hypothesis, success metric. **TK signs off** before the audience runs.

## Production audiences

*None yet — pending test 1 results.*

## Retired audiences

*None yet — track here as audiences are deprecated, with the reason and final CPC/CPL.*

## Source data inventory

| Source | Records | Freshness | Used for |
|---|---|---|---|
| Foundations sign-ups (HubSpot — Email Foundations pipeline, non-Abandoned) | 115 (as of 2026-05-27) | Active list auto-refreshes; re-export to Meta monthly | LAL seed (cell A) |
| Demo-request submissions (HubSpot — Schedule a Chat + Schedule a Demo forms) | 631 (as of 2026-05-27) | Active list auto-refreshes; re-export to Meta monthly | Exclusion from A, B |
| Cerkl.com visitors (Pixel) | Continuous | Auto via Pixel; 180-day lookback | Retargeting (cell C) |
| IG / FB account engagers | Continuous | Auto via Meta; 90-day lookback | Retargeting (cell C) |

**Decision log (2026-05-27):** Demo-request contacts moved from seed to exclusion. Rationale — demo intent skews enterprise (sales pipeline) while Foundations is a free-product CTA; including demos in the LAL would muddy the seed shape. Paid-customer exclusion and existing-Foundations-user exclusion are out of scope for these two lists; revisit if Meta audience match-quality flags retargeting of current customers.
