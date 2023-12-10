from pyrogram import Client, filters
from pyrogram.types import Message

from datetime import datetime
import json
import os


@Client.on_message(filters.me & filters.command(['mychats', 'myc'], prefixes='.'))
async def get_my_chats(client: Client, message: Message):
    await message.delete()
    file_path = f'downloads/my_chats/{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.json'
    data = [{
        'ID': obj.chat.id,
        'Name': obj.chat.username,
        'Type': str(obj.chat.type)
    } async for obj in client.get_dialogs()]

    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


    await client.send_document('me', document=file_path)

    try: os.remove(file_path)
    except: ...
