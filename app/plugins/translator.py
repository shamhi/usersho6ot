from pyrogram import Client, filters
from pyrogram.types import Message

from googletrans import Translator, LANGCODES

from app.utils import fn, rload


@Client.on_message(filters.me & filters.command(['translate', 'tr', 'p'], prefixes='.'))
@fn.with_args("<b>This command don't work without args</b>")
async def translate_text(client: Client, message: Message):
    await message.edit(rload())

    translator = Translator()
    args = fn.get_command_args(message, ['translate', 'tr', 'p'])

    if len(args.split()) > 1:
        dest, *text = args.split()

        text = " ".join(text)
        if dest not in LANGCODES.values():
            return await message.edit(f'<emoji id=5210952531676504517>❌</emoji>{dest} is not lang code')

        ttext = translator.translate(text, dest=dest).text

        return await message.edit(ttext)
