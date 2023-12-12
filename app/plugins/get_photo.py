from pyrogram import Client, filters
from pyrogram.types import Message, InputMediaPhoto

from app.utils import fn


@Client.on_message(filters.me & filters.command('photo_byid', prefixes='.'))
@fn.with_args("<b>This command don't work without args</b>")
async def get_photo_by_id(client: Client, message: Message):
    await message.delete()

    file_id = fn.get_command_args(message, 'photo_byid')

    try:
        await client.send_photo(message.chat.id, photo=file_id)
    except:
        await message.reply('<emoji id=5210952531676504517>❌</emoji>Not found')


@Client.on_message(filters.me & filters.command('ava', prefixes='.'))
async def get_avatar(client: Client, message: Message):
    await message.delete()

    limit = fn.get_command_args(message, 'ava')
    if not limit:
        limit = 0

    chat_photos = [InputMediaPhoto(photo.file_id) async for photo in client.get_chat_photos(message.chat.id, limit=limit)]

    try:
        if not chat_photos:
            return await client.send_message('me', '<emoji id=5210952531676504517>❌</emoji>Not found')

        if len(chat_photos) <= 2:
            for _ in range(len(chat_photos)):
                await client.send_photo('me', chat_photos[0])
        else:
            for i in range(0, len(chat_photos), 10):
                media = chat_photos[i:i+10]
                print(media)
                await client.send_media_group('me', media=media)
    except Exception as e:
        await client.send_message('me', f'<emoji id=5210952531676504517>❌</emoji>Error <code>{e}</code>')
