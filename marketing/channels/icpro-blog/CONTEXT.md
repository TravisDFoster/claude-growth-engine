# Internal Comms Pro Blog Channel Context

## What this channel does

Owned-media authority site at **internalcommspro.com**, separate from the Cerkl-branded cerkl.com. Cerkl writes the content; the brand is "Internal Comms Pro" (ICP). Output is a peer-expert publication for IC practitioners — trends, patterns, best practices, benchmarking — not vendor product content.

## Why a separate brand

- **Different positioning:** ICP is a community publication; Cerkl is a vendor. Same writer, different voice — peer-expert vs. product-strategist.
- **Different audience reach:** ICP captures top-of-funnel IC practitioners who would bounce off vendor content. Authority on the practice creates indirect demand for the platform.
- **Separate domain SEO:** ICP ranks for "internal comms" practice queries without competing with cerkl.com's product-led terms.

## Publishing platform

- **CMS:** Wix (not Webflow — different field schema, different rendering)
- **Site URL:** https://www.internalcommspro.com/blog
- **Author byline:** `ICP Staff` (default; individual bylines not currently used)
- **CTA model:** Single site-wide newsletter signup ("Subscribe to our newsletter") rendered by Wix in the footer. **No mid-post CTAs, no lead magnets, no Cerkl product CTAs in the body.**
- **No FAQ schema blocks** (Wix doesn't natively support; existing posts don't use)
- **Hero image:** required on every post (Wix renders ~454×256 optimized)
- **Read time:** displayed as `X min read` (Wix auto-calculates)

## Categories (13 topical)

- Showing Value
- Saving Time
- Content
- Intranet
- Mobile Workers
- Internal Comms Tools
- Collaboration
- Measurement
- Change Communications
- Strategic Planning
- Employee Retention
- Job Opportunity
- Crisis Communication

(There is also a `Podcast` content-type filter, not a topical category. Don't use it for blog posts.)

## What this channel produces

- **Pre-writing files** (`blog-posts-pre-writing/`) — Wix publishing properties (title, slug, keywords, category, meta, featured image brief) plus an outline. Output of the `icpro-blog-pre-writing` skill.
- **Drafts** (`blog-posts-draft/`) — full markdown drafts ready for Wix paste, no inline H1, no FAQ block, no CTAs. Output of the `icpro-blog-drafting` skill.
- **Live posts** (`blog-posts-live/`) — finalized, edited posts with edit log and a published Drive Doc named `YYYY-MM-DD — ICP — <H1 title>`. Output of the `icpro-blog-editing` skill.

## What this channel does **not** produce

- Cerkl-branded blog posts — see `marketing/channels/seo-blog/`
- Versus / comparison landing pages — see `marketing/channels/comparison-seo/`
- Webinar recap blogs (always Cerkl-branded) — owned by `marketing/channels/webinar/skills/webinar-recap-blog/`

## Voice — at a glance

Peer expert, not vendor. Authoritative on IC trends and patterns. Practical, direct, concise, zero-fluff — same general register as cerkl.com — but the authority comes from craft expertise, not from being the company that built the tool. The full voice rules and brand-mention rules live in [`icpro-blog-drafting`](skills/icpro-blog-drafting/SKILL.md) and [`icpro-blog-editing`](skills/icpro-blog-editing/SKILL.md) — that is the source of truth.

## Brand mention rules — strict

- **Cerkl:** rare, only as *"tools like Cerkl Broadcast"* in a list context. Never a primary recommendation. Never product copy.
- **Cerkl competitors (Simpplr, LumApps, Firstup, Workvivo, Poppulo, Staffbase, Haiilo, etc.):** **never named.** Use "modern intranet platforms" or "newer-generation internal comms tools" generically.
- **Other vendors (Slack, Teams, Outlook, Gmail, SharePoint, Yammer, etc.):** fine to name when topic requires.

## Source of truth for what to write

The shared monthly content plan: `/Users/travisfoster/claude-code/cerkl/marketing/content-plan/monthly-content-plans/[month-year].md` and `[month-year]-jira.csv`. ICPro posts are CSV rows where `Channel = Blog Posts` AND the `Summary` field begins with `Content - Blog (ICP) -`. The `(ICP)` marker is the rule that splits ICPro posts from cerkl.com posts in the shared plan.

## Capacity

Per [`marketing/content-plan/jira-csv-guidelines.md`](../../content-plan/jira-csv-guidelines.md): 1 ICPro blog post per week (matched by 1 cerkl.com blog post per week).
