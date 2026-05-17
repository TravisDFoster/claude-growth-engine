# Jira Imports

> **Once-a-week Jira CSV imports for the locked week of [`../rolling-4week.md`](../rolling-4week.md).** One CSV per week, named by ISO week. End-to-end flow lives in [`../process.md`](../process.md); CSV field mappings live in [`../jira-csv-guidelines.md`](../jira-csv-guidelines.md). This folder is the operational record of what got imported when.

---

## Cadence

Generated and imported as part of the weekly cycle described in [`../process.md`](../process.md#weekly-cadence):

1. **Mon** — rolling-4week Week 1 locks; writing+editing agent starts
2. **Tue** — writing agent finishes; CSV generated for the locked week; Travis imports to Jira
3. **Wed** — Furqan reviews drafts in Drive (linked from Jira tasks)
4. **Thu–Fri** — Furqan does publishing prep
5. **Mon–Fri (next week)** — content publishes

The CSV must be generated **after** the writing agent finishes so each blog Task's description can include its Drive Doc URL.

---

## Naming

`imports/YYYY-Www.csv` — ISO week of the **publish week**, not the lead week.

Examples:
- `imports/2026-W23.csv` → CSV imported Tue 2026-05-19, content publishes week of Mon 2026-05-25
- `imports/2026-W24.csv` → CSV imported Tue 2026-05-26, content publishes week of Mon 2026-06-01

Use [ISO week numbers](https://en.wikipedia.org/wiki/ISO_week_date). When in doubt, the date `YYYY-MM-DD` of the Monday of the publish week is unambiguous.

---

## What's in a CSV

Per [`../jira-csv-guidelines.md`](../jira-csv-guidelines.md): one row per Task + subtask. Each blog Task description includes:

- Brief slug + link to `../../seo/briefs/<slug>.md`
- Drive Doc URL of the final draft
- Primary keyword + secondary keywords
- Webflow CMS properties (Primary Category, Primary Solution, All Categories)

The two manual fills required at import time:

1. **Epic ID** — the existing Jira Epic for the month's campaign (e.g., `2026 Foundations Free`)
2. **Subtask owner IDs** — per the ownership table in [`../jira-csv-guidelines.md`](../jira-csv-guidelines.md#ownership)

---

## Lifecycle

- **`imports/`** — current and recent weekly CSVs (rolling, ~3 months)
- **`archive/`** — CSVs older than ~3 months. Manual move at quarter close, or any time `imports/` gets noisy.
- Never edit a CSV after import. If a row is wrong, fix it in Jira directly and re-generate the next week's CSV with the correction noted in the commit.

---

## Generating a CSV

When asked "generate the Jira CSV for [week]" or "run the Jira import for [ISO week]":

1. Read the locked Week 1 rows from [`../rolling-4week.md`](../rolling-4week.md)
2. Confirm the writing agent has finished and each blog row has a Drive Doc URL
3. Apply field mappings + subtask templates from [`../jira-csv-guidelines.md`](../jira-csv-guidelines.md)
4. Output to `imports/YYYY-Www.csv`
5. Print a summary: total Task count, total subtask count, the Epic name that needs to be filled
6. Travis imports manually via Jira's CSV importer; sets Epic ID + subtask owner IDs at import time

---

## Open items

- **CSV header reference:** when the first import lands, snapshot the column order here so re-generation stays consistent.
- **Drive URL injection:** confirm whether the writing agent writes URLs to a side artifact the CSV generator reads, or whether the generator scrapes them from chat output.
