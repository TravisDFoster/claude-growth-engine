# IC Trends — Daily Recap

> Daily recap of important internal-communications news and trends, ranked by relevance to Cerkl's ICP and competitive set. Output: `daily/YYYY-MM-DD.md` plus a chat-printed summary.

## Trigger
- "Run the IC trends recap"
- "Daily IC news"
- "What's new in internal comms today"
- "Run ic-trends-daily"

## Inputs
None. The process pulls from `sources.md`. Today's date is determined at runtime (use absolute `YYYY-MM-DD`).

## Context to load
- /Users/travisfoster/claude-code/cerkl/shared/icp.md
- /Users/travisfoster/claude-code/cerkl/shared/competitors.md
- /Users/travisfoster/claude-code/cerkl/research/CONTEXT.md
- /Users/travisfoster/claude-code/cerkl/research/ic-trends/sources.md
- /Users/travisfoster/claude-code/cerkl/research/ic-trends/output-template.md

---

**Parallelization fallback:** Step 2 fans out to 4 parallel sub-agents. If the runtime has the `Agent`/`Task` tool, dispatch them in one message with 4 Agent calls (each gets a self-contained brief). If not, parallelize via multiple `WebSearch`/`WebFetch` calls in a single message — same effect, one less indirection.

## Steps

### Step 1 — Read sources and resolve today's date
- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** `sources.md`
- **Inputs:** Current date
- **Produces:** In-memory: 4 fetch buckets + today's `YYYY-MM-DD`
- **What to do:** Parse `sources.md` into 4 fetch buckets — (a) competitor blogs, (b) IC publications, (c) analyst/research, (d) community signal. Resolve today's date as absolute `YYYY-MM-DD`.

### Step 2a — Fetch competitor blog activity (sub-agent)
- **Owner:** Claude (sub-agent)
- **Parallelizable with:** 2b, 2c, 2d
- **Needs:** WebSearch / WebFetch
- **Inputs:** Competitor list from `sources.md` (Staffbase, Simpplr, LumApps, Firstup, Poppulo, Workvivo, Haiilo, AxiosHQ, Workshop, ContactMonkey)
- **Produces:** Bulleted list (max 8 items, last 7 days only): vendor, headline, URL, 1-line takeaway, publish date
- **Sub-agent brief must say:** Search each competitor's blog/news landing page. Keep only items dated within the last 7 days. Skip product-launch announcements; prioritize POV pieces, original research, partnerships, exec hires. Return ≤200 words. Use absolute YYYY-MM-DD dates.

### Step 2b — Fetch IC publication coverage (sub-agent)
- **Owner:** Claude (sub-agent)
- **Parallelizable with:** 2a, 2c, 2d
- **Needs:** WebSearch / WebFetch
- **Inputs:** Publication list from `sources.md` (Ragan, PR Daily, IABC, Davis & Co., Gallagher, Brunswick, Edelman)
- **Produces:** Bulleted list (max 8 items, last 7 days): publication, headline, URL, 1-line takeaway, publish date
- **Sub-agent brief must say:** Find the most-discussed IC topics this week. Skip vendor-paid placements (flag if uncertain). Return ≤200 words. Use absolute YYYY-MM-DD dates.

### Step 2c — Fetch analyst / research signals (sub-agent)
- **Owner:** Claude (sub-agent)
- **Parallelizable with:** 2a, 2b, 2d
- **Needs:** WebSearch
- **Inputs:** Analyst list from `sources.md` (Gartner, Forrester, McKinsey, Gallup, HBR, SHRM)
- **Produces:** Bulleted list (max 5 items, last 30 days — analyst content moves slower): firm, title, URL, 1-line takeaway, publish date
- **Sub-agent brief must say:** Look for new reports or articles touching internal communications, employee experience, organizational change, or AI-in-comms. Return ≤200 words. Use absolute YYYY-MM-DD dates.

### Step 2d — Fetch community signal (sub-agent)
- **Owner:** Claude (sub-agent)
- **Parallelizable with:** 2a, 2b, 2c
- **Needs:** WebSearch
- **Inputs:** /r/internalcomms top posts (last 7 days), LinkedIn search for "internal communications" posts (last week, by relevance)
- **Produces:** Bulleted list (max 5 items): thread/post title, URL, 1-line takeaway, why it matters
- **Sub-agent brief must say:** Identify what practitioners are actually discussing — pain points, tool comparisons, layoff/restructure questions, hiring signals. Return ≤200 words.

### Step 3 — Synthesize and rank
- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** Step 2a–2d outputs, `output-template.md`, `competitors.md` (for the Cerkl angle)
- **Inputs:** All four sub-agent results
- **Produces:** In-memory ranked list of 5–10 items
- **What to do:** Score each item on (a) novelty (is this new today, not warmed-over?), (b) relevance to Cerkl ICP and Foundations positioning, (c) signal vs. noise. Keep the top 5–10. For each kept item, draft: headline, source, URL, publish date, 1–2 line summary, and a 1-line "Why it matters for Cerkl" *only when it actually does* (don't force it).

### Step 4 — Write the daily file
- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** `output-template.md`
- **Inputs:** Step 3 ranked list, today's date
- **Produces:** `cerkl/research/ic-trends/daily/YYYY-MM-DD.md`
- **What to do:** Fill the template with the ranked list. Open with a 2-sentence "today's headline takeaway." Move anything below the top cut into the Watchlist section. Use the Notes section for gaps (paywalled sources, 404s, "no new analyst content this week").

### Step 5 — Print summary to chat
- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** —
- **Inputs:** The file from Step 4
- **Produces:** Chat output
- **What to do:** Print: (1) the file path created, (2) today's headline takeaway, (3) the top 3 items as terse bullets with URLs, (4) one-line invitation: "Want me to dig into any of these?"

---

## Output

- **File:** `cerkl/research/ic-trends/daily/YYYY-MM-DD.md`
- **Chat:** file path + headline takeaway + top 3 bullets
- **Consumer:** Travis (morning read)

## Future work

- **Wire to `/schedule`** for daily 7am autorun. The schedule entry would target this process file with a fixed prompt: "Run the IC trends daily recap." See `cerkl/PRINCIPLES.md` and the `/schedule` skill when ready.
- **Weekly rollup** — `weekly/YYYY-WW.md` aggregating the dailies.
- **Watchlist mechanism** — let Travis flag specific topics/phrases to track week-over-week.
- **Ignore list** — vendors or publications consistently producing noise (filter at Step 2 fetch level).
- **Cross-folder feed** — surface items into `marketing/channels/newsletter/` for Cerkular consideration via push-update protocol.

## Learnings

<!-- append "what broke / what we changed" notes here as the process runs -->
