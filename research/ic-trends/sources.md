# IC Trends — Sources

Source list for the daily IC trends recap. The process re-reads this file every run; edits take effect immediately.

---

## (a) Competitor blogs

Pulled from `cerkl/shared/competitors.md`. The interesting signal is what competitors are *betting on* (POV pieces, original research, partnerships, exec hires) — not their product launches.

| Competitor | Blog / news URL |
|---|---|
| Staffbase | https://staffbase.com/blog |
| Simpplr | https://www.simpplr.com/blog |
| LumApps | https://www.lumapps.com/learn/blog |
| Firstup | https://firstup.io/blog |
| Poppulo | https://www.poppulo.com/blog |
| Workvivo | https://www.workvivo.com/blog |
| Haiilo | https://haiilo.com/blog |
| AxiosHQ | https://www.axioshq.com/blog |
| Workshop | https://www.useworkshop.com/blog |
| ContactMonkey | https://www.contactmonkey.com/blog |

## (b) IC publications & consultancies

| Publication | URL | Notes |
|---|---|---|
| Ragan Communications | https://www.ragan.com | Primary IC trade publication |
| PR Daily | https://www.prdaily.com | Ragan property; PR/IC overlap |
| IABC / Communication World | https://www.iabc.com/communicationworld | Practitioner association |
| Davis & Co. | https://www.davisandco.com/blog | IC consulting POV |
| Gallagher | https://www.ajg.com/employeeexperience | Annual "State of the Sector" report |
| Brunswick Group | https://www.brunswickgroup.com/insights | Strategic comms |
| Edelman | https://www.edelman.com/trust | Trust Barometer; employee comms cuts |

## (c) Analyst / research

Analyst content moves slower (monthly cadence is realistic).

| Source | URL | Notes |
|---|---|---|
| Gartner | https://www.gartner.com | Search "internal communications," "employee experience" |
| Forrester | https://www.forrester.com | Same searches |
| McKinsey | https://www.mckinsey.com/featured-insights/leadership | Org health, change comms |
| Gallup Workplace | https://www.gallup.com/workplace | Engagement data |
| HBR | https://hbr.org | Search "internal communications," "employee communications" |
| SHRM | https://www.shrm.org | HR overlap, comms tactics |

## (d) Community signal

What practitioners are actually talking about — pain points, tool comparisons, layoffs/restructure questions.

- **Reddit:** https://www.reddit.com/r/internalcomms (sort by Top, last 7 days)
- **LinkedIn:** search "internal communications," filter Posts → past week → most relevant
- **Substacks (verify on first run; update list as ones earn their place):** "All Hands" by Joel Schwartzberg

---

## Maintenance

- Add a source: append to the right category with URL.
- Remove a source: delete the row.
- The process re-reads this file every run; no rebuild needed.

---

## Known limitations

Discovered 2026-05-07 cold-start run.

- **Reddit `/r/internalcomms`**: `WebFetch` returns "unable to fetch from www.reddit.com." Until an alternate ingestion path exists (RSS, browser MCP, manual paste), Step 2d community signal will rely on web-search summaries rather than direct top-of-week threads. Note this in the daily Notes section when it bites.
- **JS-rendered blog landing pages** (Staffbase notably; likely others): `WebFetch` extracts post titles but not publish dates. When a date can't be verified, mark items "circa &lt;month&gt;" or "freshness inferred from content," and prefer dated press-release pickups as the timestamp anchor.
- **Gated reports** (Gallagher full report, ContactMonkey full PDF, Edelman Trust Barometer): use the public landing-page summary + a press-release pickup as the anchor; don't pretend to have read the full PDF.
