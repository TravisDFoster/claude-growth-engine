# IC Deep Dive — Forrester: "AI Will Rewrite Employee Experience, And Deep Listening Shows How"

**Date:** 2026-05-15   |   **Category:** Analyst report / blog (with companion reports)

---

## TL;DR

Forrester Principal Analyst **David Brodeur-Johnson** is naming a new category — **"deep listening"** — defined as AI that turns the "digital exhaust" of Teams chats, channel conversations, and meeting transcripts into real-time sentiment, emotion, and friction signals across the workforce, no surveys required. Forrester says vendors are **one to two years away from full-featured offerings**; early movers will "detect emerging issues earlier, intervene more effectively, understand the impact of change initiatives in days rather than quarters." The Cerkl-relevance hook is sharp: **Forrester is naming the lane Cerkl wants to own — measurable, channel-native delivery with read-through analytics — but Forrester's frame puts the value in *upstream sentiment*, not downstream delivery.** Cerkl is on the right map but on the wrong axis as written.

## What it is

A **February 6, 2026** Forrester blog post by **David Brodeur-Johnson** (Principal Analyst, Employee Experience research lead) and **James McQuivey, PhD**, introducing "deep listening" as Forrester's frame for the next 24 months of EX investment. The blog is the public hook for two paywalled companion reports — *"Deep Listening Is Your Next Employee Success Propellant"* (RES189386) and *"For Deep Listening For EX, You Need A Viable AI Technology Stack"* (RES189391) — plus a client-only webinar, *"Deep Listening Will Power The Future Of Work."* This is a category-naming move, not a one-off think piece.

