from pyrogram import Client, filters
from pyrogram.types import Message

from app.utils import fn


@Client.on_message(filters.me & filters.command('stt', prefixes='.'))
@fn.with_reply
async def parse_text(client: Client, message: Message):
    await message.delete()

    path = await client.download_media(message.reply_to_message, file_name='downloads/media.mp3')
    file_bytes = fn.get_file_bytes_by_path(path)

    parsed_text = await fn.speech_to_text(file_bytes=file_bytes)
    await client.send_message('me', text=f"@{message.chat.username}\n\n{parsed_text}")
