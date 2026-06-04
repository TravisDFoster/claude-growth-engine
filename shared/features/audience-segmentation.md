# Feature: Dynamic Audience Sync & Segmentation

> Part of Cerkl Broadcast. For product overview, see [broadcast.md](../broadcast.md).

**Available on:** All plans

---

## How It Works

Audience Manager is where the org actually lives inside Broadcast. Communicators build rules-based segments once — by department, location, role, hire date, time zone, or any employee attribute — and Broadcast keeps them current automatically as employee data changes. No IT ticket per send. Manual CSV uploads handle committees, contractors, or one-off cohorts.

Three audience views sit side by side: **Subscribers** (active recipients), **Unsubscribes** (history of opt-outs), and **Bounced** (delivery failures). All three support search, sort, filter, column customization, and CSV export — any slice of the org is one filter away from a downloadable list.

## HRIS & Identity Integration

Broadcast syncs with every major HRIS and identity system: Workday, SAP, PeopleSoft, ADP, Paycor, and Active Directory. Multiple sources can run simultaneously when payroll, HRIS, and IdP each own different attributes. Setup uses a no-code Import Mapping Utility — no custom code, no ongoing IT involvement after initial mapping. The interface surfaces upload status, record counts, conflict flags, and processing history per file.

For **email-less employees** (frontline, retail, manufacturing floor), an SFTP Multi-File Integration adds them by Unique ID instead of email. They appear in the Audience table with a "No Email Provided" status, default to a **Mobile Only** opt-in, and log into the Broadcast Mobile app using a workspace name, Unique ID, and optional security-question answers.

## Segments: Manual vs. Dynamic

**Dynamic Segments** are rules-based on subscriber attributes and auto-update as data changes — ideal for department, role, location, tenure, or time zone (anything HRIS-driven). Rules use **Any vs. All** logic (OR vs. AND) with nested rule sets for compound targeting, and support *Is*, *Is Not*, *Is Blank*, and *Is Not Blank* operators against any enabled attribute. Once a subscriber's attributes change in the source system, they enter or exit dynamic segments automatically on the next sync — no list scrubbing.

**Manual Segments** are free-form lists built by CSV upload or by adding subscribers individually. They persist until edited — ideal for committees, special projects, one-off cohorts, or exclusion lists.

**Time-zone segments** work whenever time zone is included in the integration. Combined with scheduled blasts, this sends the same message at, say, 8:00 AM local time across every region without scheduling separate sends.

The Segments table is divided into four permission views — **My Segments**, **Shared With Me**, **Global**, and **All** — with configurable columns for audience count, bounce count, creator, access level, and last-edited date. Bulk actions cover duplicate, delete, and access-level changes.

## Attributes & Custom Data

Three layers of subscriber data feed segmentation and personalization:

- **Default attributes** — name, email, opt-in status, date subscribed, date personalized, privacy. Always available.
- **Integration attributes** — anything mapped from HRIS during setup (department, manager, location, hire date, employee ID).
- **Manual Attributes** — up to 50 free-form fields per subscriber, 255 characters each. For temporary data not held in the people system: event RSVPs, training-cohort flags, exclusion tags.

Manual Attributes upload via **Audience > Import List** with headers `Manual 1` through `Manual 50`. Admins assign each one a display name in **Settings > Attributes** and toggle whether it's available as an audience-table column, a Dynamic Segment rule, or a personalization field in blasts. Per-attribute fallbacks for missing values are set in Blast Controls. The legacy "Custom Fields" feature is deprecated — existing data is preserved, but new manual imports use Manual Attributes.

## Imports, Conflicts & Bulk Actions

**Audience > Import List** handles CSV/TXT (UTF-8) uploads for new subscribers, attribute updates, or appending to manual segments. The first column must be Email; column headers must match accepted attribute fields. Unmatched headers flag as Ineligible and skip on continue.

During import, communicators choose opt-in status for the upload, segments to append, and conflict management — **Merge** (fills blanks only) or **Overwrite** (replaces existing values; requires typing `OVERWRITE` to confirm). A persistent **History & Queue panel** shows the 100 most recent uploads org-wide with importer, size, segments targeted, and merge/overwrite choice. After processing, the importer gets a verification email with row-level results.

