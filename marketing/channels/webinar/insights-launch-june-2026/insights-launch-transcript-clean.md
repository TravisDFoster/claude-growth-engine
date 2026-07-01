# Insights Launch — Cleaned Transcript

**Webinar:** Introducing Broadcast Insights: The Next Generation of Broadcast Analytics
**Date:** 2026-06-23
**Duration:** ~56 min of captured content (transcript begins 00:03:53; ~first 4 min of pre-roll uncaptioned)
**Audience:** Existing Cerkl Broadcast customers (internal product launch + enablement)

**Speakers (canonical names):**
- **Rachel** — Rachel Folz, Head of Product, Cerkl
- **Maddy** — Maddy Rieman, Head of Customer Success, Cerkl
- **Matt** — live demo driver (Aethos demo account)
- **Carly** — Customer Success, fielding/relaying Q&A in chat

**Source files:**
- `raw/insights-launch_transcript.cc.vtt` (Google-style auto-caption export; no speaker voice tags)
- Recordings (not ingested, in Downloads): `insights-launch_webinar_record_Shared-Screen.mp4`, `insights-launch_webinar_record_speaker-only.mp4`, `insights_webinar_recording_06-23-2026.mp4`
- No chat export (`.txt`) and no slide deck (`.pptx`) were available — so no chat is folded inline and no `deck-extract.md` was produced.

**Cleanup conventions applied:**
- Auto-caption name errors corrected: "Foles/Fles" → **Folz**; "Maddie" → **Maddy**; "ASO's/ATHOS/Athos/ethos" → **Aethos**; "circle.com/Circle" → **Cerkl/cerkl.com**; "DAWs/MAWs/Moz" → **DAUs/MAUs**.
- Speaker attribution is **inferred** from context (the `.vtt` has no voice tags). Strong anchors used: Rachel opens the guiding principles and owns product/engineering rationale ("as Rachel mentioned," "as Folz mentioned"); Maddy carries the CS lens and references Rachel in third person; Matt drives the demo; Carly relays Q&A. Genuinely ambiguous short turns are marked `[attribution uncertain]`.
- Captions merged into readable speaker turns; timecodes kept at every speaker switch and roughly every 1–2 minutes inside long stretches.
- `[unclear]` marks captions I could not resolve, with a best guess in italics.
- Section anchors are **topic-based**, not slide numbers — no deck was ingested, so slide references are unavailable.

---

## 1. Welcome & Guiding Principles
*[Topic: Experience, Visualization, Performance — and "this is a ground-up rebuild, not a reskin"]*

**Rachel** *(03:53)*: I'm excited. So I want to start with the guiding principles that brought us into this new Insights experience. The number one for me was **experience**. Insights 2 — legacy, the version you're seeing in your app today — really did serve its purpose and let you gain measurement, and it was great. But over time it got really slow and difficult to use. We kept adding reporting, and it got more complex to navigate.

**Rachel** *(04:21)*: So experience was really, really important this round. And it's important to note this Insights is **not a reskinning** — we rebuilt it from the ground up, end to end. The back end, the front end, everything is brand new. There are a lot of changes here, which we'll go over in detail, but as you move through it I hope you feel how much attention the engineering and product teams put into the experience.

**Rachel** *(04:56)*: **Visualization** was very important too. A lot of what I heard from you over the years is that you were having to do a lot of visualization yourselves — you don't have graphics people on your team, you don't necessarily have data analysts. So increasing the amount of out-of-the-box visualization was really important.

**Rachel** *(05:12)*: And last, but certainly not least, **performance**. The Insights tab has been available to you since Saturday — or late Friday night — and I hope you're seeing the difference in speed: how fast things come back when you send something, how events drip in over time. A major increase in overall performance was super important to us.

**Rachel** *(05:41)*: And as you go, hit that Q&A — Carly can answer you, or she might ask it live. So get those questions flowing, especially once I get to the demo.

**Carly** *(05:55)*: Absolutely. We love questions. We hear each other talk all day long, so we don't feel like you're interjecting at all — that's what this session is for.

---

## 2. Key Changes — Experience
*[Topic: drop-column tables · business-oriented date ranges · real-time speed · 18 months of data]*

