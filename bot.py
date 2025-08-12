import os
import discord
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables from .env
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)

# Use a supported model
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash-latest")

# Setup Discord bot
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!ask"):
        prompt = message.content[len("!ask"):].strip()

        if not prompt:
            await message.channel.send("💬 Please type something after `!ask`.")
            return

        await message.channel.send("🤖 Thinking...")

        try:
            response = model.generate_content(prompt)
            reply = response.text.strip()
            await message.channel.send(reply[:2000])  # Discord max msg length
        except Exception as e:
            await message.channel.send(f"⚠️ Gemini API error: {str(e)}")

# Run the bot
client.run(DISCORD_TOKEN)
