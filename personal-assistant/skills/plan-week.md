# Skill: Plan Week (Monday)

Triggered on Monday morning (or when Travis says "plan the week", "weekly plan", "set up the week").

Goal: a 10-minute re-rank ritual, **in chat** — no file materialization. The week's shape is agreed conversationally; INDEX is the only file edited.

## Procedure

1. **Refresh first** if INDEX's `Last refreshed` is older than ~5 days — run `skills/refresh.md`, then continue.

2. **Compute Week A/B parity** from the anchor in `calendar/recurring.md` (Week A starts 2026-05-04): parity = `((Monday − anchor) / 7) mod 2`. Note which standing meetings fall this week.

3. **Sweep Calendar Anchors**
   - Drop past dates (anything shipped gets a `## Log` line in its project file with the date).
   - Ask Travis for new hard dates entering the horizon.

4. **Re-rank Top of Mind with Travis**
   - Propose promotions/demotions based on: anchors inside this week, blockers that cleared, items that slipped.
   - Keep it ≤5. Demoted items need nothing — their state lives in their project files.

5. **Surface the week's shape in chat** — terse:
   ```
   ## Week of <Monday> (Week <A|B>)

   **Standing meetings:** <inline>
   **Hard dates this week:** <from anchors>

   ### Focus
   1. <Top of Mind #1 — what "done by Friday" looks like>
   2. ...

   ### Watch
   - <blocked/passive items with a date risk>
   ```
   Flag tight spots ("Promo Email #1 sends Sunday — Thu/Fri are the only build days").

6. **Edit INDEX on confirm** — Top of Mind order + anchor changes. That's the only write.

## Don't

- Don't write a weekly plan file or mirror the calendar — Google Calendar is the truth; the chat summary is the plan.
- Don't load domain context.
- Don't rewrite `recurring.md` — if a standing meeting changed, ask Travis to update it.
- Don't fabricate effort estimates. If you can't tell whether the week is overloaded, ask.
