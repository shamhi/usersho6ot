from pyrogram import Client, compose

from loguru import logger
from sys import stderr
import asyncio
import logging

from app.config import Config
from app.utils.database_actions import on_startup_database


logger.remove()
logger.add(stderr, format='<white>{time:HH:mm:ss}</white>'
                          ' | <level>{level: <8}</level>'
                          ' | <cyan>{line}</cyan>'
                          ' - <white>{message}</white>')


async def main():
    await on_startup_database()

    app1 = Client(
        name=Config.SESSION_NAME1,
        api_id=Config.API_ID1,
        api_hash=Config.API_HASH1,
        plugins=dict(root='app/plugins'),
    )

    app2 = Client(
        name=Config.SESSION_NAME2,
        api_id=Config.API_ID2,
        api_hash=Config.API_HASH2,
        plugins=dict(root='app/plugins'),
    )

    await compose([app1, app2])




if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
