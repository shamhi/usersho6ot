from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.errors import FloodWait

from app.utils import nums, rload

import asyncio


def num(n):
    return "".join([nums.get(int(str(n)[i])) for i in range(len(str(n)))])


def hcode(s):
    return f"<code>{s}</code>"


@Client.on_message(filters.me & filters.command(['all_command', 'commands', 'cmds'], prefixes='.'))
async def get_all_commands(client: Client, message: Message):
    all_commands = {
        f'{num(1)} {hcode("calc, c")}': '<b><i>A simple calculator</i></b>\n'
                                        f'<b>{rload()}Example</b> {hcode(".calc 2+2*2")}\n\n',
        f'{num(2)} {hcode("ppic")}': '<b><i>Parse userpics of members from groups, supergroups and channels</i></b>\n'
                                     f'<b>{rload()}Example</b> {hcode(".ppic @group_username (limit: int)")}\n\n',
        f'{num(3)} {hcode("mpic")}': '<b><i>Parse userpics of members by messages from groups, supergroups and channels</i></b>\n'
                                     f'<b>{rload()}Example</b> {hcode(".mpic @group_username (limit: int)")}\n\n',
        f'{num(4)} {hcode("python, py")}': '<b><i>Execute python code and output result</i></b>\n'
                                           f'<b>{rload()}Example</b> {hcode(".python print(message.text)")}\n\n',
        f'{num(5)} {hcode("read_stories, rss")}': '<b><i>Looking stories users from groups, supergroups and channels</i></b>\n'
                                                  f'<b>{rload()}Example</b> {hcode(".read_stories @group_username")}\n\n',
        f'{num(6)} {hcode("chatgpt, gpt")}': '<b><i>Send request to GPT and output result</i></b>\n'
                                             f'<b>{rload()}Example</b> {hcode(".gpt Write a simple code on cpp")}\n\n',
        f'{num(7)} {hcode("ip")}': '<b><i>Send info and location by ip-address</i></b>\n'
                                   f'<b>{rload()}Example</b> {hcode(".ip 172.86.219.18")}\n\n',
        f'{num(8)} {hcode("mychats, myc")}': '<b><i>Send all chats that user has</i></b>\n'
                                             f'<b>{rload()}Example</b> {hcode(".myc *args **kwargs")}\n\n',
        f'{num(9)} {hcode("full_info, info")}': '<b><i>Send info about chat, user or message</i></b>\n'
                                                f'<b>{rload()}Example</b> {hcode(".full_info *args **kwargs")}\n\n',
        f'{num(10)} {hcode("photo_byid")}': '<b><i>Send photo by file id</i></b>\n'
                                            f'<b>{rload()}Example</b> {hcode(".photo_byid `file_id`")}\n\n',
        f'{num(11)} {hcode("emoji, em")}': '<b><i>Send info about emoji by reply</i></b>\n'
                                           f'<b>{rload()}Example</b> {hcode(".emoji *args **kwargs")}\n\n',
        f'{num(12)} {hcode("emoji_list, eml")}': '<b><i>Send avatars from chat</i></b>\n'
                                                 f'<b>{rload()}Example</b> {hcode(".eml *args **kwargs")}\n\n',
        f'{num(13)} {hcode("avatars, ava")}': '<b><i>Send avatars from chat</i></b>\n'
                                              f'<b>{rload()}Example</b> {hcode(".ava `limit(int)`")}\n\n',
        f'{num(14)} {hcode("translate, tr, p")}': '<b><i>Send avatars from chat</i></b>\n'
                                                  f'<b>{rload()}Example</b> {hcode(".tr dest(`en`, `ru`), text")}\n\n',
        f'{num(15)} {hcode("spam")}': '<b><i>Send messages to user</i></b>\n'
                                      f'<b>{rload()}Example</b> {hcode(".spam user (required), sec (optional=0), limit (optional=100), text (optional=random)")}\n\n',
        f'{num(16)} {hcode("weather")}': '<b><i>Send weather info</i></b>\n'
                                         f'<b>{rload()}Example</b> {hcode(".weather Moscow")}\n\n',
        f'{num(17)} {hcode("all_commands, commands, cmds")}': '<b><i>Send all available commands</i></b>\n'
                                                              f'<b>{rload()}Example</b> {hcode(".commands *args **kwargs")}\n\n'
    }

    text = ''
    i = 0
    for cmd, desc in all_commands.items():
        text += f"{cmd} : {desc}"

        if i % 2 == 0:
            try:
                await message.edit(text)
            except FloodWait as e:
                if isinstance(e, int):
                    await asyncio.sleep(e)
                else:
                    return await message.edit(f'<b><emoji id=5210952531676504517>❌</emoji>Error: <pre>{e}</pre></b>')
            await asyncio.sleep(.1)

        i += 1
