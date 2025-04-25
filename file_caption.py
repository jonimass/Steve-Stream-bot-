from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@Client.on_message(filters.document | filters.video | filters.audio)
async def send_with_caption(client, message: Message):
    file = message.document or message.video or message.audio
    caption = f"**File Name:** {file.file_name}\n**Size:** {round(file.file_size / (1024 * 1024), 2)} MB"

    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("Download Now", url=message.link)]
    ])

    await message.reply_document(
        document=file.file_id,
        caption=caption,
        reply_markup=buttons
    )
