# Marketing & Growth Ops — Portfolio Review

> Personal Assistant · Growth Project Tracker
> **Date:** 2026-05-28 (Thursday)
> **Audience:** Tarek Kamil (CEO) + leadership team
> **Author:** Travis Foster, Head of Marketing & Growth Ops

## TL;DR

The portfolio is in a Friday-delivery crunch: three items land **2026-05-29** — Weekly Sales Report V1 (first publish to Marc + Josh), the downloadable-asset CTA swap, and Canva design skills Phase 1 — with the SEM Landing Page A/B test launching **2026-06-03**. Two flagship launches stay hard-blocked on external dependencies: Meta Ads on conversion-event verification and The Cerkular on the HubSpot → Broadcast API (Jira FUTURE-232); Competitor Dissatisfaction Mining is paused on tooling budget until end of June. Momentum over the last two weeks is strongest in SEO/schema and webinar follow-through, where most of the shipped work landed.

## Stats

- **23** active projects
- **5** Top of Mind
- **4** hard deadlines in the next 14 days (2026-05-28 → 2026-06-11): Weekly Sales Report · Downloadable Asset Emails · Canva Design Skills (all 5/29) · SEM LP launch (6/03)
- **4** blocked or at-risk: Meta Ads — Blocked · The Cerkular — Blocked · Comp Dissat — Pending budget · YouTube — Pending TK

## Top of Mind

### 1. Meta Ads Channel Launch
- **Next step:** Stand up `marketing/channels/paid-meta/` folder, then verify the Foundations sign-up event firing in Meta Pixel + Conversions API
- **Due:** —
- **On track:** **Blocked** — conversion-event verification is the hard gate before test 1 can launch
- **Why it matters:** New paid channel. Phase 1 (account access) and Phase 2 targeting decisions with TK are locked; test 1 can't go live until the sign-up conversion is verified end-to-end.

### 2. SEO Strategy & Plan
- **Next step:** Phase 2 #1 — define the content planning process (esp. blogs) with explicit SEO linkage (keyword → angle → internal linking → CTA)
- **Due:** —
- **On track:** Yes
- **Why it matters:** Phase 1 closed 2026-05-15 (skills inventory). Phase 2 wires SEO into the content engine so every blog post earns its keyword pull — foundational for organic pipeline.

### 3. The Cerkular
- **Next step:** Resolve personalization-link feasibility in a Blast (Jira FUTURE-232), then upload the HubSpot audience to Broadcast
- **Due:** —
- **On track:** **Blocked**
- **Why it matters:** Prospect-nurture newsletter delivered via Broadcast. The HubSpot → Broadcast API integration is the launch gate — an engineering dependency outside Travis's direct control.

### 4. Ad Conversion Tracking
- **Next step:** Observe a real event firing in Google Ads (passive verification of the 2026-05-15 diagnose + fix)
- **Due:** —
- **On track:** Yes — passive monitor
- **Why it matters:** Conversion-attribution backbone for paid spend. Fix landed 5/15; now waiting on a real-world event to confirm. Demoted from active focus to monitor.

### 5. Competitor Dissatisfaction Mining
- **Next step:** Re-investigate end of June — confirm webscraping-tool budget, reassess tooling, decide resume vs. shelve
- **Due:** 2026-06-30 (re-investigation gate)
- **On track:** **Pending budget**
- **Why it matters:** Net-new sales pipeline from dissatisfied competitor users. First enriched list shipped to sales 2026-05-18; paused 5/18 once the scrape-and-enrich loop proved to need tooling spend (Apify / BrightData class) that isn't approved.

## Upcoming Milestones (2026-05-28 → 2026-06-27)

| Date | Milestone |
|---|---|
| **2026-05-29** | Weekly Sales Report V1 — first publish to Marc + Josh |
| **2026-06-03** | 🚀 SEM Landing Page A/B test LAUNCH (deprioritized from 5/20; current LP performing well) |
| **2026-06-13** | 🚀 Insights 3.0 launch · press release embargo lifts (delayed 5/09 → 6/01 → 6/13) |
| **2026-06-24** | Earliest SEM LP A/B test readout (6/03 launch + 21-day minimum run) |

## Full Project Ledger

