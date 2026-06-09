---
name: build-process
description: When the user wants to build a new process, set up a new workflow, formalize a recurring task, spin up a new agent/researcher/role, or turn an ad-hoc job into something Claude can run repeatably. Triggers on phrases like "build a new process," "set up a new workflow," "create a new job for X," "spin up a [role]," "make this repeatable," "formalize this." Outputs a `[job]-process.md` orchestrator, any new `SKILL.md` files needed, and routing-table updates in every parent CLAUDE.md on the path. Domain-agnostic — works for marketing, sales, ops, research, personal-assistant work, anywhere in this workspace.
metadata:
  version: 0.1.0
---

# Build a Process

Meta-process for installing a new repeatable job into this workspace's routing system. Output is a `[job]-process.md` orchestrator (and supporting files) wired into the routing tables of every `CLAUDE.md` on its path.

Read [PRINCIPLES.md](../../PRINCIPLES.md) before applying this skill if you haven't recently.

---

## When to use this skill

**Use when:**
- The user has a recurring task they want to make repeatable.
- A new role or agent needs a home in the workspace.
- A one-off conversation produced something worth formalizing.

**Don't use when:**
- The job is genuinely one-shot — answer in chat instead.
- The user wants a marketing channel — defer to [`marketing/channels/build-channel-process.md`](../../marketing/channels/build-channel-process.md), the marketing-specific specialization. The general process here applies everywhere else.

---

## The 8-phase build

### Phase 1 — Scope the job

Ask the user, plainly, before scaffolding anything:

1. **Deliverable** — in one sentence, what does this job produce?
2. **Trigger** — manual invocation, scheduled, or event-driven?
3. **Frequency** — one-shot, daily, weekly, ad-hoc?
4. **Consumer** — who reads/uses the output? Where does it land?
5. **Inputs** — what does the job pull from (files, URLs, APIs, prior outputs)?
6. **Owner per step** — Claude / User / Joint / External?

If any answer is "not sure," stop and discuss before scaffolding. Cheap to redesign now; expensive after files exist.

### Phase 2 — Locate the job in the routing chain

Find its home by walking down from the workspace root.

- Is there an existing dept that fits? Route there.
- If not, propose a new dept and **wait for user approval before creating top-level folders**.
- Within the dept, does an existing subdomain fit, or does it warrant a new subfolder?
- Confirm the path with the user before creating directories.

**Routing depth is flexible.** A path might be 2 levels deep (root → process) or 5 levels deep (root → dept → subdomain → channel → project → process). The invariant: every router on the path loads only what its scope needs.

**Add a child `CLAUDE.md` only when** the folder has ≥3 executors or its conventions diverge from the parent's. A folder with one process file routes from the parent directly.

**Naming-collision check** — before settling on a folder name, skill name, or process slug, grep for it across the workspace. Two `*-daily-process.md` files with overlapping triggers will confuse routing.

