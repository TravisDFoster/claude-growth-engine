# Skill: Refresh

Triggered at the start of a session, after time away, or when Travis asks "catch me up" / "what's changed".

Goal: tell Travis what moved since he last looked — **derived from git, not reconciled from ledgers**.

## Procedure

1. **Determine the look-back window**
   - If Travis names one ("since last week", "since Friday") — convert to absolute date.
   - Otherwise default to 7 days.

2. **Pull what moved via git log**
   ```
   git log --since="<date>" --pretty=format:'%h %ad %s' --date=short --name-only
   ```
   - Run from `/Users/travisfoster/claude-code/cerkl/`.
   - Group touched paths by top-level folder (marketing/, sales/, research/, ...). Commit messages + paths are the signal; don't read the diffs unless something is surprising.

3. **Read the tails of Top of Mind project files**
   - For each project linked in INDEX's Top of Mind, read the last ~15 lines (`Read` with offset) for recent `## Log` entries.

4. **Surface a summary** — terse:
   ```
   ## Refresh — <date>
   - What shipped: <from commits + log entries>
   - Movement on Top of Mind items: <per item, or "none">
   - Past-due Calendar Anchors: <list, or "none">
   - Suggested INDEX edits: <promote/demote/anchor changes — proposals only>
   ```

5. **Apply INDEX edits only on Travis's confirm.** Top of Mind is his call.

6. **If git log is empty**: say so. Don't fabricate motion.

## Don't

- Don't load domain context.
- Don't run git mutations (commit/push) — read-only.
- Don't maintain any ledger. This skill reads and proposes; the only file it ever edits (on confirm) is `INDEX.md`.
