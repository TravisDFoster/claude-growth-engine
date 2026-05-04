# Skill: Plan (Daily)

Triggered when Travis asks "what should I focus on today", "what's next", "plan my day", or wants help picking between competing items right now.

Goal: surface today's priorities against today's actual schedule. Use `current-week.md` as the source of truth for the day; INDEX is the ledger of what's possible.

For Monday weekly materialization, see `plan-week.md`. For Friday wrap-up, see `retro.md`.

## Procedure

1. **Read live state** (cheap)
   - `INDEX.md` — already loaded
   - `calendar/current-week.md` — read today's section
   - If `current-week.md` doesn't exist or is from a previous week → recommend Travis run `plan-week` first; don't fake a daily plan from scratch

2. **Pull today's section** from `current-week.md`
   - Today's meetings, free blocks, pre-allocated priorities
   - These were set Monday — start from them, don't re-derive

3. **Reconcile with reality**
   - Anything Travis just told you happened or shifted? Update.
   - Past-due rows in INDEX (Due before today)? Flag explicitly.
   - For any row marked "Verify" — read the project's Status block (top ~10 lines)

4. **Surface staleness signals**
   - Project Status block `Last updated` >14 days old → flag
   - "Verify" status persisting across sessions → flag
   - Blocker waiting on a named person with no movement → flag

5. **Present trade-offs, not decisions** — if two items compete:
   - What each unblocks downstream
   - What slips if it doesn't move today
   - Effort estimate — **if you don't know, ask Travis** rather than guessing
   Let Travis call it.

6. **Output format** — terse markdown:
   ```
   ## Today (<weekday> <date>)

   **Meetings:** <inline list>
   **Free time:** <total + blocks>

   ### Priorities
   1. <task> — <why now> — <effort if known>
   2. ...

   ### At risk / past due
   - <flag list>

   ### Trade-offs to weigh
   - <if competing options>

   ### Stale check
   - <if any flags>
   ```

## Don't

- Don't load `marketing/`, `sales/`, `hubspot/`, `strategy/`, or `shared/`.
- Don't propose how to *do* the work. Route domain work to top-level `cerkl/CLAUDE.md`.
- Don't pin tasks to specific time slots. Day-level allocation, free blocks listed — Travis decides time-of-day in the moment.
- Don't restate the full INDEX. Plan is a *filter*, not a copy.
- Don't fabricate effort estimates. Ask if unsure.
