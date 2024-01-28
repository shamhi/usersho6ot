from pyrogram import Client, filters
from pyrogram.types import Message

from app.utils import fn, rcheck


@Client.on_message(filters.me & filters.command('mr', prefixes='.'))
@fn.with_args("<b>This command don't work without args</b>")
async def mark_chat_as_read(client: Client, message: Message):
    chat = fn.get_command_args(message, 'mr')

    if chat == "all":
        chats = [obj.chat.id async for obj in client.get_dialogs() if obj.unread_messages_count]
        count = 0
        for chat in chats:
            await client.read_chat_history(chat_id=chat)
            count += 1
    else:
        count = 1
        await client.read_chat_history(chat_id=chat)

    await message.edit(text=f"{rcheck()}Mark as read {count} chats from")
