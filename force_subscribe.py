from pyrogram import Client, filters
from pyrogram.types import Message
from config import FORCE_SUB_CHANNEL

@Client.on_message(filters.private & filters.incoming)
async def force_sub(client, message: Message):
    try:
        user = await client.get_chat_member(FORCE_SUB_CHANNEL, message.from_user.id)
        if user.status not in ["member", "administrator", "creator"]:
            await message.reply(f"Please join @{FORCE_SUB_CHANNEL} to use this bot.")
    except:
        await message.reply(f"Please join @{FORCE_SUB_CHANNEL} to use this bot.")
