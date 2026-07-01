# /// script
# requires-python = ">=3.9"
# dependencies = ["requests"]
# ///
"""
pull_deals.py — Deal Report (Phase 1): per-deal health over the ACTIVE OPEN
Sales Pipeline + RFP Process pipelines (owner trio), scored by deterministic rules.

This is the 99% Python layer: it pulls deals + stage/close-date history +
per-deal engagements (meetings/notes/tasks/emails) and contact associations,
computes structural health metrics, scores them via `score.py` (the tuning
surface), writes one JSON, and renders the deterministic HTML board.

NO email *bodies* here — Phase 1 uses engagement metadata only (counts, direction,
timestamps, tracked-flag). Body ingestion + the inference pass on flagged deals is
Phase 2 (see deal-report-process.md / the deal-health-analyst skill).

Usage (run from anywhere; paths resolve from __file__):
    set -a && source /Users/travisfoster/claude-code/cerkl/.env && set +a
    uv run pull_deals.py                 # all three AEs
    uv run pull_deals.py --owner Marc    # one rep (substring match on name)
"""

import argparse
import datetime as dt
import json
import os
import sys

import requests

# Reuse the weekly report's data layer (HubSpot helpers, owners, pipelines) which
# lives in the sibling sales-reporting/scripts — put it on the path before importing.
DEAL_REPORT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_SALES = os.path.dirname(DEAL_REPORT)
sys.path.insert(0, os.path.join(_SALES, "sales-reporting", "scripts"))

import pull_pipeline as pp   # token, search, OWNERS, OWNER_IDS, DOLLAR_PIPELINE_IDS, fetch_stage_meta, fetch_portal_id, _int
import pull_notes as pn      # batch_assoc, batch_read

BASE = "https://api.hubapi.com"

ENGAGEMENT_PROPS = {
    "meetings": ["hs_timestamp"],
    "notes": ["hs_timestamp"],
    "tasks": ["hs_timestamp", "hs_task_status", "hs_task_subject"],
    "emails": ["hs_timestamp", "hs_email_direction", "hs_email_status",
               "hs_email_tracker_key", "hs_email_open_count", "hs_email_click_count"],
}
# Activities that count as a "touch" for recency (a task due date is not a touch).
TOUCH_TYPES = ("meetings", "notes", "emails")


def parse_ts(v):
    """HubSpot timestamp (ISO string or epoch-ms string) → naive UTC datetime, or None."""
    if not v:
        return None
    v = str(v)
    if v.isdigit():
        return dt.datetime.utcfromtimestamp(int(v) / 1000)
    try:
        return dt.datetime.fromisoformat(v.replace("Z", "+00:00")).replace(tzinfo=None)
    except ValueError:
        return None


def batch_read_history(tok, ids, props, hist_props):
    """v3 batch read with propertiesWithHistory: {id: {'props': {...}, 'history': {prop: [entries]}}}."""
    if not ids:
        return {}
    headers = {"Authorization": f"Bearer {tok}", "Content-Type": "application/json"}
    out, ids = {}, list(ids)
    # HubSpot caps batch reads that request propertiesWithHistory at 50 inputs (not 100).
    for i in range(0, len(ids), 50):
        chunk = ids[i:i + 50]
        r = requests.post(
            f"{BASE}/crm/v3/objects/deals/batch/read", headers=headers,
            json={"inputs": [{"id": x} for x in chunk], "properties": props,
                  "propertiesWithHistory": hist_props}, timeout=30,
        )
        r.raise_for_status()
        for res in r.json().get("results", []):
            out[res["id"]] = {"props": res.get("properties", {}),
                              "history": res.get("propertiesWithHistory", {})}
    return out


def stage_age_days(history, now):
    """Days since the deal last entered its current stage (newest dealstage history entry)."""
    ts = [parse_ts(h.get("timestamp")) for h in history or []]
    ts = [t for t in ts if t]
    return (now - max(ts)).days if ts else None