**Maddy** *(06:05)*: Now that we've covered the guiding principles, let's talk about key changes and how they tie back. First, experience. You're going to see **drop-column tables** — the same pattern we've rolled out across the rest of the application. You can add columns and make it your own view, instead of seeing every column at once. It lets you focus on what matters most to you in your role.

**Maddy** *(06:52)*: **Business-oriented reporting.** One of my favorite things: we now include **today** in the default reporting ranges. Previously, to see a blast you sent this morning you'd have to change the reporting period to today. Now it's automatic. We also added more business-oriented ranges — last quarter, this quarter — so it fits how you speak internally.

**Rachel** *(07:27)*: And we're already seeing users use the business-oriented date ranges and custom dashboards — "this is the Q1 report, this is the Q2 report, compare it to last year" — and they're able to lay those down really quickly. It's wonderful to see in action.

**Maddy** *(07:46)*: It's the small things. And then a not-so-small thing — **real-time speed.** This thing is moving and shaking. We're crunching a lot of numbers on the back end, and as Rachel mentioned, it's a complete redo from the ground up. The way we structured it lets it load much faster.

**Maddy** *(08:05)*: If you're a customer with hundreds of thousands of subscribers or employees, you know what I'm talking about. It used to take almost 30 seconds to load at times — now you'll see a much quicker experience.

**Maddy** *(08:26)*: And lastly, **18 months of data**. This is tied to performance — a major reason we wanted to speed things up was changing "all-time" Insights to the previous 18 months. That gives you a year and a half. One note: as of January 2025… if we look 18 months back, we'll start rolling in the next week or so, and we'll talk about how you can export your data. So starting today you have 18 months historically in new Insights.

**Rachel** *(09:09)*: And the 18 months was purposeful — some of you run a July-to-July budget cycle, some December-to-December, some February-to-February. We wanted to make sure that no matter where you are in the year, you can get your prior year's data for whatever your fiscal or reporting year is. So 18 months was very intentional.

**Maddy** *(09:36)*: Absolutely.

---

## 3. Key Changes — Visualization
*[Topic: downloadable graphs · custom-dashboard descriptions · individual pulse-survey & acknowledgment results]*

**Maddy** *(09:38)*: Key changes for visualization. One of my new favorites — **downloadable graphs**. You set your reporting period and filters, and if you want to include a graph in a report for your boss or higher-ups, you simply download the file and drop it into a PowerPoint, Google Slides, whatever you use. Historically you'd take a quick screenshot; now it's an actual file.

**Maddy** *(10:13)*: **Context on custom dashboards.** You can now give a block a description. Historically it was just the component with not much context. Now you can communicate to colleagues what a block is reporting, or what they should be looking at the data for.

**Maddy** *(10:41)*: And lastly, **individual pulse-survey and acknowledgment results** — drilling into how people responded to those two components within a Blast. Historically it was aggregated from the top; now you can drill into how individuals respond to pulse surveys and acknowledgments.

**Rachel** *(11:09)*: It adds extensibility. Some of you wanted that individual response data — for asking if someone's coming to something, or if they have a question. If you need to link the response to the person, this will be very helpful. And if your organization can't support that, we have things to help — ask your CSM. But most of the feedback was "we'd really like the individual responses so we can cascade those comms."

**Maddy** *(11:41)*: Absolutely.

---

## 4. Performance & Data Validity
*[Topic: <1% margin of error · unsubscribed-user insights · deleted-content analytics · non-human filtering]*

**Rachel** *(11:43)*: Let's talk about performance and data validity. Broadly, our new Broadcast Insights is dealing with a **margin of error of 0.57 — sub-1% data validity**. At any time we're refreshing as you load a page; we load each block individually, so you get the data the second it comes down, and when you change a filter the data updates again.

**Rachel** *(12:02)*: Because there's so much data flowing, you may see a variance between two blocks or two pages — we use **materialized views** to bring you the speed. Think about everyone who's ever opened one of your emails in the last 18 months and everything they did. That's a lot of data, so those views help us get you to what matters quickly.

**Rachel** *(12:20)*: Also important: you can now get **unsubscribed-user insights**. For employee-comms or college-communications teams, you unsubscribe users for lots of reasons — leaving the org, leaving campus — but you still earned those analytics. Those people did things with the comms you created. In the prior version they'd just disappear — we talked about it like Thanos snapped and they were gone. In new Insights, their data is **anonymized**: you keep the credit for the click, open, view, session, impression, but they're anonymized. And you can filter them out in views.

