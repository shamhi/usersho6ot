from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode

from app.utils import fn

@Client.on_message(filters.me & filters.command(['calc', 'c'], prefixes='.'))
async def send_calculate(client: Client, message: Message):
    args = fn.get_command_args(message, ['calc', 'c'])

    if not args:
        return await message.reply('Args is None')

    try:
        await message.edit(f'**__{args}__** = **`{eval(args)}`**', parse_mode=ParseMode.MARKDOWN)
    except Exception as er:
        await message.edit(f"**__{args}__** = **`{er}`**", parse_mode=ParseMode.MARKDOWN)
