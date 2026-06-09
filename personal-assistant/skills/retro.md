# Skill: Retro (Friday)

Triggered Friday afternoon, end-of-week, or when Travis says "Friday retro", "wrap up the week".

Goal: close the week honestly — what shipped, what slipped, what to remember — and leave one short append-only note as the record.

## Procedure

1. **Derive the week from git**
   ```
   git log --since="<Monday>" --pretty=format:'%h %ad %s' --date=short --name-only
   ```
   Group by folder; this is the draft "shipped" list. Confirm with Travis — git shows motion, he confirms meaning.

2. **Walk Top of Mind** — for each item: shipped / progressed / slipped / dropped?
   - Anything shipped or materially changed: append a dated line to that project's `## Log` (e.g. `- 2026-06-12 — CTA swap shipped across 4 sequences`).
   - Slipped items: note the reason in the log line. Repeated slips are a signal — say so.

3. **Write the week's retro note** — `calendar/archive/<YYYY-WNN>.md` (append-only history, one short file per week):
   ```
   # W<NN> Retro — <date>

   ## Shipped
   - <list>

   ## Slipped / carried
   - <task> — <reason>

   ## Notes
   - <decisions, blockers hit, anything worth remembering>
   ```

4. **Propose Monday's starting point** — suggested Top of Mind re-rank + anchor sweep. Don't apply; Monday's `plan-week` does that with Travis.

5. **Confirm** — "W<NN> closed: <N> shipped, <M> slipped. Retro note at `calendar/archive/<YYYY-WNN>.md`."

## Don't

- Don't run on a non-Friday without confirming ("Closing the week early?").
- Don't reconcile any ledger — the log lines and the retro note ARE the record.
- Don't auto-edit Top of Mind — propose only.
- Don't load domain context.
