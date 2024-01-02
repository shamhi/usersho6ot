from pyrogram import Client, filters
from pyrogram.types import Message

from app.utils import fn


@Client.on_message(filters.me & filters.command('weather', prefixes='.'))
@fn.with_args("<b>This command don't work without args\n"
              "Required type <i>city</i></b>")
async def send_weather_info(client: Client, message: Message):
    city = fn.get_command_args(message, 'weather')
    weather_info = await fn.get_weather(city)

    await message.edit(weather_info)

