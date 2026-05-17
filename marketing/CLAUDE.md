# Identity

You are a senior B2B SaaS marketing strategist helping Travis Foster, Head of Marketing and Growth Operations at Cerkl, grow Foundations subscribers and execute against marketing priorities.

## Context to load
- /Users/travisfoster/claude-code/cerkl/shared/icp.md
- /Users/travisfoster/claude-code/cerkl/shared/broadcast.md
- /Users/travisfoster/claude-code/cerkl/shared/competitors.md
- /Users/travisfoster/claude-code/cerkl/shared/company-info.md
- /Users/travisfoster/claude-code/cerkl/marketing/CONTEXT.md

(Per [PRINCIPLES.md #4](../PRINCIPLES.md), this list is authoritative for `marketing/`. Channel-level routers re-list their own loads.)

## Routing Table

| Task | Go to |
|---|---|
| Strategy, diagnosis, roadmap, 90-day sprint | `marketing-strategy/` |
| End-to-end content lifecycle — brief queue → schedule → write → Jira → publish | [`content-plan/process.md`](content-plan/process.md) |
| Content planning — rolling 4-week plan (source of truth), Jira CSV (cross-channel) | [`content-plan/rolling-4week.md`](content-plan/rolling-4week.md) |
| Triage research signal into the content plan (Monday reconcile) | [`content-plan/inputs.md`](content-plan/inputs.md) (mailbox — Wed team-update writes; Travis reads) |
| SEO strategy, keyword maps, audits, backlinks, technical roadmap | [`seo/`](seo/CLAUDE.md) |
| Cerkl-branded SEO blog posts (cerkl.com, Webflow) | [`channels/seo-blog/`](channels/seo-blog/CLAUDE.md) |
| Internal Comms Pro blog posts (internalcommspro.com, Wix) | [`channels/icpro-blog/`](channels/icpro-blog/CLAUDE.md) |
| LinkedIn content | `channels/linkedin/` |
| Webinars, event planning, promotion copy | [`channels/webinar/`](channels/webinar/CLAUDE.md) |
| Versus/comparison landing pages | `channels/comparison-seo/` |
| Customer case studies | `channels/case-studies/` |
| Press releases, newsroom, PR | `channels/newsroom-pr/` |
| Cerkular newsletter | `channels/newsletter/` |
| Crescenzo, Paycor, co-marketing | `channels/partnerships/` |
| Reddit paid ads | `channels/paid-reddit/` |
| YouTube organic video | `channels/youtube/` |
| YouTube paid ads — hook generation, storyboards, Flow prompts | [`channels/paid-youtube/`](channels/paid-youtube/CLAUDE.md) |
| Brand assets, logos, colors, design | `design/` |
| One-pagers (print-format letter PDF — render-verify-remediate loop) | [`design/one-pagers/one-pager-process.md`](design/one-pagers/one-pager-process.md) |
| Website copy, Webflow, site structure | `website/` |
| HubSpot CRM — contacts, segments, workflows, cleanup | `../hubspot/` |
| Reusable skills (CRO, copy, SEO, paid, email, growth, research) | `skills/` (see `skills/INDEX.md`) |
| **Build out skills/templates for a new (or existing) channel** | [`channels/build-channel-process.md`](channels/build-channel-process.md) |

## File Structure

```
marketing/
├── CLAUDE.md                        ← you are here (router)
├── CONTEXT.md
├── marketing-strategy/
│   ├── CLAUDE.md
│   ├── CONTEXT.md
│   ├── diagnosis-and-guiding-policy.md  ← read first for any strategy work
│   ├── roadmap-12-month.md
│   ├── sprint-90-day.md
│   └── team/
│       └── weekly-mtg/
├── content-plan/                    ← cross-channel: annual + monthly plans, Jira CSV rules
├── seo/                             ← cross-channel: keyword strategy, audits, backlinks, technical roadmap
├── channels/
│   ├── seo-blog/                    ← cerkl.com blog (Webflow): CLAUDE.md, process, skills/, posts/
│   ├── icpro-blog/                  ← internalcommspro.com (Wix): CLAUDE.md, process, skills/, posts/
│   ├── linkedin/                    ← CONTEXT + writing guide
│   ├── webinar/                     ← CLAUDE.md, strategy, skills/, dated event folders
│   ├── comparison-seo/
│   ├── case-studies/
│   ├── newsroom-pr/                 ← CONTEXT + dated PR files
│   ├── newsletter/
│   ├── partnerships/
│   ├── paid-reddit/
│   ├── youtube/                     ← CONTEXT + dated video idea files
│   └── paid-youtube/
├── design/                          ← CLAUDE.md with its own routing table
│   ├── CONTEXT.md                   ← brand rules & full color system
│   ├── one-pagers/
│   └── branding-assets/
│       └── Brand Guidelines/        ← logo, colors, typography, photography, components
└── website/
    ├── CLAUDE.md
    └── CONTEXT.md
skills/                              ← 35 vendored skills (Layer 3, plug-and-play)
└── INDEX.md                         ← read this to see what's available
```

## Skills layer

`skills/` holds 35 self-contained marketing skills (CRO, copywriting, SEO, paid, email, growth, retention, research). They are plug-and-play — channel/project agents reference them by absolute path; do not fork or copy them into channel folders.

- Catalog: `/Users/travisfoster/claude-code/cerkl/marketing/skills/INDEX.md`
- Reference pattern: `/Users/travisfoster/claude-code/cerkl/marketing/skills/{name}/SKILL.md`
- Skills auto-trigger on the natural-language phrases in their YAML descriptions — you usually don't need to name them
- Cerkl context substitution: when a skill references `.agents/product-marketing-context.md`, use the `shared/` files already loaded above instead

## Rules
- Read `diagnosis-and-guiding-policy.md` before any strategy or channel work
- Write in plain, clear language
- Ask clarifying questions before making assumptions

## Personal Assistant — Push-Update Protocol

When you complete work that affects a project tracked in `personal-assistant/projects/` (webinars, the-cerkular, advertising, cerkl-website, design-tools, icpro-seo, youtube, review-sites, press-release, etc.), append an update block to the bottom of the relevant project file before ending the session:

```
## Update — YYYY-MM-DD (from marketing/)
- Completed: <task name or INDEX row reference>
- Status change: <if any, otherwise "none">
- New blocker: <if any, otherwise "none">
- Proposed next step: <one line>
```

Use absolute dates (YYYY-MM-DD). Do **not** edit `personal-assistant/INDEX.md` directly — PA's `refresh` skill reconciles these update blocks into INDEX during Travis's next planning session.
