# Feature: Calendar Invites

> Part of Cerkl Broadcast. For product overview, see [broadcast.md](../broadcast.md).

**Available on:** Foundations+ and Omni AI

---

## What It Does

Calendar Invites send real Outlook and Google Calendar events to a targeted employee audience — not ICS attachments, not "add to calendar" links bolted onto an email. The event lands on the recipient's calendar, can be accepted or declined like any other meeting, and stays in sync with whatever the communicator does next in Broadcast. Sending works like a [email-blasts.md](email-blasts.md), but the delivery target is the calendar. Find it under **Blasts > Invites**, with separate tables for **Upcoming**, **Drafts**, **Past**, and **Canceled**.

## Why It Matters (vs. ICS Files)

Most internal comms tools — and every Gmail/Outlook workaround — attach an `.ics` file or paste a calendar link. Once sent, it's frozen. If the meeting moves or the event is canceled, communicators send a follow-up email and hope employees update their calendars manually.

Broadcast sends a live calendar event:

- **Updates overwrite the original.** Editing details and clicking **Send Update** rewrites the event in every invitee's calendar — no duplicates, no stale meeting rooms.
- **Cancellations actually cancel.** Canceling removes the event from invitee calendars and triggers a notification email. Type "CANCEL" to confirm — intentionally hard to do by accident.
- **Audience changes are real changes.** Adding invitees sends them the event; removing them clears it from their calendar. Removed invitees cannot be re-added to the same Invite.
- **Native accept/decline.** Invitees respond inside their own calendar client.

## Rules-Based Targeting

Invites use the same Audience Manager as blasts, so events go to dynamic segments — not static distribution lists. Target by **role, location, department, tenure**, or any combination of HRIS attributes Broadcast already syncs. Segments stay live: a new hire who matches the criteria after the Invite is sent can be added via **Sync New** without rebuilding the audience. Invites support unlimited segment-based invitees plus up to 50 individuals layered on top, batched in groups of 250.

## Send on Behalf of Leadership

The **Organizer Name** and **Organizer Email** fields control who the event appears to come from. A communicator can send a CEO all-hands or a CHRO benefits-enrollment session that lands on calendars under the executive's identity, not the comms team's. Best practice is to use a group or aliased mailbox, since accept/decline replies route to the Organizer address. Organizer Name and Email are the only fields locked after the first send — everything else remains editable.

## Building an Invite

Four sections, only two required:

| Section | Required? | Contents |
|---|---|---|
| **Invite Info** | Yes | Title, Start/End date and time, Time Zone, Organizer Name, Organizer Email |
| **Description** | Optional | Event details; 3,000 character limit (includes HTML); bold, italics, lists, hyperlinks |
| **Location** | Optional | Meeting Link, Physical Location, Access Details |
| **Audience** | Yes | Segments + individuals via the Audience Builder |

The **Title** does triple duty: subject line of the email, name of the event on the calendar, and — for Google Workspace recipients — potential trigger for a Flare banner.

## Google Workspace Flare Banners

Google Calendar auto-generates decorative banners on events whose titles contain certain keywords. There's no admin toggle to disable them — the behavior is baked into Google Calendar. Known triggers include **All Hands, Lunch, Happy Hour, Hackathon, Workshop, Training, Team Building, Retreat, Meeting, Breakfast, Dinner, Drinks**, and several "plan/vacation" phrasings. Banners aren't a defect — they often add useful flair to a town hall — but communicators should know they exist. Use **Send Sample** to confirm the visual treatment before a staff-wide send.

## Lifecycle Management

After sending, the Invite lives in the **Upcoming** table until its end date passes. From the ellipsis menu, communicators can **Edit Invite**, **Manage Audience**, **Duplicate**, or **Cancel** — and any update propagates to the calendar event itself, not a follow-up email asking employees to do the work.
