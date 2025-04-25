import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("temp"))
async def temp_message(client, message: Message):
    sent = await message.reply("⏳ This message will auto-delete in 10 seconds.")
    await asyncio.sleep(10)
    await sent.delete()
    await message.delete()
