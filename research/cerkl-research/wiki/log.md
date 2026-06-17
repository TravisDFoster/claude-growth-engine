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

## [2026-05-29] ingest | Trust & credibility cluster — 5 sources from the 2026-05-29 ic-trends recap
- Batch ingest (one session) of 5 sources surfaced by Travis from the 2026-05-29 daily recap. Decisions taken at the discuss checkpoint: reconstruct Gartner via WebSearch (WebFetch 403), ingest the paywalled Ragan critics piece thin/partial, create a new `trust-and-credibility` topic + concepts.
- Sources created (raw/ + wiki/sources/):
  - [[ragan-week-in-comms-cloudflare-wix-clickup-2026-05-29]] (Ragan/Devlin, 2026-05-29) — full fetch; stripped an embedded benign `<system-reminder>` TodoWrite nudge from the raw archive
  - [[gartner-information-integrity-risk-2026-05-13]] (Gartner, 2026-05-13, n=337) — WebSearch reconstruction; WebFetch returned 403; flagged not-verbatim
  - [[edelman-trust-barometer-2026]] (Ragan/Devlin pickup, **2026-02-12** — corrected from the recap's uncertain "2026" date)
  - [[why-employees-right-not-to-trust-ic]] (Ghassan Karian / isitworking Substack, 2026-05-26) — full fetch
  - [[ragan-toughest-internal-critics-2026-05-29]] (Ragan/Devlin, 2026-05-29) — PARTIAL, Ragan Insider paywall (preview + 1 quote only)
- New topic: [[trust-and-credibility]] (lazy-created; 3 anchoring sources)
- New concepts: [[measurers-vs-builders]] (Cloudflare/Prince — the attack on IC measurement), [[ic-credibility-deficit]] (Karian's 3 trust-killers), [[context-delivery]] (Karian's radical-honesty cure), [[trust-brokering]] (Edelman frame)
- New entities (11): [[cloudflare]], [[matthew-prince]], [[wix]], [[avishai-abrahami]], [[clickup]], [[zeb-jones]], [[edelman]], [[ghassan-karian]], [[ipsos-karian-and-box]], [[british-gas]], [[jon-beck]]
- Updated entities: [[gartner]] (info-integrity source + trust topic), [[sean-devlin]] (3 new pieces + connections), [[ragan-communications]] (3 new appearances)
- Updated concepts: [[layoff-comms-choreography]] (+3 cases, external-first channels), [[ai-washing]] (Wix/ClickUp explicit AI-attribution; norm shifting from disclaim→foreground), [[boilerplate-layoff-language]] (Karian euphemism catalog + candour↔trust mechanism)
- Updated topics: [[ic-measurement-and-roi]] (measurers-vs-builders rebuttal + verifiable-comms + candour-measurable), [[delivery-as-comms-strategy]] (added 6th evidence stream: trust/credibility), [[leadership-communications]] (CEO credibility gap + manager-vs-leader trust)
- Updated [[index]] (1 topic, 4 concepts, 11 entities, 5 sources)
- Key surfacing: the day's signal is a coherent **trust-in-the-AI-era** thread — Gartner (info-integrity = #1 enterprise risk) + Edelman (institutional trust high, comms-trust gap) + Karian (employee distrust of IC is rational) — converging against Cloudflare's [[measurers-vs-builders]]. Cerkl's counter: verifiable, candid, well-targeted delivery is how trust is *built and proven*; governance-by-gatekeeping (Simpplr) answers integrity-risk with control, Cerkl answers with proof.
- Provenance caveats: Gartner body is reconstructed (re-source before quoting); Ragan critics piece is paywalled/partial; Edelman seen only via the Ragan pickup (primary 2026 report + the IC Index 2026 remain un-ingested).
- Pages touched: ~33

## [2026-06-04] ingest | Manager-cascade-is-broken cluster — Karian (2026-06-04) + Gallup (2026-01-14) + Gartner (2026-04-29)
- Three-source ingest triggered by Travis pointing at the Karian item in the 2026-06-04 ic-trends recap and requesting a deep-dive + vault import. Discussion checkpoint: surfaced 5 takeaways; Travis selected (a) Karian + Gallup + Gartner ingest scope, (b) vendor-split anchor for Current Thesis, (c) create [[route-around-vs-enable]] as a new concept page.
- Companion deep-dive (NOT ingested as source; used only for synthesis): `cerkl/research/ic-trends/deepdives/karian-middle-manager-burnout-2026-06-04.md`
- **Provenance correction during ingest:** the daily-recap Step 2d sub-agent had conflated Karian's role-design essay with Gallup's span-of-control data ("12.1 reports / +50% since 2013"). Karian's article does **not** contain that stat. Daily/2026-06-04.md + rolling-7day.md corrected; Gallup re-anchored as the actual source. Also surfaced a separate inconsistency in Gallup itself: time series shown (10.9 → 10.9 → 12.1) doesn't support the "+50% since 2013" headline — most likely refers to share of teams with 25+ reports. Flagged on the [[gallup-span-of-control-2026]] source page; **conservative citation pinned to the concept page**.
- Sources created (raw/ + wiki/sources/):
  - [[karian-middle-manager-burnout-2026-06-04]] (Ghassan Karian / isitworking Substack, 2026-06-04) — full fetch; 5-root-cause structural-burnout thesis; IKB EX-benchmark backed
  - [[gallup-span-of-control-2026]] (Gallup / Jim Harter, 2026-01-14) — full fetch; US manager panel n=16,442 + 92,252-team meta-analysis; **3x weekly-feedback engagement multiplier** is the highest-leverage IC-relevant finding
  - [[gartner-managers-working-harder-2026-04-29]] (Gartner HR practice, 2026-04-29) — **PARTIAL** (WebFetch 403); body reconstructed from sub-agent summary; re-source before quoting
- New concepts (3): [[manager-burnout-structural-thesis]] (Karian's 5-root-cause role-design frame; IKB + Gallup + Gartner corroboration), [[route-around-vs-enable]] (2026 IC vendor-positioning split: Simpplr=enable; Firstup/Workvivo/Staffbase/ContactMonkey/Workshop+Cerkl=route-around; Karian's third axis = role redesign, no vendor sits there), [[span-of-control]] (Gallup quantitative substrate; median-vs-mean nuance pinned)
- Updated entities (4): [[ghassan-karian]] (manager-burnout thesis + structural-redesign prescription + personal-vs-corporate voice note), [[ipsos-karian-and-box]] (EX-benchmark database details, IC Index 2026 n=5,000, leadership diagnostics, 2023 hybrid-work research), [[gallup]] (US manager panel methodology + weekly-feedback finding + +50% inconsistency flag), [[gartner]] (Q1 2026 HR survey appearance)
- Updated topic — major: [[manager-cascade]] — Current Thesis rewritten around the vendor-split frame; 3 new entities; 3 new concepts; 3 new sources read; new contradictions section
- Updated topics — minor backlinks: [[leadership-communications]] (extended manager-cascade bullet + 3 concepts + 3 sources), [[change-management-communications]] (+2 concepts), [[employee-engagement]] (+2 concepts + 1 source), [[employee-experience]] (+1 concept)
- Updated [[index]]: 1 topic description, 2 entity descriptions, 3 concepts added, 3 sources added
- Key surfacing — the structural-burnout thesis is past "single-source claim" stage (Karian narrative + Gallup quantitative + Gartner analyst-tier corroboration converging from independent methodologies). For Cerkl: the route-around lane is right *because managers are structurally exhausted*, not because they're bad at cascading — a credibility-preserving honest framing. The Ragan ECCC 56/4 gap remains the load-bearing buyer-language hook (not the 12.1 stat).
- Cerkl positioning notes filed (in [[manager-cascade]] + [[route-around-vs-enable]]): the both-sides synthesis (enable where cascade works + route around where it doesn't, same delivery measurement) is the differentiable lane vs. the crowded route-around chorus AND vs. Simpplr's enable-only stance — but the claim is rhetorical until a product-level cascade-pre-brief feature is identified.
- Companion recommendation: Travis's deep-dive flags 3 [`shared/competitors.md`](../../../shared/competitors.md) updates (manager-cascade row in "Where Competitors Win"; vs. Firstup section refresh; vs. Simpplr section refresh). Not edited from this vault session — competitors.md sits in sibling read-only context.
- Provenance caveats: Gartner body reconstructed (same pattern as [[gartner-information-integrity-risk-2026-05-13]]); Gallup +50% headline doesn't match shown time series; IKB EX-benchmark methodology not publicly disclosed.
- Pages touched: ~13 (3 sources + 4 entities + 3 concepts + 1 major topic + 4 minor topic backlinks + index)



## [2026-06-09] ingest | Gallup — 3 Employee Engagement Strategies for 2026 (and SHRM ingest cancelled, daily-recap correction)

- Ingested 1 source: [[gallup-engagement-strategies-2026]] (~2026-05; companion to *State of the Global Workplace 2026*; surfaced via ic-trends daily recap 2026-06-09). Verified the 2.1x manager-AI-support → weekly+ usage stat verbatim against source.
- New concept page: [[manager-as-ai-champion]] — the cascade-works-here exception inside [[manager-burnout-structural-thesis]]; reconciles Gallup 2.1x with Karian's structural-broken finding (behavior-modeling is lighter weight than 15-min cascade conversation; exhausted managers can model a tool even when they can't carry a cascade).
- Updated entity: [[gallup]] — new Key Idea + new source entry + 2 new Connections (manager-cascade extended; new [[manager-as-ai-champion]]).
- Updated topics: [[ai-in-internal-comms]] (new "June 2026 addition — the adoption-mechanism finding" paragraph in Current Thesis; +1 concept; +1 Sources-Read row); [[manager-cascade]] (new "June 2026 update — one specific cascade DOES work" paragraph in Current Thesis; +1 concept; +1 Sources-Read row); [[employee-engagement]] (new "June 2026 — the AI-rollout cut" paragraph in Current Thesis; +1 concept; +1 Sources-Read row).
- Updated [[index]]: 3 topic descriptions extended; 1 concept added (manager-as-ai-champion); 1 source added (gallup-engagement-strategies-2026).
- **Cancelled ingest: SHRM** — *The Path Forward: SHRM's AI Legislative Framework* (May 2026). The ic-trends recap's analyst sub-agent 2c hallucinated two stats ("AI champions raise tool usage 65%"; "strategic comms improve trust 16%") that don't appear in the document — WebFetch couldn't read the SHRM PDF binary, and the sub-agent confabulated downstream. Direct PDF read confirmed. The real SHRM document is a policy/lobbying framework (8 governance pillars, AI + HI = ROI guiding principle) with its own real stats (46% expect AI in HR; 5.7x shift-vs-displace; 67% awareness barrier; 49% have AI policies; 60/33/35 large/small/midsize AI-in-HR split) — worth a future ingest *on its own terms* but does not support the "IC is the AI adoption engine" thesis it was bundled into today.
- **Provenance correction applied to ic-trends layer:** removed SHRM item #3 from `ic-trends/daily/2026-06-09.md`, downgraded headline + Notes-Convergence paragraph from three-source to two-source (Simpplr + Gallup); removed SHRM entry #3 from `ic-trends/rolling-7day.md`; updated the convergence bullet in `marketing/content-plan/inputs.md`. Inline correction note left in the daily recap.
- Key cross-cut for future filing: the **manager-as-AI-champion** finding pulls evidence onto the *enable* side of [[route-around-vs-enable]] **only** for AI-rollout content (general IC delivery still subject to the cascade-is-structurally-broken argument). Sharpens, not dissolves, the Cerkl both-sides positioning — route around for general delivery, enable manager modeling for AI rollout, same measurement on both paths.
- Open questions filed at [[manager-as-ai-champion]]: selection effect (modeling-vs-directing distinction in the Gallup data); leader vs direct-manager scope; whether Cerkl's read-attribution can support a "manager-modeled this week" content pattern that scales the mechanism.
- Pages touched: 6 (1 new source + 1 new concept + 1 entity + 3 topics + index).

## [2026-06-15] ingest | Engagement→experience cluster — 3 Ragan sources from the 2026-06-15 ic-trends recap
- **Sources ingested (3, all Ragan, June 2026):** [[ragan-engagement-to-experience-2026-06-11]] (Interact roundtable, vendor-tier), [[ragan-9-lessons-ai-integrated-comms-2026-06-11]] (Paul Gennaro / NY Life CCO, practitioner-tier), [[ragan-evp-corporate-wallpaper-lhh-2026-06-10]] (Tony Kihl / LHH, practitioner-tier). All 3 raw bodies saved to `raw/` (immutable). No prompt-injection in any fetched page.
- **New concepts (4):** [[engagement-to-experience-pivot]] (the 2026 reframe — demote engagement metrics for lived experience + outcomes); [[ai-integrated-comms-function]] (IPR nine-item checklist + NY Life proof — the practitioner "how" layer under the analyst-trio); [[comms-as-knowledge-steward]] (IC governs the knowledge AI draws on; "content problem is solved"); [[corporate-wallpaper]] (EVP failure mode: stated ≠ lived; antidote = EVP-as-campaign).
- **New topic (1):** [[employer-brand]] — lazy-created, anchored on the LHH EVP case. Single-source; flagged needing an analyst/primary-research anchor before blog-citable.
- **New entities (10):** [[interact]], [[cindy-knezevich]], [[daren-jennings]], [[paul-gennaro]], [[new-york-life]], [[samantha-stark]], [[phyusion]], [[institute-for-public-relations]], [[tony-kihl]], [[lhh]]. Updated [[ragan-communications]] (Center for AI Strategy program + vendor-roundtable distribution pattern) and [[sean-devlin]] (EVP byline).
- **Topics updated (6):** [[employee-experience]] (pivot becomes the trade-press banner), [[employee-engagement]] (vendors now argue *against* engagement-as-goal; "flat 20 years" flagged uncited), [[ic-measurement-and-roi]] (measurers-vs-builders rebuttal gets practitioner evidence), [[ai-in-internal-comms]] (practitioner operating-model frame + knowledge-steward), [[manager-cascade]] (LHH cascade-decks as worked enable-side example), [[change-management-communications]] (unified-change-narrative + EVP-as-transformation).
- **Key cross-cut for future filing:** IPR's **37%**-of-orgs-have-a-clear-AI-change-story now sits beside Gallup's **26%**-have-a-clear-AI-plan — two independent 2026 sources pinning the rollout-comms vacuum at ~a quarter-to-a-third of orgs. Strong dual-anchor for the [[ai-rollout-comms]] / [[enablement-illusion]] chain.
- **Cerkl positioning note:** the engagement→experience pivot is double-edged — its outcome/behavior-change emphasis is Cerkl's home ground, but "experience" is also the EX-suite vendors' justification for destinations (Interact: intranet *is* the experience layer). Own the proof layer, don't cede the noun.
- **Open follow-ups filed:** is IPR's full 2026 generative-AI research public? (research-tier anchor worth a direct ingest); should [[interact]] be added to `shared/competitors.md` as an intranet adjacency?; does employer-brand get a non-self-reported anchor?
- Pages touched: 24 (3 sources + 4 concepts + 1 topic created + 6 topics updated + 10 entities + 2 entities updated [Ragan, Devlin] + index; some overlap).
