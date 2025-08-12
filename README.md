# Monday Bot 🤖 | Your AI-Powered Discord Assistant

Monday Bot is an AI-powered Discord chatbot that uses **Google's Gemini AI** (`gemini-1.5-flash-latest`) to provide intelligent, conversational responses.  
Ask questions, get instant answers, and make your Discord server smarter — all with a single `!ask` command.

---

## 📖 What is Monday Bot?

Monday Bot was built to bring AI-assisted conversations to Discord without complicated setups.  
It acts as a personal assistant inside your server — able to answer questions, explain concepts, and respond naturally.  
By leveraging **Google Generative AI**, it delivers fast and relevant answers in real time.

---

## ✨ Features

- 🗣 **Ask Anything** – Just type `!ask <your question>` and get an AI-generated answer
- ⚡ **Powered by Gemini AI** – Uses Google's latest generative AI model
- 🔒 **Secure** – API keys stored in `.env` file (never exposed)
- 🎯 **Lightweight** – Minimal dependencies, easy to run locally or on a server
- 📦 **Open Source** – Modify and extend as you wish

---

## 🛠 Installation Guide

### 1️⃣ Clone the repository
```bash
git clone https://github.com/mukesh207/monday_Bot.git
cd monday_Bot
```

# Create venv
python -m venv venv

# Activate on Linux/Mac
source venv/bin/activate

# Activate on Windows
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up your .env file
DISCORD_BOT_TOKEN=your_discord_bot_token_here
GEMINI_API_KEY=your_gemini_api_key_here

#  How to get your Discord Bot Token
  Go to the Discord Developer Portal
  
  Click New Application → Name it (e.g., "Monday Bot")
  
  Go to Bot → Click Add Bot
  
  Under Token, click Reset Token and copy it
  
  Enable MESSAGE CONTENT INTENT under "Privileged Gateway Intents"
  
  Invite your bot to a server:
  
  Go to OAuth2 → URL Generator
  
  Select bot scope and Send Messages + Read Message History permissions
  
  Copy the generated link and open it in your browser to add the bot

# How to get your Gemini API Key
  Go to Google AI Studio

  Sign in with your Google account
  
  Go to Get API Key
  
  Copy the key and paste it into your .env under GEMINI_API_KEY

# Run the bot
python monday_Bot/bot.py

| Command           | Description                              |
| ----------------- | ---------------------------------------- |
| `!ask <question>` | Ask Gemini AI a question and get a reply |

