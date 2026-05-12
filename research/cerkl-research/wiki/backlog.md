# Backlog

Deferred process improvements and schema-change proposals. CLAUDE.md governs the current schema; this file tracks what should change next.

---

## [2026-05-11] Schema observation — channel-level topics
- Added topic [[internal-email]] during ContactMonkey ingest. Not in original CLAUDE.md taxonomy. It's a channel-level topic (parallel to existing `intranet-and-digital-workplace`).
- Consider: do we add other channel-level topics — `manager-cascade`, `mobile-employee-apps`, `town-halls-and-all-hands`, `digital-signage`, `video-comms` — when first touched?
- Consider: should `intranet-and-digital-workplace` split into a discipline-level topic (digital workplace strategy) and a channel-level topic (intranet platform)?
- Decision needed before next batch of channel-specific sources lands.

## [2026-05-11] Schema observation — `employee-listening` as concept vs topic
- Created [[employee-listening]] as a concept (in `wiki/concepts/`). It could also be a topic, since it has its own vendor category, framework conversations, and primary sources.
- Current view: concept is right — the surface area is narrower than the broad IC-discipline topics (frontline, engagement, EX). Listening is *one practice within EX*.
- Re-evaluate if a second listening-focused source lands and the concept page starts feeling cramped.

## [2026-05-11] Open: independent (non-vendor) internal-email benchmark sources
- [[contactmonkey]] and [[workshop]] are the only ingested email-related sources — both vendor-tier. Need a non-vendor cross-check (Ragan, IABC, Poppulo Research) to honor the "primary > analyst > vendor" anchoring rule.
- Add to lint pass: when [[internal-email]] has only vendor-tier sources, flag "authority skew" and recommend new sources.

## [2026-05-11] Schema decisions confirmed by Travis
- **Channel-level topics:** add when first touched. Confirmed by creating [[manager-cascade]] from [[six-internal-comms-trends-2026]].
- **[[employee-listening]] → topic upgrade:** confirmed for when a second listening-focused source lands. Concept page is current placeholder; promote to topic on second touch.
- **Authority-skew flagging on [[internal-email]]:** confirmed.

## [2026-05-11] Open: prior-Workshop-report YoY comparison
- Workshop publishes the *Internal Comms Trends Report* annually. The 2025 edition (if it exists) would allow YoY comparison on manager-cascade gap, AI usage, channel effectiveness.
- Worth ingesting if available — would let us say "the manager-cascade gap widened/narrowed from X to Y."

## [2026-05-11] Open: cascade-effectiveness primary-research source
- [[manager-cascade]] currently rests on a single vendor-tier source. Strong candidate for the Edelman Trust Barometer (which measures employee trust by source: managers, executives, peers). Add to ingest queue when convenient.
