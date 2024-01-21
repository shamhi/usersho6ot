import asyncio
import logging
from os.path import exists

from pyrogram import Client, compose

from app.config import Config


async def main():
    app1 = Client(
        name=Config.SESSION_NAME1,
        api_id=Config.API_ID1,
        api_hash=Config.API_HASH1,
        plugins=dict(root='plugins' if exists(path='plugins') else 'app/plugins'),
    )

    app2 = Client(
        name=Config.SESSION_NAME2,
        api_id=Config.API_ID2,
        api_hash=Config.API_HASH2,
        plugins=dict(root='plugins' if exists(path='plugins') else 'app/plugins'),
    )

    await compose([app1, app2])


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
