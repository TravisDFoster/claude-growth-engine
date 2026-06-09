# Skill: Capture

Triggered when Travis says "add a task", "log this", "remember to X", or drops a quick item that needs to land in the system.

Goal: get the item into the right project file fast, without losing context.

## Procedure

1. **Identify the project** — match the task topic against the files in `projects/`.
   - Clear match → use it.
   - Multiple plausible matches → ask Travis.
   - No match → call `skills/new-project.md` (create-vs-fold criteria live there). Continue with whatever it returns.

2. **Append a dated log line** to the project's `## Log` (create the section at the bottom of the file if it doesn't exist):
   ```
   - YYYY-MM-DD — captured: <tight imperative one-liner> (due YYYY-MM-DD if any)
   ```
   Convert relative dates ("Friday", "next week") to absolute before writing.

3. **Rich context goes with it** — background, people, links, constraints: add to the project's Notes section (or as indented sub-lines under the log entry if it's brief).

4. **Escalate only if warranted**
   - Hard date → add a Calendar Anchors line in `INDEX.md`.
   - It has Travis's attention *now* → propose a Top of Mind change (his call; ≤5 items).
   - Otherwise INDEX is untouched — the log line is enough.

5. **Show what you wrote** so Travis can correct on the spot.

## Don't

- Don't add the same item to multiple projects. Pick one; cross-reference if needed.
- Don't promote every capture to Top of Mind. Most belong only in the project log.
- Don't skip date conversion. "Soon" / "ASAP" / "next week" become YYYY-MM-DD or nothing.
- Don't load domain context to guess. If you don't know which project, ask.
