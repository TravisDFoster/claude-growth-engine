# Wiki Log

Append-only operation log. One entry per ingest, query, lint, or init. Newest at the bottom.
Header format: `## [YYYY-MM-DD] operation | Title`. Parseable with `grep "^## \[" log.md`.

---

## [2026-05-11] init | Vault scaffolding
- Created CLAUDE.md schema and `wiki/` structure (topics, entities, concepts, sources)
- Topic taxonomy listed in CLAUDE.md (broad IC scope); topic pages lazy-created on first source touch
- Initial state: empty index, no sources ingested

## [2026-05-11] ingest | State of the Global Workplace 2026 (Gallup)
- Source URL: https://www.gallup.com/workplace/697904/state-of-the-global-workplace-global-data.aspx
- Emphasis per Travis: lead with engagement-decline narrative and frontline gap
- Created source: [[state-of-the-global-workplace-2026]]
- Created entity: [[gallup]]
- Created concepts: [[employee-engagement-three-bucket-model]], [[thriving-struggling-suffering]], [[engagement-by-work-location]]
- Created topics: [[employee-engagement]], [[employee-experience]], [[frontline-communications]], [[culture-and-belonging]], [[ic-measurement-and-roi]]
- Updated index.md with all 10 new pages
- Pages touched: 10

