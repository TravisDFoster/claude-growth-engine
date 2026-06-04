# Cerkl Broadcast vs. Microsoft Viva Amplify

> Account-specific comparison handout for TMNAS leadership — active conversation.
> Reader: TMNAS leadership + tech lead. Tech lead asked why not just use the Viva tools "included in our Microsoft license." Leadership is wary of anything that feels like social media. They have no comms metrics today and reacted strongly to Cerkl Insights.
> Goal: informative comparison, no CTA. Defeat the "it's already in our license" assumption and lead with measurement.
> Slug: cerkl-vs-viva-amplify | Date: 2026-05-29
> Recipe: Comparison (no CTA): hero-compact → number-row.cols-3 → feature-grid.cols-2 → callout-card → footer
>
> Fact basis (verified 2026-05-29 against Microsoft Learn / Microsoft Support):
> - Amplify is NOT in base M365; requires paid Viva Suite (~$12/user/mo) or Employee Communications & Communities add-on (~$2/user/mo).
> - Amplify reporting "only stores the count and not the user information" (no per-person read receipts); "unlicensed user signals may not be accurately reported."
> - Amplify publishes to Outlook, Teams, SharePoint; one-to-many with audience targeting (no per-employee personalization).
> Deliberately NOT leaning on AI/MyNews personalization — reader finds AI/"social" framing off-putting. Wedge = measurement, reliable targeted delivery, reach, cost.
>
> **Remediation applied during render (2026-05-29):** verify gate flagged a 185px footer overrun. Resolved with (1) Tier-A `--body-size:15px` on the .page div; (2) removed the hero subtitle line (hero-compact budget is "no body" — the lead line under the hero was the same overflow cause documented on allcore-msp-premeeting); (3) trimmed each feature-grid.cols-2 cell from ~65–80 words to ~50–55 words (and dropped the Flagger Force stat from the "Reaching everyone" cell). Second pass: PASS, single page. Copy below reflects the shipped PDF.

---

<!-- component: hero-compact (single Cerkl Broadcast lockup, left; H1 below divider) -->
<!-- Render as:
     <div class="hero-compact">
       <span class="wordmark-ph"><img src="../../../branding-assets/Broadcast/Cerkl Broadcast Horizontal Lockup/Medium (160px)/cerkl_broadcast_horizontal_lockup_full_color_medium.png" alt="Cerkl Broadcast"></span>
     </div>
     <h1 style="font-size:24px; color:var(--accent-dark); margin:14px 0 0; letter-spacing:-0.01em;">Cerkl Broadcast vs. Microsoft Viva Amplify</h1>
-->
<!-- Subtitle removed during remediation (hero-compact = no body). -->

**Cerkl Broadcast wordmark (left, 160px medium):** `../../../branding-assets/Broadcast/Cerkl Broadcast Horizontal Lockup/Medium (160px)/cerkl_broadcast_horizontal_lockup_full_color_medium.png`

# Cerkl Broadcast vs. Microsoft Viva Amplify

<!-- component: number-row.cols-3 -->
<!-- Each cell: .num-cell with .big (stat), .lbl (label ≤8 words), .sub (≤14 words). Lead with the cost + measurement contrast that resonates for this account. -->

**Cell 1 — variant: ruby**
- **big:** $2–12
- **lbl:** Per user / month for the Viva add-on
- **sub:** Amplify isn't in base Microsoft 365 — it needs the paid Viva Suite or Comms add-on.

**Cell 2 — variant: default (cobalt)**
- **big:** 0
- **lbl:** Per-person read receipts in Amplify
- **sub:** Microsoft: Amplify "stores the count, not the user." You never see who actually read it.

**Cell 3 — variant: forest**
- **big:** $0
- **lbl:** Cerkl Broadcast Foundations
- **sub:** Per-employee read + acknowledgment analytics, included free on the plan most teams start on.

<!-- component: feature-grid.cols-2 -->
<!-- 4 cells × 50–85 words. Each cell: ✓ icon + h4 (≤4 words) + body. Head-to-head on the four dimensions this account cares about. -->

**Cell 1 — h4: What it actually costs**
Amplify isn't part of base Microsoft 365. Turning it on requires a paid Microsoft Viva license — the full Viva Suite (~$12/user/month) or the Employee Communications & Communities add-on (~$2/user/month). Cerkl Broadcast Foundations is free forever — no per-seat or per-message fee — and most teams run their whole program on it.

**Cell 2 — h4: Who actually read it**
This is the gap that matters most when you have no comms metrics today. Amplify reports aggregate views; Microsoft's own docs note it "only stores the count and not the user information" — no individual read receipts. Cerkl shows opens, reads, and acknowledgments per employee: who saw a critical update, and who still needs a nudge.

**Cell 3 — h4: Reaching everyone**
Amplify publishes inside Microsoft 365 — Outlook, Teams, SharePoint — so its reach and measurement lean on employees who hold a license and open those surfaces. Cerkl delivers to the inbox people already use, plus a mobile app and microsites — so deskless and frontline staff get the message too.

**Cell 4 — h4: Built for comms**
Amplify is a campaign-publishing layer; the rest of Viva (Engage) is a social feed. Cerkl is built for one job — getting a message to the right people and proving it landed. HRIS-synced audiences target by role, location, or department with no IT ticket.

<!-- component: callout-card (default cobalt) -->
<!-- quote ≤25 words + attribution ≤8 words -->

> Amplify helps you publish inside Microsoft 365. It can't tell you who read the message. Cerkl delivers to the inbox — and shows you who did.

— The measurement gap, in one line

<!-- component: footer -->
<!-- No CTA. Wordmark + neutral brand line + Microsoft source note for credibility. -->
**Wordmark (footer, 80px small):** `../../../branding-assets/Broadcast/Cerkl Broadcast Horizontal Lockup/Small (80px)/cerkl_broadcast_horizontal_lockup_full_color_small.png`

Microsoft facts verified against Microsoft Learn & Microsoft Support, May 2026 · Cerkl Broadcast
