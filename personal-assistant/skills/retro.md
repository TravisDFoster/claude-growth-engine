# Skill: Retro (Friday)

Triggered Friday afternoon, end-of-week, or when Travis says "Friday retro", "wrap up the week", "archive the week".

Goal: capture what happened this week, carry slipped items forward, archive `current-week.md`. This is a closing rite — Monday's `plan-week` builds on what retro produced.

## Procedure

1. **Read `current-week.md`**
   - Walk through each day's `Priorities for the day`.
   - For each, ask Travis: shipped / carried over / dropped / scope changed?
   - Capture per-day notes: blockers hit, surprises, what slowed things down.

2. **Reconcile completed work into INDEX**
   - For each task Travis confirms shipped: remove from INDEX, append to project file's `## Completed` section with the date.
   - For each task that progressed but isn't done: update the project file's Status block (`Last updated: <today>`); leave the INDEX row.
   - For each task that's now blocked: update the project file's Status block + INDEX `On track` column.

3. **Run a quick INDEX audit**
   - Any row not touched this week and >14 days since project's `Last updated`? Surface it: "stale — still active?"
   - Any project file with Status block dated >2 weeks ago? Same flag.
   - Don't auto-modify. Ask Travis to confirm.

4. **Capture the week's narrative**
   - Append a `## Friday Retro Notes` section to `current-week.md` with:
     ```
     ## Friday Retro Notes — <date>

     ### Shipped this week
     - <list>

     ### Slipped or carried over
     - <task> — <reason> — going to <next week | dropped | reprioritized>

     ### Notes & observations
     - <anything Travis flags worth remembering: a person was unresponsive, a process was clunky, a decision was made>
     ```

5. **Stage carryover for next week**
   - Slipped tasks: confirm they stay in INDEX (most do).
   - If something needs explicit early-Monday attention, note it as a `## For Monday's plan-week` block at the very bottom of the retro notes.

6. **Archive the file**
   - Compute the ISO week number for the Monday of `current-week.md` (e.g. 2026-05-04 → W19).
   - Move `current-week.md` to `calendar/archive/<YYYY-WXX>.md`.
   - Use `Bash`: `mv calendar/current-week.md calendar/archive/2026-W19.md`.
   - Do not leave a stub `current-week.md` behind. Monday's `plan-week` skill creates the new one fresh.

7. **Confirm with Travis**
   - Show: "Archived to `archive/2026-W19.md`. <N> tasks shipped, <M> carried over, <K> stale items flagged. Ready for Monday's plan-week."

## Don't

- Don't run on a non-Friday without confirming. If Travis triggers it Wed, ask: "Closing the week early?"
- Don't archive an empty `current-week.md` — if no work was tracked, ask whether to skip retro this week.
- Don't auto-promote carryovers into a fresh `current-week.md` for next week — that's `plan-week`'s job.
- Don't load domain context.

## Edge cases

- **No `current-week.md` exists:** retro has nothing to close. Tell Travis the week was never materialized — skip to Monday's plan-week.
- **Multiple weeks' lag:** if `current-week.md` is from 3 weeks ago, the retro is mostly archaeology. Ask Travis if he wants to do it properly or just archive without reconciling.
- **Pending sibling-agent updates:** if you see unprocessed `## Update — ...` blocks in project files, suggest running `refresh` first so retro reconciles against fresh state.