**Rachel** *(13:11)*: Some of you also delete content. Before, it was scary — "please don't delete this, you'll lose the insights." We're not doing that anymore. No matter what state content is in, you can now see any analytics gathered over it.

**Rachel** *(13:32)*: One of the more surprising things as I've looked at Insights is how much **reach** your content has — you're getting many more impressions, sessions, and clicks now that we're using a more event-driven architecture that counts things based on something having happened. That's a big difference, and you'll see it in your numbers.

**Rachel** *(13:48)*: Additionally, we have **clustering and filtering logic for non-human interactions**. The world is complex — between organizational IT policies and personal policies, there are a lot of filters and systems between your message and your audience. We do our best to consistently filter out non-human interactions so your analytics are real.

**Maddy** *(14:36)*: And I'll mention — those of you who've been with Cerkl from the beginning would have worked with my team to assess whether we can bypass automatic opens or clicks that IT instills, based on the dedicated IP we provide you. Those still stand. This is **in addition** to that, and it makes your analytics more accurate. You may have already heard us have this conversation during implementation — this is an add-on to it.

---

## 5. Event-Driven Architecture & the New CTR Formula
*[Topic: event-driven vs. publish-date reporting · click-through-rate calculation change]*

**Rachel** *(15:26)*: In old Broadcast Insights — Legacy — everything was driven by the date it was sent or published. That was your range. So when you looked at content you had to encapsulate the publish date in your date range to capture it, which gave you a pretty narrow slice.

**Rachel** *(15:46)*: New Broadcast Insights is **event-driven**. An "event" is a broad technical term — an open, a click, an impression, a session, a deliver. If an asset or a person has an event, they're included. So your reports are driven more by what people *do* than by what communicators did — the publish date doesn't really factor in. If I saw it in my channel, you'll now see impressions on it. It's a different paradigm, and you're getting the most accurate numbers.

**Rachel** *(16:13)*: One surprising thing early on was how many older messages staff are opening — emails from months ago. People keep their newsletters, search for a story, find it, and click. It's interesting how people manage their content, and you'll see that as you dig in.

**Rachel** *(16:52)*: We also updated our **click-through-rate formula** to be more in line with industry standard: **clicks divided by delivers**, as opposed to Legacy, which divided by opens. So there's a difference in the math.

**Rachel** *(17:10)*: Any questions so far, Carly? Are we good to move to the live demo?

**Carly** *(17:16)*: Let's roll the live demo. I have one question I'm answering that I want to make sure you show, but we'll cross that bridge when we get there.

**Matt** *(17:28–17:30)*: Absolutely, let's do it. [attribution uncertain on the hand-off line "Matt, am I good to go?"]

---

## 6. Live Demo — Overview Pages
*[Topic: blast overview & content overview — the "10,000-foot" view]*

**Matt** *(17:30)*: For those who've chatted with me before, you're familiar with my **Aethos** demo — my pretend financial-services company, where I do most of my demo work. Our designer, Allison, made a beautiful brand for it, and it has an org chart. This is exactly what you should see on your side. This account has content in it, so if you're Foundations or Essentials you won't have content — but I'll cover it for everybody.

**Matt** *(18:04)*: Let's start with the **overview**. There's a blast overview and a content overview. This is for the person flying over at 10,000 feet, or a quick check-in — "I just want to see what's going on," not the machinations of an individual email. A common block is **blast key metrics** — the big three numbers most important for that asset type. Then **blast metrics over time**: hover to see delivered, total opens, total clicks.

**Matt** *(18:41)*: Then a **blast activity log** — these are all dropdowns. You have a lot of traffic; you send hundreds or thousands of blasts a month. You want to see when things go out, then flip the layer and see when they actually opened or clicked. That can make a big difference in strategy. Here I had three delivers in the period, but opens spread out — so should I send Tuesday at 2pm or Tuesday at 9am? Some strategy to play with.

**Matt** *(19:32)*: **Last sent** is just a count of assets — how many blasts were sent — and we have **highest and lowest open-rate blast**. You'll see something similar on the content side. A big thing for me in Insights 3: you're never asked to jump a nav item; you can always get back to where you were. If I dig into a particular blast, I'll open it in a new tab so you don't lose your place.

