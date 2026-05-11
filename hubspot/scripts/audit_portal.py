# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "hubspot-api-client",
#   "python-dotenv",
#   "requests",
#   "certifi",
# ]
# ///

import os
import sys
import time
import certifi
import requests
from datetime import datetime, timedelta
from pathlib import Path
from dotenv import load_dotenv
from hubspot import HubSpot

# Fix macOS SSL certificate verification
os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

load_dotenv()

TOKEN = os.getenv("HUBSPOT_API_TOKEN") or os.getenv("HUBSPOT_ACCESS_TOKEN")
if not TOKEN:
    sys.exit("ERROR: No HubSpot token found. Set HUBSPOT_API_TOKEN or HUBSPOT_ACCESS_TOKEN in .env")

client = HubSpot(access_token=TOKEN)
HEADERS = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}

NOW = datetime.utcnow()

def ms(dt):
    return str(int(dt.timestamp() * 1000))

T30  = ms(NOW - timedelta(days=30))
T60  = ms(NOW - timedelta(days=60))
T90  = ms(NOW - timedelta(days=90))
T180 = ms(NOW - timedelta(days=180))
T365 = ms(NOW - timedelta(days=365))

def sleep():
    time.sleep(0.2)

def _search(api_fn, filters, props):
    req = {"filterGroups": [{"filters": filters}], "properties": props, "limit": 1}
    try:
        r = api_fn(public_object_search_request=req)
        sleep()
        return r.total
    except Exception as e:
        print(f"    [warn] {e}")
        sleep()
        return -1

def cc(filters):
    return _search(client.crm.contacts.search_api.do_search, filters, ["email"])

def co(filters):
    return _search(client.crm.companies.search_api.do_search, filters, ["name"])

def dc(filters):
    return _search(client.crm.deals.search_api.do_search, filters, ["dealname"])

ALL = [{"propertyName": "createdate", "operator": "GT", "value": "0"}]
HAS  = lambda p: [{"propertyName": p, "operator": "HAS_PROPERTY"}]
NHAS = lambda p: [{"propertyName": p, "operator": "NOT_HAS_PROPERTY"}]
GT   = lambda p, v: [{"propertyName": p, "operator": "GT", "value": v}]
LT   = lambda p, v: [{"propertyName": p, "operator": "LT", "value": v}]
EQ   = lambda p, v: [{"propertyName": p, "operator": "EQ", "value": v}]
GTE  = lambda p, v: [{"propertyName": p, "operator": "GTE", "value": v}]

def pct(n, total):
    if total <= 0 or n < 0: return "N/A"
    return f"{n / total * 100:.1f}%"

def grade(ratio):
    if ratio < 0: return "?"
    if ratio < 0.05: return "A"
    if ratio < 0.15: return "B"
    if ratio < 0.30: return "C"
    if ratio < 0.50: return "D"
    return "F"

