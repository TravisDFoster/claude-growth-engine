# Skill: Plan Week

Triggered on Monday morning (or when Travis says "plan the week", "weekly plan", "materialize the week", "let's set up the week").

Goal: produce a fresh `calendar/current-week.md` that materializes the upcoming week — recurring meetings expanded into dated slots, free time identified, INDEX priorities allocated to days. Treat the output as a working draft, not a contract.

## Procedure

1. **Confirm the target week**
   - Default: the week containing today.
   - If today is Tue–Sun, ask: "Materialize the current week (started <Monday's date>) or next week (starting <next Monday>)?"
   - All dates absolute (YYYY-MM-DD).

2. **Compute Week A / B parity**
   - Read the anchor in `calendar/recurring.md` (currently: Week A starts 2026-05-04).
   - For Monday `M` of the target week: parity = `((M − anchor) / 7) mod 2` → `0` = A, `1` = B.

3. **Expand recurring → dated slots**
   - Pull every weekly meeting into its weekday slot.
   - Pull bi-weekly meetings matching the target week's parity.
   - Pull any monthly meetings whose date falls inside the target week.

4. **Read existing ad-hocs** for the week
   - If `current-week.md` already has ad-hocs noted, preserve them.
   - Ask Travis: "Any ad-hoc meetings already on your calendar for this week I should add?" — only ask if you're starting fresh; if regenerating mid-week, just preserve what's there.

5. **Compute free blocks per day**
   - Assume working hours 9:00 am – 5:00 pm unless Travis says otherwise.
   - Subtract meetings.
   - List remaining contiguous blocks as `H:MM am/pm – H:MM am/pm (Xh)`.
   - Sum total free hours per day.

6. **Pull priorities from INDEX**
   - Read `INDEX.md` Top of Mind + High-priority rows.
   - Note hard deadlines that fall inside this week or the following week (forward visibility).

7. **Allocate priorities to days, not time slots**
   - Hard deadlines first: work backward from due date.
   - Travis-owned blockers next.
   - Group related work on the same day where it makes sense (e.g. webinar landing page + follow-up email together).
   - **If you don't know the effort of a task, ask Travis** before slotting (per the design rule — no effort estimates in INDEX).
   - Don't pin to specific time slots — the day-level allocation is enough.

8. **Identify carryover candidates**
   - INDEX rows that didn't make this week's allocation. List them at the bottom of `current-week.md` so they're visible if a free block opens up.

9. **Write `calendar/current-week.md`** using this structure:
   ```
   # Current Week — <Monday> to <Friday>

   > **Week <A|B>** · Materialized <today>. Friday retro will archive this to `archive/<YYYY-WXX>.md`.

   ## Week At a Glance
   <table: Day | Meetings | Free time | Top priority>

   **Hard deadline this week:** <if any>

   ---

   ## Daily
   <one section per Mon–Fri, each with: Meetings · Free blocks · Priorities for the day · Ad-hocs/notes>

   ## Carryover candidates
   <Med/Low INDEX items not slotted>

   ## Friday retro notes
   _(populated during Friday retro)_
   ```

10. **Surface the plan to Travis**
    - Show the Week At a Glance table inline.
    - Flag any tight spots: "Press Release deadline Fri — Mon and Tue are your only big focus blocks before Maria needs the draft."
    - Ask: anything to adjust before finalizing?

## Don't

- Don't pin tasks to specific time slots within a day. Day-level allocation only.
- Don't load domain context (`marketing/`, `sales/`, `hubspot/`, `strategy/`).
- Don't rewrite `recurring.md`. If a recurring meeting needs to change, ask Travis to update `recurring.md` directly, then re-materialize.
- Don't archive last week here — the `retro` skill handles that on Friday.
- Don't fabricate effort estimates. If you can't tell whether a task fits a day, ask.

## Edge cases

- **Mid-week re-materialization** (e.g. major schedule change): preserve any ad-hocs and Friday retro notes already in `current-week.md`. Re-compute free blocks and priorities only.
- **No INDEX deadlines this week:** focus on Travis-owned blockers and active in-progress work.
- **Priority count > available capacity:** don't cram. Surface the conflict — "5 High items, ~30h of free time, you'll need to push 2 to next week. Which?"