**Matt** *(20:03)*: All filters are **page-level**. Some pages focus on people, others on assets — content, blasts, and the like. We've split apart the different kinds of segments. **Targeted segments** are what you chose in the audience builder when you made the blast. **Segments** are the lists you made, to cut down to just those people. In old Insights those concepts were muddy.

**Matt** *(20:45)*: You can filter by campaign, sender profile, creator, and categories. And this — the **date-range selector** — is my future baby; I love it. These business-oriented ranges are what Maddy mentioned. "Today" and "last 28 days" include today, and you can see the actual dates, so "last year" isn't ambiguous. You can set a custom range going back 18 months and apply it easily. That's the overview page.

---

## 7. Live Demo — Metrics & Per-Blast Drill-Down
*[Topic: metrics tables · per-blast key metrics, audience, links, pulse results · retargeting]*

**Matt** *(20:28 [should read 21:28])*: Let's move into metrics — Maddy, if I miss anything, jump in.

**Maddy** *(21:35)*: Metrics is similar to Legacy, but new and improved — a drop-column table with many column options.

**Maddy** *(21:58)*: And quick note: when you edit a table as the logged-in user — we just got a question about this, "I'm pulling reports weekly" — any of these blocks in table format will **uphold the columns you added** for you as that user.

**Matt** *(22:29)*: I can't recall which way we went on one detail — there was debate because there's so much data — so I'll follow up. [attribution uncertain] Lots of columns to choose from; when possible they can be sorted and filtered. If I dig into one, you get this attractive view of the blast: **blast key metrics**, and the **info "i"** tells you exactly what we're measuring and what you might use it for. There's an **audience tab** (everybody, and how they interacted) and a **links tab** with every link in the blast.

**Matt** *(23:13)*: I had a link to a Kelly Clarkson video because I thought it'd be funny — and I can click any link to see specifically who clicked it. Looks like me, Carly, and Jordan clicked this one. I can **export** the table specific to that link. And then **performance**.

**Matt** *(23:33)*: This **pulse-survey result** shows what I'm measuring, and you can see individuals and their responses, paginate through them, and search by subscriber. In one case I said three, in another I said five. You can **filter by response**, which is powerful for an event-registration case — "are you going to do this, do you want to volunteer?" — to get the list of people who said yes, or who didn't respond.

**Rachel** *(24:09)*: Which is probably helpful for other things too — the ability to **retarget** that specific blast: "you didn't take action here, let's make sure you do."

**Matt** *(24:20)*: **Blast unique opens** — this is one of those downloads. Anywhere you see a visualization like this, you can download it and drop it in a Teams message, a slide deck, a report. Hover to see specifics — this is the clicks, and these are not-clicks. You also get a **blast activity log** showing the seven days after send — when they actually opened, when they clicked.

**Matt** *(25:14)*: Peek the blast with the eyeball, and you can filter results by **segment** and by **audience status** — subscribed or unsubscribed. If I had unsubscribed users on this, I could cut them out or focus on them.

---

## 8. Live Demo — Audience View
*[Topic: people-focused view · per-person performance vs. organization average]*

**Matt** *(25:38)*: Now the **audience view** — this is about people. I can filter by segment to get the specific list of people I want, edit the table, and add columns: opens, bounces, spam reports. I'll pick on Carly — this is Carly's little blast report: how many blasts she's getting, opens, unique clicks, and the specific blasts she received.

**Matt** *(26:24)*: You also get a **performance review** — not that kind. If Carly says "I'm not getting them," I can say, "Carly, your blasts delivered on these days, your open rate is just below average, your click-through rate is a little above average" — because that's the organization average. So I can be specific at the asset level and the performance level, and download and share that report with her.

**Maddy** *(27:02)*: I love comparing an individual against your organization's average for open and click rate. In Legacy we had ways to compare — for News Digest, orgs of the same size or industry, or general averages — but this tells you, based on *your* org's performance, how this individual engages with your blast content. It keeps it relatable to your organization.

**Rachel** *(27:45)*: And those organizational averages are calculated using your organization's data from the last 18 months — so any comparison is *your* data.

**Maddy** *(27:58)*: I have not seen that dropdown — how have I missed that? I like it a lot.

**Matt** *(28:06)*: There's a lot to see. I believe Christie and Sam collaborated to make that little dot possible.

**Carly** *(28:15)*: Love it — I love learning something new on this webinar.

