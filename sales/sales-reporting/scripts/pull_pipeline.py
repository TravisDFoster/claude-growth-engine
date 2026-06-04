# /// script
# requires-python = ">=3.9"
# dependencies = ["requests"]
# ///
"""
pull_pipeline.py — Weekly Sales Report, pipeline metrics pull.

Fetches deal metrics for the configured pipelines/owners over a week window,
aggregates them in Python, and writes one compact JSON summary. Claude reads the
summary — never the raw deal payloads — to keep report-assembly token-cheap.

Usage:
    source ../../../.env   # exposes HUBSPOT_ACCESS_TOKEN (cerkl/.env)
    uv run pull_pipeline.py                         # defaults to current ISO week (Mon-Sun)
    uv run pull_pipeline.py --week-start 2026-05-25 --week-end 2026-05-31
    uv run pull_pipeline.py --out /path/to/out.json

Notes:
- Week boundaries are interpreted in the machine's LOCAL timezone (Mon 00:00:00 ->
  Sun 23:59:59). HubSpot stores timestamps in UTC; the small boundary skew is
  acceptable for V1.
- Won/lost are classified off HubSpot's calculated booleans hs_is_closed /
  hs_is_closed_won, not hardcoded stage IDs — robust to stage renames.
- Email Foundations is a free/PLG funnel with no dollar amounts and mostly no owner.
  It is decoupled from the AE metrics: queried separately with NO owner filter and
  reported count-only (new deals in period, by stage). It does not appear in the
  AE new-deals / by-owner / by-pipeline breakdowns.
"""

import argparse
import datetime as dt
import json
import os
import sys
import time

import requests

BASE = "https://api.hubapi.com"
SEARCH_URL = f"{BASE}/crm/v3/objects/deals/search"
PIPELINES_URL = f"{BASE}/crm/v3/pipelines/deals"

# --- Targets (resolved from the API on 2026-05-28) -------------------------
DOLLAR_PIPELINES = {
    "10060180": "Sales Pipeline",
    "22124812": "RFP Process",
}
FOUNDATIONS_PIPELINE = "800251979"
FOUNDATIONS_LABEL = "Email Foundations"
ALL_PIPELINES = {**DOLLAR_PIPELINES, FOUNDATIONS_PIPELINE: FOUNDATIONS_LABEL}

# Demo-request forms (HubSpot form submissions counted top-of-funnel, no owner filter).
# Add a row here if a new demo form goes live.
DEMO_FORMS = {
    "c0af68f9-b9e5-4222-bc09-c7552fafe13b": "Schedule a Chat (Webflow)",
}

OWNERS = {
    "77450212": "Josh Mandelman",
    "206074297": "Marc Fregoe",
    "207312707": "Tarek Kamil",
}

ALL_PIPELINE_IDS = list(ALL_PIPELINES.keys())
DOLLAR_PIPELINE_IDS = list(DOLLAR_PIPELINES.keys())
OWNER_IDS = list(OWNERS.keys())


def token():
    t = os.environ.get("HUBSPOT_ACCESS_TOKEN") or os.environ.get("HUBSPOT_API_TOKEN")
    if not t:
        sys.exit("ERROR: HUBSPOT_ACCESS_TOKEN not in env. Run: source cerkl/.env")
    return t


def to_ms(date_str, end=False):
    d = dt.datetime.strptime(date_str, "%Y-%m-%d")
    if end:
        d = d.replace(hour=23, minute=59, second=59)
    return int(time.mktime(d.timetuple()) * 1000)