**Source URLs:**
- Forrester blog post: [forrester.com/blogs/ai-will-rewrite-employee-experience-deep-listening-shows-how](https://www.forrester.com/blogs/ai-will-rewrite-employee-experience-deep-listening-shows-how/)
- David Brodeur-Johnson analyst bio: [forrester.com/analyst-bio/david-brodeurjohnson/BIO2751](https://www.forrester.com/analyst-bio/david-brodeurjohnson/BIO2751)
- Brodeur-Johnson companion piece on GenAI + digital exhaust: [forrester.com/blogs/genai-offers-the-digital-employee-experience-opportunity-of-a-lifetime](https://www.forrester.com/blogs/genai-offers-the-digital-employee-experience-opportunity-of-a-lifetime/)
- Forrester EX category blog index: [forrester.com/blogs/category/employee-experience](https://www.forrester.com/blogs/category/employee-experience/)
- Companion (today's #1 deep-dive context) — Gartner "people-centric AI" 2026-05-13: [gartner.com](https://www.gartner.com/en/newsroom/press-releases/2026-05-13-gartner-predicts-by-2027-50-percent-of-enterprises-without-a-people-centric-ai-strategy-will-lose-their-top-ai-talent)

## What it does / claims

Forrester defines **deep listening** as a stack — not a product, not a survey methodology — with five claimed capabilities:

1. **Passive sentiment detection across digital channels.** "Privacy‑focused preprocessing and advanced natural language processing" on Teams chats, channel conversations, and meeting transcripts. No survey instrument required.
2. **Emotional granularity beyond "engaged/disengaged."** Distinguishes *"tension from fear, cynicism from frustration, or burnout from ordinary stress"* — verbatim from the post.
3. **Topic categorization at scale.** Auto-categorizes conversations into themes like *"workload imbalance or dissatisfaction with organizational changes."*
4. **Real-time change-impact measurement.** *"Understand the impact of change initiatives in days rather than quarters"* — the headline operational claim.
5. **Privacy-by-design as table-stakes, not optional.** Co-author McQuivey's framing: *"Through 'privacy by design' deep listening, leaders get a real-time pulse on employees — turning raw conversations into actionable intelligence."*

**The thesis quote:** *"Passive listening across digital channels produces exponentially more insight than employee surveys."*

**The competitive-advantage claim:** Vendors are "one to two years away from delivering full-featured offerings." Early-mover orgs that build now will:
- Detect emerging issues earlier
- Intervene more effectively
- Understand change-initiative impact in days, not quarters
- Build more emotionally supportive environments

**What the post does *not* contain:** No statistics, no maturity model diagram, **no named vendors** (Forrester names zero vendors in the public blog — Microsoft Viva Glint, Qualtrics, Medallia, Perceptyx, Workvivo Seer all go unmentioned), and no pricing. The reports are paywalled — the blog is the lead magnet.

## Who it's for

- **Primary audience / ICP overlap:** Forrester's enterprise EX-leader subscriber base — CHRO, CHRO direct reports, VP/Head of Employee Experience, VP/Head of Internal Communications at 5,000+ employee orgs. Direct overlap with **Cerkl's paid ICP (Omni AI)**, which is mid-market to enterprise with messy comms environments, distributed/frontline workforces, and IT co-buyer ([icp.md](../../shared/icp.md)).
- **Strong fit when:** The buyer's #1 EX KPI is *"understand sentiment / detect friction before it churns,"* not *"distribute messages reliably."* The post will resonate hardest in orgs that already invested in Viva Glint / Qualtrics / Medallia / Perceptyx and feel survey-only listening is too slow.
- **Weak fit when:** The buyer's mandate is the comms team's job — write, send, measure read-through, segment audiences. The post does not address the "how do I get my message in front of my employees" problem; it addresses the "how do I understand what my employees feel" problem. **This is the cleavage line for Cerkl positioning.**

## How it slots into Cerkl's competitive set / positioning

This is the section that earns the deep-dive. Three things Travis needs to be clear-eyed about:

### 1. Does Cerkl already do "deep listening"? **No — and that's fine.**

Cerkl ships **read-through analytics across email + cross-channel delivery** — who opened, who clicked, what segment performed, what time of day. That is *delivery measurement*. Forrester's "deep listening" is something different: **passive NLP on Teams chats and meeting transcripts to surface unsolicited sentiment.** Cerkl has neither (a) a Teams transcript ingest path, nor (b) a sentiment-classification model, nor (c) the privacy-by-design preprocessing layer Forrester says is table-stakes. Pretending Cerkl is in this category dilutes the actual wedge.

### 2. What's the gap between Forrester's frame and what Cerkl markets?

Forrester is framing **the EX/Comms category through a sentiment-analytics lens**. By Forrester's frame, the value flows like this:

```
Digital exhaust (Teams, meetings) → AI sentiment layer → EX leader insight → action
```

Cerkl's frame flows differently:

```
Comms team intent → Personalized cross-channel delivery → Employee read → Measurement
```

**These are not the same pipeline. They are not even the same job.** Forrester's frame answers *"what do my employees feel?"* Cerkl answers *"did my message get to the right employee, on the right channel, and did they read it?"* Both jobs exist. The risk is that **Forrester's frame is being adopted by enterprise EX buyers as the new evaluation lens for the entire EX/Comms category by 2027** — and a buyer reading the Forrester piece may incorrectly conclude that any EX tool worth buying does sentiment NLP on collaboration exhaust. That's the threat. **The opportunity** is that Forrester is *also* implicitly validating that "raw collaboration channels are the new EX measurement surface" — which is exactly the channel-native frame Cerkl already pitches on the delivery side.

### 3. Which competitors most leverage this frame?

| Competitor | How they leverage Forrester's "deep listening" |
|---|---|
| **Workvivo (Seer)** | **Already there.** [Seer launched 2026-05-06](https://www.workvivo.com/newsroom/workvivo-launches-seer/) explicitly as *"people intelligence"* — Workvivo's own framing: *"combining feedback with real-time signals from communication, collaboration, and engagement."* That is Forrester's deep-listening category, almost verbatim. Workvivo will cite this Forrester blog in sales decks within 30 days. ([shared/competitors.md vs. Workvivo](../../shared/competitors.md#vs-workvivo) — already flagged Seer.) |
| **Microsoft Viva Glint** | **Structurally best-positioned.** Already owns the data plane (Teams chat + meeting transcripts via Viva Insights + sentiment via Glint). [Copilot Highlights moves to GA April 2026](https://www.microsoft.com/en-us/microsoft-viva/glint) generating AI summaries of survey + behavior signals. If anyone hits Forrester's "full-featured" bar first, it is Microsoft. |
| **Qualtrics / Medallia** | **Survey-platform incumbents pivoting hard.** Qualtrics is shipping "Agentic AI" — multi-agent listening with action triggers; Medallia is leaning into conversational/voice/video feedback. Both will brand themselves "deep listening leaders" within 90 days. |
| **Staffbase** | **Adjacent — likely to add a sentiment layer.** Staffbase's [Navigator + AI quality narrative](../../shared/competitors.md#vs-staffbase) is governance-upstream; deep listening is the natural extension. Watch for a Staffbase product announcement layering sentiment classification onto intranet content + comments by Q3 2026. |
| **Simpplr** | **Comms AI is in the wrong job for this — for now.** [Comms AI (Feb 2026)](../../shared/competitors.md#vs-simpplr) is comms-creation/orchestration, not sentiment NLP. Simpplr's "Smart Answers" intranet AI is closer; expect a Simpplr listening play within 12 months. |
| **Firstup / LumApps / Poppulo** | **Mid-pack.** All three are pitching agentic AI for comms orchestration (Firstup's Five Pillars, LumApps Agent Hub, Poppulo's Create/Target/Analyze). None is yet positioned as a *listening* platform. They will follow Forrester's frame, not lead it. |
| **Workshop / ContactMonkey / Axios HQ** | **Out of frame entirely.** SMB/Foundations-tier email-first competitors will not engage with Forrester's deep-listening narrative — wrong buyer, wrong stack. Useful: this is a frame that does *not* threaten Cerkl Foundations. |

**The competitor that most matters:** **Workvivo Seer.** Forrester's frame is the analyst legitimacy Seer needed at launch. Expect Workvivo to cite this blog (or one of the paywalled reports) in every Seer pitch by Q3 2026.

## Comparison to alternatives — adjacent analyst frames

The prompt asks how Forrester's "deep listening" compares with other analyst frames currently in market. This is the strategic context:

| Analyst frame | How it compares to Forrester's "deep listening" |
|---|---|
| **Gartner "people-centric AI" (2026-05-13, today's #1 deep-dive)** | Different axis, complementary message. Gartner's frame is **AI governance + adoption** — CHROs as owners of decision rights, tool UX, and rollout comms ([gartner.com 2026-05-13](https://www.gartner.com/en/newsroom/press-releases/2026-05-13-gartner-predicts-by-2027-50-percent-of-enterprises-without-a-people-centric-ai-strategy-will-lose-their-top-ai-talent)). Forrester's frame is **AI as a sentiment-detection instrument**. Both put the CHRO/EX leader at the center of AI-era org design. **Travis read:** Gartner says *"deploy AI deliberately to people"* — Forrester says *"listen for what AI deployment is doing to people."* They reinforce each other. |
| **Josh Bersin — "HR in the flow of work" / Superworker** | Bersin's frame is broader — AI as the operating model shift for HR, not specifically a listening category ([joshbersin.com/imperatives](https://joshbersin.com/imperatives/)). Bersin is the populist version of the Forrester argument: AI-driven career assistants boost satisfaction 25%, etc. Less likely to be cited verbatim in an enterprise RFP than Forrester, but more likely to be cited in a board deck. |
| **Perceptyx / Qualtrics "continuous listening"** | Vendor-led precursor. The "continuous listening" frame has been in market 3–4 years; Forrester's "deep listening" is the **AI-native evolution of it**. Forrester is putting the analyst stamp on what Perceptyx, Qualtrics, and Glint have been building toward. ([perceptyx.com — From Measurement to Problem Solving](https://blog.perceptyx.com/from-measurement-to-problem-solving-the-role-of-continuous-listening)) |
| **IDC / McKinsey on EX analytics** | Neither has named a comparable category as cleanly as Forrester has here. McKinsey's EX analytics work treats sentiment as one input among many; Forrester is putting sentiment *at the center.* That category-naming clarity is what gives this Forrester piece outsized impact. |

## Gotchas

- **The blog names zero vendors.** That's deliberate analyst hygiene, but means buyers will Google their way to Viva Glint / Qualtrics / Medallia / Workvivo Seer and conclude *those* are the deep-listening leaders. The vendor narrative race starts now.
- **"Privacy by design" is doing a lot of work.** [73% of companies now use online monitoring tools](https://www.expressvpn.com/blog/workplace-surveillance-trends-us/); employees are pushing back hard on activity tracking (cf. [Meta's no-opt-out backlash, 2026-05-13](https://www.businesstoday.in/technology/story/meta-staff-protest-over-activity-tracking-tool-amid-privacy-concerns-531282-2026-05-13) — covered in today's #9 daily). Forrester acknowledges the surveillance risk in one phrase and moves on; practitioner reaction will be sharper. From an ITSP analysis: *"Employees accept AI in listening when it helps them be heard and helps managers act, not when it feels like surveillance"* ([itspmagazine.com](https://www.itspmagazine.com/redefining-cybersecurity-blog-with-tape3/ai-enabled-employee-sentiment-analysis-balancing-insights-and-action-with-privacy-and-security)).
- **"One to two years away" is the most important sentence in the post.** It frames the next 24 months as the build window — and gives every vendor in the EX/Comms space a deadline to ship a credible deep-listening capability before the category locks in (likely Forrester Wave Q2 2027 or Q2 2028).
- **The frame favors incumbents with the data, not new entrants.** Microsoft (Viva + Teams data), Workvivo (Zoom-bundled, Seer launched), Qualtrics (survey corpus). A Cerkl-sized newcomer cannot get the Teams transcript firehose without a Microsoft partnership or a Zoom partnership — both of which are owned by competitors today.

## Community signal

- **G2 / Capterra:** N/A (analyst report, not a product)
- **Practitioner take 1 — pro-frame, with guardrails:** Ghassan Karian, IC consultant ([isitworking.substack.com, 2025-12-04](https://isitworking.substack.com/p/the-new-science-of-listening-how)): *"Employees accept AI in listening when it helps them be heard and helps managers act, not when it feels like surveillance. Anonymity by default, avoid productivity scoring on individuals, explainability about data collection."* — The most thoughtful practitioner framing of the same idea Forrester is naming.
- **Practitioner take 2 — pragmatic vendor view:** EX Magazine editorial ([emexmag.com, 2025-06-24](https://www.emexmag.com/the-future-of-work-deep-listening-and-ai-reshape-employee-experience-management/)): *"Choosing the right vendor must be profoundly influenced by the company's tolerance for 'deep listening' and its potential implications."* — Even pro-deep-listening publications flag organizational readiness as the gate, not technology.
- **Practitioner take 3 — privacy skepticism is real:** Workplace surveillance pushback is at a multi-year high ([ExpressVPN trends 2026](https://www.expressvpn.com/blog/workplace-surveillance-trends-us/)) — 73% monitoring, employees walking away from jobs over privacy erosion. Any IC team selling "deep listening" internally will need a stronger consent + transparency story than Forrester provides in the blog.
- **No Ragan / Reworked / HR Executive direct coverage of this specific blog post yet** (as of 2026-05-15). That's a real signal — the IC trade press has not picked this up. Forrester is naming the category before practitioners are talking about it, which is the analyst playbook (define the frame, then trade press follows). Expect Reworked / HR Executive coverage within 60 days.

## Recommendation

- **Action:** **Worth watching — *and* worth a small positioning move now.** This is a category-naming event that will shape EX/Comms RFPs by 2027. Cerkl does not need to *enter* the deep-listening category, but Cerkl does need to be ready to answer the question *"how do you do deep listening?"* in enterprise deals where the buyer has read this Forrester piece.
- **First thing to do:** Draft a **one-paragraph "Cerkl's view on deep listening"** position for sales enablement and the website. Working draft: *"Forrester's 'deep listening' frame is right about where EX measurement is heading — passive, real-time, channel-native. Cerkl owns the delivery half of that loop: who got the message, on which channel, when, and whether they read it. Sentiment analytics on Teams chat is the other half — and it's a job better done by Microsoft Viva, Workvivo Seer, or Qualtrics, integrated alongside Cerkl. We don't compete with the listening layer. We make sure the *response* to what you hear actually reaches the right employees."* This is the **complement-not-compete** positioning. It also implicitly endorses Microsoft/Zoom partnerships as integration targets rather than acquisition threats.
- **Time-box:** 2 weeks. Decide by 2026-05-29 whether to (a) publish a short blog post responding to the Forrester frame, (b) brief AEs on the language above, or (c) sit on it and watch for Workvivo Seer / Staffbase / Simpplr to cite Forrester in sales decks first.
- **What would change my mind:**
  - If **Workvivo Seer cites this blog directly** in a public sales asset → escalate; Cerkl needs a counter-narrative immediately.
  - If **Microsoft Viva ships a Forrester-blessed "deep listening" GA feature** in the next 6 months → the category is locked in faster than expected, and Cerkl needs an explicit Viva integration story.
  - If **Forrester Wave Q2 2027 evaluates EX platforms specifically on deep-listening criteria** (no longer just engagement/intranet) → the category has fully replaced the previous evaluation lens; Cerkl must be in or alongside the deep-listening conversation, not adjacent to it.
  - If **a Cerkl customer asks for sentiment analysis on Teams chat as a feature request** → time to revisit whether a lightweight sentiment-on-newsletter-replies capability belongs in the roadmap.

## Open questions

- **Does Forrester's companion report (RES189386, RES189391) name vendors?** The public blog names none. The paywalled reports likely do. Worth a Forrester subscriber check — Travis, do we have access via a Forrester seat at Cerkl or via a customer?
- **Is "deep listening" being baked into the next Forrester Wave: Employee Experience Management Platforms?** Q2 2025 Wave existed; Q2 2026 Wave timing is unconfirmed publicly. If the 2026 or 2027 Wave evaluation criteria explicitly include "deep listening capability," every EX vendor's roadmap shifts overnight.
- **What's the data-residency / consent model Forrester actually recommends?** The blog says "privacy by design" three times but provides no specifics. Without that, "deep listening" remains conceptually vulnerable to the [Meta no-opt-out backlash](https://www.businesstoday.in/technology/story/meta-staff-protest-over-activity-tracking-tool-amid-privacy-concerns-531282-2026-05-13) reaction pattern. Forrester clients should pull RES189391 for the technical answer.
- **Should Cerkl invest in a lightweight sentiment-on-newsletter-replies feature** (analyze reply text, NPS-style comment fields, free-text feedback in Cerkular newsletters) to have *some* answer in the deep-listening conversation, even if not the full Teams-transcript stack? Low cost, on-strategy (it's analytics on Cerkl's own delivery surface, not new data ingestion), and gives the AE a "yes, we do that" answer when the deep-listening question lands. Worth a 30-minute product conversation with the team.
- **Cross-reference with [today's #1 daily item (Gartner people-centric AI)](../daily/2026-05-15.md):** Both analysts are putting the EX leader at the center of AI-era org design. Is there a single Cerkl POV piece that lands *both* frames — Gartner's adoption-and-governance + Forrester's listening-and-response — as the bookends of the 2026 EX leader mandate? **Strong content opportunity for Cerkular newsletter.**

---

## Cross-reference to `shared/competitors.md`

This deep-dive doesn't add a new competitor to the table — it adds a **new evaluation lens** that affects how four existing rows should be read. Suggested updates:

1. **vs. Workvivo row:** Add a line — *"As of 2026-05-15, Workvivo Seer is the most likely vendor to capture Forrester's 'deep listening' framing in market — Cerkl reframe is **complement-not-compete on listening**: 'We're the response layer; Seer is the listening layer.'"*
2. **vs. Staffbase row:** Add a watch-item — *"Staffbase Navigator + AI-quality narrative is one product release away from a deep-listening play; track Q3 2026 announcements."*
3. **Head-to-Head Positioning preamble:** Consider adding a paragraph on the **adjacent analyst frame** — Forrester deep listening + Gartner people-centric AI — that the IC/EX category is being evaluated against, separate from feature-to-feature comparison.
4. **New gap to commission:** Cerkl POV blog post / sales-enablement one-pager — *"How Cerkl thinks about deep listening (and why we're proud not to be in that lane)."* Different artifact than a "vs." page; fits in marketing's POV calendar.