---

## 9. Live Demo — Content Overview & Metrics
*[Topic: content across channels · channel color scale · event-driven reach]*

**Matt** *(28:15)*: Let's move to **content**. Overviews are the 10,000-foot view. As a longtime content user and cheerleader, I love this — you get visibility that was more obscured before. Here we're looking at all content across channels. You'll see a **color scale**: News Digest is blue, mobile is green, intranet is teal — you'll see it everywhere, including Content Archive (the peak). So you build associations.

**Matt** *(28:48)*: We have **content metrics by channel** — total sessions, impressions, or clicks. A session is when someone starts engaging — they opened something, fired up the app, went to the content archive — and then they impress on content. Everything served gets an impression, an opportunity for engagement, and then there's the click. It's a funnel.

**Matt** *(29:23)*: **Content metrics over time**, same cuts. Note the clearer language: **total** means everything, not deduped; **unique** means just the first time. Content is about totals because people usually see content multiple times. This stacked column lets you hover sections — looks like 20 sessions came from content block, three from Archive, 29 from News Digest. Also easy to download — so "where are people seeing this?" has two answers: by time, or generally over the last 28 days / last year.

**Matt** *(30:22)*: **Content click activity logs** are powerful for complex multi-shift orgs — see when they're clicking, filtered to a channel like News Digest. Looks like it mounts up on Tuesdays at 9 and 2. Then **active users by channel** (a simple bar graph) and **most/least popular by click rate** comparing stories. I can filter any of it — let's spin up a campaign… In the "Aethos News" campaign for the last 28 days, most content metrics came from News Digest with a little Archive, and my most/least popular changed too. Filters are a powerful way to slice it — then download and build a nice slide deck.

**Maddy** *(31:42)*: Or make a custom dashboard.

**Matt** *(31:44)*: **Content metrics** — tables about assets, focused on content, just like Blast. Lots of columns; a few new ones: push alerts, campaigns, priority, source. Clicking a story takes you deeper — who impressed on it or clicked it, and the story's performance. "You published that story — where did people see it?" Yes, I can tell you: mostly the content block, then some News Digests. Here's the activity — it was out, I pushed it in the content block, then more sessions came in. You can follow the story with this chart, which you can download.

**Maddy** *(33:04)*: Quick note on the metrics page about **event-driven** reporting vs. published-date. Right now we're looking at the last 28 days — and I promise Rachel Folz did not publish 90 stories in this Aethos account in the last 28 days. This is a change for you all: you now get events on any content that's been out across your channels in the window. We're seeing people go back to historic News Digests or blasts sent weeks or months ago. Previously you lost those metrics; now you can see them — an important data story to keep in your back pocket.

**Rachel** *(34:50)*: Good example: in Legacy, that first story with my highest audience reach of 16 wouldn't have been on this list, because it wasn't published in the last 28 days. But since it had a reach of 16 and 69 impressions via a content block, there it is. So I get a lot more value out of my content — if you're a content org, you'd be excited, because the reach is much bigger. You might have secret hits with a big life beyond publish that tell you what your audience wants more of.

---

## 10. Live Demo — Channels
*[Topic: channels gateway · per-channel key metrics · News Digest specifics]*

**Matt** *(35:48 [content audience])*: Speaking of audience — this is a change. If someone doesn't have a session or impression on content in my 28 days, they won't be listed. That doesn't mean they unsubscribed — just that they haven't interacted with content in the window. Widen the range and you'll catch more people, so check that first. I'll pick on Carly again — six sessions, 23 total impressions — and I can see which stories she impressed on and when ("you saw it at noon on June 22nd, in the News Digest").

**Maddy** *(37:30)*: And this mirrors the blast-audience experience — similar graphs. I like the repetitive nature: I learn it here and get it similarly over there.

**Matt** *(37:37)*: As you get more advanced you'll notice the page title is always shown, the thing you're focused on is in the slide, and the key metrics are the big three. It's all very mathy and organized. I had a great time making this flowchart — well, a series of Post-its I loosely connected. Maria is the flowchart queen. Let's talk about **channels**.

