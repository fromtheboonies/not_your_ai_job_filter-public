<p align="center">
  ![Not Your AI Job Filter banner](https://raw.githubusercontent.com/fromtheboonies/not_your_ai_job_filter-public/main/assets/not-your-ai-job-filter-banner.png)
</p>

# Not Your AI Job Filter

A lightweight Python-based prototype for fetching emails from a Microsoft Outlook.com inbox using the Microsoft Graph API. This project serves as a foundation for developing intelligent job alert filtering tools powered by automation or AI.

> ⚡ I originally built this to clean up my inbox during a casual job search. It now serves as a platform to experiment with email classification, NLP filtering, and automation workflows.

> 💡 This repo is a sanitized, public version of a personal utility project. It does not include real credentials or production logic.

---

## 📦 Features

- Secure OAuth2 login using MSAL (Microsoft Authentication Library)
- Connects to personal Microsoft accounts (e.g., Outlook.com)
- Fetches the 5 most recent messages from your inbox
- Reuses cached tokens when available to avoid repeated login prompts
- Provides a base for future email filtering, scoring, and classification

---

## 🛠️ Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/not_your_ai_job_filter-public.git
cd not_your_ai_job_filter-public
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

## 🔐 Microsoft Entra App Registration

To use this project with your Outlook.com inbox, you'll need to register an application with Microsoft Entra (formerly Azure Active Directory).

### Steps:

1. Go to [https://entra.microsoft.com](https://entra.microsoft.com)
2. Sign in with your Microsoft account
3. Navigate to **Microsoft Entra ID > App registrations**
4. Click **+ New registration**

| Field                   | Value                                                                      |
| ----------------------- | -------------------------------------------------------------------------- |
| Name                    | `JobFilterAI`                                                              |
| Supported account types | ✅ Accounts in any organizational directory and personal Microsoft accounts |
| Redirect URI            | ✅ Mobile & desktop → `http://localhost`                                    |

### After Registration:

* Go to **Authentication**:

  * Ensure `http://localhost` is added under platform configurations
  * Enable **"Allow public client flows"**

* Go to **API Permissions**:

  * Add: `Mail.Read` (delegated)
  * Click “Grant admin consent” if available

* Copy your:

  * `Application (client) ID`
  * `Directory (tenant) ID`

---

## 🔧 Environment Configuration

Save `example.env` file as `.env` file in the root directory and update the credentials with what was generated in Microsoft Entra Overview page for your app:

```env
CLIENT_ID=your_app_client_id_here
TENANT_ID=your_tenant_id_here
```

> ⚠️ **Do not commit this file** — it contains sensitive credentials for your registered app.

---

## 🚀 Running the Script

> 🧪 Try it in 3 minutes:
> 1. Register your app on https://entra.microsoft.com
> 2. Fill in your credentials in `.env` (use the example.env file)
> 3. Run `python fetch_graph_emails.py`

```bash
python fetch_graph_emails.py
```

This will:

* Attempt silent login using MSAL token cache
* If no valid token exists, prompt you to authenticate via browser
* Retrieve and print the 5 most recent messages from your inbox

---

## 🧱 Project Structure

```bash
not_your_ai_job_filter-public/
├── fetch_graph_emails.py      # Main script
├── requirements.txt           # Python dependencies
├── .env                       # Your credentials (excluded from Git)
├── .gitignore                 # Prevents tracking sensitive/dev files
└── README.md                  # You are here
```

---

## 📌 Future Enhancements (Ideas)

* Keyword- or skill-based job alert filtering
* Message scoring and classification
* Automatic tagging or folder sorting (e.g., “Ignore”, “Worth Reviewing”)
* Export messages to JSON, CSV, or a local database
* Optional GPT/NLP-based ranking of job listings

---

## 🧰 Dev Notes

To regenerate your `requirements.txt` from your virtual environment:

```bash
pip freeze > requirements.txt
```

If MSAL token cache issues arise, you can clear cached accounts manually:

```python
for acct in app.get_accounts():
    app.remove_account(acct)
```

---

## 🛡️ License

This project is licensed under the [MIT License](LICENSE).
You're free to use, modify, and distribute it — attribution is appreciated.

---

## 🙋‍♂️ Want to Use This As a Starter?

You're welcome to fork and adapt this project. If you build something cool on top of it, let me know — I'd love to check it out!
