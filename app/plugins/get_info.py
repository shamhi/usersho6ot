from pyrogram import Client, filters
from pyrogram.types import Message

from app.utils import fn



@Client.on_message(filters.me & filters.command('info', prefixes='.'))
async def send_info(client: Client, message: Message):
    await message.delete()

    target = fn.get_command_args(message, 'info')
    if not target:
        if message.reply_to_message:
            target = message.reply_to_message

        try:
            await client.send_message('me', text=f"<pre language=json>{target}</pre>")
        except:
            await client.send_message('me', text=f"<pre language=json>{message.chat}</pre>")

        return

    try:
        chat = await client.get_chat(target)
        if len(str(chat)) > 4096:
            chat = await fn.paste_yaso(str(message))
        await client.send_message('me', text=f"<pre language=json>{chat}</pre>")
    except:
        chat = 'Not found'
        await client.send_message('me', text=chat)


@Client.on_message(filters.me & filters.command('full_info', prefixes='.'))
async def send_full_info(client: Client, message: Message):
    await message.delete()

    target = fn.get_command_args(message, 'full_info')
    if not target:
        if len(str(message)) > 4096:
            message = await fn.paste_yaso(str(message))
        return await client.send_message('me', text=f"<pre language=json>{message}</pre>")

    try:
        chat = await client.get_chat(target)
        if len(str(chat)) > 4096:
            chat = await fn.paste_yaso(str(message))
        await client.send_message('me', text=f"<pre language=json>{chat}</pre>")
    except:
        chat = '<emoji id=5210952531676504517>❌</emoji>Not found'
        await client.send_message('me', text=chat)


@Client.on_message(filters.me & filters.command('emoji', prefixes='.'))
@fn.with_reply
async def get_emoji_info(client: Client, message: Message):
    emoji = f'<pre language=json>"text": "{message.reply_to_message.text}"\n"entities": {message.reply_to_message.entities}</pre>'

    if len(str(emoji)) > 4096:
        emoji = await fn.paste_yaso(str(emoji))

    await message.edit(emoji)
