from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait

from zipfile import ZipFile
from datetime import datetime
import asyncio
import os

from app.utils import fn


@Client.on_message(filters.me & filters.command('ppic', prefixes='.'))
@fn.with_args("<b>This command don't work without args</b>")
async def get_group_userpics(client: Client, message: Message):
    args = fn.get_command_args(message, command='ppic')
    if len(args.split()) > 1:
        chat = args.split()[0]
        limit = int(args.split()[1])
    else:
        chat = args
        limit = 0

    await message.edit(f'<emoji id=5947553854030614234>🟡</emoji>Начался процесс парсинга юзеров из чата <code>{chat}</code><emoji id=5256026508346011293>🔤</emoji>')
    file_ids = [member.user.photo.big_file_id async for member in client.get_chat_members(chat_id=chat, limit=limit)
                if member.user.photo]

    await message.edit(
        f'<emoji id=5947553854030614234>🟡</emoji>Начался процесс парсинга аватарок у {len(file_ids)} юзеров из чата <code>{chat}</code><emoji id=5256026508346011293>🔤</emoji>')
    path = f'app/downloads/{chat}.zip'
    count = 0
    for file_id in file_ids:
        try:
            with ZipFile(path, 'a') as archive:
                file_bytes = await client.download_media(file_id, in_memory=True)
                file_name = f'chat_photo_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_{"".join(str(datetime.timestamp(datetime.now())).split("."))}.jpg'
                with open('app/downloads/temp.jpg', 'wb') as f:
                    f.write(file_bytes.getvalue())

                archive.write('app/downloads/temp.jpg', file_name)

                count += 1
        except:
            ...

    await message.edit(f'<emoji id=5206607081334906820>✔️</emoji>Процесс окончен! Спарсено {count} аватарок у {len(file_ids)} юзеров из чата <code>{chat}</code>')

    await client.send_document('me', document=path)

    try:
        os.remove('app/downloads/temp.jpg')
        os.remove(path)
    except:
        ...


@Client.on_message(filters.me & filters.command('mpic', prefixes='.'))
@fn.with_args("<b>This command don't work without args</b>")
async def get_message_userpics(client: Client, message: Message):
    args = fn.get_command_args(message, command='mpic')
    if len(args.split()) > 1:
        chat = args.split()[0]
        limit = int(args.split()[1])
    else:
        chat = args
        limit = 0

    check = await client.get_chat(chat)
    if not check.permissions.can_send_messages:
        return await message.edit('<emoji id=5210952531676504517>❌</emoji>Невозможно спарсить юзеров по сообщениям')

    await message.edit(f'<emoji id=5947553854030614234>🟡</emoji>Начался процесс парсинга юзеров из чата <code>{chat}</code>')

    file_ids = []
    async for member in client.search_messages(chat, limit=limit):
        if not member.from_user:
            continue
        if member.from_user.photo not in file_ids:
            file_ids.append(member.from_user.photo.big_file_id)

    await message.edit(f'<emoji id=5947553854030614234>🟡</emoji>Начался процесс парсинга аватарок у {len(file_ids)} юзеров из чата <code>{chat}</code>')

    path = f'app/downloads/{chat}.zip'
    count = 0
    for file_id in file_ids:
        try:
            with ZipFile(path, 'a') as archive:
                file_bytes = await client.download_media(file_id, in_memory=True)
                file_name = f'chat_photo_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_{"".join(str(datetime.timestamp(datetime.now())).split("."))}.jpg'
                with open('app/downloads/temp.jpg', 'wb') as f:
                    f.write(file_bytes.getvalue())

                archive.write('app/downloads/temp.jpg', file_name)

                count += 1
        except:
            ...

    await message.edit(f'<emoji id=5206607081334906820>✔️</emoji>Процесс окончен! Спарсено {count} аватарок у {len(file_ids)} юзеров из чата <code>{chat}</code>')

    await client.send_document('me', document=path)

    try:
        os.remove('app/downloads/temp.jpg')
        os.remove(path)
    except:
        ...
