# Cerkl Broadcast vs. Microsoft Viva (Engage + Amplify) — Capability Comparison

> Internal research reference, not a print one-pager. Scope: measurement/reporting and audience lists/targeting, with general capability context.
> For the polished, account-specific handouts (TMNAS), see the sibling files `cerkl-vs-viva-amplify-2026-05-29.md` and `cerkl-vs-viva-engage-2026-05-29.md`.
> Slug: cerkl-vs-viva-engage-amplify | Date: 2026-05-29
>
> Fact basis:
> - Cerkl column verified against internal source of truth `shared/broadcast.md` (2026-05-29). Where external web research conflicted with `broadcast.md`, `broadcast.md` wins.
> - Viva columns verified against Microsoft Learn / Microsoft Support (2026-05-29). Microsoft ships frequent Viva updates — re-verify caps/limits before any public claim.
> - Known corrections applied to earlier web research: SMS is NOT a Cerkl channel; Okta SSO is confirmed; the AI feature is "News Digests / AI Newsletters" (Omni AI is the plan tier); Foundations+/Omni AI pricing is audience-based ("contact sales"), not a published $799/mo; Calendar Invites (real Outlook/Google events) added.

---

## TL;DR

These three tools play different games. **Viva Engage** is an enterprise social network (the Yammer successor). **Viva Amplify** is a campaign-publishing layer inside Microsoft 365. **Cerkl Broadcast** is a dedicated, measured, personalized employee-comms system. Cerkl's two structural advantages over both Viva products are exactly the two areas in scope: **recipient-level measurement** and **dynamic, personalized audience targeting at scale** — and both are available starting on the **free Foundations** plan.

---

## What each is fundamentally built for

| | Core design | Comms model |
|---|---|---|
| **Viva Engage** | Social network — communities, Storyline, Leadership Corner, Answers, Campaigns, recognition | Two-way social engagement; pull/opt-in feed |
| **Viva Amplify** | Multi-channel campaign authoring inside M365 | "Write once," auto-reformat per channel |
| **Cerkl Broadcast** | Dedicated employee comms + AI 1:1 personalization | Targeted/personalized broadcast with read-level tracking |

---

## Priority 1 — Measurement / Reporting

| Capability | Viva Engage | Viva Amplify | Cerkl Broadcast |
|---|---|---|---|
| **Per-recipient open / read** | No — aggregate "reach" only (~15s dwell threshold) | No — aggregate "unique viewers," anonymized; suppressed below a threshold | **Yes** — per-employee opens + reads |
| **Read confirmation / acknowledgment** | No | No | **Yes** — timestamped read receipts + required acknowledgments (all plans) |
| **Per-link click tracking** | Not documented | Not documented | **Yes** — who clicked what, near real-time |
| **Cross-channel in one view** | No (single-channel) | Yes — Email/Teams/SharePoint/Engage side by side | **Yes** — email/mobile/Teams/Slack/SharePoint (Omni AI tier) |
| **Sentiment / AI themes** | Yes (Premium) | Yes (reactions only) | Engagement scoring (method not public) |
| **Export / API** | CSV; Graph API rate-limited; MGDC export being retired | CSV / image / PPT; no native Power BI or API | CSV + **REST API** (Foundations+); RSS/SFTP |
| **History retention** | 18 months (cut from 24) | Undocumented | Undocumented |
| **Available on free tier** | Basic only; full analytics need paid Viva add-on | No — bundled in paid Viva only | **Yes** — email analytics + read receipts on free Foundations |

**The headline gap for both Viva products: no email-grade, recipient-level measurement.** Engage reports aggregate community/network engagement (views, reactions, replies); Amplify reports anonymized aggregate "unique viewers." Neither tracks per-recipient opens, per-link clicks, or "who hasn't read this." Cerkl does all three — plus timestamped read receipts and required acknowledgments — **starting on the free plan**.

**Sharp, citable Amplify flaw:** Dynamic Distribution Groups break its analytics — Microsoft Graph resolves a DDG as a *single* recipient, so a 1,200-person send can register as **one** unique viewer. Microsoft's own Q&A says to use static lists instead.

---

## Priority 2 — Audience Lists / Targeting

