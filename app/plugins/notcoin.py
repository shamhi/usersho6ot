from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.raw import functions


@Client.on_message(filters.me & filters.command('ncu', prefixes='.'))
async def send_notcoin_url(client: Client, message: Message):
    result = await client.invoke(functions.messages.RequestWebView(
        peer=await client.resolve_peer('notcoin_bot'),
        bot=await client.resolve_peer('notcoin_bot'),
        platform='android',
        from_bot_menu=False,
        url='https://clicker.joincommunity.xyz/clicker',
    ))

    await message.edit(result.url)
