from pyrogram import Client, filters
from pyrogram.types import Message

from app.utils import fn


@Client.on_message(filters.me & filters.command('ppic', prefixes='.'))
async def get_group_userpics(client: Client, message: Message):
    chat = fn.get_command_args(message, command='ppic')
    print('Начался процесс парсинга юзеров')
    file_ids = [member.user.photo.big_file_id async for member in client.get_chat_members(chat_id=chat, limit=1000)
                if member.user.photo]

    print(f'Начался процесс парсинга аватарок из {len(file_ids)}')
    count = 0
    for file_id in file_ids:
        try:
            await client.download_media(file_id, f'downloads/{chat}/')
            count += 1
            print(count)
        except Exception as err:
            print(err)

    print(f'Процесс окончен! Спарсено {count} аватарок')


@Client.on_message(filters.me & filters.command('mpic', prefixes='.'))
async def get_message_userpics(client: Client, message: Message):
    chat = fn.get_command_args(message, command='mpic')

    print('Начался процесс парсинга юзеров')
    file_ids = []
    async for member in client.search_messages(chat, limit=100):
        if not member.from_user:
            continue
        if member.from_user.photo not in file_ids:
            file_ids.append(member.from_user.photo.big_file_id)

    print(f'Начался процесс парсинга аватарок из {len(file_ids)}')
    count = 0
    for file_id in file_ids:
        try:
            await client.download_media(file_id, f'downloads/{chat}/')
            count += 1
            print(count)
        except Exception as err:
            print(err)
    print(f'Процесс окончен! Спарсено {count} аватарок')
