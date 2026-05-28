# System Status

> Living checklist of account-level prerequisites for Meta paid campaigns. Update inline as items change state — this file is loaded into context on every paid-meta task.

**Last reviewed:** 2026-05-27

---

## Account access

| Item | Status | Notes |
|---|---|---|
| Meta Business Manager access | ✅ Restored 2026-05-14 | IT + Meta support resolved access. Unblock conversation w/ Joey at SEM Sync 2026-05-13. |
| Page ownership verification | ✅ Confirmed 2026-05-14 | Verified during Phase 1 unblock. |

## Tracking infrastructure

| Item | Status | Notes |
|---|---|---|
| Meta Pixel installed on Cerkl.com | ❓ Verify | Hard prerequisite — required for retargeting (cell C) and Leads-objective optimization |
| Conversions API (CAPI) wired | ❓ Verify | Hard prerequisite — required for reliable Leads optimization post-iOS 14.5 |
| Foundations sign-up conversion event firing | ❓ Verify — **hard blocker** | Required before any Leads-objective campaign can launch. Verify in Events Manager: event fires, deduped between Pixel + CAPI, attributed to correct domain. |
| Domain verification (cerkl.com) | ❓ Verify | Required for accurate iOS 14.5+ aggregated event measurement |
| Aggregated Event Measurement priority order | ❓ Verify | If domain is verified, confirm Foundations sign-up is priority 1 on the event list |

## HubSpot source lists (CSV inputs to Meta)

| Item | Status | Notes |
|---|---|---|
| HubSpot list — Meta Seed — Foundations Sign-ups | ⏳ Build in UI | Recipe in [audience-guidelines.md](audience-guidelines.md). ~115 contacts expected. Public Lists v3 API can't create cross-object contact lists; UI required. |
| HubSpot list — Meta Exclusion — Demo Requests | ✅ Built 2026-05-27 (listId 1658) | 631 unique contacts. Active. Re-export monthly. |

## Audiences (Meta side)

| Item | Status | Notes |
|---|---|---|
| Custom Audience — Foundations sign-up emails | ❓ To build | Upload CSV exported from HubSpot list `Meta Seed — Foundations Sign-ups` after CAPI verification |
| Lookalike — 1% US + CA from above | ❓ To build | Cell A in test 1 |
| Custom Audience — Demo requests (exclusion) | ❓ To build | Upload CSV exported from HubSpot list `Meta Exclusion — Demo Requests` (listId 1658) |
| Custom Audience — Pixel visitors 180d | ❓ To build (auto once Pixel is live) | Cell C in test 1 |
| Custom Audience — IG / FB engagers 90d | ❓ To build (auto) | Cell C in test 1 |

## Creative

| Item | Status | Notes |
|---|---|---|
| Pains-concept storyboard | Not started | Reuse paid-youtube hook skills for first pass |
| Pains-concept video render | Not started | Depends on AI video tool selection — see [design-tools.md](../../../personal-assistant/projects/design-tools.md) |
| Aspect-ratio variants needed | 9:16 (Stories/Reels), 1:1 (Feed), 4:5 (Feed) | Plan native variants if budget supports; for test 1 a single placement may be acceptable |

## Open questions for TK

- Conversion event setup status (above) — TK owns timeline to resolve
- Whether the Segment → Google Ads attribution plumbing (separate "Ad Conversion Tracking" project) shares any CAPI infrastructure we can reuse for Meta
