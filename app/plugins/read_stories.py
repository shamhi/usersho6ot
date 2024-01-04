from pyrogram import Client, filters
from pyrogram.types import Message

from random import choice
import asyncio

from app.utils import fn



@Client.on_message(filters.me & filters.command(['read_stories', 'rss'], prefixes='.'))
@fn.with_args("<b>This command don't work without args</b>")
async def read_stories(client: Client, message: Message):
    args = fn.get_command_args(message, ['read_stories', 'rss'])
    if len(args.split()) > 1:
        target_chat = args.split()[0]
        limit = int(args.split()[1])
    else:
        target_chat = args
        limit = 0
    await message.edit(f'<emoji id=5981043230160981261>⏱</emoji>Начался процесс парсинга юзеров из чата '
                       f'<code>{target_chat}</code><emoji id=5256026508346011293>🔤</emoji>')
    members = [member.user.id async for member in client.get_chat_members(target_chat, limit=limit)
               if not member.user.is_stories_unavailable and not member.user.is_deleted]
    await message.edit(f'<emoji id=5981043230160981261>⏱</emoji>Начался процесс просмотра сторисов у {len(members)} '
                       f'юзеров из чата <code>{target_chat}</code><emoji id=5256026508346011293>🔤</emoji>')
    count = 0
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

            count += 1
        except:
            ...

    await message.edit(f'<emoji id=5206607081334906820>✔️</emoji>Процесс завершен, просмотрено {count} сторисов у '
                       f'{len(members)} юзеров из чата <code>{target_chat}</code>')