def hget(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        sleep()
        return r.json() if r.ok else {}
    except Exception as e:
        print(f"    [warn] {url} — {e}")
        sleep()
        return {}

# ── 1. DATABASE SIZE ──────────────────────────────────────────────────────────
print("[1/8] Database size...")
total_contacts  = cc(ALL)
total_companies = co(ALL)
total_deals     = dc(ALL)
mktg_contacts   = cc(EQ("hs_marketable_status", "true"))
print(f"      contacts={total_contacts:,}  companies={total_companies:,}  deals={total_deals:,}")

tc  = max(total_contacts, 1)
tco = max(total_companies, 1)
td  = max(total_deals, 1)

# ── 2. EMAIL DELIVERABILITY ───────────────────────────────────────────────────
# Counts only contacts that still need action (still marketing). Hard-bounce/optout
# properties are permanent stamps — once set, they stay forever. Suppression at Cerkl
# means flipping hs_marketable_status to false, so AND with marketable=true to count
# only the un-suppressed remainder.
print("[2/8] Email deliverability...")
MKT = EQ("hs_marketable_status", "true")
hard_bounced   = cc(HAS("hs_email_hard_bounce_reason_enum") + MKT)
soft_bounced   = cc(HAS("hs_email_bounce") + NHAS("hs_email_hard_bounce_reason_enum") + MKT)
global_unsub   = cc(EQ("hs_email_optout", "true") + MKT)
never_emailed  = cc(NHAS("hs_email_last_send_date"))
bounces_3plus  = cc(GTE("hs_email_bounce", "3") + MKT)

# ── 3. DATA COMPLETENESS ─────────────────────────────────────────────────────
print("[3/8] Data completeness...")
missing_email     = cc(NHAS("email"))
missing_company_c = cc(NHAS("company"))
missing_industry  = cc(NHAS("industry"))
missing_country   = cc(NHAS("country"))
missing_lifecycle = cc(NHAS("lifecyclestage"))
missing_owner_c   = cc(NHAS("hubspot_owner_id"))
missing_jobtitle  = cc(NHAS("jobtitle"))
co_no_domain      = co(NHAS("domain"))
co_no_industry    = co(NHAS("industry"))
co_no_country     = co(NHAS("country"))

# ── 4. ENGAGEMENT HEALTH ──────────────────────────────────────────────────────
print("[4/8] Engagement health...")
act_30d  = cc(GT("hs_last_sales_activity_timestamp", T30))
act_90d  = cc(GT("hs_last_sales_activity_timestamp", T90) + LT("hs_last_sales_activity_timestamp", T30))
act_180d = cc(GT("hs_last_sales_activity_timestamp", T180) + LT("hs_last_sales_activity_timestamp", T90))
act_365d = cc(GT("hs_last_sales_activity_timestamp", T365) + LT("hs_last_sales_activity_timestamp", T180))
inactive = cc(LT("hs_last_sales_activity_timestamp", T365))
never    = cc(NHAS("hs_last_sales_activity_timestamp"))
zero_pv  = cc(EQ("hs_analytics_num_page_views", "0"))

# ── 5. DUPLICATE ANALYSIS ─────────────────────────────────────────────────────
print("[5/8] Duplicate analysis (proxy metrics)...")
# Full dedup requires paginating all records — flagged for /merge-duplicate-companies
# Proxy: companies without a domain can't be auto-deduped
co_no_domain_pct = co_no_domain / tco

# ── 6. OWNER HEALTH ───────────────────────────────────────────────────────────
print("[6/8] Owner health...")
try:
    archived = client.crm.owners.owners_api.get_page(archived=True, limit=100)
    sleep()
    archived_ids = [str(o.id) for o in (archived.results or [])]
except Exception as e:
    print(f"    [warn] archived owners: {e}")
    archived_ids = []

deact_contacts  = 0
deact_companies = 0
for oid in archived_ids[:15]:
    n = cc(EQ("hubspot_owner_id", oid))
    if n > 0: deact_contacts += n
    c = co(EQ("hubspot_owner_id", oid))
    if c > 0: deact_companies += c

unowned_c  = cc(NHAS("hubspot_owner_id"))
unowned_co = co(NHAS("hubspot_owner_id"))

# ── 7. LIST & WORKFLOW HEALTH ─────────────────────────────────────────────────
print("[7/8] List & workflow health...")
lists_data    = hget("https://api.hubapi.com/contacts/v1/lists?count=1")
dynamic_data  = hget("https://api.hubapi.com/contacts/v1/lists/dynamic?count=1")
wf_data       = hget("https://api.hubapi.com/automation/v3/workflows")
forms_data    = hget("https://api.hubapi.com/forms/v2/forms?limit=500")

total_lists    = lists_data.get("total", "N/A")
active_lists   = dynamic_data.get("total", "N/A")
all_workflows  = wf_data.get("workflows", [])
total_wf       = len(all_workflows)
active_wf      = sum(1 for w in all_workflows if w.get("enabled", False))
total_forms    = len(forms_data) if isinstance(forms_data, list) else "N/A"

# ── 8. DEAL PIPELINE HEALTH ───────────────────────────────────────────────────
print("[8/8] Deal pipeline health...")
deals_no_amount   = dc(NHAS("amount"))
deals_no_close    = dc(NHAS("closedate"))
stale_deals       = dc(LT("hs_lastmodifieddate", T60))

# ── GRADING ───────────────────────────────────────────────────────────────────
g_db      = "B"  # informational
g_deliv   = grade((max(hard_bounced, 0) + max(global_unsub, 0)) / tc)
g_complete= grade((max(missing_email, 0) + max(missing_lifecycle, 0)) / tc)
g_engage  = grade((max(never, 0) + max(inactive, 0)) / tc)
g_dupes   = "C" if co_no_domain_pct > 0.3 else "B"  # judgment
g_owner   = "A" if not archived_ids else ("B" if deact_contacts < 100 else "C" if deact_contacts < 1000 else "D")
g_list    = "B"  # informational — requires deeper inspection
g_deal    = grade((max(deals_no_amount, 0) + max(deals_no_close, 0)) / td)

grades = {
    "Database Size":        g_db,
    "Email Deliverability": g_deliv,
    "Data Completeness":    g_complete,
    "Engagement Health":    g_engage,
    "Duplicate Analysis":   g_dupes,
    "Owner Health":         g_owner,
    "List & Workflow Health": g_list,
    "Deal Pipeline Health": g_deal,
}

order = {"A": 0, "B": 1, "C": 2, "D": 3, "F": 4, "?": 99}
overall = max((g for g in grades.values() if g != "?"), key=lambda g: order[g], default="?")

# ── REPORT ────────────────────────────────────────────────────────────────────
date_str = NOW.strftime("%Y-%m-%d")
Path("reports").mkdir(exist_ok=True)
report_path = f"reports/hubspot-audit-{date_str}.md"

report = f"""# HubSpot CRM Audit Report

**Date:** {date_str}
**Portal:** Cerkl

## Executive Summary

| Dimension | Grade | Key Finding |
|-----------|-------|-------------|
| Database Size | {g_db} | {total_contacts:,} contacts · {total_companies:,} companies · {total_deals:,} deals |
| Email Deliverability | {g_deliv} | {hard_bounced:,} hard bounced · {global_unsub:,} unsubscribed (both still marketing) |
| Data Completeness | {g_complete} | {missing_email:,} missing email ({pct(missing_email, tc)}) · {missing_lifecycle:,} missing lifecycle |
| Engagement Health | {g_engage} | {never:,} never active · {inactive:,} inactive 12+ months |
| Duplicate Analysis | {g_dupes} | {co_no_domain:,} companies ({pct(co_no_domain, tco)}) without domain — manual dedup required |
| Owner Health | {g_owner} | {len(archived_ids)} deactivated owners · {deact_contacts:,} contacts affected |
| List & Workflow Health | {g_list} | {total_lists} lists · {total_wf} workflows ({active_wf} active) |
| Deal Pipeline Health | {g_deal} | {deals_no_amount:,} missing amount · {stale_deals:,} stale (60+ days) |

**Overall Grade: {overall}**

---

## Detailed Findings

### 1. Database Size

| Metric | Count |
|--------|-------|
| Total Contacts | {total_contacts:,} |
| Total Companies | {total_companies:,} |
| Total Deals | {total_deals:,} |
| Marketing Contacts | {mktg_contacts:,} |

---

### 2. Email Deliverability — {g_deliv}

Counts reflect contacts that **still need action** (currently marked as marketing). Already-suppressed contacts are excluded — they retain the bounce/optout property history but are no longer billed or emailed.

| Metric | Count | % of Contacts |
|--------|-------|---------------|
| Hard Bounced — still marketing | {hard_bounced:,} | {pct(hard_bounced, tc)} |
| Soft Bounced — still marketing | {soft_bounced:,} | {pct(soft_bounced, tc)} |
| Global Unsubscribes — still marketing | {global_unsub:,} | {pct(global_unsub, tc)} |
| Never Emailed | {never_emailed:,} | {pct(never_emailed, tc)} |
| 3+ Bounces — still marketing | {bounces_3plus:,} | {pct(bounces_3plus, tc)} |

---

### 3. Data Completeness — {g_complete}

#### Contacts
| Field | Missing | % of Contacts |
|-------|---------|---------------|
| Email | {missing_email:,} | {pct(missing_email, tc)} |
| Company name | {missing_company_c:,} | {pct(missing_company_c, tc)} |
| Industry | {missing_industry:,} | {pct(missing_industry, tc)} |
| Country | {missing_country:,} | {pct(missing_country, tc)} |
| Lifecycle stage | {missing_lifecycle:,} | {pct(missing_lifecycle, tc)} |
| Owner | {missing_owner_c:,} | {pct(missing_owner_c, tc)} |
| Job title | {missing_jobtitle:,} | {pct(missing_jobtitle, tc)} |

#### Companies
| Field | Missing | % of Companies |
|-------|---------|----------------|
| Domain | {co_no_domain:,} | {pct(co_no_domain, tco)} |
| Industry | {co_no_industry:,} | {pct(co_no_industry, tco)} |
| Country | {co_no_country:,} | {pct(co_no_country, tco)} |

---

### 4. Engagement Health — {g_engage}

| Activity Window | Count | % of Contacts |
|----------------|-------|---------------|
| Active last 30 days | {act_30d:,} | {pct(act_30d, tc)} |
| Active 31–90 days ago | {act_90d:,} | {pct(act_90d, tc)} |
| Active 91–180 days ago | {act_180d:,} | {pct(act_180d, tc)} |
| Active 181–365 days ago | {act_365d:,} | {pct(act_365d, tc)} |
| Inactive 365+ days | {inactive:,} | {pct(inactive, tc)} |
| Never active | {never:,} | {pct(never, tc)} |
| Zero page views | {zero_pv:,} | {pct(zero_pv, tc)} |

---

### 5. Duplicate Analysis — {g_dupes}

Full duplicate detection requires paginating all records and is handled by the `/merge-duplicate-companies` skill.

**Proxy signal:** {co_no_domain:,} companies ({pct(co_no_domain, tco)}) have no domain, limiting automated deduplication by domain. These require manual review.

---

### 6. Owner Health — {g_owner}

| Metric | Count |
|--------|-------|
| Deactivated owners | {len(archived_ids)} |
| Contacts assigned to deactivated owners | {deact_contacts:,} |
| Companies assigned to deactivated owners | {deact_companies:,} |
| Contacts with no owner | {unowned_c:,} |
| Companies with no owner | {unowned_co:,} |

---

### 7. List & Workflow Health — {g_list}

| Metric | Count |
|--------|-------|
| Total lists | {total_lists} |
| Active (dynamic) lists | {active_lists} |
| Total workflows | {total_wf} |
| Active workflows | {active_wf} |
| Total forms | {total_forms} |

---

### 8. Deal Pipeline Health — {g_deal}

| Metric | Count | % of Deals |
|--------|-------|------------|
| Total deals | {total_deals:,} | — |
| Missing amount | {deals_no_amount:,} | {pct(deals_no_amount, td)} |
| Missing close date | {deals_no_close:,} | {pct(deals_no_close, td)} |
| Stale (60+ days, any stage) | {stale_deals:,} | {pct(stale_deals, td)} |

---

## Next Steps

Run the skills below in order based on your audit results.
"""

with open(report_path, "w") as f:
    f.write(report)

print(f"\nAudit complete. Report: {report_path}")
print("\n── GRADES ──────────────────────────────────────")
for dim, g in grades.items():
    print(f"  {g}  {dim}")
print(f"\n  Overall: {overall}")
