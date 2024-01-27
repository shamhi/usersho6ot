from time import perf_counter

from pyrogram import Client, filters
from pyrogram.types import Message

from app.utils import fn


@Client.on_message(filters.me & filters.command('ping', prefixes='.'))
async def pong(client: Client, message: Message):
    start = perf_counter()
    await message.edit("<b>🏓Pong!</b>")
    end = perf_counter()
    await message.edit(f"<b>🏓Pong! {round(end - start, 3)}s</b>")
