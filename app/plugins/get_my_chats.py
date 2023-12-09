from pyrogram import Client, filters
from pyrogram.types import Message



@Client.on_message(filters.me & filters.command(['mychats', 'myc'], prefixes='.'))
async def get_my_chats(client: Client, message: Message):
    await message.delete()
    async for _ in client.get_dialogs():
        print(_.chat.username, _.chat.type)
