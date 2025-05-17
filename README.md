# Not Your AI Job Filter

A Python-based prototype to connect to your Outlook.com inbox via the Microsoft Graph API, fetch recent job alert emails, and lay the groundwork for AI-assisted job filtering.

This is the project foundation. Later versions will classify, score, and organize emails based on relevance to your skills and preferences.

---

## 📦 Features

- Secure OAuth2 login using MSAL (Microsoft Authentication Library)
- Connects to your personal Microsoft account (Outlook.com)
- Fetches your 5 most recent emails
- Skips re-authentication if a cached token is available
- Future-proofed for filtering, tagging, or sorting job-related messages

---

## 🛠️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/not_your_ai_job_filter.git
cd not_your_ai_job_filter
````

### 2. Create and Activate a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate          # macOS/Linux
.venv\Scripts\activate             # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Microsoft Entra App Registration (One-Time Setup)

1. Go to [https://entra.microsoft.com](https://entra.microsoft.com)
2. Sign in with your **Outlook.com** or **Microsoft personal account**
3. Navigate to **Microsoft Entra ID > App registrations**
4. Click **+ New registration**

### Registration Fields:

| Field                   | Value                                                                      |
| ----------------------- | -------------------------------------------------------------------------- |
| Name                    | `JobFilterAI`                                                              |
| Supported account types | ✅ Accounts in any organizational directory and personal Microsoft accounts |
| Redirect URI            | ✅ Mobile & desktop → `http://localhost`                                    |

### After Creating the App:

1. Go to **Authentication** tab

   * Under **Platform configurations**, ensure `http://localhost` is added
   * Under **Advanced settings**, enable **Allow public client flows**

2. Go to **API permissions** tab

   * Click **+ Add a permission** → **Microsoft Graph** → **Delegated permissions**
   * Add: `Mail.Read`
   * Click **Grant admin consent** if available

3. Copy your:

   * **Application (client) ID**
   * **Directory (tenant) ID**

---

## 🔧 Configure Your Environment

Create a file named `.env` in the root directory:

```env
CLIENT_ID=your_app_client_id_here
TENANT_ID=your_tenant_id_here
```

Never commit this file to GitHub — it contains credentials.

---

## 🚀 Running the Script

```bash
python fetch_graph_emails.py
```

### What Happens:

* The script tries to log in silently using a cached token
* If none found or it’s expired, it opens a browser login
* Upon success, it calls Microsoft Graph to retrieve your 5 most recent emails
* Prints subject, sender, and preview text to the terminal

---

## 🧱 Project Structure

```bash
not_your_ai_job_filter/
├── fetch_graph_emails.py      # Main script
├── requirements.txt           # Dependencies
├── .env                       # Local credentials (not committed)
├── .gitignore                 # Ignores .env, .venv, pyc files
└── README.md                  # This file
```

---

## 🛣️ Next Steps (Planned)

* ⛏️ Extract and parse job alert emails (e.g., from LinkedIn, Indeed)
* 🧠 Filter or score based on your skills, preferences, and red flags
* 🗂️ Move emails into folders (`Mail.ReadWrite` permission required)
* 💾 Save parsed data to `.json` or SQLite
* 🖼️ Build a dashboard or CLI summary

---

## 🧰 Dev Notes

If you ever want to regenerate `requirements.txt` from your current environment:

```bash
pip freeze > requirements.txt
```

If MSAL login issues persist, try deleting cached tokens by calling:

```python
for acct in app.get_accounts():
    app.remove_account(acct)
```

---

## 🛡️ Disclaimer

This is a personal utility project, not affiliated with Microsoft, Outlook, or any job platform. Do not share `.env` or access tokens publicly.
