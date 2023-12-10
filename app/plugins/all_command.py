from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode

import asyncio


@Client.on_message(filters.me & filters.command(['all_command', 'commands', 'cmds'], prefixes='.'))
async def get_all_commands(client: Client, message: Message):
    all_commands = {
        '<emoji id=5305763715692377402>1️⃣</emoji> <code>calc, c</code>': '<b><i>A simple calculator</i></b>\n'
                                                                          '<b><emoji id=5821116867309210830>🔃</emoji>Example</b> <code>.calc 2+2*2</code>\n\n',
        '<emoji id=5307907239380528763>2️⃣</emoji> <code>ppic</code>': '<b><i>Parse userpics of members from groups, supergroups and channels</i></b>\n'
                                                                       '<b><emoji id=5821116867309210830>🔃</emoji>Example</b> <code>.ppic @group_username (limit: int)</code>\n\n',
        '<emoji id=5305783000095537258>3️⃣</emoji> <code>mpic</code>': '<b><i>Parse userpics of members by messages from groups, supergroups and channels</i></b>\n'
                                                                       '<b><emoji id=5821116867309210830>🔃</emoji>Example</b> <code>.mpic @group_username (limit: int)</code>\n\n',
        '<emoji id=5305255243104138538>4️⃣</emoji> <code>python, py</code>': '<b><i>Execute python code and output result</i></b>\n'
                                                                             '<b><emoji id=5821116867309210830>🔃</emoji>Example</b> <code>.python print("Hello world")</code>\n\n',
        '<emoji id=5305288155438526869>5️⃣</emoji> <code>read_stories, rss</code>': '<b><i>Looking stories users from groups, supergroups and channels</i></b>\n'
                                                                                    '<b><emoji id=5821116867309210830>🔃</emoji>Example</b> <code>.read_stories @group_username</code>\n\n',
        '<emoji id=5305642863902604489>6️⃣</emoji> <code>chatgpt, gpt</code>': '<b><i>Send request to GPT and output result</i></b>\n'
                                                                               '<b><emoji id=5821116867309210830>🔃</emoji>Example</b> <code>.gpt Write a simple code on cpp</code>\n\n',
        '<emoji id=5305603955793867793>7️⃣</emoji> <code>ip</code>': '<b><i>Send info and location by ip-address</i></b>\n'
                                                                     '<b><emoji id=5821116867309210830>🔃</emoji>Example</b> <code>.ip 172.86.219.18</code>\n\n',
        '<emoji id=5305371288825509083>8️⃣</emoji> <code>mychats, myc</code>': '<b><i>Send all chats that user has</i></b>\n'
                                                                               '<b><emoji id=5821116867309210830>🔃</emoji>Example</b> <code>.myc *args **kwargs</code>\n\n',
        '<emoji id=5307703499016910744>9️⃣</emoji> <code>full_info, info</code>': '<b><i>Send info about chat, user or message</i></b>\n'
                                                                                  '<b><emoji id=5821116867309210830>🔃</emoji>Example</b> <code>.full_info *args **kwargs</code>\n\n',
        '<emoji id=5305763715692377402>1️⃣</emoji><emoji id=5305749482170758709>0️⃣</emoji> <code>emoji</code>': '<b><i>Send info about emoji by reply</i></b>\n'
                                                                                  '<b><emoji id=5821116867309210830>🔃</emoji>Example</b> <code>.emoji *args **kwargs</code>\n\n',
        '<emoji id=5305763715692377402>1️⃣</emoji><emoji id=5305749482170758709>0️⃣</emoji> <code>all_commands, commands, cmds</code>': '<b><i>Send all available commands</i></b>\n'
                                                                                                                                        '<b><emoji id=5821116867309210830>🔃</emoji>Example</b> <code>.commands *args **kwargs</code>\n\n'
    }

    text = ''
    for cmd, desc in all_commands.items():
        text += f"{cmd} : {desc}"
        await message.edit(text, parse_mode=ParseMode.HTML)
        await asyncio.sleep(.1)
