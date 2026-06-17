# Insights (Beta) — Overview & Reference

> **Status:** This feature is currently in **Beta** and **under construction**. Everything below is **subject to change** before release to users. This doc is updated during the development process.
>
> This is not exhaustive, but it gives a better idea of the different capabilities within the Insights (Beta) navigation. For more information on different NHI settings and which apply to Insights (Beta), see the related article.

**Permissions:** You must have the **View Insights** permission to view these pages. Actions within a page may require additional permissions.

---

## Contents

- [Insights (Beta) Overview](#insights-beta-overview)
- [Blasts](#blasts)
  - [Overview](#blasts--overview)
  - [Metrics](#blasts--metrics)
  - [Metrics > Specific Blast](#blasts--metrics--specific-blast)
  - [Audience](#blasts--audience)
  - [Audience > Specific Subscriber](#blasts--audience--specific-subscriber)
- [Content](#content)
  - [Overview](#content--overview)
  - [Metrics](#content--metrics)
  - [Metrics > Specific Content](#content--metrics--specific-content)
  - [Audience](#content--audience)
  - [Audience > Specific Subscriber](#content--audience--specific-subscriber)
  - [Channels](#content--channels)
    - [Channels > News Digest](#channels--news-digest)
    - [Channels > Content Archive](#channels--content-archive)
    - [Channels > Blast Content Blocks](#channels--blast-content-blocks)
    - [Channels > Mobile](#channels--mobile)
    - [Channels > Intranet](#channels--intranet)
    - [Channels > Teams](#channels--teams)
  - [Categories](#content--categories)
    - [Categories > Specific Category](#categories--specific-category)
- [Dashboards](#dashboards)
  - [Page Overview](#page-overview)
  - [Dashboard Creation/Editing](#dashboard-creationediting)
  - [Dashboard Blocks](#dashboard-blocks)
- [Exports](#exports)
- [Metric Definitions](#metric-definitions)
- [FAQs](#faqs)
- [Questions?](#questions)

---

## Insights (Beta) Overview

Within Insights (Beta), you can see data based on the selected time frame (unless explicitly called out otherwise). In the upper right-hand corner of every page (except Categories), there is a **time selector**. The selected time carries from page to page, but **resets to default on refresh**.

Insights (Beta) only includes data for the **last 18 months**. This is an 18-month **rolling window** — each day, the day 18 months ago drops off.

### Time options

| Option | Definition |
|---|---|
| **Last 28 Days** *(default)* | Rolling last 28 days, including today |
| **Today** | Today's date |
| **This Week** | Current week (Sunday – today) |
| **Last Week** | Previous week (Sunday – Saturday) |
| **This Month** | Current calendar month (1st – today) |
| **Last Month** | Previous calendar month |
| **This Quarter** | Current quarter (Jan–Mar, Apr–Jun, Jul–Sep, Oct–Dec) |
| **Last Quarter** | Previous quarter |
| **This Year** | Current year-to-date (Jan 1 – today) |
| **Custom Range** | Opens date range selector for manual adjustment |

### Time zone

How data is presented depends on how far back you are looking:

- Data within **90 days** is presented in your **browser time**.
- Data after **90 days** is presented in **UTC**.

> **Note:** For calculations and further explanations of the different Insights metrics, see [Metric Definitions](#metric-definitions).

### Legacy Insights vs. Insights (Beta)

Be careful when comparing date ranges between Legacy Insights and Insights (Beta) — Legacy Insights does not always include today. This can cause date ranges to differ slightly, leading to comparisons against different ranges.

---

## Blasts

Within Insights (Beta), **Blasts** has three subnavigations: **Overview**, **Metrics**, and **Audience**.

### Blasts > Overview

The Overview section includes high-level metrics around Blast communications.

**Page filters:**

- **Targeted Segments** — Segments used for targeting within Blast audiences.
- **Campaigns** — Campaigns assigned to Blasts.
- **Sender Profile** — When enabled, the Sender Profiles used when sending Blasts.
- **Send From** — The name of the sender used when sending Blasts.
- **Blast Creator** — The creator of sent Blasts.
- **Targeted Categories** — Categories/interests used for targeting within Blast audiences.

**Metric blocks:**

**Blast Key Metrics**

- **Delivered** — The number of Blasts successfully delivered to targeted Subscribers. *(Secondary value: Delivery Rate)*
- **Open Rate** — Percent of delivered Blasts that registered a Unique Open. *(Secondary value: Unique Opens)*
- **Click-Thru Rate** — Percent of recipients who clicked within the Blasts. *(Secondary value: Unique Clicks)*

The dot on the percentage bar lets you compare these rates to your organization's average from the last 18 months.

**Blast Metrics Over Time** — Displays how Delivers, Total Opens, and Total Clicks trend over time.

- *Block actions:* **View Metrics** (opens Blasts > Metrics in a new tab); **Ellipsis > Download PNG** (downloads the graph image, named after the block title).

**Blast Activity Log** — Displays a count of each Subscriber's Delivers, Total Opens, and Total Clicks, broken down by day and hour.

- *Block actions:* **Metric drop-down** (Delivered, Total Opens, Total Clicks); **Ellipsis > Download PNG**.
- *Note:* Heat map data is only available for the previous 90 days.

**Blasts Sent** — Displays a daily breakdown of the number of Blasts this organization is sending compared to the average.

- *Block actions:* **Ellipsis > Download PNG**.
- *Example:* If you sent 6 Blasts to 1,000 people each, that counts as 6 Blasts sent in this graph, not 6,000.

**Highest Open Rate Blasts** — Displays up to 5 Blasts with the highest Open Rate.

- *Block actions:* **View Blasts Metrics** (opens Blasts > Metrics in a new tab); **New Tab icon** (opens the Blast-specific metrics page in a new tab).

**Lowest Open Rate Blasts** — Displays up to 5 Blasts with the lowest Open Rate.

- *Block actions:* **View Blasts Metrics** (opens Blasts > Metrics in a new tab); **New Tab icon** (opens the Blast-specific metrics page in a new tab).

> **Private Blasts:** All private Blasts, regardless of whether you have access, display in a private state — titled "Private Blast" with no preview image. If you have access, you can click the Blast to see more.

### Blasts > Metrics

The Metrics section includes table metrics around Blast communications.

**Columns:**

- **Default:** Blast, Delivered, Unique Opens, Unique Clicks, Open Rate, Click-Thru Rate, Blast Creator
- **Additional:** Subject Line, Campaigns, Sender Profile, Target Segments, Total Opens, Total Clicks, Send From, Translation, Time Zone, Targeted Categories, Bounces, Spam Reports

In the sticky **Blast** column, you may see icons indicating a Blast **was retargeted** or **is a retarget of another**. Clicking a Blast opens a detail page with more specific information.

**Search:** By Blast Name or Subject Line.

**Filters:** Targeted Segments, Campaigns, Sender Profile, Send From, Blast Creator, Targeted Categories.

**Sort (when enabled):** Blast (Send Date/Time), Delivered, Unique Opens, Unique Clicks, Open Rate, Click-Thru Rate, Blast Creator, Sender Profile, Total Opens, Total Clicks, Send From, Translation, Time Zone, Bounces, Spam Reports.

**Export:** All columns on your table. **Edit Table:** Add, remove, and rearrange columns in your default view.

> **Private Blasts:** display in a private state (see note above).

### Blasts > Metrics > Specific Blast

When you click a Blast from the list, you see a page with Blast-specific metrics.

**Page filters:** **Segments**; **Audience Status** (Subscribed or Unsubscribed — all users by default).

**Date range:** Inherited from the previous page but changeable in the upper right. Keep the send date in mind when changing the range.

**Header info/actions:** Blast thumbnail, title, send from, sent date, subject line, and creator. Icons indicate the Blast was retargeted, is a retarget of another, or is Private. Actions open the Insights page for the retargeted/original Blast, or open the Blast thumbnail.

**Blast Key Metrics:**

- **Delivered** — Times this Blast successfully delivered to targeted Subscribers. *(Secondary: Delivery Rate)*
- **Open Rate** — Percent of Unique Opens this Blast received. *(Secondary: Unique Opens)*
- **Click-Thru Rate** — Percent of recipients who clicked at least one link in this Blast after opening. *(Secondary: Unique Clicks)*

The dot on the percentage bar lets you compare against your org's 18-month average.

**Audience tab:**

- **Default columns:** Audience Member, Delivered, Unique Opens, Total Opens, Unique Clicks, Total Clicks
- **Additional:** Bounces, Spam Reports
- **Search:** Audience Member first name, last name, or email.
- **Sort:** Audience Member (Name), Delivered, Unique Opens, Total Opens, Unique Clicks, Total Clicks, Bounces, Spam Reports.
- **Export** / **Edit Table** available.

**Links tab:**

- **Default columns:** URL, Unique Clicks, Total Clicks
- Clicking a link opens a modal listing all the specific Subscribers who clicked it.
- **Search:** by URL. **Sort:** URL, Unique Clicks, Total Clicks. **Export** available.
- Only links with data appear in this table.

> **Customer Success Callout:** This links table **does** include personalized links (acknowledgments, pulse surveys, unsubscribe, etc.). If there's feedback around these links, submit it to Product.

**Performance tab** — blocks displayed depend on the Blast's contents:

- **Acknowledgment Results** *(conditional)* — Metrics around this Blast's Acknowledgment. **Expand icon** opens a modal of recipients, whether they acknowledged, and the date.
- **Pulse Survey Results** *(conditional)* — Metrics around this Blast's Pulse Survey. **Expand icon** opens a modal of recipients and their responses.
  - *Customer Success Callout:* To prevent users from seeing individual subscriber survey responses, disable the expand option via **ISS > Organization > Organization Summary > Configuration > Organization Settings > "Display Individual Pulse Survey Responses."**
- **Blast Unique Opens** — Open engagement: how many recipients who opened this Blast clicked any link. **Ellipsis > Download PNG**.
- **Clicks per Unique Open** — Click engagement: how many recipients who opened this Blast clicked any link. **Ellipsis > Download PNG**.
- **Blast Activity Log** — Count of each recipient's Delivers, Total Opens, and Total Clicks by day and hour. **This heatmap is locked to the first 7 days after send.** Metric drop-down (Delivered, Total Opens, Total Clicks); **Ellipsis > Download PNG**.
  - *Note:* Heat map data is only available for the previous 90 days.

### Blasts > Audience

The Audience section includes table metrics around Blast audiences.

**Columns:**

- **Default:** Audience Member, Delivered, Unique Opens, Unique Clicks, Open Rate, Click-Thru Rate
- **Additional:** Total Opens, Total Clicks, Bounces, Spam Reports

Clicking a Subscriber opens a detail page with more specific information.

**Search:** Audience Member first name, last name, or email. **Filters:** Segments; Audience Status.

**Sort (when enabled):** Audience Member, Delivered, Unique Opens, Unique Clicks, Open Rate, Click-Thru Rate, Total Opens, Total Clicks, Bounces, Spam Reports.

**Export** / **Edit Table** available.

> **Unsubscribed members** display anonymously as "Unsubscribed User." You cannot click into anonymous users for details.

### Blasts > Audience > Specific Subscriber

When you click a Subscriber from the list, you see a page with Blast metrics for that Subscriber.

**Page filters:** Sender Profile; Send From; Blast Creator. **Date range:** inherited, changeable in the upper right.

**Header info/actions:** Subscriber name and email; action opens the subscriber details modal.

**Blast Key Metrics:**

- **Blast Volume** — Average number of Blasts delivered to this Subscriber per day.
- **Unique Opens** — Count of Blasts this Subscriber opened at least once.
- **Unique Clicks** — Count of Blasts this Subscriber clicked at least one link in.

**Metrics tab:**

- **Default columns:** Blast, Delivered, Unique Opens, Total Opens, Unique Clicks, Total Clicks
- **Additional:** Blast Creator, Sender Profile, Send From, Subject Line, Bounces, Spam Reports
- The sticky **Blast** column may show retargeted/retarget icons. There is **no click action** on the Blast in this table.
- **Search:** Blast Name or Subject Line. **Sort:** Blast (Sent Date), Delivered, Unique Opens, Total Opens, Unique Clicks, Total Clicks, Bounces, Spam Reports.
- **Export** / **Edit Table** available.
- *Private Blasts* display with "Private Blast" as title and subject line, no preview image.

**Performance tab:**

- **Open Rate vs. Average** — This Subscriber's Open Rate vs. the org's (org data = last 18 months). **Ellipsis > Download PNG**.
- **Click-Thru Rate vs. Average** — This Subscriber's CTR vs. the org's (last 18 months). **Ellipsis > Download PNG**.
- **Blasts Delivered** — Number of Blasts delivered to this Subscriber over time. **Ellipsis > Download PNG**.
- **Blast Activity Log** — This Subscriber's Delivers, Total Opens, Total Clicks by day and hour. Metric drop-down; **Ellipsis > Download PNG**.
  - *Note:* Heat map data is only available for the previous 90 days.

---

## Content

Within Insights (Beta), **Content** has five subnavigations: **Overview**, **Metrics**, **Audience**, **Channels**, and **Categories**.

### Content > Overview

The Overview section includes high-level metrics around Content.

**Page filters:** Targeted Segments (restriction or interest); Campaigns; Targeted Categories; Content Creator; Priority; Content Type; Authors; Source (RSS feed title).

**Metric blocks:**

**Content Key Metrics**

- **Total Sessions** — Total unique starts to engagement through any Broadcast Channel. A Session begins when a Subscriber enters your Channel. *(Secondary: Sessions/Subscriber)*
- **Total Impressions** — Total views of content delivered via any Broadcast Channel. An Impression occurs each time a Subscriber is shown a piece of Content, whether or not they click. *(Secondary: Impressions/Session)*
- **Total Clicks** — Total clicks on content delivered via any Broadcast Channel. The Content Click Rate is the percentage of Impressions that resulted in a click. *(Secondary: Content Click Rate)*

**Content Metrics by Channel** — Breakdown of Sessions, Impressions, and Clicks in each Channel. Metric drop-down (Total Impressions, Total Sessions, Total Clicks); **Ellipsis > Download PNG**.

**Content Metrics Over Time** — Breakdown of Sessions, Impressions, and Clicks in each Channel over time. Metric drop-down; **Ellipsis > Download PNG**.

**Content Click Activity Log** — Click activity for your Content overall and by channel, by day and hour. Metric drop-down (All Channels, News Digests, Content Archive, Content Block, Mobile, Intranet, Teams); **Ellipsis > Download PNG**.

- *Note:* Heat map data is only available for the previous 90 days.

**Active Users by Channel** — Number of Active Users across each Broadcast Channel. **Ellipsis > Download PNG**.

**Most Popular Content by Click Rate** — Up to 5 Content pieces with the highest Click Rate across all Channels. **View Content Metrics**; **New Tab icon**.

**Least Popular Content by Click Rate** — Up to 5 Content pieces with the lowest Click Rate across all Channels. **View Content Metrics**; **New Tab icon**.

> **Deleted posts** display along with their metrics in a reduced "deleted" visual state. Anyone can click deleted posts to see more.

### Content > Metrics

The Metrics section includes table metrics around content pieces.

**Columns:**

- **Default:** Post, Audience Reach, Total Impressions, Total Clicks, Click Rate
- **Additional:** Content Type, Circulation End Date, Expiration Date, Targeted Categories, Targeted Segments, Source, Priority, Pinned Until, Restricted, Author, Campaigns, Push Alert, Advocacy

Clicking a Content piece opens a detail page.

**Search:** by post title.

**Filters:** Targeted Segments, Campaigns, Targeted Categories, Content Creator, Priority, Content Type, Authors, Source, Push Alert, Channel.

**Sort (when enabled):** Post (Publish Date), Audience Reach, Total Impressions, Total Clicks, Click Rate, Content Type, Circulation End Date, Expiration Date, Source, Priority, Pinned Until, Restricted, Author, Push Alert, Advocacy.

**Export** / **Edit Table** available.

**ID column icons:**

- Published and live within feeds
- Published and available on the Archive, but not circulating within feeds
- Expired post
- Deleted post

> **Deleted posts** display along with metrics in a reduced state; anyone can click them for more.

### Content > Metrics > Specific Content

When you click a Content piece from the list, you see a page with Content-specific metrics.

**Page filters:** Segments; Personalized (whether members have explicitly personalized); Audience Status.

**Header info/actions:** Story image, title, author, and publish dates.

**Status icons:**

- **Published** — *Published Until {date}* (past publish date & set to change status); *Published Forever* (past publish date & evergreen)
- **Archived** — *Archived Until {date}* (past Circulation End Date & set to expire); *Archived Forever* (past Circulation End Date & evergreen)
- **Expired** — Past Expiration Date
- **Deleted** — Published & since deleted
- **Top Story**, **Pinned**, **Targeted Segments**, **Restriction Segments**

**Actions:** Open the Story Page in a new tab; open the Content details modal.

**Content Key Metrics:**

- **Audience Reach** — Unique Subscribers with at least one Impression recorded for this Content.
- **Total Impressions** — Total times Content was shown to your Subscribers on any Channel.
- **Total Clicks** — Total unique times Content was clicked within any Channel.

**Audience tab:**

- **Default columns:** Audience Member, Total Impressions, Total Clicks, Click Rate
- **No click action** on the Audience Member.
- **Search:** Audience Member first name, last name, or email. **Sort:** Audience Member (Name), Total Impressions, Total Clicks, Click Rate. **Export** available.
- *Unsubscribed members* display anonymously as "Unsubscribed User."

**Performance tab** *(filters: Targeted/Restricted Segments)*:

- **Content Metrics by Channel** — Sessions, Impressions, Clicks by Channel. Metric drop-down; **Ellipsis > Download PNG**.
- **Content Activity** — Sessions, Impressions, Clicks by Channel over time. Metric drop-down; **Ellipsis > Download PNG**.

### Content > Audience

The Audience section includes table metrics around Content audiences.

**Columns:**

- **Default:** Audience Member, Total Sessions, Total Impressions, Total Clicks, Click Rate
- **Additional:** Clicks Per Session, Personalized

Clicking an Audience Member opens a detail page.

**Search:** Audience first name, last name, or email. **Filters:** Segments, Personalized, Audience Status, Channel.

**Sort (when enabled):** Audience Member (Name), Total Sessions, Total Impressions, Total Clicks, Click Rate, Clicks Per Session, Personalized.

**Export** / **Edit Table** available.

> **Unsubscribed members** display anonymously as "Unsubscribed User."

### Content > Audience > Specific Subscriber

When you click a Subscriber from the list, you see a page with Content metrics for that Subscriber.

**Page filters:** Campaigns; Content Creator; Priority; Content Type; Authors; Source.

**Header info/actions:** Subscriber name and email; action opens the subscriber details modal.

**Audience Key Metrics:**

- **Total Sessions** — Total unique starts to engagement initiated by this Subscriber through any Broadcast Channel.
- **Total Impressions** — Total views from this Subscriber on Content via any Broadcast Channel.
- **Total Clicks** — Total clicks from this Subscriber on Content via any Broadcast Channel.

**Metrics tab:**

- **Default columns:** Post, Last Activity, Total Impressions, Total Clicks
  - *Last Activity* = the date this Subscriber last interacted with the post in any way (Impressions/Clicks).
- **No click action** on the Content piece.
- **Search:** Content title. **Sort:** Post, Last Activity, Total Impressions, Total Clicks. **Export** available.
- *ID column icons:* Published/live; Published/archive-only; Expired; Deleted.

**Performance tab:**

- **Content Metrics by Channel** — Sessions, Impressions, Clicks by Channel. Metric drop-down; **Ellipsis > Download PNG**.
- **Content Activity** — Sessions, Impressions, Clicks over time. Metric drop-down; **Ellipsis > Download PNG**.
- **Content Activity Log** — Sessions, Impressions, Clicks for this Subscriber by day and hour. Metric drop-down; **Ellipsis > Download PNG**.
  - *Note:* Heat map data is only available for the previous 90 days.

### Content > Channels

The Channels section includes high-level summary metrics around Content Channels.

**Page filters:** Campaigns; Content Type.

**Metric blocks** — each displays Sessions, Impressions, and Click Rate for that channel's activity:

- **News Digests**
- **Content Archive**
- **Blast Content Blocks**
- **Mobile**
- **Intranet**
- **Teams**

#### Channels > News Digest

When you click **View** inside the News Digest block, you see News Digest-specific metrics.

**Page filters:** Segments; Personalized; Audience Status.

**News Digest Key Metrics:**

- **Delivered** — News Digests successfully delivered to targeted Subscribers. *(Secondary: Delivery Rate)*
- **Open Rate** — Percent of delivered News Digests that registered a Unique Open. *(Secondary: Unique Opens)*
- **Click-Thru Rate** — Percent of recipients who clicked within News Digest. *(Secondary: Unique Clicks)*

The dot on the percentage bar lets you compare against your org's 18-month average.

**Performance tab:**

- **News Digest Over Time** — How Deliveries, Total Opens, and Total Clicks trend over time. **View Metrics** (opens Content > Metrics); **Ellipsis > Download PNG**.
- **News Digest Activity Log** — Deliveries, Total Opens, Total Clicks by day and hour. Metric drop-down; **Ellipsis > Download PNG**. *(Heat map: previous 90 days only.)*
- **News Digest Delivered** — Daily breakdown of News Digests delivered vs. the average. **Ellipsis > Download PNG**.
- **Percent Personalized** — Percentage of current News Digest–eligible Subscribers who have explicitly personalized. **Ellipsis > Download PNG**. *(Time period locked — always current data.)*
- **News Digest Delivery Format Breakdown** — The format eligible Subscribers are set to receive. **Ellipsis > Download PNG**. *(Time period locked.)*
- **News Digest Delivery Frequency** — How often eligible Subscribers are set to receive, based on org defaults and (when allowed) individual preferences. **Ellipsis > Download PNG**. *(Time period locked.)*
  - If your org is on a **fixed schedule**, the schedule displays instead of the chart and download is disabled.
- **News Digest Delivery Day Breakdown** — Which day of the week eligible Subscribers are set to receive. **Ellipsis > Download PNG**. *(Time period locked.)*
  - If your org is on a **fixed schedule**, the schedule displays instead of the chart and download is disabled.

#### Channels > Content Archive

When you click **View** inside the Content Archive block, you see Content Archive–specific metrics.

**Page filters:** Segments; Audience Status.

**Content Archive Key Metrics:**

- **Total Sessions** — Unique starts to engagement from Subscribers within this Channel.
- **Total Impressions** — Times Content from this Channel appeared in a Subscriber's feed.
- **Total Clicks** — Times Subscribers clicked on Content from this Channel.

**Performance tab:**

- **Content Archive Breakdown** — Avg. Sessions/Active User; Active Users; Avg. Total Clicks/Session; Content Click Rate; Avg. Impressions/Session; Avg. Impressions/Active User.
- **Content Archive Most Active Users** — Up to 5 most active Subscribers by Sessions. **View All Active Users** opens a modal (Session count, last Session date, Total Clicks) with export.
- **Content Archive Activity Trends** — Sessions, Impressions, Clicks across time. Metric drop-down; **Ellipsis > Download PNG**.
- **Content Archive Activity Log** — Sessions, Impressions, Clicks by day and hour. Metric drop-down; **Ellipsis > Download PNG**. *(Heat map: previous 90 days only.)*

#### Channels > Blast Content Blocks

When you click **View** inside the Blast Content Block block, you see Blast Content Block–specific metrics.

**Page filters:** Segments; Audience Status.

**Blast Content Block Key Metrics:** Total Sessions; Total Impressions; Total Clicks *(same definitions as Content Archive)*.

**Performance tab:**

- **Blast Content Block Activity Trends** — Sessions, Impressions, Clicks across time. Metric drop-down; **Ellipsis > Download PNG**.
- **Blast Content Blocks Activity Log** — Sessions, Impressions, Clicks by day and hour. Metric drop-down; **Ellipsis > Download PNG**. *(Heat map: previous 90 days only.)*

#### Channels > Mobile

When you click **View** inside the Mobile block, you see Mobile-specific metrics.

**Page filters:** Segments; Audience Status.

**Mobile Key Metrics:** Total Sessions; Total Impressions; Total Clicks.

**Performance tab:**

- **Mobile Breakdown** — Avg. Sessions/Active User; Active Users; Avg. Total Clicks/Session; Content Click Rate; Avg. Impressions/Session; Avg. Impressions/Active User.
- **Mobile Most Active Users** — Up to 5 most active Subscribers by Sessions. **View All Active Users** modal with export.
- **Mobile Activity Trends** — Sessions, Impressions, Clicks across time. Metric drop-down; **Ellipsis > Download PNG**.
- **Mobile Activity Log** — Sessions, Impressions, Clicks by day and hour. Metric drop-down; **Ellipsis > Download PNG**. *(Heat map: previous 90 days only.)*
- **Mobile Daily Active Users** — Count of Active Users in this Channel over time. **Ellipsis > Download PNG**.

#### Channels > Intranet

When you click **View** inside the Intranet block, you see Intranet-specific metrics.

**Page filters:** Segments; Audience Status.

**Intranet Key Metrics:** Total Sessions; Total Impressions; Total Clicks.

**Performance tab:**

- **Intranet Breakdown** — Avg. Sessions/Active User; Active Users; Avg. Total Clicks/Session; Content Click Rate; Avg. Impressions/Session; Avg. Impressions/Active User.
- **Intranet Most Active Users** — Up to 5 most active Subscribers by Sessions. **View All Active Users** modal with export.
- **Intranet Activity Trends** — Sessions, Impressions, Clicks across time. Metric drop-down; **Ellipsis > Download PNG**.
- **Intranet Activity Log** — Sessions, Impressions, Clicks by day and hour. Metric drop-down; **Ellipsis > Download PNG**. *(Heat map: previous 90 days only.)*

#### Channels > Teams

When you click **View** inside the Teams block, you see Teams-specific metrics.

**Page filters:** Segments; Audience Status.

**Teams Key Metrics:** Total Sessions; Total Impressions; Total Clicks.

**Performance tab** *(filters: Targeted/Restricted Segments, Categories, Campaigns)*:

- **Teams Breakdown** — Avg. Sessions/Active User; Active Users; Avg. Total Clicks/Session; Content Click Rate; Avg. Impressions/Session; Avg. Impressions/Active User.
- **Teams Most Active Users** — Up to 5 most active Subscribers by Sessions. **View All Active Users** modal with export.
- **Teams Activity Trends** — Sessions, Impressions, Clicks across time. Metric drop-down; **Ellipsis > Download PNG**.
- **Teams Activity Log** — Sessions, Impressions, Clicks by day and hour. Metric drop-down; **Ellipsis > Download PNG**. *(Heat map: previous 90 days only.)*

### Content > Categories

The Categories section includes table metrics around Content categories.

Category metrics are **always based on current data**. For that reason:

- This page does **not** have a date range filter.
- Only **live Subscribers** are included (no bounced or unsubscribed users).

**Columns (default):** Category, Interested Subscribers, Percent of Audience, Category Source.

Clicking a Category opens a detail page.

**Search:** by Category name. **Filters:** Segments; Personalized; Category Source (Organization or Other Categories — e.g., from feeds or manually added; all by default).

**Sort (when enabled):** Category, Interested Subscribers, Percent of Audience, Category Source. **Export** available.

> **Notes:** To be considered "interested" in a Category, a Subscriber must have more than **0.5 interest weight**. For more on category interest and weight, see the related article. **Category data is shared across organizations.**

#### Categories > Specific Category

When you click a Category from the list, you see Subscriber metrics for that Category. As with the Categories list, metrics are **always current data** — no date range filter, live Subscribers only.

**Page filters:** Segments; Personalized.

**Audience tab:**

- **Default columns:** Audience Member, Interest Level, Opt-in Status
- **No click action** on the Subscribers.
- **Search:** Audience Member name or email. **Sort:** Audience Member, Interest Level, Opt-in Status. **Export** available.

---

## Dashboards

Within Insights (Beta), the Dashboards page allows for the creation of custom reports.

### Page Overview

This page shows the Dashboards in your Organization that you have access to. Create new Dashboards using the **Create Dashboard** button in the upper right.

**Tabs:**

- **My Dashboards** — Dashboards you created, regardless of access level.
- **Shared with Me** — Dashboards created by others and shared with you.
- **Global** — Dashboards created by others and shared with everyone.
- **All** — All Dashboards you have access to, regardless of access level or creator.

**Table columns:**

- **Name** — Name of the Dashboard.
- **Description** — Description given to the Dashboard.
- **Creator** — Creator of the Dashboard.
- **Last Updated** — The last time pieces of the Dashboard were updated and by whom (name/description change, adding/removing blocks, moving/resizing blocks).
- **Access Level** — Restricted/Global; click to see/change who has access.
- **Date Created** — Creation date of the Dashboard.

**Ellipsis options:** **View Dashboard** (opens the editor/detail view); **Edit Info** (rename/update description); **Manage Access** (change access level); **Delete** (remove the Dashboard from your Organization).

### Dashboard Creation/Editing

Within the Dashboard edit/detail view, some actions are at the page level and others at the block level.

**Page-level actions:**

- **Manage Access** — Change the access level of the Dashboard.
- **+ New Block** — Opens a modal to add a new block with a custom time period/description.
  - *Note:* The following blocks have a **locked time period** (current data, on the main page too): Percent Personalized, News Digest Delivery Format Breakdown, News Digest Delivery Frequency, News Digest Delivery Day Breakdown, Content Categories Reference List.
- **Ellipsis > Edit Info** — Rename or update the description.
- **Ellipsis > Delete** — Remove the Dashboard from your Organization.

**Block-level actions** (same as their main-page counterparts, plus):

- **Expand/Contract** — Set block width to 50% or 100% (Dashboards allow two columns of blocks max).
- **Ellipsis > Edit** — Edit:
  - **Time Period** *(locked for the current-data blocks listed above)*
  - **Description** *(optional, max 240 characters)*
  - **Filters** *(match the options on the main page counterpart; see the filters spreadsheet for the full list per block)*
- **Ellipsis > Duplicate** — Opens a modal with a duplicate block, "COPY" prepended to the description. *(Not saved until "Add to Dashboard" is selected.)*
- **Ellipsis > Download PNG** — Downloads the graph image, named after the block title.
- **Ellipsis > Delete** — Remove the block from the Dashboard.
- **Drag and Drop** — Hover the middle of the block header to drag the block to a new location.
- **Change Height** — Hover the bottom of the block to drag up/down and change height.

### Dashboard Blocks

You can add any of these blocks to your Dashboard. They share the same definitions as their main-page counterparts, plus a few dashboard-only blocks (simple tables called **Reference Lists**).

> **Note:** The maximum number of blocks per Dashboard is **30**.

**Blasts**

- **Overview blocks:** Blast Key Metrics, Blast Metrics Over Time, Blast Activity Log, Blasts Sent, Highest Open Rate Blasts, Lowest Open Rate Blasts
- **Dashboard-only:**
  - **Blast Metrics Reference List** — Columns: Blast, Sent Date, Delivered, Unique Opens, Unique Clicks, Open Rate, Click-Thru Rate
  - **Blast Audience Reference List** — Columns: Audience Member, Delivered, Unique Opens, Unique Clicks, Open Rate, Click-Thru Rate

**Content** *(Foundation and Essential packages will not see this tab or its blocks.)*

- **Overview blocks:** Content Key Metrics, Content Metrics by Channel, Content Metrics Over Time, Content Click Activity Log, Active Users by Channel, Most Popular Content by Click Rate, Least Popular Content by Click Rate
- **Channel blocks:**
  - **News Digest:** News Digest, News Digest Key Metrics, News Digest Over Time, News Digest Activity Log, News Digest Delivered, Percent Personalized, News Digest Delivery Format Breakdown, News Digest Delivery Frequency, News Digest Delivery Day Breakdown
  - **Content Archive:** Content Archive, Content Archive Key Metrics, Content Archive Breakdown, Content Archive Most Active Users, Content Archive Activity Trends, Content Archive Activity Log
  - **Blast Content Block:** Blast Content Block, Blast Content Block Key Metrics, Blast Content Block Activity Trends, Blast Content Block Activity Log
  - **Mobile:** Mobile, Mobile Key Metrics, Mobile Breakdown, Mobile Most Active Users, Mobile Activity Trends, Mobile Activity Log, Mobile Daily Active Users
  - **Intranet:** Intranet, Intranet Key Metrics, Intranet Breakdown, Intranet Most Active Users, Intranet Activity Trends, Intranet Activity Log
  - **Teams:** Teams, Teams Key Metrics, Teams Breakdown, Teams Most Active Users, Teams Activity Trends, Teams Activity Log
- **Dashboard-only:**
  - **Content Metrics Reference List** — Columns: Post, Publish Date, Audience Reach, Total Impressions, Total Clicks, Click Rate, Expiration Date
  - **Content Audience Reference List** — Columns: Audience Member, Total Sessions, Total Impressions, Total Clicks, Click Rate
  - **Content Categories Reference List** — Columns: Category, Interested Subscribers, Percent of Audience, Category Source

---

## Exports

Currently there is no exports page — exports happen in a modal. It is a future change to move them to a separate page.

---

## Metric Definitions

The calculations for these metrics are based on the data within the selected time period, unless noted otherwise on the page.

> **Customer Success Callout:** For a list of all the block tooltips in Insights III, see the tooltips spreadsheet.

### Active Users (#)

Number of Audience Members who recorded at least one Session within the Channel, regardless of whether they clicked.

- *Calculation:* N/A
- *Example:* Within Mobile, 25 people recorded at least one Session → Mobile had 25 Active Users.

### Audience Members (#)

Number of those in your Audience, including Subscribers, Bounced, and Unsubscribed users.

- *Calculation:* N/A
- *Example:* 10,000 Subscribers + 5,000 Unsubscribed = **15,000** Audience Members.

### Audience Reach (#)

Number of Audience Members who had at least one Impression/Open recorded for a piece of Content.

- *Note:* Within DCT summary rows, Audience Reach is based on the total number of unique Audience Members.
- *Calculation:* # of Audience Members with ≥1 Impression or Open
- *Example:* 500 people opened the same piece of Content in their News Digest → Audience Reach of 500.

### Blast Volume (#)

Average number of Blasts delivered to this Subscriber per day.

- *Calculation:* # of Blasts Delivered ÷ Number of Days
- *Example:* Subscriber "A" received 4 Blasts in the last 28 days → Blast Volume = 4 ÷ 28 = **0.14**.

### Blasts Sent (#)

Count of the Blasts created and sent in Broadcast.

- *Calculation:* N/A
- *Example:* Send 3 emails to 4,000 Subscribers on Tuesday → Blasts Sent for Tuesday = **3**.

### Bounced Audience Member (#)

Number of those in your Audience that have bounced.

- *Calculation:* N/A
- *Example:* 10,000 Subscribers + 200 Bounced → Bounced Audience Member count = **200**.

### Bounces (#)

Number of messages that failed to be delivered to Audience Members for a Blast or Digest.

- *Calculation:* N/A
- *Example:* A Blast sent to 1,000 people with 50 failures → Bounce count = **50**.

### Click-Thru Rate (%)

Percentage of delivered Blasts/Digests that registered at least one click.

- **Legacy Insights vs. Insights (Beta):** In Legacy Insights the formula is (Unique Clicks ÷ Unique Opens) × 100. **Insights (Beta) was updated to reflect the business standard.**
- *Calculation:* (Unique Clicks ÷ Delivered) × 100
- *Example:* 2,000 received the Blast, 300 clicked at least one link → (300 ÷ 2,000) × 100 = **15%**.

### Clicks per Session (#)

Average number of clicks generated during a single engagement session in any Channel. Higher values indicate deeper interaction within each visit.

- *Calculation:* Total Clicks ÷ Total Sessions
- *Example:* 20 clicks across 5 Content Archive visits → 20 ÷ 5 = **4**.

### Clicks per Unique Open (%)

Percentage of Audience Members who opened a Blast and then clicked a link.

- *Calculation:* (Unique Clicks ÷ Unique Opens) × 100
- *Example:* 500 opens, 300 of those recipients clicked → (300 ÷ 500) × 100 = **60%**.

### Content Click Rate (%)

Percentage of Impressions that resulted in a click on a piece of Content in your Channels.

- *Calculation:* (Total Clicks ÷ Total Impressions) × 100
- *Example:* 6,000 Impressions, 1,350 clicks → (1,350 ÷ 6,000) × 100 = **22.5%**.

### Delivered (#)

Number of Blasts/Digests successfully delivered to Audience Members' inboxes.

- *Calculation:* N/A
- *Example:* A Blast sent to 1,000 with 950 delivered → Delivered = **950**.

### Delivery Rate (%)

Percentage of Blasts/Digests successfully delivered to Audience Members' inboxes.

- *Calculation:* (Delivered ÷ Sent) × 100 — where Total Sent = Delivered + Bounced
- *Example:* Delivered to 500, bounced for 50 → (500 ÷ (500 + 50)) × 100 = **90.9%**.

### Interest Level

A Subscriber's relative interest in a Category, based on all those interested in the same Category. Three buckets:

- **Above Average:** ≥ 1 standard deviation above the mean
- **Average:** within 1 standard deviation of the mean (between −1 and 1)
- **Below Average:** ≤ −1 standard deviation below the mean

- *Calculation:* (Subscriber's weight − mean weight of all interested Subscribers) ÷ standard deviation of the weight of all interested Subscribers, then bucketed by the thresholds above.
- *Example:* 4 Subscribers interested in "Cerkl" with weights 1.3, 1.2, 1.1, 1.0 (Total = 4.6; Mean = 1.15; SD = 0.1291):
  - Sub A: (1.3 − 1.15) ÷ 0.1291 = **1.16 → Above Average**
  - Sub B: (1.2 − 1.15) ÷ 0.1291 = **0.38 → Average**
  - Sub C: (1.1 − 1.15) ÷ 0.1291 = **−0.387 → Average**
  - Sub D: (1.0 − 1.15) ÷ 0.1291 = **−1.16 → Below Average**

### Interested Subscribers (#)

Number of Subscribers with an interest weight of **0.60 or more** in a Category.

- *Note:* Within DCT summary rows, this is based on the total number of unique Audience Members. Bounced Subscribers are not included.
- *Calculation:* N/A
- *Example:* 10,000 Subscribers, 6,000 with ≥0.6 weight in Category "A" → 6,000 Interested Subscribers.

### Open Rate (%)

Percentage of Audience Members who opened the Blasts/Digests they received.

- *Calculation:* (Unique Opens ÷ Delivered) × 100
- *Example:* 2,000 received, 1,800 opened → (1,800 ÷ 2,000) × 100 = **90%**.

### Percent of Audience (%)

Percentage of current Subscribers with an interest weight of 0.60 or more in a Category.

- *Note:* Within DCT summary rows, this is based on the total number of unique Subscribers. Bounced Subscribers are not included in the denominator.
- *Calculation:* (Subscribers with ≥0.60 interest ÷ Current Subscriber count) × 100
- *Example:* 6,000 of 10,000 → (6,000 ÷ 10,000) × 100 = **60%**.

### Response Rate (%)

Rate at which Audience Members targeted to receive a Blast containing an Acknowledgement or Pulse Survey submitted a response.

- *Calculation:* (Count of Responses ÷ Target Audience) × 100
- *Example:* Targeted 800, 600 responded → (600 ÷ 800) × 100 = **75%**.

### Sent (#)

Number of send attempts for a Blast/Digest. Inferred from two values because SendGrid does not provide Sent directly.

- *Calculation:* Delivers + Bounces
- *Example:* 950 delivered + 50 bounced → **1,000**.

### Subscribers (#)

Number of current, non-bounced Subscribers in the system.

- *Calculation:* N/A
- *Example:* 10,000 people in the audience → Subscriber count = **10,000**.

### Target Audience (#)

Number of Audience Members selected to receive a specific Blast or Digest.

- *Calculation:* N/A
- *Example:* Three Segments totaling 1,999 Subscribers + 1 Individual Recipient → Target Audience = **2,000**.

### Total Clicks (#)

Total number of tracked click events across Blasts and Content. Includes multiple clicks from individual Audience Members.

- *Calculation:* N/A
- *Example:* 500 members each click Content "A" twice → 1,000 Total Clicks.

### Total Impressions (#)

Total number of times a piece of Content is shown to an Audience Member.

- *Note:* For Content Block Impressions, if the same piece appears multiple times within a Blast for layout purposes, it does not double the Impressions for that piece within the Blast.
- *Calculation:* N/A
- *Example:* 3 pieces on Mobile + 4 in a Digest → Total Impressions = **7**.

### Total Opens (#)

Total number of times a Blast or Digest was opened by Audience Members. Includes multiple opens from individuals.

- *Calculation:* N/A
- *Example:* A member opens a Blast 3 times → 3 Total Opens.

### Total Sessions (#)

Total count of times engagement started within a Channel. A Session is recorded when an Audience Member opens a Channel or a Digest/Blast containing a Content Block.

- *Calculation:* N/A
- *Example:* Opens Mobile App 2 times + News Digest 1 time → 3 Total Sessions.

### Unique Clicks (#)

Number of distinct Audience Members who clicked at least one tracked link within a Blast. Two levels:

- **Blast Overview Level** — How many recipients clicked ANY tracked link in a Blast. One user cannot record more than one Unique Click at the Blast level.
- **Per-Blast Link Level** — How many recipients clicked each tracked link. One user cannot record more than one Unique Click on each link, but can record more than one across links.

- *Calculation:* N/A
- *Example:* A member clicks 5 different links in a Blast → Blast Overview Level: 1 Unique Click; Per-Blast Link Level: 1 Unique Click on each of the 5 links (5 total in the links table).

### Unique Opens (#)

Number of Audience Members who opened a Blast/Digest at least once.

- *Calculation:* N/A
- *Example:* A member opens a Blast 3 times → 1 Unique Open.

### Unsubscribed Audience Member (#)

Number of those in your Audience that have unsubscribed.

- *Calculation:* N/A
- *Example:* 10,000 Subscribers + 5,000 Unsubscribed → Unsubscribed Audience Member count = **5,000**.

> **Margin of error:** There may be a small variance between reports. Insights uses **Materialized Views** across very large datasets, introducing a measured variance of around **0.57%** in exchange for dramatically faster query performance.
>
> *Example:* When viewing a list of Blasts, engagement is grouped at a higher level, so metrics use an approximate count. When viewing a list of Subscribers, Blast data is broken down per user, so a direct count is possible. Both are accurate, but you may see this margin of error due to the different views.

> **Legacy Insights vs. Insights (Beta):** In Legacy Insights, content metrics (e.g., Impressions and Sessions) are based on uniques; in Insights (Beta) they are focused on **totals**. This can cause a discrepancy when comparing between the two navigations.

---

## FAQs

**How does data reporting work when a Subscriber updates to a privacy level that does not report metrics?**

Data reporting is based on the Subscriber's **current** privacy level. If a Subscriber changes to a privacy level that doesn't report Insights data, already collected/displayed data is not impacted. Going forward, their future activity is no longer tracked/displayed in Insights (Beta) — unless they change their privacy level again.

> **Note:** Blast email metrics are slightly different. If the Subscriber was set to a non-tracking privacy level when the email was sent, changing their privacy level won't start showing their metrics for that already-sent email, because privacy level is tied to the email Blast as a whole.

**Callouts for DCT within Insights:**

- The summary row (top row with totals) is a separate backend call from the table data. Metrics should line up; if you notice a discrepancy, let engineering know.
- For Audience Member searches, you can currently only search by email, first name, **OR** last name. Full name search will not work on every table until **BD-10729: [Insights III] Table Cleanup: Full Name Search** is complete (status: Ready).
- When logged in via ISS and performing an export for a user, the export is based on the **user's** saved columns, not ISS user column changes. This is true for all DCT currently; changing it would require a feature request.
- *(Once there is an exports page, behavior with emails/displays when logged in as a user will be documented.)*
- **PSA:** You can horizontally scroll using **SHIFT + SCROLL**.

**Is there any delay in seeing info within the Insights Navigation?**

Data is collected in Analytics in real time, but there can be a delay syncing Broadcast data into Insights (e.g., unsubscribe event, new communications, segment changes). This time varies depending on how long Google takes to process changes. As for the public API *(NOT YET AVAILABLE to users)*, all analytics data is available in real time with minimal processing delay per event.

**For Retargeted Blasts, how do metrics display?**

Metrics for Retargets are split into two related pages:

- **Overview metrics** — Separate per-Blast (opens/delivers/clicks based on actions within the Retarget or Retargeted Blast).
- **Acknowledgement metrics** (if applicable) — Separate per-Blast.
- **Pulse Survey metrics** (if applicable) — **Combined per-survey** (responses on the Retargeted Blast also display for the Retarget).

**Does Slack data display in Insights?**

We are collecting data for Slack, but it is not displayed anywhere. We would need **FUTURE-810: Slack Insights** to start seeing those events.

**More information on time zone logic:**

Data is organized based on the timeframe: within 90 days → user's browser time; after 90 days → UTC. Based on backend logic, there is a chance data isn't accounting for your time zone correctly within the 90-day window. We expect this to be rare:

- On the backend, we pass through the time zone string, but it is **case sensitive** and must match exactly to the IANA names in our system. If we cannot match the user's time zone, data falls back to UTC.
- If a client runs into this, let Product know and/or comment on **BD-10511: [Insights III] Timezones – Fallback Case** (status: To Do).

**Are there any callouts CS should know about the Legacy Insights data backfilled into Insights (Beta)?**

Data was backfilled from Legacy Insights up until **June 1, 2026**. At that date, data coming into Insights (Beta) began going through the new reporting API flow/logic. Additional callouts:

- Unsubscribe data was included in the backfilled data.
- Privacy level was considered when exporting data for the backfill — if a user was set to "not report" at the time of export, none of their data was pulled over.

> **Customer Success Callout:** For a list of reasons you may see different data in Legacy Insights vs. Insights (Beta), see the comparison document.

---

## Questions?

If you have any questions, please send a message in the Slack **#product-questions** channel so anyone with an answer can provide one.