def resolve_period(args):
    """Resolve the reporting window into (start_iso, end_iso, label, period_label, num_weeks).

    Priority: explicit --week-start/--week-end > --weeks N (trailing N ISO weeks,
    ending with the current week's Sunday) > default (current ISO week)."""
    if args.week_start and args.week_end:
        start = dt.date.fromisoformat(args.week_start)
        end = dt.date.fromisoformat(args.week_end)
    else:
        n = args.weeks or 1
        today = dt.date.today()
        this_monday = today - dt.timedelta(days=today.weekday())
        start = this_monday - dt.timedelta(weeks=n - 1)
        end = this_monday + dt.timedelta(days=6)

    num_weeks = max(1, round(((end - start).days + 1) / 7))
    sy, sw, _ = start.isocalendar()
    ey, ew, _ = end.isocalendar()
    if num_weeks <= 1:
        label = f"{sy}-W{sw:02d}"
        period_label = f"Week of {start.isoformat()} → {end.isoformat()}"
    elif sy == ey:
        label = f"{sy}-W{sw:02d}-W{ew:02d}"
        period_label = f"{num_weeks} weeks · {start.isoformat()} → {end.isoformat()}"
    else:
        label = f"{sy}-W{sw:02d}_to_{ey}-W{ew:02d}"
        period_label = f"{num_weeks} weeks · {start.isoformat()} → {end.isoformat()}"
    return start.isoformat(), end.isoformat(), label, period_label, num_weeks


def fetch_feature_gap_labels(tok):
    """value -> label map for the feature_gaps checkbox options (the gap taxonomy)."""
    r = requests.get(f"{BASE}/crm/v3/properties/deals/feature_gaps",
                     headers={"Authorization": f"Bearer {tok}"}, timeout=30)
    r.raise_for_status()
    return {o["value"]: o["label"] for o in r.json().get("options", [])}


def fetch_stage_meta(tok):
    """Map stage_id -> {label, order, pipeline, is_closed, is_holding} for target pipelines.

    Holding = an open stage with win-probability <= 0.1 (e.g. Sales Pipeline 'Nurture').
    These are dormant and reported separately from active pipeline.
    """
    headers = {"Authorization": f"Bearer {tok}"}
    r = requests.get(PIPELINES_URL, headers=headers, timeout=30)
    r.raise_for_status()
    meta = {}
    for pipe in r.json().get("results", []):
        if pipe["id"] not in ALL_PIPELINES:
            continue
        for s in pipe.get("stages", []):
            md = s.get("metadata", {})
            is_closed = str(md.get("isClosed", "false")).lower() == "true"
            try:
                prob = float(md.get("probability", 0))
            except (TypeError, ValueError):
                prob = 0.0
            meta[s["id"]] = {
                "label": s["label"],
                "order": s.get("displayOrder", 0),
                "pipeline": ALL_PIPELINES[pipe["id"]],
                "is_closed": is_closed,
                "is_holding": (not is_closed) and prob <= 0.1,
            }
    return meta


def fetch_form_submissions(tok, form_guid, start_ms, end_ms):
    """Pull submissions for one form within the window. Newest-first; stop paging
    once the page's oldest entry is older than the window start."""
    headers = {"Authorization": f"Bearer {tok}"}
    url = f"{BASE}/form-integrations/v1/submissions/forms/{form_guid}"
    out, offset = [], None
    while True:
        params = {"limit": 50}
        if offset:
            params["after"] = offset
        r = requests.get(url, headers=headers, params=params, timeout=30)
        r.raise_for_status()
        data = r.json()
        results = data.get("results", [])
        for s in results:
            ts = s.get("submittedAt", 0)
            if start_ms <= ts <= end_ms:
                out.append(s)
        # newest-first ordering: if we've fallen below the window start, no more.
        if results and results[-1].get("submittedAt", 0) < start_ms:
            break
        offset = data.get("paging", {}).get("next", {}).get("after")
        if not offset:
            break
        time.sleep(0.2)
    return out


def fetch_demos(tok, start_ms, end_ms):
    """Aggregate demo-request form submissions across DEMO_FORMS in the window.

    No owner filter — these are top-of-funnel demand signal."""
    submissions, by_form = [], {}
    for guid, name in DEMO_FORMS.items():
        rows = fetch_form_submissions(tok, guid, start_ms, end_ms)
        by_form[name] = len(rows)
        for s in rows:
            vals = {v["name"]: v.get("value", "") for v in s.get("values", [])}
            submissions.append({
                "submitted_at": dt.datetime.fromtimestamp(s["submittedAt"] / 1000).isoformat(timespec="seconds"),
                "form": name,
                "first_name": vals.get("firstname", ""),
                "last_name": vals.get("lastname", ""),
                "email": vals.get("email", ""),
                "company": vals.get("company", ""),
                "company_size": vals.get("contact_company_size", ""),
                "page_url": s.get("pageUrl", ""),
                "message": vals.get("message", ""),
            })
    submissions.sort(key=lambda r: r["submitted_at"], reverse=True)
    return {"total": len(submissions), "by_form": by_form, "submissions": submissions}


