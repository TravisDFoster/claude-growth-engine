# Cerkl Broadcast vs. Microsoft Viva Engage

> Account-specific comparison handout for TMNAS leadership — active conversation.
> Reader: TMNAS leadership + tech lead. Leadership explicitly dislikes the "social media" concept; this piece validates that instinct (Engage IS a social feed) and positions Cerkl as serious, measured, non-social internal comms. Tech lead asked why not just use the Viva tools "in our Microsoft license." No comms metrics today; loved Cerkl Insights.
> Goal: informative comparison, no CTA. Thesis: a feed is the wrong tool for must-read comms; Cerkl is targeted delivery + measurement.
> Slug: cerkl-vs-viva-engage | Date: 2026-05-29
> Recipe: Comparison (no CTA): hero-compact → number-row.cols-3 → feature-grid.cols-2 → callout-card → footer
>
> Fact basis (verified 2026-05-29 against Microsoft Learn / Microsoft Support / M365 blog):
> - Engage is the Yammer successor: communities, Storyline, Stories, Leadership Corner, Answers, Campaigns.
> - Free in M365: community feeds, basic analytics, Storyline. Premium comms features (Leadership Corner, Answers, Campaigns, advanced analytics) require paid Viva Suite or Employee Communications & Communities add-on.
> - Analytics are social-engagement style (views, reactions, replies) — NO per-message read receipts.
> - Pull/opt-in: content lives in a feed employees must visit; frontline reach needs the Teams Engage app.
>
> **Remediation applied during render (2026-05-29):** verify gate flagged a 166px footer overrun. Resolved with (1) Tier-A `--body-size:15px` on the .page div; (2) removed the hero subtitle line (hero-compact budget is "no body"); (3) trimmed each feature-grid.cols-2 cell from ~65–80 words to ~50–55 words (dropped the "separate Teams Engage app" clause from the "Reaching everyone" cell). Second pass: PASS, single page. Copy below reflects the shipped PDF.

---

<!-- component: hero-compact (single Cerkl Broadcast lockup, left; H1 below divider) -->
<!-- Render as:
     <div class="hero-compact">
       <span class="wordmark-ph"><img src="../../../branding-assets/Broadcast/Cerkl Broadcast Horizontal Lockup/Medium (160px)/cerkl_broadcast_horizontal_lockup_full_color_medium.png" alt="Cerkl Broadcast"></span>
     </div>
     <h1 style="font-size:24px; color:var(--accent-dark); margin:0; letter-spacing:-0.01em;">Cerkl Broadcast vs. Microsoft Viva Engage</h1>
-->
<!-- Subtitle removed during remediation (hero-compact = no body). -->

**Cerkl Broadcast wordmark (left, 160px medium):** `../../../branding-assets/Broadcast/Cerkl Broadcast Horizontal Lockup/Medium (160px)/cerkl_broadcast_horizontal_lockup_full_color_medium.png`

# Cerkl Broadcast vs. Microsoft Viva Engage

<!-- component: number-row.cols-3 -->
<!-- Each cell: .big (stat ≤5 chars), .lbl (≤8 words), .sub (≤14 words). Lead with the delivery + measurement contrast against a social feed. -->

**Cell 1 — variant: ruby**
- **big:** 0
- **lbl:** Read confirmations from a social feed
- **sub:** Engage tracks views, reactions, and replies — not whether a person read a must-read message.

**Cell 2 — variant: default (cobalt)**
- **big:** Pull
- **lbl:** Engage is opt-in by design
- **sub:** Content lives in a feed employees must visit — nothing guarantees the message is seen.

**Cell 3 — variant: forest**
- **big:** $0
- **lbl:** Cerkl Broadcast Foundations
- **sub:** Targeted internal email that lands in the inbox — with per-employee read analytics, free.

<!-- component: feature-grid.cols-2 -->
<!-- 4 cells × 50–85 words. ✓ icon + h4 (≤4 words) + body. Thesis: feed ≠ delivery; reach everyone; prove it landed; not another social network (speaks to leadership's aversion). -->

**Cell 1 — h4: A feed, not delivery**
Viva Engage is the Yammer successor: communities, Storyline, Leadership Corner, Stories. It's built for culture, conversation, and recognition — content employees discover by choosing to visit the feed. That's a different job from making sure a specific message reaches a specific person. A fine place for community; not a system for must-read communication.

**Cell 2 — h4: Reaching everyone**
Because Engage is opt-in, anyone who never opens the feed simply misses the post — a real risk for deskless and frontline staff. Cerkl delivers to the inbox and channels people already check, plus mobile and microsites. Flagger Force reaches 2,000 employees across 10+ states; St. Elizabeth sees a 54% employee open rate.

**Cell 3 — h4: Proof it landed**
With no comms metrics today, this shows up immediately. Engage offers social-style analytics — views, reactions, community activity — not per-message read confirmation. Cerkl's Insights (redesigned May 2026) shows opens, reads, and acknowledgments per employee: exactly who saw the open-enrollment notice or safety bulletin, and who still needs a follow-up.

**Cell 4 — h4: Not another network**
If a social feed feels like the wrong fit for serious internal communication, that instinct is sound. Cerkl isn't a social network competing for attention — it's structured, targeted email plus measurement, built for communicators. Keep Engage for culture; use Cerkl to make sure the messages that matter reach everyone and get read.

<!-- component: callout-card (default cobalt) -->
<!-- quote ≤25 words + attribution ≤8 words -->

> A feed is built for culture and conversation — not the open-enrollment deadline or the safety bulletin. Cerkl makes those land, and proves it.

— Why a feed isn't a comms strategy

<!-- component: footer -->
<!-- No CTA. Wordmark + neutral brand line + Microsoft source note for credibility. -->
**Wordmark (footer, 80px small):** `../../../branding-assets/Broadcast/Cerkl Broadcast Horizontal Lockup/Small (80px)/cerkl_broadcast_horizontal_lockup_full_color_small.png`

Microsoft facts verified against Microsoft Learn & Microsoft Support, May 2026 · Cerkl Broadcast
