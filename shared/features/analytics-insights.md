# Feature: Analytics & Insights

> Part of Cerkl Broadcast. For product overview, see [broadcast.md](../broadcast.md).

**Available on:** Email/Blast analytics on all plans; Content & omni-channel analytics on Omni AI.

---

## What It Does

Insights is Broadcast's single source of truth for internal comms performance — real engagement, not just opens. Every plan gets Blast (email) analytics; Omni AI unlocks Content analytics and cross-channel comparisons across News Digest, Content Archive, Blast Content Blocks, Mobile, intranet, and Teams.

The current generation — **Insights (Beta)**, internally "Insights III" — restructures the navigation around **Blasts**, **Content**, and **Dashboards**, adds session/impression metrics across channels, and changed the Click-Thru Rate formula to the business standard (see [Metric Definitions](#metric-definitions)). It replaces Legacy Insights; Legacy data was backfilled up to **June 1, 2026**, after which data flows through the new reporting API.

Every page responds to a **time selector** (top-right of every page except Categories) and a **filter set** that varies by page. The selected time carries page to page but resets to default on refresh.

**Time periods:** Last 28 Days *(default)*, Today, This Week, Last Week, This Month, Last Month, This Quarter, Last Quarter, This Year, Custom Range.

**Data window:** rolling **18 months** — each day, the day 18 months ago drops off.

**Time zone:** data within 90 days is shown in the user's **browser time**; data older than 90 days is shown in **UTC**.

Any page can be exported to CSV and any block pinned into a custom Dashboard. See [audience-segmentation.md](audience-segmentation.md) for how segments feed every filter. **Permission:** View Insights is required; some in-page actions need additional permissions.

---

## Blast Insights

**Insights > Blasts** has three sub-pages: **Overview**, **Metrics**, and **Audience**.

- **Overview** — high-level Blast Key Metrics (Delivered/Delivery Rate, Open Rate/Unique Opens, Click-Thru Rate/Unique Clicks, each comparable to the org's 18-month average), plus Blast Metrics Over Time, a Blast Activity Log heatmap, Blasts Sent vs. average, and Highest/Lowest Open Rate Blasts.
- **Metrics** — per-blast table (default: Blast, Delivered, Unique Opens, Unique Clicks, Open Rate, Click-Thru Rate, Blast Creator; many additional columns). Sticky Blast column flags retargets.
- **Audience** — per-recipient table (Audience Member, Delivered, Unique Opens, Unique Clicks, Open Rate, Click-Thru Rate).

Clicking a blast opens a detail page with four areas: **Audience** (per-subscriber delivers, opens, clicks, bounces, spam reports); **Links** (unique/total clicks per URL — click a URL to see who clicked it; **includes** personalized links like acknowledgments, pulse surveys, unsubscribe); **Performance** (conditional Acknowledgment Results and Pulse Survey Results blocks — see [pulse-surveys-acknowledgments.md](pulse-surveys-acknowledgments.md) — plus Blast Unique Opens, Clicks per Unique Open, and a Blast Activity Log locked to the first 7 days after send). Pulse Survey results combine original and retargeted sends; an ISS org setting ("Display Individual Pulse Survey Responses") can hide individual responses.

Clicking a subscriber opens their Blast history with vs.-average comparisons (Open Rate, Click-Thru Rate), Blasts Delivered over time, and a per-subscriber activity log. Retargeted blasts jump-link between original and retarget — see [email-blasts.md](email-blasts.md) for retargeting mechanics.

**Unique vs. total.** Unique counts a subscriber's first action; total counts every action. Use unique for rates, totals for raw volume.

**Private blasts** display anonymously ("Private Blast," no preview) unless you have access. **Unsubscribed members** display anonymously ("Unsubscribed User") and can't be clicked into.

---

## Content Insights (Omni AI)

**Insights > Content** has five sub-pages: **Overview**, **Metrics**, **Audience**, **Channels**, and **Categories**. Content engagement is measured in **Sessions**, **Impressions**, and **Clicks**.

- **Overview** — Content Key Metrics (Total Sessions/Sessions per Subscriber, Total Impressions/Impressions per Session, Total Clicks/Content Click Rate), Content Metrics by Channel and Over Time, a Content Click Activity Log, Active Users by Channel, and Most/Least Popular Content by Click Rate.
- **Metrics** — per-piece table (Post, Audience Reach, Total Impressions, Total Clicks, Click Rate; ID-column icons flag live / archive-only / expired / deleted). **Deleted posts still display** with metrics in a reduced state.
- **Audience** — per-subscriber table (Total Sessions, Total Impressions, Total Clicks, Click Rate, Clicks per Session, Personalized).

Clicking a piece shows status (Published/Archived/Expired/Deleted, Top Story, Pinned, targeting), Audience Reach / Impressions / Clicks, a per-subscriber Audience tab, and a Performance tab (Content Metrics by Channel, Content Activity over time). Clicking a subscriber shows their content history with per-channel breakdowns and an activity log.

> **Note:** Foundation/Essential packages do not see the Content tab or its blocks.

---

## Channel Dashboards (Omni AI)

**Insights > Content > Channels** gives a summary card (Sessions, Impressions, Click Rate) for each channel, each with a **View** into a dedicated page:

- **News Digest** — Delivered/Delivery Rate, Open Rate, Click-Thru Rate (vs. 18-month average), plus News Digest Over Time, activity log, News Digest Delivered vs. average, and four **current-data** blocks (time period locked): **Percent Personalized**, **Delivery Format Breakdown**, **Delivery Frequency**, **Delivery Day Breakdown**. On a fixed schedule, the schedule replaces the chart and download is disabled. See [ai-personalization.md](ai-personalization.md).
- **Content Archive**, **Mobile**, **Intranet**, **Teams** — share a structure: Total Sessions / Impressions / Clicks key metrics, a Breakdown block (Avg. Sessions/Active User, Active Users, Avg. Total Clicks/Session, Content Click Rate, Avg. Impressions/Session, Avg. Impressions/Active User), Most Active Users (top 5, expandable to a full exportable list), Activity Trends, and an Activity Log heatmap. **Mobile** adds Daily Active Users over time. **Teams** adds Targeted/Restricted Segment, Category, and Campaign filters.
- **Blast Content Blocks** — Total Sessions / Impressions / Clicks, Activity Trends, and an Activity Log.

A **Session** begins when a subscriber enters a channel (or opens a Digest/Blast containing a Content Block). Heatmap (activity log) data is available for the previous **90 days** only.

---

## Category Insights (Omni AI)

**Insights > Content > Categories** ranks every category by **Interested Subscribers** (interest weight > 0.5), **Percent of Audience**, and **Category Source** (Organization vs. Other — feeds, manual, etc.). Category metrics are **always current data** — no date filter, live subscribers only. **Category data is shared across organizations.** Clicking a category shows its audience with each subscriber's **Interest Level** (Above Average / Average / Below Average, by standard deviation) and Opt-in Status.

---

## Custom Dashboards

Build dashboards under **Insights > Dashboards** ("Create Dashboard"). The page lists **My Dashboards**, **Shared with Me**, **Global**, and **All**. Each dashboard mixes blocks — Blast and Content blocks plus dashboard-only **Reference Lists** (Blast Metrics, Blast Audience, Content Metrics, Content Audience, Content Categories) — each with its own time period (max 240-char description) and filter set. A single dashboard can show last week's blast metrics next to last quarter's engagement next to a locked current-data block. Blocks are drag-rearranged, expand/contract between 50% and 100% width (two columns max), and resize in height. **Max 30 blocks per dashboard.**

Current-data blocks have a **locked time period**: Percent Personalized, News Digest Delivery Format Breakdown, News Digest Delivery Frequency, News Digest Delivery Day Breakdown, Content Categories Reference List.

Dashboards have a **Restricted/Global** access level managed per dashboard; administrators have full visibility, team members access only what they're shared into.

Exports currently happen in a modal (a dedicated Exports page is a future change). When logged in via ISS and exporting for a user, the export reflects the **user's** saved columns, not ISS column changes.

---

## Metric Definitions

| Metric | What It Means / Calculation |
|---|---|
| **Click-Thru Rate** | **(Unique Clicks ÷ Delivered) × 100.** Updated to the business standard — Legacy used Unique Clicks ÷ Unique Opens (now reported separately as *Clicks per Unique Open*) |
| **Open Rate** | (Unique Opens ÷ Delivered) × 100 |
| **Delivery Rate** | (Delivered ÷ Sent) × 100, where Sent = Delivered + Bounced |
| **Clicks per Unique Open** | (Unique Clicks ÷ Unique Opens) × 100 |
| **Content Click Rate** | (Total Clicks ÷ Total Impressions) × 100 |
| **Clicks per Session** | Total Clicks ÷ Total Sessions — depth of interaction per visit |
| **Total Sessions** | Times engagement started in a channel (channel open, or Digest/Blast with a Content Block) |
| **Total Impressions** | Times content was shown to a subscriber (no interaction required); duplicate content within one Blast isn't double-counted |
| **Audience Reach** | Unique subscribers with ≥1 Impression/Open for a piece of content |
| **Active Users** | Subscribers with ≥1 Session in a channel, regardless of clicks |
| **Blast Volume** | Avg. Blasts delivered to a subscriber per day (Delivered ÷ days) |
| **Interest Level** | A subscriber's relative interest in a category, bucketed by std. dev: Above Average (≥1), Average (−1 to 1), Below Average (≤−1) |
| **Interested Subscribers / Percent of Audience** | Subscribers with interest weight ≥0.60 in a category (count / % of current subscribers; bounced excluded) |
| **Engagement Score** *(legacy concept)* | Blends Open Rate, Click Rate, and Super Click Rate — comparative, not a health score |
| **% Personalized** | Share of subscribers receiving personalized content (explicit personalization **and** implicit-engagement-driven tailoring) |

**Unique vs. total.** Unique counts a subscriber once (first action); total counts every action. At the per-link level a subscriber can register one Unique Click *per link*.

**Tips.** For Open Rate, set a sensible default News Digest delivery time/frequency and resend the Welcome Email annually to non-personalized subscribers. For CTR, diversify content sources, mine the Categories opportunities, and tune story title/summary/image. For engagement, content needs to be new, thought-provoking, and relevant.

---

## Edge Cases

**Click-Thru Rate redefinition.** Insights (Beta) reports CTR as Unique Clicks ÷ **Delivered**; Legacy used ÷ Unique Opens. When comparing to historical Legacy numbers, expect lower CTR figures — the old definition now lives as *Clicks per Unique Open*.

**Legacy vs. Beta data discrepancies.** Legacy content metrics (Impressions, Sessions) were unique-based; Insights (Beta) uses **totals**. Legacy date ranges don't always include today. Both can cause apparent discrepancies when comparing the two. Backfill ran through June 1, 2026; privacy level at export time was honored (non-reporting users weren't pulled over).

**Measurement margin.** Insights uses Materialized Views over very large datasets, introducing a measured variance of ~**0.57%** in exchange for speed. List-level (e.g., Blasts) metrics use grouped/approximate counts; per-subscriber views use direct counts — both accurate, but they can differ slightly.

**Apple Mail Privacy Protection (Sept 2021).** Apple pre-opens emails and strips tracking on iOS, inflating opens (~40% of blasts land on Apple devices per an internal Cerkl audit). No technical workaround; Broadcast force-logs an open whenever a click occurs. Official guidance: prioritize **clicks** over opens.

**Data delay.** Analytics is collected in real time, but syncing Broadcast events (unsubscribes, new comms, segment changes) into Insights can lag depending on processing time. Wait before sharing same-day numbers with leadership.

**Privacy level is current-state (with one exception).** Reporting follows a subscriber's *current* privacy level; switching to a non-reporting level stops future tracking but doesn't erase prior data. **Exception:** Blast email metrics are tied to the privacy level at send time and won't retroactively appear.

**Time-frame & time-zone gotchas.** Default is Last 28 Days. Within 90 days, data is browser-time; older data is UTC. A rare backend case: time-zone strings are case-sensitive IANA matches — an unmatched zone falls back to UTC (report to Product / BD-10511).

**Heatmaps.** Activity Log (heatmap) data is available for the previous 90 days only.

---

## Plan Gating

| Surface | All Plans | Omni AI |
|---|---|---|
| Blast Insights (Overview, Metrics, Audience, Links, Performance) | Yes | Yes |
| Custom Dashboards, Blast Reference Lists, Exports, Filtering | Yes | Yes |
| Content Insights (Overview, Metrics, Audience) | — | Yes |
| Channels: News Digest, Content Archive, Blast Content Blocks, Mobile, Intranet, Teams | — | Yes |
| Category Insights | — | Yes |
| Sessions / Impressions / Engagement Score / % Personalized | — | Yes |

> Foundation/Essential packages do not see the Content tab or its blocks. Channel-specific dashboards require the corresponding channel active in the instance — see [omni-channel-publishing.md](omni-channel-publishing.md). Cerkl publishes an annual Broadcast Benchmark Report; News Digest delivery metrics compare against National Average, Cerkls of the same size, and same industry inside the product.
