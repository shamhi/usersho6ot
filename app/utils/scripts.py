from typing import Union

from pyrogram import Client
from pyrogram.types import Message, Chat

import asyncio
import aiohttp
import string
import random

from app.config import Config


def get_command_args(message: Union[Message, str], command: Union[str, list[str]] = None, prefixes: str = '.') -> str:
    if isinstance(message, str):
        return message.split(f'{prefixes}{command}', maxsplit=1)[-1].strip()

    if isinstance(command, str):
        args = message.text.split(f'{prefixes}{command}', maxsplit=1)[-1].strip()
        return args

    elif isinstance(command, list):
        for cmd in command:
            args = message.text.split(f'{prefixes}{cmd}', maxsplit=1)[-1]

            if args != message.text:
                return args.strip()

    return ''


def get_reply_to_message_info(target: Message) -> str:
    return f'ㅤㅤㅤㅤㅤㅤㅤㅤ**USER INFO**ㅤㅤㅤㅤㅤㅤㅤㅤ\n' \
           f'User ID: `{target.from_user.id}`\n' \
           f'User Name: `{target.from_user.username}`\n' \
           f'User Status: `{target.from_user.status}`\n' \
           f'Is premium: `{target.from_user.is_premium}`\n' \
           f'Date: `{target.date}`\n\n' \
           f'ㅤㅤㅤㅤㅤㅤㅤㅤ**CHAT INFO**ㅤㅤㅤㅤㅤㅤㅤㅤ\n' \
           f'Chat ID: `{target.chat.id}`\n' \
           f'Chat Type: `{target.chat.type}`\n' \
           f'Chat Name: `{target.chat.username}`\n' \
           f'Reply Text: `{target.text}`'


def get_chat_info(message: Chat) -> str:
    return f'ㅤㅤㅤㅤㅤㅤㅤㅤ**CHAT INFO**ㅤㅤㅤㅤㅤㅤㅤㅤ\n' \
           f'Chat ID: `{message.id}`\n' \
           f'Chat Type: `{message.type}`\n' \
           f'Chat Name: `{message.username}`\n'


def with_reply(func):
    async def wrapped(client: Client, message: Message):
        if not message.reply_to_message:
            await message.edit('<b>Reply to message is required</b>')
        else:
            return await func(client, message)

    return wrapped


def with_args(text: str):
    def decorator(func):
        async def wrapped(client: Client, message: Message):
            if message.text and len(message.text.split()) == 1:
                await message.edit(text)
            else:
                return await func(client, message)

        return wrapped

    return decorator


async def get_gpt_response(query: str) -> str:
    url = "https://api.edenai.run/v2/text/chat"

    payload = {
        "temperature": 0,
        "max_tokens": 1000,
        "providers": "openai",
        "openai": "gpt-3.5-turbo",
        "text": query
    }

    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": f"Bearer {Config.EDEN_API}"
    }
    try:
        async with aiohttp.ClientSession() as session:
            response = await session.post(url, json=payload, headers=headers)
            if response.status == 429:
                retry_after = int(response.headers.get("Retry-After"))
                await asyncio.sleep(retry_after)
            response_data = await response.json()
            answer = response_data.get('openai', {}).get('generated_text')

        return answer
    except Exception as er:
        return f'Error\n```\n{er}\n```'


async def get_info_by_ip(ip: str) -> str:
    async with aiohttp.ClientSession() as session:
        async with session.get(f'http://ip-api.com/json/{ip}') as response:
            data = await response.json()

            info_data = {
                '<b>[IP]</b>': f'<code>{data.get("query")}</code>',
                '<b>[Provider]</b>': f'<code>{data.get("isp")}</code>',
                '<b>[Org]</b>': f'<code>{data.get("org")}</code>',
                '<b>[Country]</b>': f'<code>{data.get("country")}</code>',
                '<b>[Region]</b>': f'<code>{data.get("regionName")}</code>',
                '<b>[City]</b>': f'<code>{data.get("city")}</code>',
                '<b>[ZIP]</b>': f'<code>{data.get("zip")}</code>',
                '<b>[Lat]</b>': f'<code>{data.get("lat")}</code>',
                '<b>[Lon]</b>': f'<code>{data.get("lon")}</code>'
            }

            result = ''.join([f'{k} : {v}\n' for k, v in info_data.items()])

            return result, data.get('lat'), data.get('lon')


async def speech_to_text(file_bytes):
    try:
        url = "https://api.edenai.run/v2/audio/speech_to_text_async"
        headers = {"authorization": f"Bearer {Config.EDEN_API}"}
        data = {
            "providers": "openai",
            "language": "ru-RU",
        }
        files = {'file': file_bytes}
        print(0)
        async with aiohttp.ClientSession() as session:
            print(1)
            async with session.post(url, data=data, headers=headers, files=files) as response:
                print(2)
                result = await response.json()
                print(3)
                public_id = result.get('public_id')

                async with session.get(f'https://api.edenai.run/v2/audio/speech_to_text_async/{public_id}',
                                       headers=headers) as result:
                    print(4)
                    result = await result.json()
                    text = result.get('result', {}).get('openai', {}).get('text')

                    return text
    except Exception as er:
        return f'Error\n```\n{er}\n```'


def generate_random_string(length: int) -> str:
    characters = string.ascii_letters + string.digits
    return "".join([random.choice(characters) for _ in range(length)])

async def paste_yaso(code: str, expiration_time: int = 10080):
    try:
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=False)) as session:
            async with session.post(
                "https://api.yaso.su/v1/auth/guest",
            ) as auth:
                auth.raise_for_status()

            async with session.post(
                "https://api.yaso.su/v1/records",
                json={
                    "captcha": generate_random_string(569),
                    "codeLanguage": "auto",
                    "content": code,
                    "expirationTime": expiration_time,
                },
            ) as paste:
                paste.raise_for_status()
                result = await paste.json()
                print(result)
                print(type(result))
    except Exception:
        return "Pasting failed"
    else:
        return f"https://yaso.su/{result.get('url')}"
