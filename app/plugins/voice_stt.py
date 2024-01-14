from pyrogram import Client, filters
from pyrogram.types import Message

from app.utils import fn


@Client.on_message((filters.audio | filters.voice | filters.video | filters.video_note) & filters.private)
async def parse_text(client: Client, message: Message):
    path = await client.download_media(message, file_name='downloads/media.mp3')
    file_bytes = fn.get_file_bytes_by_path(path)

    parsed_text = await fn.speech_to_text(file_bytes=file_bytes)
    await client.send_message('me', text=f"@{message.chat.username}\n\n{parsed_text}")
