from pyrogram.types import Message, Chat
import asyncio
import aiohttp

from app.config import Config


def get_command_args(message: Message, cmd_name: str = None, prefixes: str = '.') -> str:
    if isinstance(cmd_name, str):
        args = message.text.split(f'{prefixes}{cmd_name}', maxsplit=1)[-1].strip()
        return args

    return message.text


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
