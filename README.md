# 📦 Placement Bot (Telegram UserBot)

A Telegram userbot that:
✅ Listens to specific private placement groups  
✅ Filters messages containing keywords like "internship", "hiring", etc.  
✅ Forwards matched messages to your Saved Messages  
✅ Runs as a FastAPI web service to stay alive on Railway

---

## ⚙️ Features
- Built with **Telethon** (Telegram userbot framework)
- Runs as a **background task** with FastAPI
- Keeps filtered logs in `filtered_msgs.txt`

---

## 🚀 How to deploy on Railway

1. Clone or fork this repo
2. Add these environment variables in Railway:
   | Key      | Value                                    |
   |--------|-------------------------------------------|
   | API_ID | Your numeric Telegram API ID (from https://my.telegram.org) |
   | API_HASH | Your Telegram API hash                   |

3. Make sure you have in your repo:
- `main.py`
- `requirements.txt`
- `Procfile`

4. Click **Deploy** in Railway

---

## 🧪 How to run locally

```bash
# Create virtual env (recommended)
python -m venv .venv
source .venv/Scripts/activate  # On Windows
source .venv/bin/activate     # On Linux/Mac

# Install dependencies
pip install -r requirements.txt

# Set environment variables (replace with your values)
set API_ID=1234567
set API_HASH=your_api_hash

# Start
uvicorn main:app --host=0.0.0.0 --port=8000
