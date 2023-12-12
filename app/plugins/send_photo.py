from pyrogram import Client, filters
from pyrogram.types import Message

from app.utils import fn


@Client.on_message(filters.me & filters.command('photo_byid', prefixes='.'))
@fn.with_args("<b>This command don't work without args</b>")
async def send_photo_by_id(client: Client, message: Message):
    file_id = fn.get_command_args(message, 'photo_byid')

    try:
        await client.send_photo(message.chat.id, photo=file_id)
    except:
        await message.edit(f'<emoji id=5210952531676504517>❌</emoji>Not found')
