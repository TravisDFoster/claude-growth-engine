# /// script
# requires-python = ">=3.9"
# ///
"""
score.py — transparent, rules-based deal-health scoring for the Deal Report.

This is the SINGLE TUNING SURFACE. Every threshold and weight lives here as a
named constant so the model is auditable and adjustable without touching the
pull/render code. There is NO inference in this module — a deal's band is a
deterministic function of its structural metrics.

Inference (the `deal-health-analyst` subagent) runs only AFTER this, on deals
this module bands as `watch`/`at_risk`, to explain *why* and extract next steps
from cleaned email threads (Phase 2). It never sets the band — rules flag,
inference explains.

`score_deal(metrics)` returns {score, band, reasons[]} where `reasons` is the
plain-English audit trail of what drove the score (rendered in the report).
"""

# --- Thresholds (days) ------------------------------------------------------
RECENCY_STALE = 14        # no touch in 14d  → losing momentum
RECENCY_DEAD = 30         # no touch in 30d  → cold
STAGE_AGE_SLOW = 30       # in current stage > 30d → slow
STAGE_AGE_STUCK = 60      # > 60d → stuck
NURTURE_AGE = 90          # open > 90d ...
NURTURE_QUIET = 30        # ...and quiet 30d+ → nurture candidate (flagged, not acted on)

# --- Slippage (close-date pushes) -------------------------------------------
SLIPPAGE_WATCH = 1        # pushed once
SLIPPAGE_RISK = 2         # pushed 2+ times

# --- Risk weights (points; higher total = unhealthier) ----------------------
# Each rule contributes points. Bands are cumulative thresholds below.
W = {
    "recency": 3,         # silence is the strongest single risk signal
    "stage_age": 2,
    "slippage": 2,
    "reply": 2,           # outbound with zero inbound = one-way conversation
    "tasks": 1,
    "single_thread": 1,
}

# --- Bands (total risk points) ----------------------------------------------
BAND_WATCH = 3            # >= 3 points → watch
BAND_RISK = 6            # >= 6 points → at risk


def score_deal(m):
    """m: per-deal metrics dict from pull_deals. Returns {score, band, reasons}."""
    pts = 0
    reasons = []

    rec = m.get("recency_days")
    if rec is None:
        pts += W["recency"]; reasons.append("No activity ever logged")
    elif rec >= RECENCY_DEAD:
        pts += W["recency"]; reasons.append(f"No touch in {rec}d")
    elif rec >= RECENCY_STALE:
        pts += W["recency"] - 1; reasons.append(f"Quiet for {rec}d")

    sa = m.get("stage_age_days")
    if sa is not None and sa >= STAGE_AGE_STUCK:
        pts += W["stage_age"]; reasons.append(f"Stuck in stage {sa}d")
    elif sa is not None and sa >= STAGE_AGE_SLOW:
        pts += W["stage_age"] - 1; reasons.append(f"Slow in stage {sa}d")

    sl = m.get("slippage_count", 0)
    if sl >= SLIPPAGE_RISK:
        pts += W["slippage"]; reasons.append(f"Close date pushed {sl}×")
    elif sl >= SLIPPAGE_WATCH:
        pts += W["slippage"] - 1; reasons.append("Close date pushed once")

    sent, recv = m.get("email_sent", 0), m.get("email_received", 0)
    if sent >= 2 and recv == 0:
        pts += W["reply"]; reasons.append(f"{sent} sent · 0 replies")

    overdue = m.get("tasks_overdue", 0)
    if overdue:
        pts += W["tasks"]; reasons.append(f"{overdue} overdue task{'s' if overdue != 1 else ''}")

    if m.get("contacts", 0) <= 1:
        pts += W["single_thread"]; reasons.append("Single-threaded")

    band = "at_risk" if pts >= BAND_RISK else "watch" if pts >= BAND_WATCH else "healthy"
    return {"score": pts, "band": band, "reasons": reasons}


def is_nurture_candidate(m):
    """Old + quiet + no next step. Flagged for visibility; NOT auto-moved (per Travis)."""
    age = m.get("age_days")
    rec = m.get("recency_days")
    return bool(
        age is not None and age >= NURTURE_AGE
        and (rec is None or rec >= NURTURE_QUIET)
        and m.get("tasks_open", 0) == 0
    )
