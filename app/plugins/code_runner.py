from contextlib import redirect_stdout, redirect_stderr
from io import StringIO
from time import perf_counter
from traceback import print_exc
import asyncio
import html

from pyrogram import Client, filters
from pyrogram.types import Message

from app.utils import fn


async def aexec(code, *args, timeout=None):
    exec(
        "async def __todo(client, message, *args):\n"
        + " from pyrogram import raw, types\n"
        + " app = client\n"
        + " m = message\n"
        + " r = m.reply_to_message\n"
        + " p = print\n"
        + " u = m.from_user\n"
        + " ru = getattr(r, 'from_user', None)\n"
        + "".join(f"\n {_l}" for _l in code.split("\n"))
    )

    f = StringIO()
    with redirect_stdout(f):
        await asyncio.wait_for(locals()["__todo"](*args), timeout=timeout)

    return f.getvalue()


code_result = (
    "<b><emoji id={emoji_id}>🌐</emoji> Language:</b>\n"
    "<code>{language}</code>\n\n"
    "<b><emoji id=5431376038628171216>💻</emoji> Code:</b>\n"
    '<pre language="{pre_language}">{code}</pre>\n\n'
    "{result}"
)


@Client.on_message(filters.me & filters.command(['py', 'python'], prefixes='.'))
async def run_python(client: Client, message: Message):
    code = fn.get_command_args(message, ['python', 'py'])

    await message.edit_text("<b><emoji id=5821116867309210830>🔃</emoji> Executing...</b>")

    try:
        start_time = perf_counter()
        result = await aexec(code, client, message, timeout=60)
        stop_time = perf_counter()

        if len(result) > 3072:
            result = html.escape(await fn.paste_yaso(result))
        else:
            result = f"<code>{html.escape(result)}</code>"

        return await message.edit(
            code_result.format(
                emoji_id=5260480440971570446,
                language="Python",
                pre_language="python",
                code=html.escape(code),
                result=f"<b><emoji id=5472164874886846699>✨</emoji> Result</b>:\n"
                       f"{result}\n"
                       f"<b>Completed in {round(stop_time - start_time, 5)}s.</b>",
            ),
            disable_web_page_preview=True,
        )
    except asyncio.TimeoutError:
        return await message.edit_text(
            code_result.format(
                emoji_id=5260480440971570446,
                language="Python",
                pre_language="python",
                code=html.escape(code),
                result="<b><emoji id=5465665476971471368>❌</emoji> Timeout Error!</b>",
            ),
            disable_web_page_preview=True,
        )
    except Exception as e:
        err = StringIO()
        with redirect_stderr(err):
            print_exc()

        return await message.edit(
            code_result.format(
                emoji_id=5260480440971570446,
                language="Python",
                pre_language="python",
                code=html.escape(code),
                result=f"<b><emoji id=5465665476971471368>❌</emoji> {e.__class__.__name__}: {e}</b>\n"
                       f"Traceback: {err}",
            ),
            disable_web_page_preview=True,
        )
