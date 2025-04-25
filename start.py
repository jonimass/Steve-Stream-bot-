from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.command("start"))
async def start_message(client, message: Message):
    await message.reply("Welcome to the bot!")
