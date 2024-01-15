import re

from pyrogram import Client, filters
from pyrogram.types import Message

from app.utils import fn


@Client.on_message(filters.me & filters.command('ip', prefixes='.'))
async def send_ip_info(client: Client, message: Message):
    ip = fn.get_command_args(message, 'ip')

    IP_PATTERN = r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
    if not re.match(IP_PATTERN, ip):
        return await message.edit(text=f'{ip} is not ip-address')

    try:
        info, lat, lon = await fn.get_info_by_ip(ip)
        await message.edit(text=f'<pre language=json>{info}</pre>')
        await message.reply_location(latitude=lat, longitude=lon)
    except:
        ...