def search(tok, filters, properties, obj="deals"):
    """Run a CRM-object search, following pagination. Returns list of result dicts."""
    headers = {"Authorization": f"Bearer {tok}", "Content-Type": "application/json"}
    url = f"{BASE}/crm/v3/objects/{obj}/search"
    out, after = [], None
    while True:
        body = {
            "filterGroups": [{"filters": filters}],
            "properties": properties,
            "limit": 100,
        }
        if after:
            body["after"] = after
        r = requests.post(url, headers=headers, json=body, timeout=30)
        r.raise_for_status()
        data = r.json()
        out.extend(data.get("results", []))
        after = data.get("paging", {}).get("next", {}).get("after")
        if not after:
            break
        time.sleep(0.2)  # gentle on the search rate limit
    return out


def amount(props):
    v = props.get("amount")
    try:
        return float(v) if v not in (None, "") else 0.0
    except (TypeError, ValueError):
        return 0.0


def owner_name(props):
    return OWNERS.get(props.get("hubspot_owner_id"), props.get("hubspot_owner_id") or "Unassigned")


def pipeline_label(props):
    return ALL_PIPELINES.get(props.get("pipeline"), props.get("pipeline"))


def blank_breakdown(keys):
    return {k: {"count": 0, "amount": 0.0} for k in keys}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--week-start", help="explicit window start, YYYY-MM-DD")
    ap.add_argument("--week-end", help="explicit window end, YYYY-MM-DD")
    ap.add_argument("--weeks", type=int, help="trailing N ISO weeks (e.g. --weeks 4 = last 4 weeks)")
    ap.add_argument("--out")
    args = ap.parse_args()

    start, end, label, period_label, num_weeks = resolve_period(args)
    start_ms, end_ms = to_ms(start), to_ms(end, end=True)
    tok = token()
    stage_meta = fetch_stage_meta(tok)

    base_props = [
        "dealname", "amount", "pipeline", "dealstage",
        "createdate", "closedate", "hubspot_owner_id",
        "hs_is_closed", "hs_is_closed_won",
    ]

    # 1) New AE deals created in period — $-pipelines only (Sales + RFP), owner-filtered.
    #    Foundations is intentionally excluded here; it's a PLG funnel reported separately.
    new_deals = search(tok, [
        {"propertyName": "pipeline", "operator": "IN", "values": DOLLAR_PIPELINE_IDS},
        {"propertyName": "hubspot_owner_id", "operator": "IN", "values": OWNER_IDS},
        {"propertyName": "createdate", "operator": "GTE", "value": str(start_ms)},
        {"propertyName": "createdate", "operator": "LTE", "value": str(end_ms)},
    ], base_props)

    # 2) Closed in period ($-pipelines) — ONE query, partitioned into won/lost in Python
    #    via the hs_is_closed_won flag (saves an API call vs. two separate searches).
    closed = search(tok, [
        {"propertyName": "pipeline", "operator": "IN", "values": DOLLAR_PIPELINE_IDS},
        {"propertyName": "hubspot_owner_id", "operator": "IN", "values": OWNER_IDS},
        {"propertyName": "hs_is_closed", "operator": "EQ", "value": "true"},
        {"propertyName": "closedate", "operator": "GTE", "value": str(start_ms)},
        {"propertyName": "closedate", "operator": "LTE", "value": str(end_ms)},
    ], base_props + ["closed_lost_reason", "loss_reason"])
    won = [d for d in closed if str(d["properties"].get("hs_is_closed_won")).lower() == "true"]
    lost = [d for d in closed if str(d["properties"].get("hs_is_closed_won")).lower() != "true"]

    # 3) Open pipeline snapshot ($-pipelines, current open state)
    open_deals = search(tok, [
        {"propertyName": "pipeline", "operator": "IN", "values": DOLLAR_PIPELINE_IDS},
        {"propertyName": "hubspot_owner_id", "operator": "IN", "values": OWNER_IDS},
        {"propertyName": "hs_is_closed", "operator": "EQ", "value": "false"},
    ], base_props)

    # 4a) Demo-request form submissions in period — NO owner filter (top-of-funnel demand).
    demos = fetch_demos(tok, start_ms, end_ms)

    # 4) New Foundations deals in period — NO owner filter (the PLG funnel is mostly
    #    unowned, so owner-filtering would undercount it). Count-only, reported separately.
    foundations_new = search(tok, [
        {"propertyName": "pipeline", "operator": "EQ", "value": FOUNDATIONS_PIPELINE},
        {"propertyName": "createdate", "operator": "GTE", "value": str(start_ms)},
        {"propertyName": "createdate", "operator": "LTE", "value": str(end_ms)},
    ], base_props)

    # 5) Activity engagements in period (owner-filtered) — counted per rep.
    #    Emails are skipped: the token lacks the email-read scope (see process Future work).
    #    Calls typically read 0 (AEs don't log call engagements).
    ACTIVITY_TYPES = ["calls", "meetings", "notes", "tasks"]
    activity_by_owner = {name: {t: 0 for t in ACTIVITY_TYPES} for name in OWNERS.values()}
    for t in ACTIVITY_TYPES:
        for d in search(tok, [
            {"propertyName": "hubspot_owner_id", "operator": "IN", "values": OWNER_IDS},
            {"propertyName": "hs_timestamp", "operator": "GTE", "value": str(start_ms)},
            {"propertyName": "hs_timestamp", "operator": "LTE", "value": str(end_ms)},
        ], ["hubspot_owner_id"], obj=t):
            nm = OWNERS.get(d["properties"].get("hubspot_owner_id"))
            if nm:
                activity_by_owner[nm][t] += 1
    activity = {
        "by_owner": activity_by_owner,
        "totals": {t: sum(activity_by_owner[n][t] for n in OWNERS.values()) for t in ACTIVITY_TYPES},
        "emails": None,  # scope-blocked; see Future work
    }

    # 6) Structured feature_gaps roll-up across AE deals (current state; complements the
    #    notes-extracted requests). The property is sparsely set, so this is partial signal.
    fg_labels = fetch_feature_gap_labels(tok)
    fg_deals = search(tok, [
        {"propertyName": "pipeline", "operator": "IN", "values": DOLLAR_PIPELINE_IDS},
        {"propertyName": "hubspot_owner_id", "operator": "IN", "values": OWNER_IDS},
        {"propertyName": "feature_gaps", "operator": "HAS_PROPERTY"},
    ], ["feature_gaps"])
    fg_counts = {}
    for d in fg_deals:
        for v in (d["properties"].get("feature_gaps") or "").split(";"):
            v = v.strip()
            if v and v.lower() not in ("none", "other"):
                gap_label = fg_labels.get(v, v)
                fg_counts[gap_label] = fg_counts.get(gap_label, 0) + 1
    feature_gaps_rollup = {
        "deal_count": len(fg_deals),
        "by_option": dict(sorted(fg_counts.items(), key=lambda kv: kv[1], reverse=True)),
    }

    # --- Aggregate ---------------------------------------------------------
    def agg_new():
        by_owner = blank_breakdown(OWNERS.values())
        by_pipeline = blank_breakdown(DOLLAR_PIPELINES.values())
        total = {"count": 0, "amount": 0.0}
        for d in new_deals:
            p = d["properties"]
            a = amount(p)
            total["count"] += 1
            total["amount"] += a
            by_owner[owner_name(p)]["count"] += 1
            by_owner[owner_name(p)]["amount"] += a
            by_pipeline[pipeline_label(p)]["count"] += 1
            by_pipeline[pipeline_label(p)]["amount"] += a
        return {"total": total, "by_owner": by_owner, "by_pipeline": by_pipeline}

    def agg_closed(deals, with_reason=False):
        by_owner = blank_breakdown(OWNERS.values())
        total = {"count": 0, "amount": 0.0}
        rows = []
        for d in deals:
            p = d["properties"]
            a = amount(p)
            total["count"] += 1
            total["amount"] += a
            by_owner[owner_name(p)]["count"] += 1
            by_owner[owner_name(p)]["amount"] += a
            row = {
                "name": p.get("dealname"),
                "amount": a,
                "owner": owner_name(p),
                "pipeline": pipeline_label(p),
                "closedate": p.get("closedate"),
            }
            if with_reason:
                raw = p.get("closed_lost_reason") or p.get("loss_reason") or ""
                row["reason"] = " ".join(raw.split())  # collapse newlines/whitespace
            rows.append(row)
        rows.sort(key=lambda r: r["amount"], reverse=True)
        return {"total": total, "by_owner": by_owner, "deals": rows}

    def agg_open():
        # Active pipeline excludes dormant holding stages (e.g. Nurture); those are
        # reported as a separate line so the headline pipeline number stays meaningful.
        total = {"count": 0, "amount": 0.0}
        holding = {"count": 0, "amount": 0.0}
        by_stage = {}
        by_owner = blank_breakdown(OWNERS.values())
        for d in open_deals:
            p = d["properties"]
            a = amount(p)
            sid = p.get("dealstage")
            sm = stage_meta.get(sid, {})
            if sm.get("is_holding"):
                holding["count"] += 1
                holding["amount"] += a
                continue
            total["count"] += 1
            total["amount"] += a
            by_owner[owner_name(p)]["count"] += 1
            by_owner[owner_name(p)]["amount"] += a
            slot = by_stage.setdefault(sid, {
                "pipeline": sm.get("pipeline", pipeline_label(p)),
                "stage": sm.get("label", sid),
                "order": sm.get("order", 99),
                "count": 0, "amount": 0.0,
            })
            slot["count"] += 1
            slot["amount"] += a
        rows = sorted(by_stage.values(), key=lambda r: (r["pipeline"], r["order"]))
        return {"total": total, "by_owner": by_owner, "by_stage": rows, "holding_nurture": holding}

    def agg_foundations():
        # count-only, NO owner filter: every new Foundations deal in the period, by stage
        by_stage = {}
        total = 0
        for d in foundations_new:
            p = d["properties"]
            total += 1
            stage_label = stage_meta.get(p.get("dealstage"), {}).get("label", p.get("dealstage"))
            by_stage[stage_label] = by_stage.get(stage_label, 0) + 1
        return {"new_in_period": total, "by_stage": by_stage}

    summary = {
        "label": label,
        "period_label": period_label,
        "num_weeks": num_weeks,
        "start": start,
        "end": end,
        "generated_at": dt.datetime.now().isoformat(timespec="seconds"),
        "owners": list(OWNERS.values()),
        "pipelines": list(ALL_PIPELINES.values()),
        "new_deals": agg_new(),
        "closed_won": agg_closed(won),
        "closed_lost": agg_closed(lost, with_reason=True),
        "open_snapshot": agg_open(),
        "activity": activity,
        "feature_gaps_rollup": feature_gaps_rollup,
        "foundations": agg_foundations(),
        "demos": demos,
    }

    out_path = args.out or os.path.join(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
        "tmp", f"pipeline-{label}.json",
    )
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(summary, f, indent=2)

    # Render the HTML deliverable deterministically (no LLM / sub-agent).
    import render_report
    html_path = render_report.render_to_file(summary)

    # Compact at-a-glance for the orchestrator to relay (keeps the full JSON out of context).
    nd = summary["new_deals"]["total"]
    cw = summary["closed_won"]["total"]
    cl = summary["closed_lost"]["total"]
    op = summary["open_snapshot"]["total"]
    print(f'Sales Pipeline Report — {summary["period_label"]}')
    print(f'  New pipeline : {nd["count"]} deals · ${nd["amount"]:,.0f}')
    print(f'  Closed-won   : {cw["count"]} · ${cw["amount"]:,.0f}')
    print(f'  Closed-lost  : {cl["count"]} · ${cl["amount"]:,.0f}')
    print(f'  Active open  : {op["count"]} deals · ${op["amount"]:,.0f}')
    print(f'  Foundations  : {summary["foundations"]["new_in_period"]} new (no owner filter)')
    print(f'  Demos req’d : {summary["demos"]["total"]} (no owner filter)')
    print(f'  HTML : {html_path}')
    print(f'  JSON : {out_path}')


if __name__ == "__main__":
    main()
