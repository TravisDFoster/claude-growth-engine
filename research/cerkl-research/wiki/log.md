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

## [2026-05-15] ingest | Gartner: AI Layoffs Don't Deliver Returns
- Source: local deep-dive at `cerkl/research/ic-trends/deepdives/gartner-ai-layoffs-no-returns-2026-05-15.md` (Gartner 2026-05-05 release; 403 on programmatic fetch)
- Mode: discuss-first per CLAUDE.md; Travis directed concept-page treatment for [[people-amplification]] + role in [[ai-rollout-comms]] chain
- Key finding: ~80% of orgs piloting autonomous business cut headcount; zero correlation between cut rate and AI ROI. Helen Poitevin's "people amplification, not elimination" framing is convergent with BCG / Forrester / McKinsey / MIT Sloan
- Created source: [[gartner-ai-layoffs-no-returns-2026-05-15]]
- Created concept: [[people-amplification]]
- Created entities: [[gartner]], [[helen-poitevin]]
- Updated concept: [[do-more-with-less]] (added analyst-grade rebuttal via Gartner)
- Pages touched: 5

## [2026-05-15] ingest | Gartner: People-Centric AI Strategy / 50% AI Talent Loss by 2027
- Source: local deep-dive at `cerkl/research/ic-trends/deepdives/gartner-people-centric-ai-2026-05-15.md` (Gartner 2026-05-13 release; 403 on programmatic fetch)
- Mode: discuss-first per CLAUDE.md; Travis directed concept-page treatment for [[enablement-illusion]] + [[shadow-ai-comms-problem]] (the IC-relevant reframe)
- Key finding: 88% of employees with enterprise AI also use personal AI tools — Gartner reframes shadow AI as a *comms* problem (bad UX + unclear rollout messaging), not a tooling/governance problem. Direct CHRO/CIO co-buyer naming
- Created source: [[gartner-people-centric-ai-2026-05-15]]
- Created concepts: [[enablement-illusion]], [[shadow-ai-comms-problem]]
- Created entities: [[swagatam-basu]], [[diana-sanchez]] (stubs; [[gartner]] entity created in companion ingest)
- Pages touched: 5

## [2026-05-15] ingest | Ragan: The Week in Comms (LinkedIn, GM, GitLab)
- Source: local deep-dive at `cerkl/research/ic-trends/deepdives/ragan-week-in-comms-linkedin-gm-gitlab-2026-05-15.md` (Ragan 2026-05-15)
- Mode: discuss-first per CLAUDE.md; Travis directed one-concept-plus-three-entity-pages for LinkedIn/GM/GitLab cases
- Key finding: three layoff memos in one week show *content matters less than channel and choreography*. GM's 15-minute meeting became the AI-replacement narrative even though GM didn't claim AI. "Delivery layer not destination" framing verbatim on a competitor's editorial — cleanest 2026 public proof point for Cerkl positioning
- Created source: [[ragan-week-in-comms-linkedin-gm-gitlab-2026-05-15]]
- Created concepts: [[layoff-comms-choreography]], [[ai-washing]]
- Created entities: [[linkedin]], [[gm]], [[gitlab]], [[daniel-shapero]], [[bill-staples]], [[sean-devlin]]
- Updated entity: [[ragan-communications]] (added "Week in Comms" editorial throughline)
- Pages touched: 9

## [2026-05-15] ingest | Forrester: AI Will Rewrite EX — Deep Listening Shows How
- Source: local deep-dive at `cerkl/research/ic-trends/deepdives/forrester-ai-rewrite-ex-deep-listening-2026-05-15.md` (Forrester blog 2026-02-06, by Brodeur-Johnson + McQuivey)
- Mode: discuss-first per CLAUDE.md; Travis directed concept-page treatment for [[deep-listening]] *with* the Cerkl complement-not-compete positioning baked in
- Key finding: Forrester names a new EX category — passive NLP on Teams chats / meeting transcripts → real-time sentiment, replacing surveys. 24-month vendor build window. Structurally favors data-plane incumbents (Microsoft, Workvivo-via-Zoom, Qualtrics). Cerkl positioning: complement-not-compete on listening; we own the response half of the loop
- Created source: [[forrester-ai-rewrite-ex-deep-listening-2026-05-15]]
- Created concept: [[deep-listening]]
- Created entities: [[david-brodeur-johnson]], [[james-mcquivey]]
- Updated entities: [[forrester]] (added deep-listening + Brodeur-Johnson/McQuivey), [[workvivo]] (deep-listening positioning impact on Seer), [[seer]] (analyst legitimacy from Forrester frame)
- Pages touched: 6

