from pyrogram import Client, filters
from pyrogram.types import Message
from googletrans import Translator, LANGCODES

from app.utils import fn, rload


@Client.on_message(filters.me & filters.command(['translate', 'tr', 'p'], prefixes='.'))
async def translate_text(client: Client, message: Message):
    await message.edit(rload())

    translator = Translator()
    args = fn.get_command_args(message, ['translate', 'tr', 'p'])

    if not args:
        return await message.edit('<emoji id=5210952531676504517>❌</emoji><b>Your args is empty</b>')

    if message.reply_to_message:
        dest = args.split()[0]
        text = message.reply_to_message.text
    else:
        dest, *text = args.split()
        text = " ".join(text)

    if dest not in LANGCODES.values():
        return await message.edit(f'<emoji id=5210952531676504517>❌</emoji><b>{dest}</b> is not lang code')

    translated = translator.translate(text, dest=dest)
    text = translated.text
    from_lang = translated.src
    to_lang = translated.dest

    return await message.edit(f'From <b><i>{from_lang}</i></b> to <b><i>{to_lang}</i></b>\n\n{text}')
