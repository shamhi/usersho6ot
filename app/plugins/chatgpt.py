from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode

from app.utils import fn


@Client.on_message(filters.me & filters.command(['gpt', 'chatgpt'], prefixes='.'))
async def send_gpt_response(client: Client, message: Message):
    query = fn.get_command_args(message, ['gpt', 'chatgpt'])

    if not query:
        if message.reply_to_message:
            query = message.reply_to_message.text
        else:
            return await message.edit('Query is None')

    response = await fn.get_gpt_response(query)

    try:
        if len(response) > 4096:
            response = await fn.paste_yaso(response)
        await message.edit(text=f'__Query__: **__{query}__**\n\n'
                                f'{response}', parse_mode=ParseMode.MARKDOWN)
    except:
        await message.edit(text=f'Query: {query}\n\n'
                                f'{response}')