**Matt** *(38:11)*: In Legacy, depending on your package, you waded through a lot of navigation for simple stuff. I wanted a **gateway** — for first-timers to ask "what channels are we using?" The content channels page is a quick gateway: "we don't use intranet, Teams, or mobile here, but we have sessions on Blast content block, Content Archive, and News Digests." I'll go into **Content Archive** — same pattern: key metrics, **most active users** (a very requested feature — know who's using it), broad activity trends by day, and an activity log with impressions and clicks. You can export active users for use wherever you need.

**Matt** *(39:34)*: All channels show sessions, impressions, and clicks — the outlier is **News Digest**, because it's email. You get email-driven metrics: delivers, open rates, click-through rate. See News Digest over time — delivered, opened, clicked — easy to download, plus the activity log. My default send is noon, and opens spread out a bit from there.

**Matt** *(40:22)*: You can also see the **number of News Digests delivered**, the **percent personalized** (only a small fraction of mine have gone through the personalization process to select categories and interests), and the **delivery-format breakdown** — traditional, headlines-plus, headlines-only. Note that's **locked to today** — current Broadcast data, not date-rangeable. Then **frequency** (what everyone's set at) and the **days-of-week breakdown**. Lots to diagnose your digest.

**Maddy** *(41:16)*: A much better view than Legacy's static News Digest overview. The content channels give you the same components for each channel. And we're moving away from DAUs and MAUs — daily/monthly active users — toward more complete data stories.

**Matt** *(41:53)*: You'll still know your users — but in Legacy we were so focused on DAUs and MAUs. This depicts more graphically where you're at and how people engage across channels.

---

## 11. Live Demo — Categories
*[Topic: category performance · per-person interest levels · parity with audience builder]*

**Matt** *(42:15)*: Last on the main nav before dashboards: **categories**. For content folks, categories are a big part of the personalization experience. I love a sort — I'm a monster fan of a sort. You can see percent of the audience and the **category source**: is it an organization category you selected, or one that came along for the ride? You can filter by category source and by segment — so if you're curious what the Cincinnati office thinks, filter by that segment. (Again, pulling apart what you targeted vs. the lists you make — segments vs. targeted segments.)

**Matt** *(43:02)*: If I want to see who's interested in **employee experience**, I get a list, with each person's interest averaged — Allison has average interest, Chris below average, Maddy above average. So you can see who's interested in things — helpful for volunteer opportunities, sign-ups for a class, building lists like "people very interested in cybersecurity" or "AI education." As the communicator, you're a new data store of who's actually interested. And this list should **identically mirror** what you see in the Blast target-audience builder if you target by categories — those lists are identical now.

**Maddy** *(44:14)*: Love it. Real quick — I see lots of Q&A coming through, which is fantastic. If we don't get to your question live or in a typed response, we'll **follow up with you independently**. They're not going unseen.

**Carly** *(44:43)*: And before dashboards — I saw the **export** button under categories, and I wanted to walk through it, because it's a little different from Legacy.

**Matt** *(44:58)*: For now, exports work like they do on Audience — you export and get a **local file**. I anticipate this moving back toward the Legacy model, because you'll have large, advanced data sets and won't want to wait for us to package it. So eventually it'll likely be an exports page with downloads you can reference and clear out. For now it's a local file download, and those of you with larger audiences should have a bit more luck downloading than in the past.

---

## 12. Live Demo — Custom Dashboards
*[Topic: building dashboards · governance/sharing · duplicating blocks · relative vs. locked date ranges]*

**Matt** *(45:44)*: Maddy, any questions before dashboards?

**Maddy** *(45:57)*: A lot of questions that dashboards will answer — showing people how to set filters so they can come back and see, at a glance, the reports they always need to reference or pull. Lots of interest in filters, whether campaigns or segments on the blocks.

**Carly** *(46:23)*: Hop into dashboards, then maybe we'll touch on some other things.

**Matt** *(46:30)*: I'll name my dashboard "All About Aethos News." In Legacy dashboards you could only add a **title** — now you can add a **description**. It's a blank canvas, full of possibilities. A couple of things first: **manage access** is brought into our governance system — it starts belonging to me and the admins, and I can expand it to be global or share it with specific team members. It should feel like governance everywhere else in Broadcast.

**Matt** *(47:11)*: Another favorite: everything's **visual**. You can scroll easily and recognize the look of the report before you add it. You can filter — reports can be split by blast or content if your package includes content (otherwise just blast) — and you can search. So I search "key metrics" and get all the key-metrics reports.

