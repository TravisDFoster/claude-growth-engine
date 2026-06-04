# Feature: Omni-Channel Publishing

> Part of Cerkl Broadcast. For product overview, see [broadcast.md](../broadcast.md).

**Available on:** Omni AI

---

## What It Does

Omni-channel publishing is a delivery layer over the channels employees already use — mobile, Slack, Microsoft Teams, SharePoint/intranet, and microsites. Communicators create and approve content once in the Content Hub; Broadcast routes the appropriately formatted version to each surface. Targeting and personalization carry across: an audience defined in Broadcast applies whether the content lands as a push notification, a Slack post, a Teams Newsfeed card, or an intranet launchpad item.

This is a complement to existing infrastructure, not a replacement. Companies keep SharePoint, Teams, or Slack as the backbone — Broadcast pushes the right content into each surface and tracks engagement back to one source. For content origin and the CMS layer, see [content-management.md](content-management.md). For cross-channel measurement, see [analytics-insights.md](analytics-insights.md).

| Channel | Primary use case | Install path |
|---|---|---|
| Broadcast Mobile | Deskless/frontline employees; push alerts | iOS App Store / Google Play |
| Slack | Public-channel posts in existing Slack workflow | Slack App + workspace OAuth |
| Microsoft Teams | Personalized Newsfeed inside Teams client | Microsoft Teams app store |
| SharePoint / Intranet | Personalized launchpad widget on intranet pages | Microsoft AppSource + web part |
| Microsites | Always-on personalized news hub on the web | Hosted by Broadcast |

---

## Broadcast Mobile

Built for deskless and frontline employees — including those without a corporate email address. Personalized push notifications target by role, location, or any HRIS attribute. A typical mobile rollout can be live within 24 hours of the request from **Settings > Mobile > Send Me Details**.

### Install and login

