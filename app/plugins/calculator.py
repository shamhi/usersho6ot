from pyrogram import Client, filters
from pyrogram.types import Message

from app.utils import fn

@Client.on_message(filters.me & filters.command(['calc', 'c'], prefixes='.'))
async def send_calculate(client: Client, message: Message):
    args = fn.get_command_args(message, ['calc', 'c'])

    if not args:
        return await message.reply('Args is None')

    try:
        await message.edit(f'<pre language=json>{args} = {eval(args)}</pre>')
    except Exception as er:
        await message.edit(f"<pre language=json>{args}: {er}</pre>")