| Project | Next step | Priority | Due | On track |
|---|---|---|---|---|
| Meta Ads Channel Launch | Stand up `marketing/channels/paid-meta/` folder, then verify Foundations sign-up event firing in Meta Pixel + Conversions API | High | — | Blocked |
| SEM Landing Page Rebuild | Resume Steps 4–6 (ICE hypothesis → Webflow variant → PostHog config) on revised timeline; launch 2026-06-03 | Med | 2026-06-03 | Yes |
| The Cerkular | Resolve personalization-link feasibility in Blast (Jira FUTURE-232) | High | — | Blocked |
| Competitor Dissatisfaction Mining | Re-investigate end of June — confirm budget for webscraping tools, reassess tooling, decide resume vs. shelve | Med | 2026-06-30 | Pending budget |
| SEO Strategy & Plan | Phase 2 #1 — define content planning process (esp. blogs) with explicit SEO linkage (keyword → angle → internal linking → CTA) | High | — | Yes |
| Weekly Sales Report | Define V1 metric set + extract feature requests from week's deal/call notes; publish first report to Marc + Josh by Fri | High | 2026-05-29 | Yes |
| Ad Conversion Tracking | Observe a real event firing in Google Ads (passive verification of 5/15 diagnose+fix) | Med | — | Yes |
| Webinars | Finish remaining YouTube snippets (rolling over next few weeks) | Low | — | Yes |
| Press Release | Resume final approval cycle in late May (publish embargo 2026-06-13) | Med | 2026-06-13 | Yes |
| Cerkl Website | Email builder page — add WCAG compliance blurb | Low | — | Yes |
| Comparison SEO Pages | Build channel process for `comparison-seo` (page template, research inputs, production + refresh workflow) before drafting first new page | Med | — | Yes |
| Review Sites | Gartner — push current in-progress listing forward (Product Hunt waits on Insights 3.0, 2026-06-13) | Med | — | Yes |
| ICPro SEO | Roll out schema to all blog posts (Rich Results Test verified 2026-05-22) | Med | — | Yes |
| Design Tools | Research AI video creation tools (HeyGen alternatives for Pains-concept ad video) | Low | — | n/a |
| Advertising | LinkedIn Ads — test with Rachel (Gallagher); explore Interest-Based Ads | Low | — | n/a |
| YouTube | Decide with TK — post product videos (Foundations, Audience Manager) to Cerkl YouTube? | Low | — | Pending |
| IC Trends Knowledge Base | Decide scope option (topics-only / full wiki / full + outputs) before any restructure | Low | — | n/a |
| ICP Blog May Rewrites | Decide: publish 3 Drive Docs to internalcommspro.com (Wix) or close as workspace-only | Low | — | Yes |
| PA System Refresh | Exploration — design notes captured; revisit when ready to prototype handoff-driven tracking | Low | — | n/a |
| Furqan — Backlinks Onboarding | 30-min sync to walk through `marketing/seo/backlinks/`, confirm monthly cadence (~25 prospects), decide on Ahrefs/Moz access | Med | — | Yes |
| Downloadable Asset Emails | Inventory downloadable-asset follow-up sequences and swap CTAs from book-a-meeting → Foundations | Med | 2026-05-29 | Yes |
| Canva-Connected Design Skills | Phase 1 — template discovery + connection for one-pager, blog-asset, and LinkedIn-asset skills | Med | 2026-05-29 | Yes |
| Pressure Prospecting | Review Phase 1 methodology — confirm tier defaults / voice rules / angle, pick Phase 2 owner + target pilot date | Med | — | Yes |

## Recently Shipped

- **2026-05-26** — SEO delta audit for cerkl.com completed; technical roadmap updated with verified meta descriptions + live-site findings (SEO Strategy & Plan)
- **2026-05-22** — ICPro schema: Google Rich Results Test verified passing against live blog post (ICPro SEO)
- **2026-05-21** — Meta Ads Phase 2: targeting mental model + 3-cell ABO audience cuts + TK-aligned decisions table locked (Meta Ads Channel Launch)
- **2026-05-21** — Matt Frost recap blog re-run (Draft + Edit), final score 42/50, real recording URL swapped in (Webinars)
- **2026-05-19** — Matt Frost recap one-pager rebuilt with the dynamic-Lego-bricks component set (Webinars)
- **2026-05-18** — First enriched competitor-dissatisfaction list handed off to Marc + Josh (Competitor Dissatisfaction Mining)
- **2026-05-15** — SEO Phase 1 closed: skills inventory mapped to `seo-process.md` (SEO Strategy & Plan)
- **2026-05-15** — Ad conversion tracking diagnose + fix landed (Ad Conversion Tracking)
- **2026-05-15** — ICPro schema fix landed (Rich Results Test failure diagnosed) (ICPro SEO)
- **2026-05-15** — Sourceforge listing claimed + Foundations added (Review Sites)
- **2026-05-15** — Webinars added to Resources menu (Webflow CMS, with Furqan) (Webinars)
- **2026-05-14** — Meta Ads Phase 1: account access restored, page ownership confirmed (Meta Ads Channel Launch)
- **2026-05-14** — Pressure Prospecting Phase 1 methodology design complete (Pressure Prospecting)

---

*Source ledger: [INDEX.md](INDEX.md) — refreshed 2026-05-26*
