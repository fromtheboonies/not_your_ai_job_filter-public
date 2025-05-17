import os
import requests
from dotenv import load_dotenv
from msal import PublicClientApplication

# Load credentials from .env
load_dotenv()

CLIENT_ID = os.getenv("CLIENT_ID")
TENANT_ID = os.getenv("TENANT_ID")
AUTHORITY = "https://login.microsoftonline.com/common"
SCOPES = ["Mail.Read"]

# Initialize the MSAL public client
app = PublicClientApplication(
    client_id=CLIENT_ID,
    authority=AUTHORITY,
)

# Try silent token acquisition
accounts = app.get_accounts()
if accounts:
    print("🔄 Attempting silent login...")
    result = app.acquire_token_silent(SCOPES, account=accounts[0])
else:
    result = None

# Fallback to interactive login if needed
if not result or "access_token" not in result:
    print("🔐 Prompting for login...")
    result = app.acquire_token_interactive(scopes=SCOPES)

# Proceed if authentication succeeded
if "access_token" in result:
    access_token = result["access_token"]
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json"
    }

    # Request latest emails
    response = requests.get(
        "https://graph.microsoft.com/v1.0/me/messages?$top=5",
        headers=headers
    )

    # Print response
    if response.status_code == 200:
        print("✅ Email data retrieved successfully!")
        print(response.text)
    else:
        print(f"❌ API call failed: {response.status_code}")
        print(response.text)
else:
    print("❌ Authentication failed:", result.get("error_description"))
