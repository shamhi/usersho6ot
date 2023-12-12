from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode

from app.utils import nums

import asyncio


@Client.on_message(filters.me & filters.command(['all_command', 'commands', 'cmds'], prefixes='.'))
async def get_all_commands(client: Client, message: Message):
    all_commands = {
        f'{nums.get(1)} <code>calc, c</code>': '<b><i>A simple calculator</i></b>\n'
                                               '<b><emoji id=5821116867309210830>🔃</emoji>Example</b> <code>.calc 2+2*2</code>\n\n',
        f'{nums.get(2)} <code>ppic</code>': '<b><i>Parse userpics of members from groups, supergroups and channels</i></b>\n'
                                            '<b><emoji id=5821116867309210830>🔃</emoji>Example</b> <code>.ppic @group_username (limit: int)</code>\n\n',
        f'{nums.get(3)} <code>mpic</code>': '<b><i>Parse userpics of members by messages from groups, supergroups and channels</i></b>\n'
                                            '<b><emoji id=5821116867309210830>🔃</emoji>Example</b> <code>.mpic @group_username (limit: int)</code>\n\n',
        f'{nums.get(4)} <code>python, py</code>': '<b><i>Execute python code and output result</i></b>\n'
                                                  '<b><emoji id=5821116867309210830>🔃</emoji>Example</b> <code>.python print("Hello world")</code>\n\n',
        f'{nums.get(5)} <code>read_stories, rss</code>': '<b><i>Looking stories users from groups, supergroups and channels</i></b>\n'
                                                         '<b><emoji id=5821116867309210830>🔃</emoji>Example</b> <code>.read_stories @group_username</code>\n\n',
        f'{nums.get(6)} <code>chatgpt, gpt</code>': '<b><i>Send request to GPT and output result</i></b>\n'
                                                    '<b><emoji id=5821116867309210830>🔃</emoji>Example</b> <code>.gpt Write a simple code on cpp</code>\n\n',
        f'{nums.get(7)} <code>ip</code>': '<b><i>Send info and location by ip-address</i></b>\n'
                                          '<b><emoji id=5821116867309210830>🔃</emoji>Example</b> <code>.ip 172.86.219.18</code>\n\n',
        f'{nums.get(8)} <code>mychats, myc</code>': '<b><i>Send all chats that user has</i></b>\n'
                                                    '<b><emoji id=5821116867309210830>🔃</emoji>Example</b> <code>.myc *args **kwargs</code>\n\n',
        f'{nums.get(9)} <code>full_info, info</code>': '<b><i>Send info about chat, user or message</i></b>\n'
                                                       '<b><emoji id=5821116867309210830>🔃</emoji>Example</b> <code>.full_info *args **kwargs</code>\n\n',
        f'{nums.get(1)}{nums.get(0)} <code>photo_byid</code>': '<b><i>Send photo by file id</i></b>\n'
                                                               '<b><emoji id=5821116867309210830>🔃</emoji>Example</b> <code>.photo_byid "file_id"</code>\n\n',
        f'{nums.get(1)}{nums.get(1)} <code>emoji</code>': '<b><i>Send info about emoji by reply</i></b>\n'
                                                          '<b><emoji id=5821116867309210830>🔃</emoji>Example</b> <code>.emoji *args **kwargs</code>\n\n',
        f'{nums.get(1)}{nums.get(2)} <code>ava</code>': '<b><i>Send avatars from chat</i></b>\n'
                                                          '<b><emoji id=5821116867309210830>🔃</emoji>Example</b> <code>.ava "limit(int)"</code>\n\n',
        f'{nums.get(1)}{nums.get(3)} <code>all_commands, commands, cmds</code>': '<b><i>Send all available commands</i></b>\n'
                                                                                 '<b><emoji id=5821116867309210830>🔃</emoji>Example</b> <code>.commands *args **kwargs</code>\n\n'
    }

    text = ''
    for cmd, desc in all_commands.items():
        text += f"{cmd} : {desc}"
        await message.edit(text)
        await asyncio.sleep(.1)
