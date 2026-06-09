# Identity

You are helping Travis plan, schedule, and operationalize Cerkl's organic content — the cross-channel orchestration layer that sits between SEO briefs and channel writing pipelines. Output of this folder is a Jira-importable CSV plus the operational state (`rolling-4week.md`) that drives every channel's week.

## Context to load

- /Users/travisfoster/claude-code/cerkl/marketing/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/marketing/content-plan/CONTEXT.md

(Per [PRINCIPLES.md #4](/Users/travisfoster/claude-code/cerkl/PRINCIPLES.md), this list is authoritative for `content-plan/`. Individual process files declare any additional loads they need.)

## Routing Table

| Task | Go to |
|---|---|
| Understand how the whole content system fits together (orientation) | [`content-lifecycle-process.md`](content-lifecycle-process.md) |
| Run the Monday reconcile (triage briefs, process inputs, lock next week, generate Jira scaffold) | [`plan-reconcile-process.md`](plan-reconcile-process.md) |
| Generate a month's week-by-week plan from the annual plan | [`monthly-plan-generation-process.md`](monthly-plan-generation-process.md) |
| Generate the weekly Jira CSV scaffold (invoked by plan reconcile, also runnable standalone) | [`jira/jira-scaffold-process.md`](jira/jira-scaffold-process.md) |
| Read the current state of what's being made and when | [`rolling-4week.md`](rolling-4week.md) |
| Dump a new idea/signal for Monday triage | [`inputs.md`](inputs.md) |
| See the annual campaign arc | [`2026-content-plan.md`](2026-content-plan.md) |
| Look up Jira field rules, capacity limits, ownership | [`jira-csv-guidelines.md`](jira-csv-guidelines.md) |

## File Structure

```
content-plan/
├── CLAUDE.md                              ← you are here (router)
├── CONTEXT.md                             ← stable knowledge about the system
├── content-lifecycle-process.md           ← narrative spine: brief → publish
├── plan-reconcile-process.md              ← weekly Monday reconcile
├── monthly-plan-generation-process.md     ← monthly plan from annual
├── 2026-content-plan.md                   ← annual themes + Epics + ICP context
├── jira-csv-guidelines.md                 ← Jira field rules + capacity limits
├── rolling-4week.md                       ← operational source of truth (Travis edits at reconcile)
├── inputs.md                              ← raw idea mailbox
├── monthly-content-plans/                 ← generated monthly plans, one per month
└── jira/                                  ← weekly Jira CSV import context
    ├── CONTEXT.md
    ├── jira-scaffold-process.md
    ├── _template.csv
    ├── imports/                           ← weekly CSVs awaiting / recently imported
    └── archive/                           ← CSVs older than ~3 months
```

## Rules

- Brief lifecycle changes (queued → scheduled → in-progress → shipped) always touch the brief's frontmatter in [`../seo/briefs/`](../seo/briefs/) — the brief file is canonical; this folder's tables reference it.
- Slug threading is the system's identity model. Slug stays exactly the same string from brief → rolling-4week → Jira CSV → publishing skill → Webflow URL. If you're tempted to "fix" a slug downstream, you're introducing drift — fix the source instead. See [`jira/CONTEXT.md`](jira/CONTEXT.md#slug-threading-the-canonical-identity).
- Travis writes `rolling-4week.md` at Monday reconcile; channels never edit it directly. Channels state completion in chat at session end; reconcile reads git log.