## [2026-05-15] synthesis | 2026 AI-change-comms thesis cluster (4-source)
- Travis-directed unifying treatment of items #1, #3, #4, #6 from today's [[../ic-trends/daily/2026-05-15]] recap; sub-agent deep-dives copied into raw/ with provenance preserved
- Created topic: [[change-management-communications]] (taxonomy slot first-touched by Ragan + Gartner-layoffs sources)
- Created concept: [[ai-rollout-comms]] (unifying chain spanning [[ai-in-internal-comms]] ↔ [[change-management-communications]]; the thesis page Travis directed)
- Updated topics: [[ai-in-internal-comms]] (added rollout / response / listening sections + 3 new sources), [[employee-experience]] (added Forrester deep-listening + Gartner CHRO frames)
- Index refreshed end-to-end (10 new entries, 4 entity refresh, 1 thesis concept)
- The cluster's positioning window framed: roughly 12–18 months until competitors (Workvivo, Staffbase, Simpplr, Firstup, etc.) cite the same Forrester / Gartner frames in marketing

## [2026-05-18] ingest | Ragan: The Newsletter Formatting Pressure Test (Cerkl deep-dive)
- Source URL: https://www.ragan.com/internal-comms-employee-newsletters-pressure-test/
- Emphasis per Travis (4-way recommended): richer synthesis, create delivery-as-comms-strategy topic page, flag-and-synthesize AI-anxious-buyer contradiction, practitioner-neutral wiki body + Cerkl Positioning Note section
- Created source: [[ragan-newsletter-pressure-test-2026-05-18]]
- Created entities: [[yale]], [[niamh-emerson]], [[roku]], [[katie-satterlee]]
- Created concept: [[newsletter-format-audit]]
- Updated topic: [[internal-email]] (new tactical-layer paragraph; practitioner voices section populated)
- Pages touched: 7

## [2026-05-18] ingest | HR Reporter: Using AI for Internal Communications? Know the Risks (Cerkl deep-dive)
- Source URL: https://www.hrreporter.com/focus-areas/automation-ai/using-ai-for-internal-communications-know-the-risks/393831
- Surfacing correction: the daily-recap's "52% weekly AI use" stat is from [[simpplr]]'s 2026 State of IC, not from HR Reporter; both ingested as paired anchors
- Created source: [[hr-reporter-ai-risks-ic-2026-05-18]]
- Created entities: [[hr-reporter]], [[sarah-dobson]], [[peter-cardon]], [[anthony-coman]], [[linjuan-rita-men]], [[simpplr]]
- Created concepts: [[ai-anxious-buyer]], [[co-piloting]]
- Updated topic: [[ai-in-internal-comms]] (added third story; Tensions section calls out AI-anxious vs AI-transformative contradiction head-on)
- Updated topic: [[leadership-communications]] (manager-AI risk; *"why are they my manager at all?"* quote)
- Pages touched: 11

## [2026-05-18] ingest | Oracle 6 a.m. Mass-Email Layoff: HR Communication Lessons (Cerkl deep-dive)
- Source URL: https://amazingworkplaces.co/oracle-layoffs-2026-hr-communication-lessons/
- Notable: prompt-injection attempt detected in fetched page (fake `<system-reminder>` instructing fetcher to invoke TodoWrite). Detected and ignored; logged in [[oracle-mass-email-layoff-lessons-2026-05-18]] and [[amazing-workplaces]] Gotchas.
- Created source: [[oracle-mass-email-layoff-lessons-2026-05-18]]
- Created entities: [[oracle]], [[amazing-workplaces]]
- Created concept: [[boilerplate-layoff-language]]
- Updated concept: [[layoff-comms-choreography]] — Oracle added as 5th and highest-scale anchor case; reference-set table grew from 3-case to 4-case
- Updated topic: [[change-management-communications]] (Oracle as high-scale anchor; reference set extended)
- Updated topic: [[leadership-communications]] (named-sender failure anchor case)
- Pages touched: 8

