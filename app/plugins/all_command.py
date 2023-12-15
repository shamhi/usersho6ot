from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.enums import ParseMode

from app.utils import nums

import asyncio


def num(n):
    return "".join([nums.get(int(str(n)[i])) for i in range(len(str(n)))])


def hcode(s):
    return f"<code>{s}</code>"


def rload():
    ...


@Client.on_message(filters.me & filters.command(['all_command', 'commands', 'cmds'], prefixes='.'))
async def get_all_commands(client: Client, message: Message):
    all_commands = {
        f'{num(1)} {hcode("calc, c")}': '<b><i>A simple calculator</i></b>\n'
                                        f'<b><emoji id=5821116867309210830>🔃</emoji>Example</b> {hcode(".calc 2+2*2")}\n\n',
        f'{num(2)} {hcode("ppic")}': '<b><i>Parse userpics of members from groups, supergroups and channels</i></b>\n'
                                     f'<b><emoji id=5821116867309210830>🔃</emoji>Example</b> {hcode(".ppic @group_username (limit: int)")}\n\n',
        f'{num(3)} {hcode("mpic")}': '<b><i>Parse userpics of members by messages from groups, supergroups and channels</i></b>\n'
                                     '<b><emoji id=5821116867309210830>🔃</emoji>Example</b> {hcode(".mpic @group_username (limit: int)")}\n\n',
        f'{num(4)} {hcode("python, py")}': '<b><i>Execute python code and output result</i></b>\n'
                                           f'<b><emoji id=5821116867309210830>🔃</emoji>Example</b> {hcode(".python print(message.text)")}\n\n',
        f'{num(5)} {hcode("read_stories, rss")}': '<b><i>Looking stories users from groups, supergroups and channels</i></b>\n'
                                                  f'<b><emoji id=5821116867309210830>🔃</emoji>Example</b> {hcode(".read_stories @group_username")}\n\n',
        f'{num(6)} {hcode("chatgpt, gpt")}': '<b><i>Send request to GPT and output result</i></b>\n'
                                             f'<b><emoji id=5821116867309210830>🔃</emoji>Example</b> {hcode(".gpt Write a simple code on cpp")}\n\n',
        f'{num(7)} {hcode("ip")}': '<b><i>Send info and location by ip-address</i></b>\n'
                                   f'<b><emoji id=5821116867309210830>🔃</emoji>Example</b> {hcode(".ip 172.86.219.18")}\n\n',
        f'{num(8)} {hcode("mychats, myc")}': '<b><i>Send all chats that user has</i></b>\n'
                                             f'<b><emoji id=5821116867309210830>🔃</emoji>Example</b> {hcode(".myc *args **kwargs")}\n\n',
        f'{num(9)} {hcode("full_info, info")}': '<b><i>Send info about chat, user or message</i></b>\n'
                                                f'<b><emoji id=5821116867309210830>🔃</emoji>Example</b> {hcode(".full_info *args **kwargs")}\n\n',
        f'{num(1)}{num(0)} {hcode("photo_byid")}': '<b><i>Send photo by file id</i></b>\n'
                                                   f'<b><emoji id=5821116867309210830>🔃</emoji>Example</b> {hcode(".photo_byid `file_id`")}\n\n',
        f'{num(1)}{num(1)} {hcode("emoji, em")}': '<b><i>Send info about emoji by reply</i></b>\n'
                                                  f'<b><emoji id=5821116867309210830>🔃</emoji>Example</b> {hcode(".emoji *args **kwargs")}\n\n',
        f'{num(1)}{num(2)} {hcode("emoji_list, eml")}': '<b><i>Send avatars from chat</i></b>\n'
                                                        f'<b><emoji id=5821116867309210830>🔃</emoji>Example</b> {hcode(".eml *args **kwargs")}\n\n',
        f'{num(1)}{num(3)} {hcode("ava")}': '<b><i>Send avatars from chat</i></b>\n'
                                            f'<b><emoji id=5821116867309210830>🔃</emoji>Example</b> {hcode(".ava `limit(int)`")}\n\n',
        f'{num(1)}{num(4)} {hcode("all_commands, commands, cmds")}': '<b><i>Send all available commands</i></b>\n'
                                                                     f'<b><emoji id=5821116867309210830>🔃</emoji>Example</b> {hcode(".commands *args **kwargs")}\n\n'
    }

    text = ''
    for cmd, desc in all_commands.items():
        text += f"{cmd} : {desc}"
        await message.edit(text)
        await asyncio.sleep(.1)
