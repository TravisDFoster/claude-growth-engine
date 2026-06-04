# Feature: Analytics & Insights

> Part of Cerkl Broadcast. For product overview, see [broadcast.md](../broadcast.md).

**Available on:** Email analytics on all plans; omni-channel analytics on Omni AI.

---

## What It Does

Insights is Broadcast's single source of truth for internal comms performance — real engagement, not just opens. Every plan gets email and blast analytics; Omni AI unlocks cross-channel comparisons across intranet, Teams, mobile, News Digest, and the content archive. The redesigned analytics experience shipped May 12, 2026.

Every page responds to a **reporting period** (Today, Yesterday, Last Week, Last 2/4 Weeks, All Time, Custom) and a **filter set** (segment, category, opt-in status, campaign, blast creator — varies by page). Any page can be set as Insights home, exported to CSV, or pinned into a custom dashboard. See [audience-segmentation.md](audience-segmentation.md) for how segments feed every filter.

---

## Blast Insights

**Insights > Blasts** splits into **Metrics** (per-blast) and **Audience** (per-recipient). A **Quick Insights** modal on any sent blast's ellipsis gives opens, clicks, open rate, and CTR without leaving the Blasts tab.

Clicking into a specific blast surfaces four sub-tabs: **Audience** (per-subscriber delivers, opens, unique opens, clicks, spam reports, bounces, opt-in status); **Links** (total/unique clicks and click rate per URL; click any URL to see who clicked it); **Acknowledgment** (per-recipient open status and date acknowledged — see [pulse-surveys-acknowledgments.md](pulse-surveys-acknowledgments.md)); and **Survey** (aggregated pulse question, reaction style, total responses, response rate, average, most common — combines original and retargeted sends).

Retargeted blasts show a jump link between original and retarget — see [email-blasts.md](email-blasts.md) for retargeting mechanics.

**Unique vs. total.** Every metric ships in two flavors: unique counts a subscriber's first action; total counts every action. Use unique for rates, totals for raw volume.

**What counts as an open.** Image download in the recipient's inbox. Preview-pane views with images visible also count. Broadcast force-registers an open whenever a click is recorded, to partially compensate for image-blocking.

**Finding a blast you just sent.** Insights default to Last 4 Weeks, which excludes today — switch to Today, All Time, or a Custom Range covering today. Data lands no sooner than 15 minutes after send and refreshes every 15 minutes; personalization fields take longer. Wait 1–2 hours or check next day for a clean read.

---

## Channel Dashboards (Omni AI)

Each non-email channel has its own page under **Insights > Channels**, plus a unified **Channels > Overview** comparing them all. Intranet, Mobile, Teams, and Archive share an identical metric structure; News Digest has its own snapshot built around the personalization engine.

**Channels Overview** combines all five channels: total impressions, total clicks, content click rate; channel user activity over time with DAU per channel; channel engagement score over time; usage volume (unique users, total sessions) per channel. This is where communicators answer "which channel is actually working?"

Each channel page reports activity (sessions, average duration, average clicks/session, impressions, clicks, content click rate), an activity-by-hour view (Intranet, Teams, Archive), active users and adoption rate, and an active-users-over-time graph with Avg DAU %, total unique users, Avg DAU. Mobile adds Sessions by OS (iOS vs. Android) and Authenticated Users (first-time verifications). A session is one channel open; it stays alive while the subscriber interacts and expires on inactivity.

**News Digest** at **Insights > Channels > News Digest** has three blocks: a **Cerkl Snapshot** (Engagement Score, Open Rate, CTR, % Personalized — each tile shows a colored prompt linking to a help article); **Delivery Metrics** (Delivery Rate, Open Rate, CTR, with a Compare-to selector for National Average, Cerkls of the same size, or same industry); and **Subscriber Metrics** (Total Audience, new Subscribers, Unsubscribes — self-initiated only). See [ai-personalization.md](ai-personalization.md) for how News Digest content is curated.

---

## Audience, Content, and Category Lenses

The same engagement data cut three ways: by **person**, by **piece of content**, by **topic**.

**Audience Insights** (Insights > Audience) has Metrics, Opt-Outs, and Bounced sub-pages. Metrics offers an Overview tab (per-subscriber News Digest delivers, open rate, CTR, plus all-channel sessions, impressions, clicks, click rate, clicks/session, Engagement Score) and a Details tab that breaks the same data out by channel so you can see who lives on which surface. Click any subscriber to drill into their content history. Opt-Outs distinguishes self-unsubscribes (cannot be re-subscribed under CAN-SPAM) from admin-removals (can be). Bounced lists the email and the server's bounce reason.

