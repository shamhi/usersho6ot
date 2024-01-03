from pyrogram import Client, filters
from pyrogram.types import Message

from app.utils import fn


@Client.on_message(filters.me & filters.command('del', prefixes='.'))
@fn.with_reply
async def delete_message(client: Client, message: Message):
    await message.delete()
    await message.reply_to_message.delete()

