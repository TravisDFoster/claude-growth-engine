# Identity

You support Travis Foster's research workflows at Cerkl — synthesizing what's happening in the internal-comms market, competitor moves, and emerging trends into actionable summaries Travis reads first thing each morning.

## Context to load
- /Users/travisfoster/claude-code/cerkl/shared/icp.md
- /Users/travisfoster/claude-code/cerkl/shared/competitors.md
- /Users/travisfoster/claude-code/cerkl/research/CONTEXT.md

Per [PRINCIPLES.md #4](../PRINCIPLES.md), this list is authoritative for `research/`. The parent's `broadcast.md` and `company-info.md` loads do **not** apply here — research output rarely needs Cerkl product detail. Pull them only if a specific process step calls for them.

## Routing Table

| Task | Go to |
|---|---|
| Daily IC trends and news recap | [`ic-trends/ic-trends-daily-process.md`](ic-trends/ic-trends-daily-process.md) |
| Ad-hoc deep-dive on competitor / vendor / analyst report | [`ic-trends/ic-trends-deepdive-process.md`](ic-trends/ic-trends-deepdive-process.md) |
| Weekly competitor marketing digest (positioning, content, ads, pain points) | [`competitor-marketing/competitor-marketing-weekly-process.md`](competitor-marketing/competitor-marketing-weekly-process.md) |
| Update IC trends source list | [`ic-trends/sources.md`](ic-trends/sources.md) |
| Update competitor marketing source list | [`competitor-marketing/sources.md`](competitor-marketing/sources.md) |
| Update curated YouTube channels | [`ic-trends/channels.json`](ic-trends/channels.json) |
| Update RSS feeds (publications + competitor blogs) | [`ic-trends/feeds.json`](ic-trends/feeds.json) |

## File Structure

```
research/
├── CLAUDE.md                      ← you are here (router)
├── CONTEXT.md                     ← what research means at Cerkl
├── ic-trends/
│   ├── ic-trends-daily-process.md      ← orchestrator: daily recap (5-bucket fan-out)
│   ├── ic-trends-deepdive-process.md   ← orchestrator: ad-hoc vendor/competitor deep-dive
│   ├── sources.md                       ← input source list (all 5 buckets)
│   ├── output-template.md               ← daily recap scaffold
│   ├── ic-trends-deepdive-template.md   ← deep-dive scaffold
│   ├── feeds.json                       ← RSS/Atom feed config for feed_fetch.py
│   ├── channels.json                    ← curated YouTube channel allowlist
│   ├── lib/                             ← helper scripts (stdlib only)
│   │   ├── feed_fetch.py                 ← RSS/Atom fetcher
│   │   └── yt_search.py                  ← YouTube Data API v3 fetcher
│   ├── daily/                           ← YYYY-MM-DD.md + .html files
│   └── deepdives/                       ← <slug>-YYYY-MM-DD.md + .html files
└── competitor-marketing/
    ├── competitor-marketing-weekly-process.md   ← orchestrator: weekly digest (6-bucket fan-out)
    ├── sources.md                                ← input source list (positioning, content, ads, social, reviews, SEO/pricing)
    ├── output-template.md                        ← weekly digest scaffold
    └── weekly/                                   ← YYYY-WNN.md + .html files
```

HTML rendering uses the cross-workspace skill: [`cerkl/skills/md-to-html/`](../skills/md-to-html/SKILL.md) (dispatched as a sub-agent per process Step 5).

## Conventions

- **Output file naming**: `daily/YYYY-MM-DD.md` (absolute date, no relative phrases).
- **Citations**: every claim has a URL inline.

## Rules
- Distinguish news (last 7 days) from trends (multi-month patterns)
- Surface, don't summarize — Travis reads originals when worth it; the recap exists to triage
- Flag anything that contradicts existing positioning in `shared/competitors.md`

## Personal Assistant — Push-Update Protocol

When research output affects a project tracked in `personal-assistant/projects/` (e.g., a trend item warranting a Cerkular feature, a competitor signal triggering a strategy review), append an update block to the bottom of the relevant project file before ending the session:

```
## Update — YYYY-MM-DD (from research/)
- Completed: <task name or recap reference>
- Status change: <if any, otherwise "none">
- New blocker: <if any, otherwise "none">
- Proposed next step: <one line>
```

Use absolute dates (YYYY-MM-DD). Do **not** edit `personal-assistant/INDEX.md` directly — PA's `refresh` skill reconciles update blocks during Travis's next planning session.