**Matt** *(48:10)*: Let's add a **Blast key metrics** report — default period is last 28 days. If I choose **this quarter**, that's Q2 right now, through end of June. If I choose "this quarter," when it flips to next quarter on July 1st, "this quarter" becomes the July quarter — so those are **relative**. If I'm doing a last-quarter report, that's perfect. But if it must forever be the Q1 2026 report, I'd set a **custom range** — January 1 through March 31 — so it's **locked**.

**Matt** *(49:32)*: I'll do "this year," add a block description, filter by targeted segments, campaigns, sender profile, and add to my dashboard. By default a block is 100% width; you can shrink it to 50%, and drag to resize height. I can **duplicate** a block and change it to "last quarter" — duplicated and added — for a month-over-month layout.

**Matt** *(50:33)*: The little chart preview represents what you'll get when the dashboard arrives.

**Matt** *(50:56 [Maddy])*: A lot of customers use over-time reporting — they want one dashboard for month-over-month. Being able to duplicate and make quick date/filter changes, all in one place, means you're not recreating the wheel every month. One custom dashboard upholds it for you. [attribution: Maddy]

**Matt** *(51:32)*: You'll also see **reference lists** — basically a micro table. Any time you need a list of items, that's a reference list. This blast-metrics reference list has 13 blasts; you can change pagination, stretch it to show more (there may be a max height), and clicking an item opens a **new tab** so you don't go 16 layers deep and lose your place. I can lock a dashboard to a permanent range — 2025, January 1 through December 31, apply — and it's locked to that range permanently.

**Matt** *(52:31)*: Carly, did that handle it, or something more specific?

**Carly** *(52:38)*: That works. And no one asked my opinion, but I love this — being able to identify our high-priority segments (regions or business lines we want to watch), filter to them, and put them side by side to check open rates on those blasts or digests at a glance. For the digest block you can put any segment in your org on it, and you can do the same with blast audience. The old version made it hard to see what you were filtered to, and you couldn't put a description on it to make it clear to your dashboard's consumers why it mattered.

**Matt** *(53:36)*: Any edit you want — edit, duplicate, delete, or the quick button — you can do here. Editing any of the parts is a nice experience, if I can be biased.

**Maddy** *(53:51)*: You can. And Carly, we're always interested in your opinion — you work so closely with a lot of our largest customers, so hearing how you phrase this in your meetings is helpful.

---

## 13. Q&A — Migrating from Legacy Insights
*[Topic: live-answered question on dashboard migration · Legacy availability timeline]*

**Maddy** *(54:07)*: A question I'll answer live: "Can we duplicate/copy dashboards currently in Legacy Insights into new Insights, or do they need to be rebuilt?" Bad news and good news. Since new Insights is completely rebuilt from the ground up — we rebuilt the car, the engine, everything — **they'll need to be recreated/rebuilt**. But that's why you have your dedicated Customer Success team to help, and it opens up a real opportunity to reassess how you look at the data, with all the new components, blocks, and filtering.

**Maddy** *(54:59)*: We'll uphold Legacy Insights for a period of time — I'll let Folz speak to that — but please reach out to your dedicated CS team. We want these conversations so we can learn how you're looking at the new data and reporting it to leadership.

**Rachel** *(55:36)*: Yes — **Legacy Insights should be available through the end of the year**, but I'd advise you to begin moving over: get the data you need out, and ask CS any questions. It's an incredible opportunity for all of us to learn. We didn't do everything perfectly, but we put our heart and soul into a much better experience, and I hope it helps you tell your data story even better.

---

## 14. Summer Roadmap & Looking Ahead
*[Topic: summer themes (invites, content, permissions/privacy, customization) · already-shipped items · AI direction]*

**Rachel** *(56:05)*: It's done — congratulations, you have it. Now let's talk about this summer. We're entering a new quarter, and the **summer themes are about customer experience** for customers like you. We'll spend time on interactions, experiences, and shortcomings we think we can improve to make your work in Broadcast easier and more enjoyable. A few themes:

- **Enhancing invites** — invites came out [last year]; they've been very popular. You love getting people in the room. We're looking to enhance it.
- **Content experience** — it could use some love.
- **Permissions and privacy** — continue to be very important to you and your security teams; we want you to set up your instance to feel secure.
- **Customization** — your brand matters; we want more micro places where you can inject your brand.