## [2026-05-11] ingest | ContactMonkey Internal Email Benchmark Report 2026
- Source URL: https://www.contactmonkey.com/blog/contactmonkeys-internal-email-benchmark-report-2026-key-findings-for-internal-communications-teams
- Mode: batch (no per-source discussion per Travis's direction)
- Created source: [[contactmonkey-internal-email-benchmark-2026]]
- Created entity: [[contactmonkey]]
- Created concepts: [[internal-email-benchmarks]], [[interactive-email-features]]
- Created topic: [[internal-email]] (NEW — not in CLAUDE.md taxonomy; channel-level; flagged in backlog.md)
- Updated topics: [[ic-measurement-and-roi]] (added vendor-tier row), [[frontline-communications]] (added email-channel mirror)
- Pages touched: 7

## [2026-05-11] ingest | Forrester Wave: Intranet Platforms Q2 2026
- Source URL: https://www.forrester.com/blogs/the-forrester-wave-intranet-platforms-q2-2026-our-evaluation-of-13-key-vendors/
- Mode: batch
- Created source: [[forrester-wave-intranet-platforms-q2-2026]]
- Created entities: [[forrester]], [[cheryl-mckinnon]]
- Created concept: [[ai-adoption-gap]]
- Created topics: [[intranet-and-digital-workplace]], [[ai-in-internal-comms]]
- Updated topic: [[frontline-communications]] (added Forrester finding on named frontline criterion)
- Pages touched: 8

## [2026-05-11] ingest | Workvivo Seer launch (internal deep-dive)
- Source: local file `cerkl/research/ic-trends/deepdives/Competitors/workvivo-seer-2026-05-11.md`
- Mode: batch
- Created source: [[workvivo-seer-2026-05-11]]
- Created entities: [[workvivo]], [[seer]], [[justin-black]], [[zoom]], [[glint]], [[culture-amp]], [[peakon]], [[qualtrics]]
- Created concepts: [[employee-listening]], [[people-intelligence]], [[execution-gap]]
- Updated topics: [[intranet-and-digital-workplace]], [[ai-in-internal-comms]], [[employee-experience]] (Workvivo as EX-suite vendor)
- Cited public URLs preserved in source page for blog citation
- Pages touched: 14

## [2026-05-11] ingest | PR Daily — Cisco comms leader on AI-generated content
- Source URL: https://www.prdaily.com/cisco-comms-leader-on-the-real-problem-with-ai-generated-content/
- Mode: batch (with paired Workshop ingest)
- Created source: [[cisco-comms-leader-ai-content]]
- Created entities: [[pr-daily]], [[cisco]], [[austin-roth-eagle]]
- Created concept: [[ai-slop]]
- Updated topic: [[ai-in-internal-comms]] (added practitioner-tier framing)
- Pages touched: 6

## [2026-05-11] query | Stats for IC measurement & analytics blog post
- Query: "What are some interesting stats we can use for our new blog post on measurement and analytics in internal comms?"
- Synthesized stat inventory across all 6 ingested sources, organized by authority tier (primary / analyst / vendor) and by measurement category
- Surfaced three cross-source angles: channel-gap = engagement-gap; AI denominator trap; engagement-wellbeing divergence
- Filed answer back to [[ic-measurement-and-roi]] under new "Citable Stat Anchors" section (per Karpathy's "good answers compound back" rule)

## [2026-05-11] schema | Added Blog Post Research Mode rule to CLAUDE.md
- Rule: when a query is for blog-post / article / external-content research, exclude competitor stats and sources from the answer; surface filtered competitor names at the bottom for awareness
- Competitor list hardcoded directly in CLAUDE.md (token-efficiency: avoids re-reading `shared/competitors.md` on every blog query). Manual sync required if competitors change.
- Retroactively restructured [[ic-measurement-and-roi]] "Citable Stat Anchors" section to comply (filed yesterday as blog-research synthesis)
  - Tier-1 (Gallup) and Tier-2 (Forrester) tables retained
  - Tier-3 (vendor) table removed — all entries were from competitors ([[contactmonkey]], [[workshop]])
  - Added "Competitor sources — do not cite in blog posts" subsection listing [[contactmonkey]], [[workshop]], [[workvivo]] / [[seer]] for internal context only
  - Cross-source patterns rewritten to not depend on competitor data

## [2026-05-11] ingest | PR Daily — Six internal comms trends for 2026 (Workshop)
- Source URL: https://www.prdaily.com/six-internal-comms-trends-every-communicator-should-know-in-2026/
- Mode: batch
- Created source: [[six-internal-comms-trends-2026]]
- Created entity: [[workshop]]
- Created concepts: [[do-more-with-less]], [[employee-influencers]], [[evergreen-content-strategy]]
- Created topics: [[leadership-communications]] (was in CLAUDE.md taxonomy), [[manager-cascade]] (NEW — Travis-confirmed channel-level addition)
- Updated topics: [[ai-in-internal-comms]] (Workshop AI-use stats), [[internal-email]] (81% effectiveness), [[intranet-and-digital-workplace]] (29% hardest, evergreen strategy), [[ic-measurement-and-roi]] (vendor-tier addition)
- Notable: confirmed methodological non-contradiction between Forrester (49% vendor-AI) and Workshop (73% any-AI) — different denominators
- Pages touched: 12

## [2026-05-12] ingest | Ragan 2026 Internal Email Benchmarks Report (Cerkl deep-dive)
- Source: local deep-dive at `cerkl/research/ic-trends/deepdives/ragan-email-benchmarks-report-2026-05-12.md`
- Mode: discuss-first per CLAUDE.md; Travis directed paired-anchor restructure + 2 new concepts + entity additions for PoliteMail (full), Ragan Communications, Gallagher, IABC, USC Annenberg, Meltwater
- Key finding: the "Ragan benchmark" is PoliteMail's annual report distributed via Ragan co-branding; same vendor lead-gen substance, editorial cover
- Created source: [[ragan-email-benchmarks-report-2026-05-12]]
- Created entities: [[politemail]], [[ragan-communications]], [[gallagher]], [[iabc]], [[usc-annenberg]], [[meltwater]]
- Created concepts: [[open-rate-inflation]], [[cross-channel-benchmark]]
- Restructured concept: [[internal-email-benchmarks]] — now paired-anchored on PoliteMail (66/7) and ContactMonkey (76/9) with shared methodology section
- Updated entities: [[contactmonkey]] (paired-benchmark context), [[pr-daily]] (Ragan parent + vendor-distribution pattern)
- Updated topics: [[internal-email]] (paired anchors + inflation caveat + cross-channel-vacuum), [[ic-measurement-and-roi]] (practitioner-survey + academic tier rows; PoliteMail filter; cross-channel pattern)
- Updated index.md with 9 new pages and refined descriptions
- Pages touched: 13
