# Competitor Marketing — Sources

Source inventory for the weekly digest. Organized by the six fetch buckets in `competitor-marketing-weekly-process.md`. Update this file when sources are added, retired, or change URLs — the process file references this as the authoritative list.

**Competitor set (10):** Staffbase, Simpplr, LumApps, Firstup, Poppulo, Workvivo, Haiilo, AxiosHQ, Workshop, ContactMonkey. Canonical reference: `cerkl/shared/competitors.md`.

---

## Bucket (a) — Positioning & messaging

Vendor homepages. WebFetch each, capture H1 + sub-headline + primary CTA + top nav verbatim.

| Vendor | Homepage |
|---|---|
| Staffbase | https://staffbase.com/ |
| Simpplr | https://www.simpplr.com/ |
| LumApps | https://www.lumapps.com/ |
| Firstup | https://firstup.io/ |
| Poppulo | https://www.poppulo.com/ |
| Workvivo | https://www.workvivo.com/ |
| Haiilo | https://haiilo.com/ |
| AxiosHQ | https://www.axioshq.com/ |
| Workshop | https://www.useworkshop.com/ |
| ContactMonkey | https://www.contactmonkey.com/ |

**What to capture per vendor:** hero H1, sub-headline, primary CTA text, top nav items (signals what product surfaces they emphasize), any visible category claim (e.g., "employee communications platform," "AI-powered intranet").

---

## Bucket (b) — Content distribution (blogs, gated assets, webinars)

**RSS-available (use `ic-trends/lib/feed_fetch.py` — already configured in `ic-trends/feeds.json`):**
- Staffbase blog — `https://staffbase.com/rss.xml`
- Simpplr blog — `https://www.simpplr.com/feed/`

**No working RSS (use WebFetch on landing pages):**

| Vendor | Blog URL | Notes |
|---|---|---|
| LumApps | https://www.lumapps.com/learn/blog | Webflow, no feed |
| Firstup | https://firstup.io/blog | Next.js, no feed |
| Poppulo | https://www.poppulo.com/blog | Sanity CMS, no feed |
| Workvivo | https://www.workvivo.com/blog | Next.js, JS-rendered |
| Haiilo | https://haiilo.com/blog | Cloudflare 403 on feed paths |
| AxiosHQ | https://www.axioshq.com/insights | check `/insights` and `/blog` |
| Workshop | https://www.useworkshop.com/blog | |
| ContactMonkey | https://www.contactmonkey.com/blog | WordPress, RSS explicitly disabled |

**Also watch (gated assets / webinars / podcasts):**
- Each vendor's `/resources` or `/library` page — new reports, benchmarks, ebooks signal where they think buyer pain is
- Vendor webinar pages (`/webinars`, `/events`)
- Branded podcasts (Staffbase "Beyond the Office," Simpplr "Cohesion," ContactMonkey "The Internal Comms Podcast," etc.)

---

## Bucket (c) — Advertising

**LinkedIn Ad Library (free, public):**
- Search URL pattern: `https://www.linkedin.com/ad-library/search?keyword=<vendor>`
- Capture: count of active ads, ad copy verbatim, creative format, CTA, claimed pain points
- This is the highest-signal free source for B2B SaaS advertising

**Meta Ad Library (free, public):**
- Search URL pattern: `https://www.facebook.com/ads/library/?active_status=all&ad_type=all&country=ALL&q=<vendor>`
- Less B2B-relevant for some vendors but still worth a sweep — captures Instagram/Facebook ad activity

**Sponsored content (WebSearch fallback):**
- `site:linkedin.com sponsored "<vendor>"` — surfaces sponsored posts
- `"<vendor>" sponsored content` — broader search

**Known gap:** Google Ads has no public ad library. Without SEMrush/Similarweb we can't see paid search activity. Note this gap in the digest's "limitations" section.

---

## Bucket (d) — Social & community

**LinkedIn (largely inaccessible to WebFetch — partial coverage only):**
- Vendor company pages: `https://www.linkedin.com/company/<slug>/posts/`
- Vendor exec voices — search for CEO, CMO, Head of Marketing posts via WebSearch:
  - Staffbase: Martin Böhringer (CEO)
  - Simpplr: Dhiraj Sharma (CEO)
  - Firstup: Nicole Alvino (CEO)
  - Workvivo: Joe Lennon (CEO)
  - ContactMonkey: Scott Pielsticker (CEO)
  - (Add others as you identify them via WebSearch)

