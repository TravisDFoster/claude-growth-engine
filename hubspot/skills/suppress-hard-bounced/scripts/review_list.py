# /// script
# requires-python = ">=3.10"
# dependencies = ["requests", "python-dotenv"]
# ///
"""
Review contacts in a HubSpot list for issues (bounces, unsubscribes, lifecycle)
and check for recent sales emails (engagements).
"""
import os
import sys
import time
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ["HUBSPOT_ACCESS_TOKEN"]
BASE = "https://api.hubapi.com"
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}

LIST_ID = "1648"

# --- Step 1: Get all contacts in the list ---
print(f"Fetching contacts from list {LIST_ID}...")
contacts = []
after = None

while True:
    url = f"{BASE}/crm/v3/lists/{LIST_ID}/memberships"
    params = {"limit": 100}
    if after:
        params["after"] = after

    resp = requests.get(url, headers=headers, params=params)
    resp.raise_for_status()
    data = resp.json()

    results = data.get("results", [])
    for r in results:
        contacts.append(r.get("recordId") or r.get("vid") or r)

    paging = data.get("paging", {})
    after = paging.get("next", {}).get("after")
    if not after:
        break
    time.sleep(0.1)

print(f"Total contacts in list: {len(contacts)}")

if not contacts:
    print("No contacts found.")
    sys.exit(0)

# --- Step 2: Fetch contact properties in batches ---
print("\nFetching contact details...")
contact_details = []
batch_size = 100

for i in range(0, len(contacts), batch_size):
    batch_ids = contacts[i:i+batch_size]
    payload = {
        "inputs": [{"id": str(cid)} for cid in batch_ids],
        "properties": [
            "email", "firstname", "lastname",
            "hs_email_hard_bounce_reason_enum",
            "hs_email_bounce",
            "hs_email_optout",
            "hs_marketable_status",
            "lifecyclestage",
            "hubspot_owner_id",
            "hs_sales_email_last_replied",
            "hs_last_sales_activity_timestamp",
            "hs_email_last_send_date",
            "notes_last_contacted",
            "num_contacted_notes",
            "hs_email_open",
            "hs_email_click",
        ],
    }
    resp = requests.post(
        f"{BASE}/crm/v3/objects/contacts/batch/read",
        headers=headers,
        json=payload,
    )
    resp.raise_for_status()
    for c in resp.json().get("results", []):
        props = c.get("properties", {})
        contact_details.append({
            "id": c["id"],
            "email": props.get("email", ""),
            "name": f"{props.get('firstname','') or ''} {props.get('lastname','') or ''}".strip(),
            "lifecycle": props.get("lifecyclestage", ""),
            "hard_bounce": props.get("hs_email_hard_bounce_reason_enum", ""),
            "bounce_count": props.get("hs_email_bounce", ""),
            "unsubscribed": props.get("hs_email_optout", ""),
            "non_marketing": props.get("hs_marketable_status", ""),
            "last_sales_activity": props.get("hs_last_sales_activity_timestamp", ""),
            "sales_email_replied": props.get("hs_sales_email_last_replied", ""),
            "last_email_sent": props.get("hs_email_last_send_date", ""),
            "last_contacted": props.get("notes_last_contacted", ""),
            "num_contacted": props.get("num_contacted_notes", ""),
            "email_opens": props.get("hs_email_open", ""),
            "email_clicks": props.get("hs_email_click", ""),
        })
    time.sleep(0.1)

# --- Step 3: Categorize issues ---
hard_bounced = [c for c in contact_details if c["hard_bounce"]]
unsubscribed = [c for c in contact_details if c["unsubscribed"] == "true"]
non_marketing = [c for c in contact_details if c["non_marketing"] == "false"]
no_lifecycle = [c for c in contact_details if not c["lifecycle"]]
customers = [c for c in contact_details if c["lifecycle"] in ("customer", "opportunity")]