| Capability | Viva Engage | Viva Amplify | Cerkl Broadcast |
|---|---|---|---|
| **Targeting model** | Communities + leader "audiences" | Channel-based recipient lists per send | Dynamic, rules-based segments |
| **Audience source** | Entra/M365/security/dynamic groups; org attributes (recent GA) | CSV import + DL/M365/Entra groups (SharePoint promotion only) | **HRIS/IdP sync** (Workday, SAP, PeopleSoft, ADP, Paycor, AD) + CSV |
| **Auto-updating membership** | ~24h sync; leader designation manual | Static lists recommended for accurate tracking | **Yes** — segments auto-update, no IT ticket (all plans) |
| **Granularity** | Dept/country/title (recent) | SharePoint promotion only, not the actual send | Role, location, department, tenure, custom attributes |
| **Per-recipient content personalization** | No — same post to all | No — same content per channel | **Yes** — News Digests / AI Newsletters per person (Omni AI tier) |
| **Recipient cap per send** | 40 audiences per leader | **200 recipients/groups per publication** | Tier-based (5k sends/mo free; unlimited on paid) |
| **Self-serve vs. admin-gated** | Admin-provisioned + license-gated | Communicator-driven but capped | Self-serve; decentralized permissions |
| **Real calendar invites** | No | No | **Yes** — Outlook + Google Calendar events, rules-targeted (Foundations+) |

**The headline gaps:**
- **Amplify's 200-recipient-per-publication cap** is its most-cited limit — enterprise sends must be split into multiple ≤200 lists.
- **Neither Viva product varies content per audience.** Amplify adapts *format* per channel, not *content* per segment — everyone in a channel gets the same thing. Engage targets *who sees a post*, not personalized content. Cerkl's entire value prop is the opposite: each employee can receive an individually curated digest.
- **Engage targeting is admin-gated and license-gated** (Employee Communications & Communities plan), not self-serve.
- Cerkl's dynamic HRIS-synced segmentation is available **on all plans, including free**.

---

## Where Viva actually wins (be honest)

- **Native to M365** — no extra platform, login, or spend if the org already owns Viva Suite (~$12/user/mo) or the Communications & Communities add-on (~$2/user/mo).
- **Engage** is genuinely better for two-way community, social engagement, leadership Storyline, recognition, and AI sentiment/theme analysis.
- **Amplify** reaches Teams + Engage natively (which standalone email tools don't) with built-in SharePoint governance/approvals.

**Cerkl's own weaknesses** (from third-party reviews, for honest positioning): no autosave (lost-work complaints), steep learning curve, email-builder design limits, undisclosed engagement-score methodology, no industry benchmarking, and no native external-BI connector (export is CSV/API).

---

## Cerkl facts used here (verified against `shared/broadcast.md`)

- **Channels:** email (primary), Teams, Slack, SharePoint/intranet, web, mobile app, microsites. (No SMS. No native digital signage.)
- **All plans include:** drag-and-drop builder, Audience Manager (dynamic HRIS-synced segmentation), email analytics/Insights, pulse surveys, timestamped read receipts + acknowledgments, retargeting, 133-language translation, GDPR/CCPA/encryption compliance, WCAG 2.1 AA.
- **Foundations (free forever):** 5,000 sends/mo, 3 communicator seats, 1 instance. SSO and API are add-ons here.
- **Foundations+:** audience-based pricing; adds unlimited sends/seats, API access, SSO included (Okta, Azure AD, Google Workspace), real Outlook/Google **Calendar Invites**, 3 instances.
- **Omni AI:** audience-based pricing; adds **News Digests / AI Newsletters** (per-employee personalization), omni-channel publishing + cross-channel analytics, CMS/Content Hub, enterprise support, 6 instances.
- **Scale:** reaches nearly 6 million employees monthly. SOC 2 Type II; AES-256 at rest, TLS 1.2+ in transit.

---

## Caveats — verify before any public claim

- **Engage attribute-based targeting** (dept/country/title) was reaching GA around early–mid 2026 — confirm current state and whether the 40-audience cap changed.
- **Amplify's Power BI/API absence** and both products' **data-retention limits** are inferred from missing Microsoft docs, not positive statements.
- **Viva pricing** (~$2 and ~$12/user/mo) is list/third-party — enterprise agreements differ.
- **Cerkl engagement-score methodology** is not published; don't make precise claims about how it's computed.

---

## Sources

**Microsoft Viva (verified 2026-05-29):**
- Engage analytics: https://learn.microsoft.com/en-us/viva/engage/analytics
- Engage leaders & audiences: https://learn.microsoft.com/en-us/viva/engage/leadership-identification
- Amplify reporting signals: https://support.microsoft.com/en-us/topic/use-reporting-signals-in-microsoft-viva-amplify-to-understand-campaign-performance-776ac7ec-71ef-48af-a67f-a6875f15d4e6
- Amplify publish limits (200-recipient cap): https://support.microsoft.com/en-us/topic/publish-a-viva-amplify-publication-68ee5c0d-8350-4fab-bafc-4a7a8ca72ec7
- Amplify DDG open-rate limitation: https://learn.microsoft.com/en-us/answers/questions/5441081/viva-amplify-analytics-why-cant-i-track-open-rates
- Viva pricing: https://www.microsoft.com/en-us/microsoft-viva/pricing

**Cerkl Broadcast:**
- Internal source of truth: `shared/broadcast.md` (authoritative)
- Public reference: https://cerkl.com/broadcast/plans-and-pricing
