from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait
import asyncio

from app.utils import fn


@Client.on_message(filters.me & filters.command(['typing', 'tp'], prefixes='.'))
async def send_typing_msg(client: Client, message: Message):
    orig_text = fn.get_command_args(message, ['typing', 'tp'])
    if not orig_text:
        if message.reply_to_message:
            orig_text = message.reply_to_message.text
        else:
            return await message.edit('Not found')

    text = orig_text
    tbp = ''
    sym = 'ㅤ'  # ░ㅤ👀

    while tbp != orig_text:
        try:
            await message.edit(tbp + sym)
            await asyncio.sleep(.1)
            tbp += text[0]
            text = text[1:]
            await message.edit(tbp)
            await asyncio.sleep(.1)
        except FloodWait as e:
            await asyncio.sleep(e)
