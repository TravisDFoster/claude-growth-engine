# Skill: Plan (Daily)

Triggered when Travis asks "what should I focus on today", "what's next", "plan my day", or wants help picking between competing items right now.

Goal: surface today's priorities against today's actual schedule. Google Calendar is the source of truth for the schedule — the PA never mirrors it.

## Procedure

1. **Read live state** (cheap)
   - `INDEX.md` — already loaded (Top of Mind + Calendar Anchors)
   - `calendar/recurring.md` — today's standing meetings (respect Week A/B parity)

2. **Ask for today's reality** — one question: "Anything on your calendar today beyond the standing meetings I should plan around?" Travis answers from Google Calendar; don't guess.

3. **Flag time-sensitive items**
   - Calendar Anchors due today or past due.
   - Top of Mind items whose stated next step has a date inside the next 2 days.

4. **Present trade-offs, not decisions** — if two items compete:
   - What each unblocks downstream
   - What slips if it doesn't move today
   - Effort estimate — **if you don't know, ask Travis** rather than guessing
   Let Travis call it.

5. **Output format** — terse markdown:
   ```
   ## Today (<weekday> <date>)

   **Meetings:** <standing + ad-hoc, inline>

   ### Priorities
   1. <task> — <why now>
   2. ...

   ### At risk / past due
   - <flag list, or omit>

   ### Trade-offs to weigh
   - <if competing options>
   ```

## Don't

- Don't load `marketing/`, `sales/`, `hubspot/`, `strategy/`, or `shared/`.
- Don't propose how to *do* the work. Route domain work to top-level `cerkl/CLAUDE.md`.
- Don't pin tasks to time slots. Travis decides time-of-day in the moment.
- Don't restate the full Top of Mind. Plan is a *filter*, not a copy.
- Don't fabricate effort estimates or calendar entries. Ask if unsure.