**Cross-folder consumers** — if the output of this process feeds work in another folder, the process owns the output path; the consumer reads from there. If the consumer needs to *know* about new outputs, state it in chat at session end — activity is derived from git log (see PRINCIPLES.md #8); never reach across.

### Phase 3 — Audit context loading along the route

For every `CLAUDE.md` on the path from root to leaf:

1. Read its `Context to load:` block.
2. Ask: does the new job need this for *every* task in this folder's scope, or just *some* tasks?
3. If only some, push the load down to where it's actually used.
4. Verify all paths in the block resolve (test by listing each).

Common findings: shared docs loaded "just in case," broken paths, parent-restated rules that no longer apply.

### Phase 4 — Map the steps

For each step in the workflow, capture:

| Field | Values |
|---|---|
| Step ID | `1`, `2`, `2a`, `2b`, ... |
| Owner | Claude / User / Joint / External |
| Type | Decision / Content / Tool action / Lookup / Synthesis |
| Inputs | Files, URLs, prior step outputs |
| Outputs | File paths, side effects |
| Parallelizable with | Step IDs (symmetric — if 2a lists 2b, then 2b must list 2a) |
| Needs | Skills to invoke, context files to read |

Be honest about what Claude can't do (no live logins, no posting to LinkedIn, no scheduling Zoom). Mark those steps as `External` and surface them as a checklist for the user.

### Phase 5 — Reuse vs. build

For each Claude-owned step:

1. Is there an existing `SKILL.md` that covers it? Reference it by absolute path.
2. If not, is the gap reusable across other processes? **Yes** → new `SKILL.md`. **No** → spell it out inline in the process file.
3. If a step is just "use generic skill X" with no project-specific value, drop the wrapper and reference X directly.

Trim aggressively before building. One-liners are templates, not skills. Static references are docs, not skills.

### Phase 6 — Build in dependency order

Order matters: foundations before content.

1. **Folder structure** — create the directory tree.
2. **CONTEXT.md** — only if the dept/folder is new and needs stable context.
3. **Reference docs** — input source lists, naming conventions, schemas (e.g., `sources.md` for a researcher).
4. **Templates** — output scaffolds with meaningful placeholders.
5. **New `SKILL.md` files** — only if Phase 5 said yes.
6. **The `[job]-process.md`** — the orchestrator. Use the template below.
7. **Routing-table updates** — every `CLAUDE.md` on the path gets a row.

### Phase 7 — Dry-run validation

Before declaring done:

- Pick realistic-but-fake inputs.
- Walk the user through what files would be created and where.
- Verify all linked paths resolve.
- Verify parallel steps don't write to overlapping outputs.
- Show the user the next-step output (the chat-printed summary the process produces).
- **Don't actually write the live run yet.**

The user will spot issues at this stage. Fix the tweaks and only then declare done.

### Phase 8 — Finalize

1. Confirm every link in the process file resolves.
2. Confirm routing rows are added to every `CLAUDE.md` on the path.
3. Note future work (e.g., "wire to /schedule when scheduling is set up") in a `Future work` section at the bottom of the process file.
4. Stage only this session's files (avoid `git add -A`).
5. Commit with a message that explains the *why* of the structural changes.

---

## `[job]-process.md` template

```markdown
# [Job Name]

> One-line purpose. Output: <path or destination>.

## Trigger
What the user types to start this. (Verbatim phrases.)

## Inputs
What I'll ask the user before starting. (Skip if scheduled.)

## Context to load
- absolute path
- absolute path

(Per PRINCIPLES.md #4, this list is authoritative for this scope — parent loads do not apply unless re-listed here.)

**Parallelization fallback:** if any step is parallelizable and the runtime has the `Agent`/`Task` tool, dispatch sub-agents in one message. If not, parallelize via multiple Tool calls (e.g., `WebSearch`, `WebFetch`, `Read`) in a single message — same effect.

## Steps

### Step 1 — <name>
- **Owner:** Claude
- **Parallelizable with:** —
- **Needs:** <SKILL.md absolute path or context file>
- **Inputs:** <from where>
- **Produces:** <absolute path or in-memory>
- **What to do:** Imperative one-liner.

### Step 2a — <name>
- **Owner:** Claude (sub-agent)
- **Parallelizable with:** 2b, 2c
- **Needs:** ...
- **Produces:** <distinct path>
- **What to do:** ...

### Step 2b — <name>
- **Owner:** Claude (sub-agent)
- **Parallelizable with:** 2a, 2c
- ...

## Output
- Path / format / destination / consumer.

## Future work
- Open improvements (e.g., wire to /schedule, add a source category).

## Learnings
Append "what broke / what we changed" notes here as the process matures.
```

---

## Sub-agent dispatch convention

When two or more steps share symmetric `Parallelizable with` markers, dispatch them in **one message with multiple `Agent` tool calls**. Each call gets a self-contained brief — sub-agents don't share context with each other or with you.

Parallel steps must:
- Write to non-overlapping output paths (or return in-memory results, not files).
- Not depend on each other's intermediate state.
- Be summarizable into ≤200 words apiece (sub-agent results return as a single message; long results blow context).

Each sub-agent brief must be **self-contained**. Sub-agents inherit no conversation context, so the brief must state: the task, the inputs (with absolute paths or full lists, not "see sources.md"), the output format, the length cap, and any voice/style rules. Restate even what feels obvious — "use absolute YYYY-MM-DD dates," "include URLs inline," "skip product-launch announcements."

Sequential steps run inline in the orchestrator's own context.

---

## Anti-patterns

- **Loading everything "just in case."** Every load taxes every task. Push down.
- **CLAUDE.md as a content document.** It's a router. Detail goes elsewhere.
- **Skill-wrapping a generic skill with no value-add.** Use the generic directly.
- **Pre-creating empty placeholder files.** Let the process create files at runtime.
- **A new `SKILL.md` for every micro-step.** Prefer inline steps in the process file.
- **Trusting routing to carry rules.** Restate cross-folder rules locally in the leaf `CLAUDE.md`.
- **Asymmetric parallelism.** If 2a is parallelizable with 2b, 2b must say so too.
- **Unbounded routing tables.** When a `CLAUDE.md` routing table exceeds ~12 rows, group by category or split into a child router.
- **Forgetting the routing-table update.** A process the parent `CLAUDE.md` doesn't list is invisible.
- **Creating a child `CLAUDE.md` for one executor.** Route from the parent directly.

---

## Validation checklist

Run before declaring done:

- [ ] Every `Context to load:` path along the route resolves — **test by listing each with `Bash` `[ -f <path> ] && echo OK || echo MISS`** (don't trust a visual scan; broken paths breed silently after file moves).
- [ ] No upstream `CLAUDE.md` loads anything the new process doesn't need.
- [ ] The new process file lists trigger phrases, inputs, context, steps, output.
- [ ] Every step has Owner, Needs, Inputs, Produces.
- [ ] Parallel markers are symmetric.
- [ ] Parallel steps write to non-overlapping paths.
- [ ] Every Claude step references either an existing `SKILL.md` or has inline instructions.
- [ ] Routing rows added to every `CLAUDE.md` on the path from root to leaf.
- [ ] Templates and reference docs (e.g., `sources.md`) exist if the process file references them.
- [ ] **For researcher-style processes:** every URL in `sources.md` has been smoke-tested with `WebFetch` — catches redirects, paywalls, JS-rendered pages, dead domains. (Lesson from the 2026-05-07 cc-trends build: 6 sources had problems only WebFetch could surface.)
- [ ] Dry-run executed and reviewed by the user.
- [ ] Future-work section names follow-ups (scheduling, expansion, deprecations).

---

## Adapting for non-Cerkl workspaces

This skill applies anywhere with a `CLAUDE.md` routing chain. For `personal/`:

- Root is `personal/CLAUDE.md`.
- "Departments" map to `planning/`, `projects/<project>/`, `google/`, etc.
- PRINCIPLES #8 still applies — planning derives activity from git log; processes end by stating what shipped in chat.

The phases (scope → locate → audit → map → reuse-vs-build → build → dry-run → finalize) carry over verbatim.

---

## Marketing-channel specialization

For marketing channels specifically, use [`build-channel-process.md`](../../marketing/channels/build-channel-process.md). It adds channel-specific phase labels (planning → content → promotion → event → follow-up) on top of these phases. The general process here applies elsewhere.

---

## Learnings (append-only)

Notes from real builds. Each entry: what broke, what we changed, why.

### 2026-05-07 — IC Trends researcher (first live build)

- **Conditional domain-tagging beats blanket tagging.** The IC researcher has a "Why it matters for Cerkl" line per item. First draft made it mandatory; that forced manufactured relevance. Fixed by making it conditional — only when an item actually touches Cerkl's positioning. **Rule:** if a process tags items with a domain angle, make the tag conditional and tell Claude not to force it.
- **Parallel sub-agent briefs are the highest-risk failure mode.** Each of 2a–2d needed: source list (full, not "see file"), output format, length cap (≤200 words), date convention. Easy to forget one and the sub-agent free-writes. **Rule:** every parallel sub-agent step must have an explicit `Sub-agent brief must say:` field listing the 4 fixed elements (inputs verbatim, output format, length cap, conventions). Don't trust the sub-agent to read upstream context.
- **`Rules:` in a CLAUDE.md drifts toward 4–5.** Wanted to add a 4th rule about citation format — caught myself and moved it to Conventions. **Rule:** restate "≤3 rules in CLAUDE.md" during Phase 6; route everything else to Conventions or CONTEXT.md.
- **One-executor folders correctly skip their own CLAUDE.md.** `ic-trends/` has only one process and routes from `research/CLAUDE.md` directly. Confirmed Principle #10 in practice.
- **Future-work section pays off immediately.** Listing `/schedule` integration, weekly rollup, watchlist, ignore list, and cross-folder feed as future work captured every "wouldn't it be nice" thought without bloating v1.
- **Dependency order held.** Folders → CONTEXT → sources → template → process → routing. Every later artifact referenced an earlier one with a resolved path. No backtracking.

### 2026-05-07 — IC Trends researcher (cold-start sub-agent test)

Stress-tested the routing chain by dispatching a fresh-context sub-agent with the simple command "Run the IC trends recap." Surfaced four real issues:

- **Parent and child `Context to load:` blocks were unioning, not replacing.** Root `cerkl/CLAUDE.md` mandated `shared/broadcast.md`. Research's child router said "don't load it." The cold sub-agent loaded both — the parent's mandate leaked into the child's scope. **Fix:** PRINCIPLES.md #4 updated — child router's `Context to load` now explicitly *replaces* parent's, not unions. The kludgy "(Don't load X by default)" parenthetical in `research/CLAUDE.md` was simplified to a pointer back at the principle. **Build-process implication:** during Phase 3 (audit context loading), every router on the path must be self-sufficient — don't rely on parent loads carrying through. If the child router has a `Context to load` block, list every file it actually needs.
- **Sub-agent harnesses don't always have `Agent`/`Task` tools.** The fresh agent couldn't dispatch parallel sub-agents; it parallelized at the WebSearch level instead (multiple calls in one message). Worked fine. **Implication:** every process file with a parallel step must declare a fallback — "if Agent unavailable, parallelize via multiple Tool calls in a single message." The `[job]-process.md` template should bake this in.
- **`WebFetch` blocked on Reddit and JS-rendered blog landing pages.** Predictable infra gap. **Implication for sources files:** add a "Known limitations" section listing sources that need alternate ingestion (RSS, browser MCP, manual paste). Update lists to reflect what works in practice, not what would be ideal. The build-process skill should mention this when reviewing reference docs in Phase 6.
- **Pre-existing context-load drift in `marketing/CLAUDE.md` and `sales/CLAUDE.md`.** Both have their own `Context to load` blocks but rely on the root-leaked `broadcast.md`. Under the new principle (child replaces parent), they may now under-load. **Out of scope for this build, but flagged as follow-up:** audit and update marketing/sales routers to be self-sufficient.

What worked:
- Cold sub-agent self-routed `cerkl/CLAUDE.md` → `research/CLAUDE.md` → `ic-trends-daily-process.md` without help. The routing tables alone were enough.
- Process file's explicit step-by-step (with parallelization markers) was followable end-to-end.
- Notes section captured every fetch failure cleanly — exactly the contract.
- Conditional "Why it matters for Cerkl" tag did not get force-applied to off-domain items. Phase 5 conditional-tagging guidance held up under load.

### 2026-05-07 — Workspace audit (follow-up to the principle change)

The cold-start test surfaced a flag for "marketing/CLAUDE.md and sales/CLAUDE.md may now under-load." A full audit of every router under `cerkl/` revealed a much bigger pre-existing bug:

- **41 absolute paths across 11 files were missing the `cerkl/` prefix.** Pattern: `/Users/travisfoster/claude-code/shared/...` instead of `/Users/travisfoster/claude-code/cerkl/shared/...`. Affected `sales/CLAUDE.md`, `sales/REFERENCES.md`, all 4 sales channels, `marketing/marketing-strategy/CONTEXT.md`, `marketing/website/CLAUDE.md`, `strategy/CLAUDE.md`, `strategy/REFERENCES.md`, `strategy/company-info.md`. **These paths have never resolved** — sales, strategy, and the website router have been silently failing to load their declared shared context since they were created. Under the OLD principle (parent unions with child) they leaked root's icp + broadcast through; under the NEW principle (child replaces parent) they would have loaded nothing. **Fix:** bulk regex replacement across all affected files. Verified clean by grep afterward.
- **Root cause likely:** copy-paste from a draft that lived at `/Users/travisfoster/claude-code/` before the workspace was reorganized into `cerkl/`. No one re-resolved the absolute paths on the move. **Build-process implication:** Phase 3 (audit context loading) must include a literal path-resolution step — `for path in Context_to_load: test it exists`. Add this as a hard rule to the validation checklist.
- **Marketing, sales, strategy, marketing/website, plus 4 sales channels were updated to be self-sufficient** under the new principle — `broadcast.md` added everywhere it was missing; `competitors.md` and `company-info.md` added to `marketing/`; `marketing/CONTEXT.md` added to `marketing/website/`. PA's informal "Always read first" + "Do not load" prose was converted to a standard `Context to load:` block (with explicit empty list of shared files).
- **`hubspot/CLAUDE.md` deliberately left without a `Context to load:` block** — it inherits from root (icp + broadcast). HubSpot tasks usually don't need broadcast detail; future audit could decide if root should slim down or if hubspot should declare its own minimal block.
- **Many marketing channels (`newsletter/`, `newsroom-pr/`, `comparison-seo/`, etc.) are still unaudited.** Under the new principle they need to be self-sufficient too. Out of scope for this audit — flagged as ongoing follow-up; can be done channel-by-channel as Travis works in each.

What this means for the build-process skill going forward:

1. **Add path-resolution to Phase 3** — every `Context to load:` path in every router on the route must be tested for existence, not just human-read. The tool: `Bash` `[ -f path ] && echo OK || echo MISS`.
2. **Run the same path-check across the whole workspace at first session** of any new build — not just the route. Broken paths breed silently when files are moved.
3. **When the principle changes** (like child-replaces-parent did 2026-05-07), the change is non-local. Schedule an audit pass as soon as the principle lands, not "as a follow-up." Drift compounds.

### 2026-06-09 — Full-system review (drift audit)

A top-down review of the workspace against PRINCIPLES.md found the rot concentrated entirely in the *declarative* layer — routing tables, file-structure trees, README — while the executor layer (processes, skills, PA state) held up well.

- **Routing rows and tree entries were scaffolded for folders that were never built.** `sales/CLAUDE.md` routed to `outbound/`, `discovery/`, `objection-handling/`, `enablement/` — none existed on disk, yet its tree described their contents in detail. A cold agent would have confidently navigated to four phantom folders. **Rule:** never add a routing row or tree entry for a folder that doesn't exist yet. Add the row when the folder ships. (The 2026-05-07 checklist tested `Context to load:` paths but not routing-table targets — same failure class, different field.)
- **Hand-maintained file trees are duplicated state, and duplicated state drifts.** `strategy/CLAUDE.md`'s tree was a pre-reorg fossil (showed `organic-content/`, the phantom sales subfolders). **Fix: deletion over policing** — trees removed from the rotten routers; PRINCIPLES.md #3 amended to make trees optional, shallow, and annotation-only. No lint process was added — reducing what *can* drift beats building machinery to police drift.
- **Tombstones and placeholders linger.** `strategy/company-info.md` was a "this file has moved" stub; `strategy/REFERENCES.md` was unfilled boilerplate; `strategy/monthly-plans/` and `marketing/channels/youtube/` were empty dirs. All deleted. **Rule:** when a file moves, delete the original — the git history is the tombstone.
- **Root comment vs. root behavior:** root tree claimed "shared/ ← load before any task" while root's `Context to load:` lists only `broadcast.md`. Comment fixed to match reality. Note: `hubspot/` relies on inheriting root's loads and assumes icp + broadcast — flagged, deliberately not touched (needs its own session).


