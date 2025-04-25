from pyrogram import Client, filters
from pyrogram.types import Message
from utils.decorators import premium_only

@Client.on_message(filters.command("secret"))
@premium_only
async def secret_feature(client, message: Message):
    await message.reply("This is a secret feature for premium users!")