# --- Step 4: Recent sales activity (last 90 days) ---
from datetime import datetime, timezone, timedelta
cutoff_90 = datetime.now(timezone.utc) - timedelta(days=90)
cutoff_30 = datetime.now(timezone.utc) - timedelta(days=30)

def parse_ts(ts_str):
    if not ts_str:
        return None
    try:
        ts = int(ts_str)
        return datetime.fromtimestamp(ts / 1000, tz=timezone.utc)
    except:
        try:
            return datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
        except:
            return None

recently_contacted_30 = []
recently_contacted_90 = []
for c in contact_details:
    ts = parse_ts(c["last_sales_activity"]) or parse_ts(c["last_contacted"]) or parse_ts(c["sales_email_replied"])
    if ts:
        if ts >= cutoff_30:
            recently_contacted_30.append(c)
        elif ts >= cutoff_90:
            recently_contacted_90.append(c)

# --- Step 5: Print summary ---
print(f"\n{'='*60}")
print(f"LIST REVIEW: Marketing Outreach - Primary v2 (ID {LIST_ID})")
print(f"{'='*60}")
print(f"Total contacts: {len(contact_details)}")

print(f"\n--- ISSUES ---")
print(f"Hard bounced:          {len(hard_bounced)}")
print(f"Unsubscribed:          {len(unsubscribed)}")
print(f"Non-marketing status:  {len(non_marketing)}")
print(f"No lifecycle stage:    {no_lifecycle and len(no_lifecycle) or 0}")
print(f"Protected (Customer/Opp): {len(customers)}")

print(f"\n--- RECENT SALES ACTIVITY ---")
print(f"Contacted last 30 days:  {len(recently_contacted_30)}")
print(f"Contacted last 90 days:  {len(recently_contacted_90)}")

# --- Print hard-bounced detail ---
if hard_bounced:
    print(f"\n--- HARD BOUNCED CONTACTS ({len(hard_bounced)}) ---")
    for c in hard_bounced[:20]:
        print(f"  {c['id']:>10}  {c['email']:<45}  bounce={c['hard_bounce']}  count={c['bounce_count']}")
    if len(hard_bounced) > 20:
        print(f"  ... and {len(hard_bounced)-20} more")

# --- Print unsubscribed detail ---
if unsubscribed:
    print(f"\n--- UNSUBSCRIBED CONTACTS ({len(unsubscribed)}) ---")
    for c in unsubscribed[:20]:
        print(f"  {c['id']:>10}  {c['email']:<45}  lifecycle={c['lifecycle']}")
    if len(unsubscribed) > 20:
        print(f"  ... and {len(unsubscribed)-20} more")

# --- Print recently contacted ---
if recently_contacted_30:
    print(f"\n--- CONTACTED IN LAST 30 DAYS ({len(recently_contacted_30)}) ---")
    for c in sorted(recently_contacted_30, key=lambda x: x["last_sales_activity"] or "", reverse=True)[:20]:
        ts = parse_ts(c["last_sales_activity"]) or parse_ts(c["last_contacted"])
        date_str = ts.strftime("%Y-%m-%d") if ts else "?"
        print(f"  {c['id']:>10}  {c['email']:<45}  last_activity={date_str}  lifecycle={c['lifecycle']}")

if recently_contacted_90:
    print(f"\n--- CONTACTED 31-90 DAYS AGO ({len(recently_contacted_90)}) ---")
    for c in sorted(recently_contacted_90, key=lambda x: x["last_sales_activity"] or "", reverse=True)[:20]:
        ts = parse_ts(c["last_sales_activity"]) or parse_ts(c["last_contacted"])
        date_str = ts.strftime("%Y-%m-%d") if ts else "?"
        print(f"  {c['id']:>10}  {c['email']:<45}  last_activity={date_str}  lifecycle={c['lifecycle']}")

# --- Protected contacts ---
if customers:
    print(f"\n--- PROTECTED (Customer/Opportunity) ({len(customers)}) ---")
    for c in customers:
        print(f"  {c['id']:>10}  {c['email']:<45}  lifecycle={c['lifecycle']}")
