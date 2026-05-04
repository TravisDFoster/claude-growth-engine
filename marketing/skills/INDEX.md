# Marketing Skills — Index

35 vendored skills from `coreyhaines31/marketingskills` (v captured 2026-05-04). Each is a self-contained `SKILL.md` with YAML frontmatter — Claude auto-invokes when its trigger phrases appear, or any CLAUDE.md routing table can point at it explicitly.

**How to use:**
- Channel/project CLAUDE.md files reference these by relative path (e.g. `../../skills/page-cro/SKILL.md`) — don't fork.
- Cerkl context (ICP, Broadcast features, competitors) is injected by the calling CLAUDE.md, not by editing the skill.
- The keystone is `product-marketing-context`. Cerkl's substitute is `shared/icp.md` + `shared/broadcast.md` + `shared/competitors.md` + `shared/company-info.md` — load those instead of `.agents/product-marketing-context.md` when a skill references it.

**Skipped from upstream:** `paywall-upgrade-cro`, `aso-audit`, `community-marketing`, `revops`, `directory-submissions`.

---

## Foundation

| Skill | Use when |
|---|---|
| [product-marketing-context](product-marketing-context/SKILL.md) | Setting up or refreshing the product/ICP/positioning doc that all other skills read. **For Cerkl, use `shared/` files instead — see top of this doc.** |

## Conversion (CRO)

Channel fit: `marketing/website/`, landing pages from any paid channel (`paid-reddit/`, `paid-youtube/`).

| Skill | Use when |
|---|---|
| [page-cro](page-cro/SKILL.md) | Any marketing page underperforming — homepage, landing, pricing, feature, blog. Default skill for "this page isn't converting." |
| [signup-flow-cro](signup-flow-cro/SKILL.md) | Foundations signup / trial activation flow. Direct line to the subscriber-growth KPI. |
| [onboarding-cro](onboarding-cro/SKILL.md) | Post-signup activation, first-run experience, time-to-value. People sign up but don't stick. |
| [form-cro](form-cro/SKILL.md) | Lead/contact/demo forms — anything that isn't signup. |
| [popup-cro](popup-cro/SKILL.md) | Modals, exit-intent, slide-ins, sticky bars, announcement banners. |

## Copy & Creative

| Skill | Use when |
|---|---|
| [copywriting](copywriting/SKILL.md) | Writing or rewriting page copy from scratch — headlines, value props, CTAs, hero sections. |
| [copy-editing](copy-editing/SKILL.md) | Editing or refreshing existing copy. Content audits and outdated-page cleanup. |
| [ad-creative](ad-creative/SKILL.md) | Bulk ad copy generation — headlines, descriptions, variations across platforms. |
| [social-content](social-content/SKILL.md) | LinkedIn/X/YouTube Shorts/IG content, calendars, repurposing, short-form video scripts. |
| [image](image/SKILL.md) | Marketing image creation/optimization — blog heroes, social graphics, OG images, mockups. |
| [video](video/SKILL.md) | Video production with AI tools (Remotion, HeyGen, Veo, Runway). |

## SEO

Channel fit: `channels/organic/seo-blog/`, `channels/comparison-seo/`.

| Skill | Use when |
|---|---|
| [seo-audit](seo-audit/SKILL.md) | Diagnosing SEO issues — rankings dropped, traffic loss, technical/on-page review. Default starting point for "help with SEO." |
| [ai-seo](ai-seo/SKILL.md) | Optimizing for ChatGPT, Perplexity, AI Overviews, LLM citations (AEO/GEO/LLMO). |
| [programmatic-seo](programmatic-seo/SKILL.md) | Templated pages at scale — directly applicable to Cerkl's comparison-SEO ("vs" pages). |
| [schema-markup](schema-markup/SKILL.md) | JSON-LD structured data, FAQ schema, rich snippets. |
| [site-architecture](site-architecture/SKILL.md) | Sitemap planning, IA, URL structure, internal linking. |
| [content-strategy](content-strategy/SKILL.md) | Deciding what to write — topic clusters, editorial calendars, content pillars. |

## Paid

Channel fit: `channels/paid-reddit/`, `channels/paid-youtube/`.

| Skill | Use when |
|---|---|
| [paid-ads](paid-ads/SKILL.md) | Campaign strategy, targeting, bidding, optimization across Google/Meta/LinkedIn/X. |
| [ad-creative](ad-creative/SKILL.md) | (Also listed under Copy.) Bulk creative for any paid platform. |

