# Skill: Refresh

Triggered at the start of a session, after time away, or when Travis asks "catch me up" / "what's changed".

Goal: reconcile sibling-agent updates and recent edits with INDEX so Travis starts each session on accurate state.

## Procedure

1. **Determine the look-back window**
   - If Travis names one ("since last week", "since Friday") — convert to absolute date.
   - Otherwise default to 7 days.

2. **Pull recent changes via git log**
   ```
   git log --since="<date>" --pretty=format:'%h %ad %s' --date=short -- \
     personal-assistant/ marketing/ sales/ hubspot/ strategy/
   ```
   - Run from `/Users/travisfoster/claude-code/cerkl/`.
   - This is the cheapest signal of what moved.

3. **Read sibling-agent push updates**
   For each project file in `projects/`, read just the bottom (`Read` with offset to last ~30 lines) and look for:
   ```
   ## Update — YYYY-MM-DD (from <agent>/)
   - Completed: <ref>
   - Status change: <if any>
   - New blocker: <if any>
   - Proposed next step: <one line>
   ```

4. **Reconcile each update into INDEX**
   - **Completed** → remove the row from INDEX, append to project's `## Completed` section with date.
   - **Status change** → update the project's Status block (state, on-track, last updated).
   - **New blocker** → reflect in Status block; consider whether the row in INDEX should be paused or re-prioritized.
   - **Proposed next step** → update or add the INDEX row.

5. **Archive the update block** — once reconciled, move the `## Update — ...` block out of the project's bottom area into a `## History` section (append-only). Keep the project file scannable.

6. **Surface a summary to Travis** — terse:
   ```
   ## Refresh — <date>
   - <N> sibling updates reconciled
   - Completed: <list>
   - New: <list>
   - Status changes: <list>
   - Anything that needs your attention: <list>
   ```

7. **If git log is empty and no update blocks exist**: say so. Don't fabricate motion.

## Edge cases

- **Conflict**: if INDEX disagrees with a sibling's proposed next step, surface it — don't silently overwrite. Ask Travis to resolve.
- **Update block from an unknown agent**: keep the block, flag it, but apply if the format matches.
- **Project file edited directly (not via push contract)**: git log will show it. Read the diff and ask Travis if it changes the INDEX row.

## Don't

- Don't load domain context.
- Don't run git mutations (commit/push) — read-only.
- Don't apply reconciled changes silently. Always show the summary first; apply on confirm if changes are non-trivial.
