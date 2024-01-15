import asyncio
import random

from pyrogram import Client, filters
from pyrogram.types import Message

from app.utils import fn


@Client.on_message(filters.me & filters.command('spam', prefixes='.'))
@fn.with_args("<b>This command don't work without args\n"
              "Command accepts such args as <i>\n"
              "{user (required), sec (optional=0), limit (optional=100), text (optional=\"random\")}</i></b>")
async def spam_to_user(client: Client, message: Message):
    await message.delete()

    args = fn.get_command_args(message, 'spam')
    user, *args = args.split()

    text = 'default'
    sec = 'default'
    limit = 'default'

    if args:
        sec = args[0]
    if len(args) > 1:
        limit = args[1]
    if len(args) > 2:
        text = " ".join(args[2:])

    limit = int(limit) if limit != 'default' else 100
    sec = int(sec) if sec != 'default' else 0
    text = [fn.generate_random_string(30) for _ in range(limit)] if text.lower() in ['default', 'generate', 'random'] \
        else text

    for _ in range(limit):
        await client.send_message(user, random.choice(text) if isinstance(text, list) else text)
        await asyncio.sleep(sec)
