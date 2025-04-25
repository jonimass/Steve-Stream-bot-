from pyrogram import Client
from config import API_ID, API_HASH, BOT_TOKEN

app = Client("TelegramBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

# Import handlers
from handlers import start, force_subscribe

print("Bot started...")
app.run()
