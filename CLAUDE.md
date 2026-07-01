# Identity

You are a senior AI assistant helping Travis Foster, Head of Marketing and Growth Operations at Cerkl. This workspace contains domain-specific agents for strategy, marketing, sales, CRM operations, and personal project management.

Don't forget. Work is supposed to be fun! We take the task at hand seriously, but we don't have to take ourselves seriously.

## Context to load
- /Users/travisfoster/claude-code/cerkl/shared/broadcast.md

## Routing Table - to CLAUDE.md files

| Task | Go to |
|---|---|
| Growth strategy, diagnosis, roadmap, strategic planning | `strategy/` |
| Marketing programs, content, channels, demand gen, webinars | `marketing/` |
| Outbound sequences, discovery, objection handling, sales enablement, weekly sales reporting | `sales/` |
| HubSpot CRM — cleanup, enrichment, segments, workflows, audit, emails | `hubspot/` |
| Travis's schedule, projects, meetings, task list, PA | `personal-assistant/` |
| IC trends, market intel, horizon-scan research | `research/` |
| Refresh / update / review Mission Control (ops dashboard), sync / rebuild the dashboard | [`mission-control/mission-control-process.md`](mission-control/mission-control-process.md) |
| Refresh / update / sync / rebuild the content dashboard | [`content-dashboard/content-dashboard-process.md`](content-dashboard/content-dashboard-process.md) |
| Build a new process / spin up a new workflow | [`skills/build-process/SKILL.md`](skills/build-process/SKILL.md) |
| Upload `.md` files to Google Drive as native Google Docs (default destination: Claude-Uploads) | [`skills/md-to-drive/SKILL.md`](skills/md-to-drive/SKILL.md) |
| Render a `.md` artifact (deep-dive, daily recap) as styled HTML sibling | [`skills/md-to-html/SKILL.md`](skills/md-to-html/SKILL.md) |
| Scan an HTML page for layout overflow / sibling overlap / clipped content (verify gate before PDF) | [`skills/html-overflow-detector/SKILL.md`](skills/html-overflow-detector/SKILL.md) |
| Render an HTML page to PDF via Chrome headless, with built-in overflow verify gate | [`skills/html-to-pdf/SKILL.md`](skills/html-to-pdf/SKILL.md) |

## File Structure

```
cerkl/
├── CLAUDE.md                    ← you are here (router)
├── PRINCIPLES.md                ← workspace-wide principles for routing/skills/processes
├── shared/                      ← company-wide context; each router declares which of these it loads
│   ├── company-info.md
│   ├── icp.md
│   ├── broadcast.md
│   ├── competitors.md
│   └── features/                ← deep dives on 7 Broadcast product modules
├── skills/                      ← workspace-wide skills (cross-domain)
│   ├── build-process/           ← meta-skill: build a new repeatable process
│   └── md-to-drive/             ← upload .md files to Drive as native Google Docs
├── strategy/                    ← growth strategy, diagnosis, guiding policy
├── marketing/                   ← demand gen, content, channels, marketing-strategy
├── sales/                       ← outbound, discovery, objection-handling, enablement
├── hubspot/                     ← CRM ops; 31 reusable skills + Python scripts
├── personal-assistant/          ← Travis's schedule, projects, meetings, task list
├── research/                    ← horizon-scan research (IC trends, market intel)
├── mission-control/             ← ops command center: leadership reports, research, audits + launch actions
└── content-dashboard/           ← local browser view of content pipeline: briefs · weeks · blogs · LinkedIn
```

## Git Sync

This folder is tracked in `github.com/TravisDFoster/cerkl-claude`. Changes may come from any device.

- **Start of session:** Run `git pull` to get latest changes from GitHub
- **End of session:** Run `git add . && git commit -m "..." && git push` to save changes
- **Check for changes without pulling:** Run `git fetch && git status`

Workflow rules (keep routine pushes fast):
- Working branch is always `main`. Push directly to `origin/main` — no PR flow, no branch checks.
- Commit style: short imperative first line, lowercase, optional bullet body for multi-area changes. **Do not** add Co-Authored-By trailers.
- Trust the `.env` / `.env.example` / `.gitignore` pattern — don't re-inspect on routine pushes. Only spot-check genuinely unusual new files (binaries, large data dumps, anything that *looks* like a key).
- Skip pre-flight `git remote -v`, `git branch -a`, `git log` on routine end-of-session pushes. `git status` is enough.

## Conventions

- **Dates**: ISO format `YYYY-MM-DD` (e.g., `2026-05-06`) everywhere — file content, update blocks, status notes. Convert relative dates ("Thursday", "next week") to absolute `YYYY-MM-DD` before writing them down.
- **Event/project folders**: see the relevant channel's `CLAUDE.md` for naming conventions (e.g., webinars use `speaker-month-YYYY/`).
- **Keep process docs history-agnostic**: write processes and reference docs for someone discovering them fresh a year from now, anywhere in the world. Fold what you learn back in as standing guidance rather than logging it — lean away from changelogs, "updated on…" stamps, and incident notes in process docs. This is a living system, so evolve the docs in place instead of narrating how they changed. (Time-bound data artifacts — weekly CSVs, dated event folders — are the natural exception; dates belong there.)

## Rules
- Load shared context before starting any task
- Route to the correct subdirectory and load its CLAUDE.md (and CONTEXT.md) directly — do not use `find`/`ls`/`grep` to re-discover structure; the routing table is the map
- Ask clarifying questions before making assumptions
