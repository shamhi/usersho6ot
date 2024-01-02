from typing import Union

from pyrogram import Client
from pyrogram.types import Message, Chat

import asyncio
import aiohttp
import string
import random
import datetime

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


def with_reply(func):
    async def wrapped(client: Client, message: Message):
        if not message.reply_to_message:
            await message.edit('<emoji id=5210952531676504517>❌</emoji><b>Reply to message is required</b>')
        else:
            return await func(client, message)

    return wrapped


def with_args(text: str):
    def decorator(func):
        async def wrapped(client: Client, message: Message):
            if message.text and len(message.text.split()) == 1:
                await message.edit(f'<emoji id=5210952531676504517>❌</emoji>{text}')
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
    except Exception:
        return "Pasting failed"
    else:
        return f"https://yaso.su/{result.get('url')}"


async def get_weather(city):
    try:
        code_to_smile = {
            "Clear": "Ясно \U00002600",
            "Clouds": "Облачно \U00002601",
            "Rain": "Дождь \U00002614",
            "Drizzle": "Дождь \U00002614",
            "Thunderstorm": "Гроза \U000026A1",
            "Snow": "Снег \U0001F328",
            "Mist": "Туман \U0001F32B"
        }

        url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={Config.WEATHER_API}&units=metric'

        async with aiohttp.request('GET', url=url) as response:
            data = await response.json()

        weather_description = data.get('weather')[0].get('main')
        smile = '🚫'
        if weather_description in code_to_smile:
            smile = code_to_smile.get(weather_description)

        city = data.get('name')
        current_weather = data.get('main').get('temp')
        humidity = data.get('main').get('humidity')
        pressure = data.get('main').get('pressure')
        wind = data.get('wind').get('speed')
        sunrise_timestamp = str(datetime.datetime.fromtimestamp(data.get('sys').get('sunrise')))[11:]
        sunset_timestamp = str(datetime.datetime.fromtimestamp(data.get('sys').get('sunset')))[11:]
        length_of_the_day = datetime.datetime.fromtimestamp(
            data.get('sys').get('sunset')) - datetime.datetime.fromtimestamp(data.get('sys').get('sunrise'))

        weather_info = \
            rf"<code>\*\*\* {datetime.datetime.now().strftime('%d-%m-%Y %H:%M')} \*\*\*</code>\n\n" \
            f"🌍Погода в городе:   <code>{city}\n\n</code>" \
            f"🌡️Температура:   <code>{current_weather} °C {smile}\n\n</code>" \
            f"💧Влажность:   <code>{humidity} %</code>\n\n" \
            f"🌪️Давление:   <code>{pressure} мм.рт.ст</code>\n\n" \
            f"💨Ветер:   <code>{wind} м/с</code>\n\n" \
            f"🌅Восход солнца:   <code>{sunrise_timestamp}</code>\n\n" \
            f"🌄Закат солнца:   <code>{sunset_timestamp}</code>\n\n" \
            f"⌛️Продолжительность дня:   <code>{length_of_the_day}</code>\n\n" \
            f"✨Хорошего дня!"

        with open('cities.txt', 'a') as file:
            file.write(f"{datetime.datetime.now().strftime('%d-%m-%Y %H:%M')} {city}\n")

        return weather_info
    except Exception:
        weather_info = f"⛔️Город <code>{city}</code> не найден"
        return weather_info