## [2026-05-18] ingest | McKinsey: Redesigning Technology Workforce for the Agentic AI Era (Cerkl deep-dive)
- Source URL: https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/designing-an-end-to-end-technology-workforce-for-the-ai-first-era
- Notable: direct fetch consistently timed out; synthesis built from indexer snippets + McKinsey adjacent April 2026 agentic-AI corpus. Author bylines unverified.
- Created source: [[mckinsey-agentic-ai-workforce-redesign-2026-05-18]]
- Created entity: [[mckinsey]] (first time in this vault)
- Created concepts: [[agents-as-coworkers]], [[analyst-trio-comms-as-ai-gate]]
- Updated concept: [[ai-rollout-comms]] — chain extended upstream to McKinsey workforce-design lens; HR Reporter + Oracle added as new chain anchors
- Updated topic: [[ic-measurement-and-roi]] (measurement-of-change-comms paragraph)
- Pages touched: 8

## [2026-05-18] synthesis | New topic page: delivery-as-comms-strategy
- Created topic: [[delivery-as-comms-strategy]] — unifying thesis across the four 2026-05-18 ingests
- Synthesizes evidence from newsletter audit + layoff choreography + AI-anxious-buyer + analyst-trio
- Maps directly onto Cerkl positioning verbatim
- Per Travis's "richer synthesis" direction; ready for downstream Cerkl writing (Cerkular, sales-enablement one-pager, blog post)

## [2026-05-18] index-update | Wiki index refreshed
- Index.md overwritten with 1 new topic, 13 new entities, 6 new concepts, 4 new sources
- Now: 12 topics, 47 entities, 28 concepts, 15 sources
- All new pages cross-linked to existing pages per the cross-reference rule


