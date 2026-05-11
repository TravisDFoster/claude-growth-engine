# IC Trends — Sources

Source list for the daily IC trends recap **and** ad-hoc tool deep-dives. Both processes re-read this file every run; edits take effect immediately.

Weight ordering: **competitor research + analyst reports > IC publications > community signal > YouTube**.

---

## (a) Competitor blogs

Pulled from `cerkl/shared/competitors.md`. The interesting signal is what competitors are *betting on* (POV pieces, original research, partnerships, exec hires) — not their product launches.

| Competitor | Blog / news URL | Has RSS? |
|---|---|---|
| Staffbase | https://staffbase.com/blog | ✓ active in `feeds.json` (cadence ~biweekly) |
| Simpplr | https://www.simpplr.com/blog | ✓ active in `feeds.json` (cadence ~weekly) |
| LumApps | https://www.lumapps.com/learn/blog | ✗ no RSS (Webflow site) — WebFetch fallback |
| Firstup | https://firstup.io/blog | ✗ no RSS (Next.js site) — WebFetch fallback |
| Poppulo | https://www.poppulo.com/blog | ✗ no RSS (Sanity CMS) — WebFetch fallback |
| Workvivo | https://www.workvivo.com/blog | ✗ no RSS (Next.js site) — WebFetch fallback |
| Haiilo | https://haiilo.com/blog | ✗ Cloudflare-blocked — WebFetch fallback |
| AxiosHQ | https://www.axioshq.com/blog | unverified |
| Workshop | https://www.useworkshop.com/blog | ✗ WebFetch 403 — WebSearch fallback |
| ContactMonkey | https://www.contactmonkey.com/blog | ✗ RSS explicitly disabled (410) — WebFetch fallback |

## (b) IC publications & consultancies

Primary feed source for daily-recap Step 2b. Configured in `feeds.json` (fetched directly via `lib/feed_fetch.py`).

| Publication | URL | Notes |
|---|---|---|
| Ragan Communications | https://www.ragan.com | Primary IC trade publication — in `feeds.json` |
| PR Daily | https://www.prdaily.com | Ragan property; PR/IC overlap — in `feeds.json` |
| Davis & Co. | https://www.davisandco.com/blog | IC consulting POV — ✗ no RSS endpoint (SPA catch-all), WebFetch fallback |
| IABC / Communication World | https://www.iabc.com/communicationworld | Practitioner association — no reliable feed, fall back to WebSearch |
| Gallagher | https://www.ajg.com/employeeexperience | Annual "State of the Sector" report — landing-page check |
| Brunswick Group | https://www.brunswickgroup.com/insights | Strategic comms — no reliable feed |
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

- **Reddit:** https://www.reddit.com/r/internalcomms (sort by Top, last 7 days) — *blocked by WebFetch; fall back to WebSearch*
- **LinkedIn:** search "internal communications," filter Posts → past week → most relevant — *largely inaccessible to WebFetch; known gap*
- **Substacks:** Joel Schwartzberg "All Hands" (add more as they earn their place)

## (e) Video / YouTube

Configured via `lib/yt_search.py` + `channels.json`. Discovery via search (`internal communications`, `employee experience`, etc.) + curated channel allowlist.

Curated channels live in [`channels.json`](channels.json). Discovery queries are in `yt_search.py` (`DEFAULT_QUERIES`).

Requires `YOUTUBE_API_KEY` in `cerkl/.env` (see `cerkl/.env.example`).

---

## Maintenance

- Add a competitor blog or publication: append to the right category with URL. If it has an RSS feed, also add to `feeds.json`.
- Add a YouTube channel: edit `channels.json` (handle + why).
- Add a discovery query: edit `DEFAULT_QUERIES` in `lib/yt_search.py`.
- Remove a source: delete the row (and the corresponding feed/channel entry if present).
- Both processes re-read all config files every run; no rebuild needed.

---

## Known limitations

(Discovered 2026-05-07 cold-start run; updated 2026-05-10 audit.)

- **Active RSS coverage is thin**: only Ragan, PR Daily, Staffbase, and Simpplr have working RSS. All other competitor blogs (Firstup, Workvivo, Haiilo, ContactMonkey, LumApps, Poppulo, Workshop, AxiosHQ) and Davis & Co. were audited 2026-05-10 and have no usable feed — see the `_unverified_to_test` graveyard in `feeds.json` for per-vendor failure notes. The daily recap relies on Step 2a (WebFetch / WebSearch) to cover these.
- **Staffbase RSS publishes ~biweekly**: a 7-day window will often return 0 items even though the feed is healthy. Not a feed problem — just cadence. The `daily-process.md` Step 2b sub-agent should not flag this as a feed failure.
- **Reddit `/r/internalcomms`**: `WebFetch` returns "unable to fetch from www.reddit.com." Community signal bucket relies on WebSearch summaries; note this in the daily Notes section when it bites.
- **LinkedIn**: largely inaccessible to WebFetch; treat as a known gap. If a specific IC thought-leader post goes viral, capture it manually via paste-in for now.
- **JS-rendered blog landing pages** (Staffbase, Firstup, Workvivo, LumApps, Poppulo notably): `WebFetch` extracts post titles but not publish dates. The `feed_fetch.py` helper sidesteps this where RSS exists; for the rest, WebSearch `site:domain 2026` is the cleanest workaround.
- **Gated reports** (Gallagher full report, ContactMonkey full PDF, Edelman Trust Barometer): use the public landing-page summary + a press-release pickup as the anchor; don't pretend to have read the full PDF.
- **YouTube quota**: 10,000 units/day free. Each daily recap run uses ~700 units (well within budget). Quota is shared with `personal/`'s `yt_search.py` since they use the same GCP project (`dark-yen-494320-b4`).
