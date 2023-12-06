import pyrogram.errors
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode, ChatType

from pyrogram_patch.router import Router
import asyncio

from app.functions import fn

router = Router()


@router.on_message(filters.me & filters.command('info', prefixes='.'))
async def send_info(client: Client, message: Message):
    await message.delete()

    target = fn.get_command_args(message, 'info')
    if target == '':
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


@router.on_message(filters.me & filters.command('full_info', prefixes='.'))
async def send_full_info(client: Client, message: Message):
    await message.delete()

    target = fn.get_command_args(message, 'full_info')
    if target == '':
        await client.send_message('me', text=message)
        return

    try:
        chat = await client.get_chat(target)
        await client.send_message('me', text=chat)
    except:
        chat = 'Not found'
        await client.send_message('me', text=chat)


@router.on_message(filters.me & filters.command('gpt', prefixes='.'))
async def send_gpt_response(client: Client, message: Message):
    await message.delete()

    query = fn.get_command_args(message, 'gpt')

    if query == '':
        return await message.reply('Query is None')

    if message.reply_to_message:
        query = message.reply_to_message.text

    response = await fn.get_gpt_response(query)

    try:
        await message.reply(text=response, parse_mode=ParseMode.MARKDOWN)
    except:
        await message.reply(text=response)


@router.on_message(filters.me & filters.command('ip', prefixes='.'))
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


@router.on_message(filters.me & filters.command('typing', prefixes='.'))
async def send_typing_msg(client: Client, message: Message):
    orig_text = fn.get_command_args(message, 'typing')
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
        except pyrogram.errors.FloodWait as e:
            await asyncio.sleep(e)


@router.on_message(filters.voice | filters.audio)
async def send_stt_to_me(client: Client, message: Message):
    file_bytes = await client.download_media(message, in_memory=True)
    text = await fn.speech_to_text(file_bytes)

    await client.send_message('me', text)
