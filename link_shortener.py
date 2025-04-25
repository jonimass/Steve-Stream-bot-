from pyrogram import Client, filters
from pyrogram.types import Message
import requests

@Client.on_message(filters.command("shorten"))
async def shorten_link(client, message: Message):
    if len(message.command) < 2:
        return await message.reply("Usage: `/shorten https://example.com`", quote=True)
    
    long_url = message.command[1]
    api_url = f"https://tinyurl.com/api-create.php?url={long_url}"
    response = requests.get(api_url)
    
    if response.status_code == 200:
        short_url = response.text
        await message.reply(f"🔗 Shortened URL:\n`{short_url}`", quote=True)
    else:
        await message.reply("Failed to shorten the link.", quote=True)
