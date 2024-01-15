import asyncio

from pyrogram import Client, filters
from pyrogram.types import Message

from app.utils import fn


@Client.on_message(filters.me & filters.command('del', prefixes='.'))
@fn.with_reply
async def delete_message(client: Client, message: Message):
    await message.delete()
    await message.reply_to_message.delete()


@Client.on_message(filters.me & filters.command('purge', prefixes='.'))
@fn.with_reply
async def purge(client: Client, message: Message):
    chunk = []
    async for msg in client.get_chat_history(chat_id=message.chat.id):
        if msg.id < message.reply_to_message.id:
            break

        chunk.append(msg.id)
        if len(chunk) >= 100:
            await client.delete_messages(chat_id=message.chat.id, message_ids=chunk)
            chunk.clear()
            await asyncio.sleep(1)

    if chunk:
        await client.delete_messages(chat_id=message.chat.id, message_ids=chunk)
