from functools import wraps
from pyrogram.types import Message
from config import PREMIUM_USERS

def premium_only(func):
    @wraps(func)
    async def wrapper(client, message: Message):
        if message.from_user.id not in PREMIUM_USERS:
            return await message.reply("❌ This feature is only for premium users.")
        return await func(client, message)
    return wrapper
