from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.raw.functions.contacts import Search

from app.utils import fn


@Client.on_message(filters.me & filters.command('get', prefixes='.'))
async def search_chats(client: Client, message: Message):
    query = fn.get_command_args(message, 'get')

    if len(query) < 4:
        return await message.edit('<emoji id=5210952531676504517>❌</emoji><b>Length of your query must be more 3 symbols</b>')

    await message.edit(f'<emoji id=5206607081334906820>✔️</emoji>Процесс поиска чатов по запросу <code>{query}</code>')


    results = await client.invoke(Search(q=query, limit=100))
    chats = results.chats
    users = results.users

    header = f'<b><i>Query: </i></b> <code>{query}</code>'
    chats = ''.join([f'{i+1}. {chat.title} - @{chat.username if chat.username else chat.usernames[0].username}\n' for i, chat in enumerate(chats)])
    users = ''.join([f'{i+1}. {user.first_name}{" " + user.last_name if user.last_name else ""} - @{user.username if user.username else user.usernames[0].username}\n' for i, user in enumerate(users)])
    text = f'{header}\n\n{chats}\n{users}'

    if len(text) >= 4096:
        return await message.edit(await fn.paste_yaso(str(text)))

    await message.edit(text)