## [2026-05-22] ingest | Qualtrics: Employees Experiencing More Change Are MORE Engaged (Cerkl deep-dive)
- Source URL: https://www.ragan.com/employees-experiencing-more-change-are-more-engaged/
- Underlying primary source: https://www.prnewswire.com/news-releases/qualtrics-employees-thrive-through-change-302679648.html (n=33,831, 24 countries; Qualtrics 2026 Global EX Trends Report)
- Travis's framing direction: neutral IC-industry analysis (NOT Cerkl-positioning angle)
- Created source: [[qualtrics-change-engagement-2026-05-21]]
- Created entities: [[benjamin-granger]], [[perceptyx]], [[prosci]], [[abhijit-bhaduri]]
- Updated entities: [[qualtrics]] (now key 2026 publisher entity), [[gallup]] / [[gallagher]] / [[ragan-communications]] (backlinks)
- Created concepts: [[goldilocks-zone-of-change]], [[listening-cadence]], [[change-saturation]], [[change-fatigue]]
- Updated topics: [[change-management-communications]] (new observation #5 on change-fatigue vs change-engagement debate), [[employee-engagement]] (full update with contested-direction tension), [[employee-experience]] (2026 EX research is internally contested paragraph), [[delivery-as-comms-strategy]] (added listening-cadence as 5th evidence stream)
- Key surfacing: Qualtrics names *listening frequency* (not comms quality) as the moderator; 87/44 engagement gap; Ragan added "comms quality" framing on top
- Pages touched: ~14

## [2026-05-22] ingest | McKinsey "Rewired 2.0: The Talent Plan" (Cerkl deep-dive)
- Source URL: https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/the-organization-blog/the-rewired-2-point-0-talent-plan
- Travis's framing direction: neutral IC-industry analysis
- Created source: [[mckinsey-rewired-2-2026-05-21]]
- Created entities: [[eric-lamarre]], [[kate-smaje]], [[rob-levin]], [[bcg]], [[julia-dhar]], [[bain]], [[deloitte]]
- Updated entity: [[mckinsey]] (Rewired 2.0 + new connections)
- Created concepts: [[talent-transformation-thesis]], [[70-30-tech-talent-flip]], [[human-agentic-collaboration]], [[n-2-n-3-leader-development]]
- Updated topics: [[ai-in-internal-comms]] (new consulting-tier paragraph + hypocrisy critique), [[change-management-communications]] (source row + Rewired entities + new concepts), [[leadership-communications]] (N-2/N-3 + human-agentic levers paragraph), [[delivery-as-comms-strategy]] (source row + entities + new concepts)
- Key surfacing: Lever #4 ("emotional work of helping humans feel safe alongside machine colleagues") is the most comms-adjacent quote at consulting-tier; hypocrisy critique (McKinsey cutting ~10% non-client staff while publishing talent playbook) is the loudest practitioner reaction online
- Pages touched: ~15

## [2026-05-22] ingest | The 2026 "AI-Restructure Layoff Memo" subgenre (Cerkl deep-dive)
- Source URL: https://www.ragan.com/the-week-in-comms-linkedin-gm-gitlab/ (anchoring IC trade-press commentary)
- Six anchor memos: Cisco, GitLab, GM, LinkedIn, Microsoft, Oracle (+ Meta extension); reference frameworks: Chesky/Airbnb, Collison/Stripe, Niccol/Starbucks, Sutton PUCC, Sucher HBR, SHRM RIF
- Travis's framing direction: neutral IC-industry analysis
- Created source: [[layoff-memo-subgenre-2026-05-21]]
- Created entities: [[microsoft]], [[meta]], [[chuck-robbins]], [[airbnb]], [[brian-chesky]], [[robert-sutton]]
- Updated entities: [[cisco]], [[oracle]], [[gm]], [[linkedin]], [[gitlab]] (backlinks + new concept connections)
- Created concepts: [[ai-restructure-memo-subgenre]], [[strong-quarter-layoff]], [[voluntary-first-default]], [[pucc-framework]]
- Updated concepts: [[layoff-comms-choreography]] (reference set extended to Cisco/Microsoft/Meta; new related concepts), [[ai-washing]] (added third sub-pattern: side-channel split-messaging via LinkedIn case)
- Updated topics: [[change-management-communications]] (source row + new concepts + new entities), [[leadership-communications]] (source row + entities + new concepts), [[delivery-as-comms-strategy]] (source row + entities + new concepts)
- Key surfacing: Five emerging conventions (lead with strategic thesis, name AI explicitly, pair with reinvestment, voluntary-first default, delivery mechanism as part of memo); GitLab "Act 2" = high-transparency template; Cisco = corporate-best-practice; GM/LinkedIn/Microsoft/Oracle = anti-templates
- Pages touched: ~16

## [2026-05-22] index-update | Wiki index refreshed
- Index.md updated with 17 new entities, 12 new concepts, 3 new sources
- Now: 12 topics, 64 entities, 40 concepts, 18 sources
- All new pages cross-linked per the cross-reference rule

## [2026-05-27] ingest | Ragan/Devlin — Whittle on Gartner Predicts 2026 comms strategies
- Source URL: https://www.ragan.com/ai-hr-comms-gartner-2026/ (Sean Devlin, Ragan, 2025-10-09)
- Surfaced via 2026-05-27 ic-trends daily recap + same-day deep-dive on the 75%-by-2028 chatbot prediction (deep-dive lives at ../ic-trends/deepdives/gartner-chatbots-over-intranets-2026-05-27.md and was NOT separately ingested per Travis's direction — ingest Ragan only)
- Travis's framing direction: focus on what's actually in the Ragan article (Whittle's framework + verbatims), not the broader deep-dive synthesis
- Created source: [[ragan-gartner-2026-comms-predictions-2025-10-09]]
- Created entities: [[mark-whittle]] (Gartner VP Advisory, comms practice)
- Updated entities: [[gartner]] (added Whittle + this source + tension on net-jobs posture), [[ragan-communications]] (added this source), [[sean-devlin]] (now has 2 sources; expanded Overview)
- Created concepts: [[change-leadership-three-step]] (Whittle's Acknowledge / Regulate / Train framework)
- Updated topics: [[ai-in-internal-comms]] (Sources Read row), [[change-management-communications]] (Current Thesis #6 + entities + concepts + Practitioner Voices + Sources Read), [[leadership-communications]] (Current Thesis + entities + concepts + Practitioner Voices + Sources Read)
- Key surfacings: (1) Whittle three-step framework promoted to concept page — analyst-tier practitioner pair to Poitevin's people-amplification diagnosis; (2) verbatim "effective leadership today is change leadership" lifted for downstream Cerkl writing; (3) flagged tension between Gartner's October-Whittle "AI creates more net jobs" position and Gartner's May-Poitevin "80% cut / no AI-ROI correlation" finding — same firm, same year, reconcilable but not reconciled in either source; (4) Gartner now on the record explicitly linking layoff-comms quality to employer brand
- Pages touched: ~10
