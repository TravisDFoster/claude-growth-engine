# /// script
# requires-python = ">=3.10"
# dependencies = ["requests", "python-dotenv", "certifi"]
# ///

import os, csv, time, certifi
os.environ["SSL_CERT_FILE"] = certifi.where()
os.environ["REQUESTS_CA_BUNDLE"] = certifi.where()

import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("HUBSPOT_API_TOKEN") or os.getenv("HUBSPOT_ACCESS_TOKEN")
BASE  = "https://api.hubapi.com"
H     = {"Authorization": f"Bearer {TOKEN}", "Content-Type": "application/json"}
SEARCH = f"{BASE}/crm/v3/objects/contacts/search"

def sleep(): time.sleep(0.2)

def count(filters):
    r = requests.post(SEARCH, headers=H, json={"filterGroups":[{"filters":filters}],"limit":1})
    r.raise_for_status(); sleep()
    return r.json().get("total", 0)

def paginate(filters, props):
    results, after = [], None
    while True:
        payload = {"filterGroups":[{"filters":filters}],"properties":props,"limit":100}
        if after: payload["after"] = after
        r = requests.post(SEARCH, headers=H, json=payload)
        r.raise_for_status(); sleep()
        data = r.json()
        for c in data.get("results", []):
            p = c.get("properties", {})
            results.append({k: p.get(k,"") for k in props} | {"id": c["id"]})
        after = data.get("paging",{}).get("next",{}).get("after")
        if not after: break
    return results

def create_list(name, filter_branch):
    r = requests.post(f"{BASE}/crm/v3/lists", headers=H,
                      json={"name":name,"objectTypeId":"0-1","processingType":"DYNAMIC","filterBranch":filter_branch})
    sleep()
    if r.status_code in (200, 201):
        d = r.json()
        lid = d.get("listId") or d.get("list",{}).get("listId")
        print(f"  Created list '{name}' — ID: {lid}")
        return lid
    elif r.status_code == 409:
        print(f"  List '{name}' already exists — use existing")
    else:
        print(f"  Failed to create list: {r.status_code} — {r.text[:200]}")
    return None

os.makedirs("data/audit-logs", exist_ok=True)

# ── HARD BOUNCED ──────────────────────────────────────────────────────────────
print("\n── Hard Bounced Setup ───────────────────────────────────")

hb_filters = [
    {"propertyName": "hs_email_hard_bounce_reason_enum", "operator": "HAS_PROPERTY"},
    {"propertyName": "hs_marketable_status",             "operator": "EQ", "value": "true"},
]
hb_total = count(hb_filters)
print(f"  Hard bounced still marketing: {hb_total}")

# Lifecycle breakdown
print("  Lifecycle breakdown:")
for stage in ["lead","subscriber","marketingqualifiedlead","salesqualifiedlead","opportunity","customer","other"]:
    n = count(hb_filters + [{"propertyName":"lifecyclestage","operator":"EQ","value":stage}])
    if n > 0: print(f"    {stage}: {n}")
n_none = count(hb_filters + [{"propertyName":"lifecyclestage","operator":"NOT_HAS_PROPERTY"}])
if n_none > 0: print(f"    (no lifecycle): {n_none}")

# Bounce reason breakdown
print("  Bounce reason breakdown:")
hb_all = paginate(
    [{"propertyName":"hs_email_hard_bounce_reason_enum","operator":"HAS_PROPERTY"},
     {"propertyName":"hs_marketable_status","operator":"EQ","value":"true"}],
    ["email","firstname","lastname","hs_email_hard_bounce_reason_enum","hs_email_bounce","lifecyclestage","hs_marketable_status","createdate"]
)
reasons = {}
for c in hb_all:
    r = c.get("hs_email_hard_bounce_reason_enum") or "(empty)"
    reasons[r] = reasons.get(r, 0) + 1
for reason, n in sorted(reasons.items(), key=lambda x: -x[1]):
    print(f"    {reason}: {n}")

# CSV export
csv_path = "data/audit-logs/hard-bounced-to-suppress.csv"
with open(csv_path, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id","email","firstname","lastname",
        "hs_email_hard_bounce_reason_enum","hs_email_bounce","lifecyclestage","hs_marketable_status","createdate"])
    writer.writeheader(); writer.writerows(hb_all)
print(f"  Audit CSV: {csv_path} ({len(hb_all)} records)")

# Create list
print("  Creating HubSpot list...")
create_list("CLEANUP: Hard Bounced Contacts", {
    "filterBranchType": "OR",
    "filterBranches": [{"filterBranchType":"AND","filterBranches":[],"filters":[{
        "filterType":"PROPERTY","property":"hs_email_hard_bounce_reason_enum",
        "operation":{"operationType":"ALL_PROPERTY","operator":"IS_KNOWN"}
    }]}],
    "filters": []
})

# ── GLOBAL UNSUBSCRIBES ───────────────────────────────────────────────────────
print("\n── Global Unsubscribes Setup ────────────────────────────")

us_filters = [
    {"propertyName": "hs_email_optout",      "operator": "EQ", "value": "true"},
    {"propertyName": "hs_marketable_status", "operator": "EQ", "value": "true"},
]
us_total = count(us_filters)
print(f"  Unsubscribes still marketing: {us_total}")

print("  Lifecycle breakdown:")
for stage in ["lead","subscriber","marketingqualifiedlead","salesqualifiedlead","opportunity","customer","other"]:
    n = count(us_filters + [{"propertyName":"lifecyclestage","operator":"EQ","value":stage}])
    if n > 0: print(f"    {stage}: {n}")
n_none = count(us_filters + [{"propertyName":"lifecyclestage","operator":"NOT_HAS_PROPERTY"}])
if n_none > 0: print(f"    (no lifecycle): {n_none}")

us_all = paginate(us_filters,
    ["email","firstname","lastname","hs_email_optout","hs_marketable_status","lifecyclestage","createdate"])

csv_path2 = "data/audit-logs/unsubscribed-to-suppress.csv"
with open(csv_path2, "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id","email","firstname","lastname",
        "hs_email_optout","hs_marketable_status","lifecyclestage","createdate"])
    writer.writeheader(); writer.writerows(us_all)
print(f"  Audit CSV: {csv_path2} ({len(us_all)} records)")

print("  Creating HubSpot list...")
create_list("CLEANUP: Globally Unsubscribed", {
    "filterBranchType": "OR",
    "filterBranches": [{"filterBranchType":"AND","filterBranches":[],"filters":[{
        "filterType":"PROPERTY","property":"hs_email_optout",
        "operation":{"operationType":"ENUMERATION","operator":"IS_EQUAL_TO","value":"true"}
    }]}],
    "filters": []
})

print("\n── Done ─────────────────────────────────────────────────")
print(f"  {len(hb_all)} hard bounced contacts ready to suppress")
print(f"  {len(us_all)} unsubscribed contacts ready to suppress")
print("\n  Next: complete suppression in HubSpot UI (see instructions below)")