The app is "Cerkl Broadcast" on the [Apple App Store](https://apps.apple.com/us/app/cerkl-broadcast/id1501717147) and [Google Play](https://play.google.com/store/apps/details?id=com.cerkl.mobile) — no MDM dependency. Three authentication modes:

| Mode | Requires | Flow |
|---|---|---|
| **Magic Link** | Subscribed email inbox on the sign-in device | Enter email → tap link in inbox → app opens authenticated |
| **Magic Code** | Subscribed email inbox on any device | Enter email → retrieve 8-digit code → enter in app (valid 15 min; 3 attempts before 24-hour lockout) |
| **Email-less** | Workspace Name + Unique ID; optional security questions | Tap "Login with Workspace Name" → enter workspace and ID → answer security questions if enabled |

Email-less authentication is the path for employees with no corporate inbox — manufacturing floor, drivers, field crews. Both the workspace login and security questions allow only 2-3 attempts before a 24-hour lockout. iOS users entering an email with an apostrophe should press-and-hold the apostrophe key to select the straight-vertical version; the default iOS curly apostrophe will not match the stored email. Users with multiple instances switch via the hamburger menu's instance dropdown.

### Navigation

**Hamburger menu** — identity, instance switcher, custom links, Contact Us, personalization preferences (category interests, News Digest schedule, followed authors, privacy), and settings.

**Bottom tabs.**
- **Home** — Unviewed content, ordered priority first, then trending, then ML recommendations. Tap to open, swipe right-to-left to dismiss non-priority items, three-dot menu to dismiss priority items.
- **Directory** (optional) — Searchable subscriber list with names, emails, and optionally title, phone, location.
- **Bell** — Priority content not yet opened, with unread-count badge. Opening or dismissing clears the item across Home and bell.

### Push notifications

Push is a per-instance toggle (**Settings > Mobile > Settings > Enable Push Notifications**) and a per-story decision. From a story's Distribution Settings (gear icon), expand Push Notification, toggle on, and pick a date/time. Use push for high-priority, time-sensitive content — overusing it blunts the signal.

---

## Slack

The Slack integration publishes stories, events, and shared links to public Slack channels on a schedule. Employees receive content as part of their normal Slack workflow — no additional login.

### Connection (one-time)

From **Settings > Integrations & Plugins > Slack App** — requires coordination with a Slack workspace admin:

1. **Generate Broadcast Slack Key.** Copy it on first display; key is shown once, valid 14 days. Re-generating invalidates the previous key.
2. **Sign in to Slack** in the same browser session.
3. **Click Connect** to launch the Slack OAuth flow and install the Cerkl Broadcast app to the workspace.
4. **Allow permissions** — identity, public-channel info, workspace member info including emails, posting as `@cerkl_broadcast` (including in channels it has not joined).
5. **Enter the Slack Key** when redirected back to Broadcast, then confirm. A data sync runs and a confirmation email is sent.

Connections start **paused by default** — sends fail until toggled to **Resume**. Each Broadcast organization can connect one Slack workspace at a time.

### Sending content

From any story or event, open Distribution Settings and expand **Slack > Schedule to Channel**. Pick a delivery date/time, select one or more public channels (type-ahead for large workspaces), save, then Publish. Cancel scheduled sends via the trashcan icon — cancellation is immediate. Important Days warnings appear if the scheduled date conflicts with a flagged day.

### Employee experience

Posts render in Slack as a card with story image, title, and summary, posted by the Broadcast instance. Events include date and time. A **Read More** button gates the click — clicking returns an ephemeral message with a secure **Open** link, which signs the user in and opens the story in their browser. This gating honors content privacy settings and registers impressions.

If a user lacks access to a restricted story, the ephemeral message says so. If a story is deleted or expires after posting, the Slack card remains (Slack posts cannot be retracted) but Read More returns the no-access message. Reactions and threaded comments work normally but don't sync back to Insights — Slack impressions roll into total Content Insights, but per-channel Slack analytics are not broken out today.

---

## Microsoft Teams

The Teams integration delivers a personalized Newsfeed inside the Teams client — desktop and mobile — surfacing priority content and ML-ranked recommendations without flooding Teams channels.

### Setup and install

From Broadcast: **Settings > Integrations & Plugins > Cerkl Broadcast Teams**. The Teams administrator must allow the Cerkl Broadcast app on the tenant before individual employees can add it. Employees then install from Teams via **… > More apps**, search "Cerkl Broadcast", click the tile, and **Add** — the app pins to the left-hand menu. Admins can pin the app across the tenant through Teams admin settings so employees find it without installing themselves.

### Employee experience

Two tabs:

**Newsfeed** — Instance dropdown (for multi-instance users), search, and bell for priority notifications. Below: priority content first, then ML-ranked items personalized by role, category interests, and engagement history. Tap to open the story in a browser tab (users not already signed in to Broadcast on the web, with SSO off, will need to log in). Dismiss via **…** on each card; dismissing in Notifications also removes from the main Newsfeed and vice versa for clicked content.

**About** — Cerkl description and links to website, privacy, terms. Pop-out turns the app into a standalone window; reload refreshes the Newsfeed. If the app drops into the **…** overflow when the user switches tabs, that's expected Teams behavior.

Teams content uses Broadcast's hybrid model: rule-based targeting for critical comms plus ML personalization for the rest of the feed. See [ai-personalization.md](ai-personalization.md) and [audience-segmentation.md](audience-segmentation.md).

---

## SharePoint / Intranet

For organizations on SharePoint Online (or a custom intranet that accepts header scripts), the **Intranet Notifications & Personalization** web part places a personalized launchpad on intranet pages. Each identified visitor sees their own queue of priority content and ML recommendations.

### How it works

When an employee lands on a page with the web part installed, the launchpad displays a badge with the count of high-priority items waiting. Clicking opens their feed: priority content first (driven by Distribution Settings on each story), then ML-personalized recommendations. When the employee clicks a story here, it's released from their queue across other channels (News Digest, Mobile, Teams) — read once, gone everywhere. This cross-channel coordination keeps personalization timely rather than repetitive.

### Configuration

From **Settings > Integrations & Plugins > Intranet Notifications & Personalization**: configure Launchpad position (left/right), size (small/standard/large), side and bottom spacing, theme color, and primary/secondary text colors. A Design Preview reflects changes live and supports a Mobile Mode Preview toggle. Some custom intranets carry CSS that overrides Broadcast's settings — escalate to the intranet admin if the launchpad doesn't render as expected.

### Installation paths

Click **Get Code** in the top right for two options:

- **Copy Code** — A header script for custom intranets or any platform that allows scripts in the page header.
- **Copy SharePoint Key** — A key used by the Cerkl Broadcast SharePoint web part.

### SharePoint installation (admin)

The SharePoint app is **Cerkl Broadcast for SharePoint**, free on Microsoft AppSource. Tenant install: **SharePoint Admin Center > More Features > Apps > App Catalog > Site Content**, then **+ New > App > From SharePoint Store**, search "Cerkl", **Add**, then **Deploy** after confirming trust. (If the install option reads "Request It," the tenant admin must approve first.)

Per-site placement: **Site Contents > + New > App > From my Organization** to add the app to the site; edit the target page, **Add a Section**, pick the Cerkl Broadcast for SharePoint app, click the edit pencil, paste the **SharePoint Key**, and **Apply**. Wait 10-15 seconds for the launchpad to render. Section placement on the page doesn't matter — launchpad position is controlled in Broadcast, not SharePoint.

### Where to place the web part

Practically, place it on the main intranet landing page and any high-traffic sub-page (department homepage, employee resources hub). Because position is controlled in Broadcast (left/right of the viewport, anchored to the corner), the launchpad behaves consistently wherever the web part is loaded.

### Troubleshooting

Launchpad not showing usually means either an **invalid key** (re-generate the SharePoint Key, re-paste into the web part, allow 10-15 seconds) or the **visitor is not a subscriber** (the launchpad only renders for identified subscribers — confirm the email in **Audience > Subscribers** and add them if missing). See [audience-segmentation.md](audience-segmentation.md).

---

## Microsites

Microsites are personalized employee news hubs — always-on, web-accessible, role/department/location-tailored aggregations of content from email, Teams, Slack, and SharePoint. They solve information fragmentation: one searchable place an employee can return to instead of hunting across channels. Accessible from any device.

There is no dedicated helpdesk collection for microsites yet; positioning is documented in [broadcast.md](broadcast.md) as part of the Omni AI tier. Treat microsites as a destination that complements push-based channels (mobile, Slack, Teams) rather than competing with them.

---

## Cross-Cutting Behavior

**Targeting consistency.** Audience rules and segments defined once in Broadcast apply across all channels — a "field technicians in the Western region" segment targets the same employees whether the content is a Teams card, a Slack post, a mobile push, or an intranet launchpad item. See [audience-segmentation.md](audience-segmentation.md).

**Content origin.** All channels pull from the same Content Hub. Communicators do not duplicate posts or reformat per channel — Broadcast renders the appropriate representation for each surface. See [content-management.md](content-management.md).

**Cross-channel dismissal.** When an employee opens or dismisses a priority item on one channel, it clears from the others (News Digest, Mobile, Teams, intranet launchpad). Read once, gone everywhere.

**Analytics.** Cross-channel impressions roll up into Content Insights. Email and per-story analytics are mature; Slack-specific and per-channel breakouts are evolving. See [analytics-insights.md](analytics-insights.md).

**Plan availability.** Omni-channel publishing is bundled with the Omni AI tier. Foundations and Foundations+ have email-channel publishing only.

---

*Note: The Cerkl helpdesk also publishes launch-playbook articles (pre-launch announcements, leadership notices, adoption incentive programs, launch digest stories) for mobile, Teams, and intranet. Those are change-management templates for rolling each channel out and are intentionally out of scope for this product reference.*