**Rachel** *(57:43)*: Even amid finishing Insights, we did a few things toward these goals: a new **15-minute pre-reminder** for Outlook events (an invites enhancement); you can now **export your blast tables** for usage analysis (who's using it, what we're sending — not analytics like Insights); we're accepting and optimizing **larger images**; and you'll notice more **logical sorts** on tables across Broadcast — click a heading and it sorts what you meant, instead of clicking twice. More of that, on a bigger scale, is the summer's focus.

**Maddy** *(58:30)*: And looking ahead — we're actively gathering customer feedback to shape future investments, which will in some form include **AI**. We'll keep our focus on solving real customer challenges and applying AI where it makes the biggest impact to your daily work. More to come.

---

## 15. Housekeeping & Wrap-Up
*[Topic: recording follow-up · new help desk articles · chat support]*

**Maddy** *(59:01)*: A few housekeeping notes. We'll send a **follow-up after this webinar** — even people who registered and couldn't attend will get the recording, so reassure any colleagues who couldn't join. I'll also drop a link to our **updated help desk** — we have **almost 30 brand-new articles** on the new Insights experience, so please use those.

**Maddy** *(59:35)*: And use the **chat** — Rachel Folz, over her 10 years, is one of the quickest to read through them; it's a great way for us to hear feedback directly. Use the chat icon in the bottom-right of every cerkl.com page. Our team is here to help — we want to get you acclimated to new Insights as quickly as possible, and we hope you like it as much as we do. It's been a long time coming and a lot of hard work.

**Rachel** *(01:00:16)*: Thank you all so much. I hope I hear you in chat soon.

**Maddy** *(01:00:21)*: Thank you, everybody.

---

## Cleanup notes — open questions for review

Resolve these against the recording before downstream content quotes the transcript directly.

**Speaker attribution (inferred — no voice tags in the `.vtt`):**
- The whole transcript's speaker labels are inferred from context. The Rachel ↔ Maddy hand-offs in **Sections 2–5** are the least certain — both narrate fluidly and trade short "Absolutely"/"Yeah" interjections. The anchors I trusted: Rachel opens the principles and owns product/engineering rationale; Maddy carries CS framing and refers to "Rachel" / "Folz" in third person.
- *(17:28)* The hand-off line captioned "Matt, am I good to go for you?" is ambiguous — could be a host cueing Matt, or Matt himself. Demo attributed to Matt from 17:30.
- *(50:56)* The "month-over-month / don't recreate the wheel" turn is attributed to **Maddy** interjecting during Matt's demo, but the caption flow is muddy here.
- *(22:29)* "I can't recall which way we went… I'll follow up" — attributed to Matt; could be Rachel. He commits to a **follow-up** on an unresolved table-behavior question — worth confirming what was promised.

**Name / term corrections made (confirm spellings):**
- **Rachel Folz** and **Maddy Rieman** — pulled from the `rachel-maddy-july-2026` brief (same presenters). Captions rendered "Foles/Fles" and "Maddie."
- **Aethos** — the demo account/company (captioned "ASO's," "ATHOS," "Athos," and once "ethos" in "Aethos News campaign"). Confirm the exact brand spelling.
- *(34:34)* "Ms. Toys Han" — `[unclear]`; from context (immediately followed by "Ms. Carly has 6 sessions") this is **Carly**. Confirm.
- Other names spoken, spellings unverified: **Allison** (designer), **Maria** (flowchart), **Christie** and **Sam** (built the comparison "dot"), **Jordan** and **Chris** (demo-account people).
- *(37:58)* "I know you and your **flipgards**" — `[unclear — likely "flip charts" or "flip cards"]`.

**Data points to verify before external use:**
- Margin of error **0.57 / "sub-1%"** *(11:43)* — confirm exact figure and how it's framed publicly.
- New **CTR = clicks ÷ delivers** (vs. Legacy clicks ÷ opens) *(16:52)*.
- **18 months** of history; **Legacy available through end of year** *(55:36)*; **~30 new help desk articles** *(59:35)* — confirm the help desk URL.
- Invites **15-minute pre-reminder** for Outlook *(57:43)*.

**Not produced (inputs absent):**
- No `insights-launch-deck-extract.md` — no `.pptx` was available. Section anchors are topic-based, not slide numbers.
- No chat folded inline — no chat `.txt` export was available.
