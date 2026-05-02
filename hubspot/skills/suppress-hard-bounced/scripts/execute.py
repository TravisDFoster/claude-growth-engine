# /// script
# requires-python = ">=3.10"
# dependencies = ["requests", "python-dotenv"]
# ///
"""
Execute (API part): Create HubSpot active list for hard-bounced contacts.
Also creates optional review list for contacts with 3+ bounces.
"""
import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ["HUBSPOT_ACCESS_TOKEN"]
BASE = "https://api.hubapi.com"
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}

# --- List 1: All hard-bounced contacts ---
list_payload = {
    "name": "CLEANUP: Hard Bounced Contacts",
    "objectTypeId": "0-1",
    "processingType": "DYNAMIC",
    "filterBranch": {
        "filterBranchType": "OR",
        "filterBranches": [
            {
                "filterBranchType": "AND",
                "filterBranches": [],
                "filters": [
                    {
                        "filterType": "PROPERTY",
                        "property": "hs_email_hard_bounce_reason_enum",
                        "operation": {
                            "operationType": "ALL_PROPERTY",
                            "operator": "IS_KNOWN",
                        },
                    }
                ],
            }
        ],
        "filters": [],
    },
}

resp = requests.post(f"{BASE}/crm/v3/lists", headers=headers, json=list_payload)

if resp.status_code in (200, 201):
    list_data = resp.json()
    list_id = list_data.get("listId") or list_data.get("list", {}).get("listId")
    print(f"[OK] CLEANUP list created. ID: {list_id}")
elif resp.status_code == 409:
    print("[SKIP] CLEANUP list already exists (409). Use the existing list.")
else:
    print(f"[FAIL] Could not create CLEANUP list: {resp.status_code} — {resp.text[:300]}")

# --- List 2: 3+ bounces review list ---
review_payload = {
    "name": "REVIEW: 3+ Bounces - Possible Delete",
    "objectTypeId": "0-1",
    "processingType": "DYNAMIC",
    "filterBranch": {
        "filterBranchType": "OR",
        "filterBranches": [
            {
                "filterBranchType": "AND",
                "filterBranches": [],
                "filters": [
                    {
                        "filterType": "PROPERTY",
                        "property": "hs_email_bounce",
                        "operation": {
                            "operationType": "NUMBER",
                            "operator": "IS_GREATER_THAN",
                            "value": 2,
                        },
                    }
                ],
            }
        ],
        "filters": [],
    },
}

resp2 = requests.post(f"{BASE}/crm/v3/lists", headers=headers, json=review_payload)

if resp2.status_code in (200, 201):
    review_data = resp2.json()
    review_id = review_data.get("listId") or review_data.get("list", {}).get("listId")
    print(f"[OK] REVIEW list created. ID: {review_id}")
elif resp2.status_code == 409:
    print("[SKIP] REVIEW list already exists (409). Use the existing list.")
else:
    print(f"[FAIL] Could not create REVIEW list: {resp2.status_code} — {resp2.text[:300]}")