**Reddit:**
- `/r/internalcomms` — practitioners often name competitors when asking for tool recommendations
- Reddit is blocked via WebFetch — use WebSearch with `site:reddit.com "<vendor>"` as fallback

**Vendor communities:**
- Staffbase: customer Slack (gated)
- Simpplr: LinkedIn group activity
- Most vendors don't run open practitioner communities — note where they do

**Known gap:** LinkedIn is the most important social channel for B2B IC marketing and we have shallow coverage. Acknowledge this in every digest.

---

## Bucket (e) — Reviews & customer stories

**G2 vendor pages:**
- Pattern: `https://www.g2.com/products/<slug>/reviews`
- Capture: review count last 30 days (visible), star avg, 2-3 most-recent reviews (quote recurring praise + complaint themes verbatim)

| Vendor | G2 URL |
|---|---|
| Staffbase | https://www.g2.com/products/staffbase/reviews |
| Simpplr | https://www.g2.com/products/simpplr/reviews |
| LumApps | https://www.g2.com/products/lumapps/reviews |
| Firstup | https://www.g2.com/products/firstup/reviews |
| Poppulo | https://www.g2.com/products/poppulo-harmony/reviews |
| Workvivo | https://www.g2.com/products/workvivo/reviews |
| Haiilo | https://www.g2.com/products/haiilo/reviews |
| AxiosHQ | https://www.g2.com/products/axios-hq/reviews |
| Workshop | https://www.g2.com/products/workshop/reviews |
| ContactMonkey | https://www.g2.com/products/contactmonkey/reviews |

**Customer story / case study pages (vendor-published):**
- Each vendor's `/customers`, `/case-studies`, or `/customer-stories` URL
- Widen the window to 14 days — case studies publish less frequently than blog posts
- Capture: named logo, industry, primary outcome claim, deal size signal (if mentioned)

**TrustRadius / Capterra:** Secondary — check only if G2 signal is thin for a given vendor.

---

## Bucket (f) — SEO & pricing

**SEO probes (WebSearch — free proxy, shallow vs. paid tools):**

Rotate through these high-intent IC keywords each week; note which of the 10 competitors rank top-10 on the SERP:

- "internal communications platform"
- "best internal communications software"
- "employee app"
- "intranet for internal communications"
- "best intranet platforms"
- "internal newsletter platform"
- "employee newsletter software"
- "internal communications measurement"
- "personalized employee communications"
- "ai for internal communications"

Also probe **comparison pages**: `"<vendor> vs <vendor>"` searches surface when competitors publish head-to-head pages.

**Pricing pages:**

| Vendor | Pricing URL | Public? |
|---|---|---|
| Staffbase | https://staffbase.com/pricing | typically gated |
| Simpplr | https://www.simpplr.com/pricing | typically gated |
| LumApps | https://www.lumapps.com/pricing | typically gated |
| Firstup | https://firstup.io/pricing | typically gated |
| Poppulo | https://www.poppulo.com/pricing | typically gated |
| Workvivo | https://www.workvivo.com/pricing | per-employee public |
| Haiilo | https://haiilo.com/pricing | typically gated |
| AxiosHQ | https://www.axioshq.com/pricing | check |
| Workshop | https://www.useworkshop.com/pricing | tiered, public |
| ContactMonkey | https://www.contactmonkey.com/pricing | tiered, public |

**What to capture:** is pricing public, plan tier names, lowest-tier price, any free tier (Cerkl Foundations is the Cerkl differentiator — note any competitor moves toward free tiers).

**Known gap:** without Ahrefs/SEMrush/Similarweb, we can't see traffic share, keyword volume, backlink strength, or paid-search activity. SEO bucket is a SERP-presence proxy only. Flag this in every digest.

---

## Bucket priorities (if time-constrained)

If a sub-agent can't complete all 10 vendors in its bucket, prioritize the top 5 most-direct competitors: **Staffbase, Simpplr, Firstup, Workvivo, ContactMonkey**. Document any skipped vendors in the digest's Gaps section.

---

## Maintenance

- Re-verify URLs quarterly; vendor sites move frequently
- Add exec names to bucket (d) as you identify them
- Retire keywords from bucket (f) that consistently return no competitor results; add new ones that buyers actually use (mine from `/r/internalcomms` and sales-call transcripts when available)
- When a new direct competitor emerges, add to `shared/competitors.md` first, then mirror entries into each bucket here
