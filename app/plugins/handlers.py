import pyrogram.errors

from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode

import asyncio

from app.utils import fn


@Client.on_message(filters.me & filters.command('info', prefixes='.'))
async def send_info(client: Client, message: Message):
    await message.delete()

    target = fn.get_command_args(message, 'info')
    if not target:
        if message.reply_to_message:
            target = message.reply_to_message
            info = fn.get_reply_to_message_info(target)
        else:
            info = fn.get_chat_info(message.chat)

        try:
            await client.send_message('me', text=info, parse_mode=ParseMode.MARKDOWN)
        except:
            await client.send_message('me', text=message.chat)

        return

    try:
        chat = await client.get_chat(target)
        info = fn.get_chat_info(chat)

        await client.send_message('me', text=info)
    except:
        chat = 'Not found'
        await client.send_message('me', text=chat)


@Client.on_message(filters.me & filters.command('full_info', prefixes='.'))
async def send_full_info(client: Client, message: Message):
    await message.delete()

    target = fn.get_command_args(message, 'full_info')
    if not target:
        await client.send_message('me', text=message)
        return

    try:
        chat = await client.get_chat(target)
        await client.send_message('me', text=chat)
    except:
        chat = 'Not found'
        await client.send_message('me', text=chat)


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
        await message.edit(text=f'__Query__: **__{query}__**\n\n'
                                f'{response}', parse_mode=ParseMode.MARKDOWN)
    except:
        await message.edit(text=f'Query: {query}\n\n'
                                f'{response}')


@Client.on_message(filters.me & filters.command('ip', prefixes='.'))
async def send_ip_info(client: Client, message: Message):
    import re

    await message.delete()

    ip = fn.get_command_args(message, 'ip')

    IP_PATTERN = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    if not re.match(IP_PATTERN, ip):
        return await message.reply(text=f'{ip} is not ip-address')

    try:
        info, lat, lon = await fn.get_info_by_ip(ip)
        await message.reply(text=info, parse_mode=ParseMode.HTML)
        await message.reply_location(latitude=lat, longitude=lon)
    except:
        ...



# @router.on_message(filters.voice | filters.audio)
async def send_stt_to_me(client: Client, message: Message):
    media = await client.download_media(message, in_memory=True)
    file_bytes = media.getvalue()
    text = await fn.speech_to_text(file_bytes)

    await client.send_message('me', text)
