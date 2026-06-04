# Feature: Content Management (CMS / Content Hub)

> Part of Cerkl Broadcast. For product overview, see [broadcast.md](../broadcast.md).

**Available on:** Omni AI

---

## What It Does

The **Content** tab — also called the Content Hub — is Cerkl's CMS. Every Story and Event is authored once here, then flows to [News Digests](ai-personalization.md), the Mobile App, the Content Block in [email blasts](email-blasts.md), Teams, Slack, the public Content Archive, and other surfaces enabled through [omni-channel publishing](omni-channel-publishing.md). One record, one set of tags, one audience target — Broadcast handles formatting per destination.

---

## What You Can Author

Three creation paths sit in the left-hand menu of the Content tab.

| Type | Icon | Use When |
|---|---|---|
| **Story** | Red megaphone | News, updates, longform written in Cerkl |
| **Event** | Green calendar | Anything with a date, location, or registration link — adds registration URL, Google Maps location, start/end times, all-day toggle, calendar-link toggle |
| **Share a Link** | Yellow link | A relevant article already lives elsewhere — paste a URL; Cerkl auto-pulls title, summary, and image, all editable |

Stories and Events share the same anatomy: title (200 char max, 85 recommended), subtitle/summary (250 chars — what shows in the Digest preview), body, story image (1500×1000 px / 3:2; 1600 kb max), categories, and distribution settings. **Emojis** work everywhere — paste as "Paste & Match Style" and preview, since rendering varies by client. The body editor is **Froala** with standard formatting plus inline images, embedded video, file uploads (1 MB cap), and tables; fonts, colors, and **Type Scale Styles** come from Content Controls.

### Publish, Circulation, and Expiration

Three date controls, and the distinction matters: **Publish Date** is when Content becomes eligible to send. **Circulation End Date** stops it from appearing in News Digests, Teams, Slack, Mobile, and the Content Block while keeping it searchable in the Archive and usable inside Blasts. **Expiration Date** removes it from every channel including the Archive (links already delivered still work). Toggle Expiration off for **Evergreen**. Calendars highlight **Important Days** in yellow.

---

## The Library: Drafts → Queue → Approved → Archive

The Content Hub is organized around a single lifecycle. Each library page shares the same table columns (Post, Segments, Categories, Source, Campaigns) and adds page-specific actions.

| Page | What lives there | Key actions |
|---|---|---|
| **Drafts** | Saved but not yet submitted | Edit, Copy, Add to Campaign, Delete |
| **Queue** | Submitted, awaiting approval | Edit, View Live, Preview, **Approve**, Delete |
| **Approved** | Published and/or scheduled — eligible for channels | Edit, View Live, Copy, Share Link, **Repost**, Delete |
| **Archive** | Public Subscriber-facing — items past Circulation End, before Expiration | Search, filter by Trending Categories/Authors, Follow, Subscribe |

The **Approved page** also has a calendar view color-coded for Published (green), Eligible (gray), Circulation End (blue), Expired (red), and Important Days (yellow) — useful for spotting bare days before they happen. Filters cover dates, Categories, Segments, Source, Post Priority, Push Notifications, Content Type, and Campaign. Search covers title, category, URL, and source name. Bulk actions vary by page (Approved adds Expire; Queue adds Approve).

---

## Governance: Controls, Authors, Approvals

**Content > Controls** sets instance-wide defaults: Queue notification frequency (Never/Daily/Weekly), Default Expiration Days (or Never Expire), the public Archive share link, color and Type Scale defaults, and the master Categories list (up to 40 — what Subscribers pick from during personalization). **Auto Generate Categories** AI-tags RSS-sourced articles automatically. The **Authors** toggle decides whether each piece is attributed to the organization or to a named Author Profile (image, first/last name, unique email) that Subscribers can follow.

**Social Advocacy** is the master switch for per-Content sharing buttons. Caveat: anything shared via Social Advocacy generates a public URL that stays live even after the toggle flips back — the only way to revoke is delete or revert to Draft, which wipes insights.

**Approval workflow.** Permissions split into **Create Content** and **Approve Content**. An approver's Publish sends straight to **Approved**, eligible immediately. A creator-only Publish routes to **Queue**, where an approver clicks the green check (or hits Publish Changes from the editor) to release it.

---

## Distribution Settings (the blue gear)

Every piece of Content carries its own Distribution Settings. **Posting Priority** is the most important lever: **Based on audience interests** (default), **To everyone** (bypasses interest matching), or **To everyone as the first story** (pinned to the top slot — for the most critical posts). For both "to everyone" options, choose **Just once** (recommended) or **Multiple times until a pinned date**. The same panel schedules a post to public **Slack** channels, fires a **Mobile** push notification, targets or restricts by **Segment** (restrict overrides "to everyone"), and toggles **Comments** and **Social Advocacy** on the Archive Story page.

---

## Categories: The Personalization Currency

Categories tag Content to a Subscriber's interests. The AI weights them by **explicit** signals (chosen during the welcome flow) and **implicit** signals (what Subscribers actually click), then orders each Digest by overlap between Content tags and weighted interests — broad, accurate tagging matters more than restricting tag count. Org-wide categories are set in Controls; individual Content can carry additional ad-hoc tags beyond that list.

---

## Content Sources (RSS / XML)

**Content > Sources** ingests external feeds — blog, news site, intranet — on an hourly poll (article must have been live at least an hour). For anything more urgent, use Share a Link. Per-source config covers title, associated author, URL, Expiration Days, and Initial Load Number, plus toggles for **Moderation** (on routes to Queue — recommended for third-party feeds; off auto-approves), **Link Tracking**, and Include / Exclude Categories. All source items are treated as Stories.

---

## News Digest Simulator

**Content > Simulator** projects what any Subscriber's next Digest will look like based on the current state of the Hub. Pick a Subscriber by name or email; you see their next subject line, send date, and ordered Stories. Levers that change the output: adding/expiring Content, adjusting Posting Priority, retargeting by Segment, editing headline/summary/image, or changing Categories. It reads live state, so it doubles as the fastest QA path before a campaign lands.

---

## Cross-Instance Sharing and Campaign Linkage

For orgs with multiple instances: **Repost** (Approved page) one-clicks a published piece into selected other instances, **Other Cerkls** lets a Parent Cerkl publish to Child instances at creation time, and **Share Link** (private instances only) generates a public URL anyone can open without signing in. Any Content item can join up to **4 Campaigns** via the Campaigns icon — Campaigns roll into Insights, making them the join key between Content and cross-channel analytics.

---

## Related

[ai-personalization.md](ai-personalization.md) (News Digest mechanics) · [email-blasts.md](email-blasts.md) (Content Block element) · [omni-channel-publishing.md](omni-channel-publishing.md) (Teams, Slack, SharePoint, Mobile, Microsite) · [image-gallery.md](image-gallery.md) (Story Image management)
