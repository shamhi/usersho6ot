from pyrogram import Client, filters
from pyrogram.types import Message

from random import choice
import asyncio

from app.utils import fn



@Client.on_message(filters.me & filters.command(['read_stories', 'rss'], prefixes='.'))
async def read_stories(client: Client, message: Message):
    target_chat = fn.get_command_args(message, ['read_stories', 'rss'])
    try:
        members = [member.user.id async for member in client.get_chat_members(target_chat)
                   if not member.user.is_stories_unavailable and not member.user.is_deleted]
        for member in members:
            try:
                if not client.search_messages_count(target_chat, from_user=member):
                    continue

                stories = await client.read_stories(chat_id=member, max_id=(1 << 31)-1)
                if stories:
                    for story_id in stories:
                        emojis = ["❤️", "👍", "🔥", "🎉", "🤩", "😱", "😁", "🥰", "🤯", "🤔", "👏"]
                        await client.send_reaction(chat_id=member, story_id=story_id, emoji=choice(emojis))
                        await asyncio.sleep(.1)
                    print(f'Просмотр сторис у пользователя {member} из группы {target_chat}')
            except Exception as err:
                print(err)
    except Exception as err:
        print(err)