## Email & Outreach

Channel fit: `sales/outbound/`, `sales/email-editor/`, `channels/newsletter/`.

| Skill | Use when |
|---|---|
| [email-sequence](email-sequence/SKILL.md) | Drip campaigns, welcome series, lifecycle/onboarding/re-engagement/win-back flows. |
| [cold-email](cold-email/SKILL.md) | B2B cold outreach — subject lines, opening lines, multi-touch sequences. (Used by `sales/`, not marketing.) |

## Strategy & Planning

Channel fit: `marketing/marketing-strategy/`.

| Skill | Use when |
|---|---|
| [launch-strategy](launch-strategy/SKILL.md) | Product/feature launches — Product Hunt, beta, waitlist, GTM plans. Pairs with `channels/newsroom-pr/`. |
| [pricing-strategy](pricing-strategy/SKILL.md) | Pricing/packaging decisions, freemium structure, value metrics. |
| [marketing-psychology](marketing-psychology/SKILL.md) | Reference: persuasion principles, cognitive biases, behavioral science. |
| [marketing-ideas](marketing-ideas/SKILL.md) | Inspiration / brainstorming when stuck. Starting point that routes to specific channels. |

## Growth & Retention (highest KPI leverage)

These map directly to **Foundations subscriber growth**.

| Skill | Use when |
|---|---|
| [lead-magnets](lead-magnets/SKILL.md) | Gated assets, ebooks, checklists, templates — Cerkl's existing TOFU motion. |
| [free-tool-strategy](free-tool-strategy/SKILL.md) | Engineering-as-marketing — interactive tools, calculators, graders. Foundations *is* a free tool, so this framing applies. |
| [referral-program](referral-program/SKILL.md) | Word-of-mouth, viral loops, refer-a-friend, partner programs. Lowest-CAC path for free products. |
| [churn-prevention](churn-prevention/SKILL.md) | Subscriber retention — cancel flows, save offers, win-back, dunning. Defends the KPI denominator. |

## Research & Analysis

| Skill | Use when |
|---|---|
| [customer-research](customer-research/SKILL.md) | Interview synthesis, JTBD, review mining (G2, Reddit), VOC, persona building. |
| [competitor-profiling](competitor-profiling/SKILL.md) | Researching competitors from URLs → structured profile docs. Feeds `shared/competitors.md`. |
| [competitor-alternatives](competitor-alternatives/SKILL.md) | Comparison/alternative pages — "Cerkl vs Simpplr" style. Direct fit for `channels/comparison-seo/`. |
| [analytics-tracking](analytics-tracking/SKILL.md) | GA4, GTM, event/conversion tracking, attribution, tracking plans. |
| [ab-test-setup](ab-test-setup/SKILL.md) | Designing A/B tests, hypotheses, ICE scoring, experiment programs. |

## Sales support

| Skill | Use when |
|---|---|
| [sales-enablement](sales-enablement/SKILL.md) | Pitch decks, one-pagers, objection-handling docs, demo scripts, battle cards. Pairs with `sales/enablement/`. |

---

## Cross-skill flow patterns

These are the most common chains the upstream "see also" links suggest:

- **Page underperforms** → `customer-research` → `copywriting` or `copy-editing` → `page-cro` → `ab-test-setup` → `analytics-tracking`
- **Foundations signup funnel** → `signup-flow-cro` → `onboarding-cro` → `email-sequence` → `churn-prevention`
- **New comparison page** → `competitor-profiling` → `competitor-alternatives` → `programmatic-seo` (if scaling)
- **Launch motion** → `launch-strategy` → `copywriting` (announcement) → `social-content` + `ad-creative` → `email-sequence` (lifecycle of new feature)
- **TOFU asset** → `content-strategy` → `lead-magnets` (or `free-tool-strategy`) → `email-sequence` → `signup-flow-cro`
- **SEO program** → `seo-audit` → `content-strategy` → `programmatic-seo` + `schema-markup` + `ai-seo`

## Invocation notes

- Skills are designed to **auto-trigger** on the natural-language phrases in their descriptions. You don't always need to name them — the agent picks them up from your request.
- When precision matters, name the skill explicitly: "Use the `page-cro` skill on this URL."
- For Cerkl-specific work, the calling CLAUDE.md should explicitly load `shared/` files first so the skill doesn't ask questions you've already answered.
