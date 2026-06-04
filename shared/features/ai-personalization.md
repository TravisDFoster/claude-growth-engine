# Feature: AI Personalization — News Digest / AI Newsletters

> Part of Cerkl Broadcast. For product overview, see [broadcast.md](../broadcast.md).

**Available on:** Omni AI tier

---

## What It Does

Broadcast automatically curates and delivers a personalized newsletter for each employee. ML analyzes interactions with content over time and prioritizes the stories, updates, and resources most relevant to each person — by role, stated category interests, and behavioral engagement.

Communicators retain control over required content; the AI determines ordering and display per individual. Each employee receives a uniquely tailored newsletter rather than uniform communications. Building newsletters goes from a weekly project to requiring no time at all.

Supports 133 languages. Content sources are managed in the CMS — see [content-management.md](content-management.md).

## Names Used

Cerkl uses "News Digest" and "AI Newsletters" interchangeably on their site. "MyNews" is an older internal name for the same personalization engine — avoid using it in current content.

## How News Digests Work

News Digests are generated and sent automatically for every opted-in subscriber. Personalized subscribers receive their digest at their chosen day, time, frequency, and format; non-personalized subscribers receive the org default. The AI weighs explicit category interests, implicit behavioral signals, content already seen, posting priorities, segment targeting, followed authors, and min/max content thresholds to assemble each digest.

By default, a story stops being served once a subscriber engages with the digest it appeared in (open counts). If a subscriber skips a digest for a week, some stories cycle back. Communicators override the AI via posting priorities — `To Everyone`, `To Everyone as First Story`, or segment-targeted — which guarantee delivery regardless of interest match.

Each digest is tiered: up to three top-priority stories with priority chips (Top Story, Big News, Just for You / Event for You), then Recommended For You ranked by AI relevance, then events (priority, body, or upcoming), and — for Traditional layout — Other News. Optional `% Match` and `Trending` chips can be toggled org-wide.

## Subject Line Generator

Three modes for News Digest subject lines:

| Mode | How It Works |
|---|---|
| **Classic** | Auto-generates subject lines based on subscriber content and preferences; optional branding prepend; set fallback for subscribers lacking personalized data |
| **Advanced** | Four customizable fields: Subject Line Prepend (branding text), Subscriber's Name, First Digest Story (headline), Relevant Categories (up to two org categories matching subscriber interests) |
| **Custom** | Single static subject line for all subscribers |

**Classic mode logic.** Cascade: (1) priority content in the digest → subject references it; (2) else any story >90% relevancy → that story becomes the focus; (3) else stories carry category tags → `Latest {Category 1, Category 2, Author} news from {Org Name}, just for {First Name}`; (4) else use the Fallback Subject Line; (5) else default to a content-count line (`Our # most popular stories from the past {frequency}` or `What's Trending at {Org}`).

**Fallback Subject Line.** Set at `Settings > Sending Options > News Digest > Miscellaneous Sending Controls > Fallback Subject Line`. Used when the system lacks subscriber or priority data to personalize. Identical for every recipient who hits it. Any configured Subject Line Opener is prepended.

## Language Controls

Subscribers pick their digest language during personalization — either from the Welcome Email (Your Format tab) or from any digest footer ("Personalize this email" → Delivery → Select Language). Google auto-translates stories from the org's primary language into the chosen one; subscribers also get a per-email option to re-translate. 133 languages supported.

## Welcome Email

The Welcome Email is the subscriber's first introduction to News Digests. It sends automatically at instance go-live and whenever a new opted-in subscriber is added, provided **Send Welcome Email** is toggled on under `Audience > Controls`. It prompts subscribers to complete personalization (topics, schedule, format, language, followed authors).

Format is fixed; copy and imagery are customized during pre-launch with the Implementation PM and post-launch via Customer Success or Support.

**Resend to one subscriber.** `Audience > Subscribers` → search → click **Resend Welcome Email** in the Date Personalized column.

**Resend to all non-personalized.** `Audience > Controls` → **Resend to Non-Personalized Subscribers**. Shortcut also at `Settings > Branding > Welcome Email Image`.

**Date Personalized column** states: empty (never sent — opt-in or toggle issue), date only (subscriber personalized then), date + Resend link (Team Member personalized on their behalf), Resend link only (sent but not yet personalized). Full Admins always see the Resend link.

## Personalization Process — What Subscribers Do

From the Welcome Email or any digest footer, subscribers step through four tabs: **Your Topics** (category interests, optional subcategories, optional exclusions), **Your Schedule** (frequency, day, time, timezone), **Your Format** (Headlines Only / Headlines Plus / Traditional + language), **Your People** (followed Content Authors — boosts their odds of appearing). Subscribers can update preferences any time via digest footer or org archive page.

Excluded categories are honored unless a story is `To Everyone` or `To Everyone as First Story`, which override exclusion.

## Performance Context

Church & Dwight 2024: 52% News Digest open rate — higher than their 59.1% blast open rate.

Industry benchmarks (2025 Broadcast Benchmark Report): manufacturing ~83% news digest open rate; healthcare ~48%; higher education ~57%.

For cross-channel measurement and read-rate analytics, see [analytics-insights.md](analytics-insights.md).