def closedate_slippage(history):
    """How many times the close date was pushed OUT (a top slip signal)."""
    entries = []
    for h in history or []:
        t, cd = parse_ts(h.get("timestamp")), parse_ts(h.get("value"))
        if t and cd:
            entries.append((t, cd))
    entries.sort(key=lambda x: x[0])  # chronological
    return sum(1 for i in range(1, len(entries)) if entries[i][1] > entries[i - 1][1])


def email_metrics(ids, emails):
    sent = recv = tracked = untracked = opens = clicks = 0
    for eid in ids:
        p = emails.get(eid, {})
        if "INCOMING" in (p.get("hs_email_direction") or "").upper():
            recv += 1
        else:
            sent += 1
        if p.get("hs_email_tracker_key"):
            tracked += 1
        else:
            untracked += 1
        opens += pp._int(p.get("hs_email_open_count"))
        clicks += pp._int(p.get("hs_email_click_count"))
    return dict(email_sent=sent, email_received=recv, email_tracked=tracked,
                email_untracked=untracked, email_opens=opens, email_clicks=clicks)


def task_metrics(ids, tasks, now):
    open_t = overdue = 0
    oldest_overdue = None
    for tid in ids:
        p = tasks.get(tid, {})
        if (p.get("hs_task_status") or "").upper() == "COMPLETED":
            continue
        open_t += 1
        due = parse_ts(p.get("hs_timestamp"))
        if due and due < now:
            overdue += 1
            age = (now - due).days
            oldest_overdue = age if oldest_overdue is None else max(oldest_overdue, age)
    return dict(tasks_open=open_t, tasks_overdue=overdue, oldest_overdue_days=oldest_overdue)


