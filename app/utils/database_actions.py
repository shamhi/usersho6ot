import aiosqlite


async def on_startup_database() -> None:
    async with aiosqlite.connect(database='database/sessions.db') as db:
        await db.execute(sql="""
        CREATE TABLE IF NOT EXISTS sessions (
            id INTEGER PRIMARY KEY,
            session_name TEXT,
            session_proxy TEXT
        );
        """)
        await db.commit()


async def add_session(session_name: str,
                      session_proxy: str = '') -> None:
    async with aiosqlite.connect(database='database/sessions.db') as db:
        await db.execute(sql='INSERT INTO sessions (session_name, session_proxy) VALUES (?, ?)',
                         parameters=(session_name, session_proxy))
        await db.commit()