Bulk actions on Subscribers: Update Segments, Set Privacy, Set Opt-In Status (up to 1,000 per page for bulk unsubscribe). Bounced supports bulk Delete and Clear Bounce. Segments support bulk Update Access Level and Delete.

## Compliance & Privacy

Broadcast is GDPR-aligned at the platform level (SOC 2 Type II, AES-256 at rest, TLS 1.2+ in transit). The audience-side controls extend that to per-subscriber behavior. Every subscriber carries a **privacy level** that governs how much data is collected:

| Privacy Level | Behavior |
|---|---|
| Personalize my experience (default) | Full personalization on explicit + implicit interests; insights tracked |
| Personalize but do not learn about me | Insights tracked; no implicit-interest profile building |
| Personalize but do not report on my activity | Personalization runs; no insights recorded |
| Do not personalize | No personalization; no insights tracked |

Admins set the **default privacy level** for non-personalized subscribers in **Audience > Controls > GDPR Settings**. Changing the org-wide default requires confirming consent on behalf of subscribers; the same consent gate appears on individual and bulk privacy edits.

**Restrict Domains** locks the audience to a whitelist of approved email domains — useful for internal-only orgs that want to prevent stray external addresses entering via import or integration. Foundations plans support a single domain with Restrict Domains permanently on. Changing a domain from Allow to Remove unsubscribes every existing subscriber on that domain at save. Sample blasts are exempt.

## Permissions & Segment Access

Segments default to **Restricted** on creation — visible to the creator and all Administrators only. Two access modes:

- **Global** — any team member with Manage Audience permission can view, duplicate, edit, and use the segment when sending blasts.
- **Restricted** — limited to Administrators, the creator, and explicitly named team members added under "Shared With."

This is the core mechanism for **decentralized team management**: an HR comms lead owns HR segments, an IT lead owns IT segments, regional leads own regional segments — without anyone seeing or accidentally targeting the others.

**Audience Management mode** is set globally in Audience Controls. **Manual and Integration** lets the team add/remove subscribers alongside the integration; **Integration Exclusive** locks the audience so only the integration can change it (common in tightly-governed orgs). Managed Child instances (sub-orgs whose audience is owned by a parent) can update existing subscribers and segments but cannot add new members directly.

## Opt-in Status, Unsubscribes & Bounces

Five opt-in statuses govern delivery: **Email Blasts & News Digests**, **News Digests Only**, **Email Blasts Only**, **Mobile Only** (for email-less employees), and **Unsubscribe**. Status can be set per subscriber, in bulk, at import time, or via integration. The **Allow Unsubscribe** control determines whether recipients see an unsubscribe link — disabling it is only appropriate for fully internal orgs (CAN-SPAM Act of 2003 applies to anything external).

The Unsubscribes table preserves email and unsubscribe date for the record; attributes, insights, and other data are permanently removed. The **Unsubscribed By** column tracks who removed each subscriber — admin name, "End User," "Integration," or "Deleted Team Member." **End-user unsubscribes cannot be re-subscribed** (CAN-SPAM); team-member and integration unsubscribes can be added back via CSV or Add Subscriber.

The Bounced table captures emails that failed delivery with a reason from the recipient server (nonexistent mailboxes, full mailboxes, outages, IT-side blocks). Broadcast stops sending to bounced addresses to protect sender reputation. Each record supports **Clear Bounce** (return to active — useful for temporary outages or mailboxes not yet provisioned), **View/Edit** (resolve to a corrected address), and **Delete** (cautious with integrations; the next sync may re-add and re-bounce). Campaign-level bounces also surface in [analytics-insights.md](analytics-insights.md) for ongoing list-health monitoring.

## Why This Differentiates

Most email tools manage external contact lists that someone maintains by hand. Broadcast pulls live org data — so segments reflect the actual org structure at send time, with no one reconciling distribution lists before every campaign. The combination of HRIS-driven dynamic segments, restricted-by-default permissions, manual-attribute escape hatches, and CAN-SPAM-aware opt-in handling is what makes the audience layer usable for both small comms teams and enterprises with hundreds of communicators sharing one instance.

See [email-blasts.md](email-blasts.md) for how segments target sends, and [analytics-insights.md](analytics-insights.md) for how segment-level performance is measured.