def main():
    import score  # tuning surface (local import keeps it the obvious place to edit)

    ap = argparse.ArgumentParser()
    ap.add_argument("--owner", help="filter to one rep by name substring (e.g. 'Marc')")
    ap.add_argument("--out")
    args = ap.parse_args()

    tok = pp.token()
    now = dt.datetime.utcnow()
    portal_id = pp.fetch_portal_id(tok)
    stage_meta = pp.fetch_stage_meta(tok)

    owner_ids = pp.OWNER_IDS
    if args.owner:
        owner_ids = [oid for oid, nm in pp.OWNERS.items() if args.owner.lower() in nm.lower()]
        if not owner_ids:
            sys.exit(f"no owner matching '{args.owner}' in {list(pp.OWNERS.values())}")

    # 1) Active open deals — Sales + RFP, owner-filtered, currently open. Exclude the
    #    Nurture holding stage (is_holding, win-prob ≤ 0.1) so "active" matches the
    #    weekly report; active deals that SHOULD move to Nurture are caught by the
    #    nurture_candidate flag instead.
    raw_open = pp.search(tok, [
        {"propertyName": "pipeline", "operator": "IN", "values": pp.DOLLAR_PIPELINE_IDS},
        {"propertyName": "hubspot_owner_id", "operator": "IN", "values": owner_ids},
        {"propertyName": "hs_is_closed", "operator": "EQ", "value": "false"},
    ], ["dealname", "amount", "pipeline", "dealstage", "createdate", "closedate", "hubspot_owner_id"])
    open_deals = [d for d in raw_open
                  if not stage_meta.get(d["properties"].get("dealstage"), {}).get("is_holding")]
    holding_excluded = len(raw_open) - len(open_deals)
    deal_ids = [d["id"] for d in open_deals]

    # 2) Stage + close-date HISTORY (velocity + slippage) — one batched read.
    hist = batch_read_history(tok, deal_ids, ["dealstage", "closedate"], ["dealstage", "closedate"])

    # 3) Per-deal associations → engagements + contacts (reuse pull_notes batch helpers).
    assoc = {t: pn.batch_assoc(tok, "deals", t, deal_ids) for t in ENGAGEMENT_PROPS}
    deal_contacts = pn.batch_assoc(tok, "deals", "contacts", deal_ids)

    # 4) Batch-read each engagement type's properties once.
    eng = {}
    for t, props in ENGAGEMENT_PROPS.items():
        ids = {i for lst in assoc[t].values() for i in lst}
        eng[t] = pn.batch_read(tok, t, ids, props)

    # 5) Per-deal metrics + score.
    deals = []
    for d in open_deals:
        did, p = d["id"], d["properties"]
        h = hist.get(did, {}).get("history", {})
        create = parse_ts(p.get("createdate"))

        # last touch across meetings/notes/emails
        touch_ts = []
        for t in TOUCH_TYPES:
            for i in assoc[t].get(did, []):
                ts = parse_ts(eng[t].get(i, {}).get("hs_timestamp"))
                if ts:
                    touch_ts.append(ts)
        last_touch = max(touch_ts) if touch_ts else None

        m = {
            "id": did,
            "name": p.get("dealname") or "(unnamed)",
            "owner": pp.OWNERS.get(p.get("hubspot_owner_id"), "Unassigned"),
            "pipeline": pp.ALL_PIPELINES.get(p.get("pipeline"), p.get("pipeline")),
            "stage": stage_meta.get(p.get("dealstage"), {}).get("label", p.get("dealstage")),
            "amount": pp.amount(p),
            "url": f"https://app.hubspot.com/contacts/{portal_id}/deal/{did}",
            "age_days": (now - create).days if create else None,
            "stage_age_days": stage_age_days(h.get("dealstage"), now),
            "slippage_count": closedate_slippage(h.get("closedate")),
            "recency_days": (now - last_touch).days if last_touch else None,
            "last_touch": last_touch.date().isoformat() if last_touch else None,
            "contacts": len(deal_contacts.get(did, [])),
            "meetings": len(assoc["meetings"].get(did, [])),
            "notes": len(assoc["notes"].get(did, [])),
            "no_recap": len(assoc["meetings"].get(did, [])) > 0 and len(assoc["notes"].get(did, [])) == 0,
        }
        m.update(email_metrics(assoc["emails"].get(did, []), eng["emails"]))
        m.update(task_metrics(assoc["tasks"].get(did, []), eng["tasks"], now))
        s = score.score_deal(m)
        m.update(score=s["score"], band=s["band"], reasons=s["reasons"],
                 nurture_candidate=score.is_nurture_candidate(m))
        deals.append(m)

    # Sort worst-first within the full set; render groups by owner.
    band_rank = {"at_risk": 0, "watch": 1, "healthy": 2}
    deals.sort(key=lambda x: (band_rank.get(x["band"], 9), -x["score"], -(x["amount"] or 0)))

    summary = {
        "generated_at": now.isoformat(timespec="seconds") + "Z",
        "scope": "Active open · Sales Pipeline + RFP Process",
        "owners": [pp.OWNERS[o] for o in owner_ids],
        "deal_count": len(deals),
        "holding_excluded": holding_excluded,
        "bands": {b: sum(1 for d in deals if d["band"] == b) for b in ("at_risk", "watch", "healthy")},
        "nurture_candidates": sum(1 for d in deals if d["nurture_candidate"]),
        "deals": deals,
    }

    out_path = args.out or os.path.join(DEAL_REPORT, "tmp", "deal-report.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    import render_deal_report
    html_path = render_deal_report.render_to_file(summary)

    b = summary["bands"]
    print(f'Deal Report — {summary["scope"]}')
    print(f'  Deals analyzed : {summary["deal_count"]}  ({", ".join(summary["owners"])})')
    print(f'  At risk / Watch / Healthy : {b["at_risk"]} / {b["watch"]} / {b["healthy"]}')
    print(f'  Nurture candidates (flagged) : {summary["nurture_candidates"]}')
    print(f'  Holding/Nurture-stage excluded : {summary["holding_excluded"]}')
    print(f'  HTML : {html_path}')
    print(f'  JSON : {out_path}')


if __name__ == "__main__":
    main()
