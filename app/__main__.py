from pyrogram import Client, compose
from pyrogram_patch import patch
from pyrogram_patch.fsm.storages.memory_storage import MemoryStorage
import asyncio
import logging

from app.config import Config
from app.plugins import router


def setup_patch(app: Client):
    patch_manager = patch(app)

    patch_manager.set_storage(MemoryStorage())
    patch_manager.include_router(router)



async def main():
    app1 = Client(
        name="userbot1",
        api_id=Config.API_ID1,
        api_hash=Config.API_HASH1,
     )

    app2 = Client(
        name="userbot2",
        api_id=Config.API_ID2,
        api_hash=Config.API_HASH2,
    )

    setup_patch(app1)
    setup_patch(app2)

    await compose([app1, app2])


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