**Content Insights** (Insights > Content) lists every published piece with audience reach, aggregate reach %, impressions, clicks, click rate. The time filter here is **publish date**, not engagement date — a deliberate quirk. Click any title for per-subscriber and per-channel breakdowns.

**Category Insights** (Insights > Categories) has two pages. **Most Popular** ranks categories already in Content Controls by interest level (Above Average / Average / Below Average via standard deviation), audience reach, and percent of audience. **Opportunities** surfaces categories subscribers engage with that you **aren't** currently using (no content tagged in 30 days, or not in Content Controls). A blue plus icon jumps to Content Controls to add the category — this is where communicators spot topic gaps.

---

## Custom Dashboards

Build dashboards at **Insights > New Dashboard**. Components mix and match, each with its own reporting period and filter set — a single dashboard can show last week's blast metrics next to last quarter's engagement history next to a forward-looking projected News Digest delivery schedule. Components include Engagement History, Projected News Digest Deliveries, Delivery Interval and Delivery Format pie charts, Cerkl Snapshot, Blast Metrics, Blast Audience Metrics. Components are drag-resizable; time period and filter selections persist.

Dashboards are **private by default**. Team Sharing exposes the dashboard to fellow Team Members and can be disabled. Public Sharing generates a read-only link — once shared, anyone with the URL retains access; it cannot be unshared. Administrators have full visibility; team members access only what they're shared into.

Any Insights table or dashboard component exports to CSV via the filter icon's **Export to CSV** button. Wait for email or check **Insights > Exports**. Exports reflect the page **as currently filtered** — set timeframe and filters first.

---

## Metric Definitions

| Metric | What It Means |
|---|---|
| **Engagement Score** | Blends Open Rate, Click Rate, and Super Click Rate (open + multiple clicks). Comparative, not a health score — use to find low-engagement cohorts |
| **% Personalized** | Share of subscribers receiving personalized content. Includes those who explicitly went through personalization **and** those whose implicit engagement is enough for the AI to tailor |
| **Open Rate** | Unique Opens / Delivers |
| **CTR** | Unique Clicks / Unique Opens |
| **Content Click Rate** | Clicks / Impressions |
| **Impression** | Content appeared on screen — does not require interaction |
| **Audience Reach** | Unique subscribers who had an impression opportunity across all channels |
| **DAU / Adoption Rate** | Daily Active Users; active users as % of total audience |

**Tips.** For Open Rate, set sensible default News Digest delivery time (early morning or lunchtime) and frequency, and resend the Welcome Email annually to non-personalized subscribers. For CTR, diversify content sources, mine the Opportunities page, and tune story title/summary/image (Headlines Only format makes titles do more work). For Engagement Score, content needs to be new, thought-provoking, and relevant.

---

## Edge Cases

**Apple Mail Privacy Protection (Sept 2021).** Apple pre-opens emails and strips tracking on iOS devices, inflating opens. ~40% of blasts land on Apple devices per an internal Cerkl audit. No technical workaround exists. Broadcast force-logs an open whenever a click occurs, but for blasts without links the picture is incomplete. Official guidance: shift the primary engagement metric from opens to **clicks**.

**Data population delay.** Insights load no earlier than 15 minutes after send and refresh every 15 minutes. Personalization fields and large audiences push that further. Wait 12–24 hours for a representative picture before sharing with leadership.

**Time-frame exclusion.** Last Week / Last 2 / Last 4 Weeks exclude today. Use Today, All Time, or a Custom Range covering today for same-day data.

**Content time filter.** Content Insights filters by **publish date**, not engagement date — different from every other Insights page.

---

## Plan Gating

| Surface | All Plans | Omni AI |
|---|---|---|
| Blast Insights (Metrics, Audience, Links, Survey, Acknowledgment) | Yes | Yes |
| Audience Insights, Opt-Outs, Bounced | Yes | Yes |
| Content & Category Insights | Yes | Yes |
| Custom Dashboards, Exports, Filtering, Sharing | Yes | Yes |
| News Digest Insights & Cerkl Snapshot | — | Yes |
| Channels Overview, Intranet, Mobile, Teams, Archive | — | Yes |
| Engagement Score, % Personalized | — | Yes |

Channel-specific dashboards require the corresponding channel active in the instance — see [omni-channel-publishing.md](omni-channel-publishing.md). Cerkl publishes an annual Broadcast Benchmark Report; the News Digest Delivery Metrics block compares directly against National Average, Cerkls of the same size, and same industry inside the product.
