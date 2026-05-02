# HubSpot Skills Context

## How Skills Work

Each skill follows a 4-stage pattern:

| Stage | What happens |
|-------|-------------|
| **Plan** | Explains the approach, asks for any configuration needed |
| **Before** | Audits current state, exports CSV baseline, shows what will change |
| **Execute** | Makes the changes — API scripts or step-by-step UI instructions |
| **After** | Verifies the fix, compares before/after, confirms success |

Skills with scripts have ready-to-run Python files in `skills/{skill-name}/scripts/`. Skills requiring HubSpot UI work provide precise build instructions.

## Workflow

1. **Audit** — Run `hubspot-audit` to establish a baseline and identify issues
2. **Plan** — Run `hubspot-implementation-plan` to get a prioritized, sequenced roadmap
3. **Execute** — Work through skills in the recommended order
4. **Maintain** — Use `weekly-cleanup-routine` and `quarterly-database-cleanup` to keep it that way

## Skills Reference

### Audit & Planning

| Skill | Description |
|-------|-------------|
| `hubspot-audit` | Comprehensive audit of contacts, companies, deals, properties, lists, workflows, and forms. Grades each finding and maps it to the skill that fixes it. |
| `hubspot-implementation-plan` | Generate a phased implementation plan from audit findings with prioritized action items. |

### Database Hygiene

| Skill | Description |
|-------|-------------|
| `delete-no-email-contacts` | Identify and delete contacts with no email address — unusable records that inflate the database |
| `suppress-hard-bounced` | Suppress contacts with hard-bounced email addresses to protect sender reputation |
| `suppress-global-unsubscribes` | Suppress globally unsubscribed contacts to ensure compliance and reduce wasted spend |
| `suppress-ghost-contacts` | Find and suppress ghost contacts — records with no activity, no engagement, and no business value |
| `merge-duplicate-companies` | Detect and merge duplicate company records using domain matching and fuzzy name comparison |
| `reassign-deactivated-owners` | Reassign contacts and deals owned by deactivated HubSpot users to active team members |

### Data Enrichment

| Skill | Description |
|-------|-------------|
| `enrich-company-name` | Populate missing company names on contacts by pulling from associated company records |
| `enrich-industry` | Backfill contact industry values from associated company industry data |
| `standardize-geo-values` | Normalize country and state/region values to consistent formats across the database |
| `assign-unowned-contacts` | Assign marketing contacts with no owner to team members based on territory or segment rules |
| `fix-lifecycle-stages` | Detect and correct lifecycle stage violations — contacts stuck in the wrong stage or regressed backwards |
| `backfill-geo-data` | Backfill missing country and state values using IP geolocation, form submissions, and company data |

### Segmentation & Scoring

| Skill | Description |
|-------|-------------|
| `create-icp-tiers` | Create an ICP tier property and assign tier values based on firmographic criteria |
| `build-lead-scoring` | Design and implement a lead scoring model using HubSpot scoring properties and behavioral signals |
| `build-smart-lists` | Build active smart lists for key segments — ICP tiers, lifecycle stages, engagement levels, suppression groups |
| `create-segment-lists` | Create a standard set of segment lists for reporting, targeting, and suppression |

### Automation Workflows

| Skill | Description |
|-------|-------------|
| `new-contact-hygiene-workflow` | Build a workflow that screens new contacts on creation — validates email, enriches data, assigns owners |
| `engagement-suppression-workflow` | Create a workflow that automatically suppresses contacts after prolonged disengagement |
| `lifecycle-progression-workflow` | Set up automated lifecycle stage progression based on engagement thresholds and sales activity |
| `bounce-monitoring-workflow` | Build a workflow that monitors bounce events and auto-suppresses contacts exceeding bounce thresholds |

### Ongoing Maintenance

| Skill | Description |
|-------|-------------|
| `weekly-cleanup-routine` | A repeatable weekly checklist covering the highest-impact maintenance tasks |
| `quarterly-database-cleanup` | Run a quarterly hygiene sweep — re-audit contacts, prune stale records, refresh suppression lists |
| `review-bounced-contacts` | Review contacts with 3+ bounces and decide on suppression or re-verification |
| `cleanup-lists` | Audit and archive unused, redundant, or stale lists cluttering the portal |
| `cleanup-forms` | Review forms for unused, broken, or duplicate entries and recommend consolidation |
| `cleanup-workflows` | Identify workflows that are off, broken, or redundant and recommend which to archive or fix |
| `cleanup-dashboards` | Audit dashboards for unused, duplicate, or outdated reports and recommend consolidation |
| `cleanup-deals` | Review deal pipeline hygiene — stale deals, missing properties, and stage violations |
| `cleanup-properties` | Find unused, duplicate, or poorly named contact/company/deal properties and recommend cleanup |
| `cleanup-lead-owners` | Audit lead owner assignments for imbalances, orphaned records, and routing issues |
