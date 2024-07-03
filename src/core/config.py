import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher

from core.const import TOKEN, DEBUG
from db.query import init_db
from handlers.users import (
    start,
    help,
    echo,
    cancel,
)
from utils.notify import notify_admins
from utils.bot_commands import set_bot_commands

async def on_startup(bot: Bot):
    await init_db()
    await notify_admins(bot=bot, text='Бот запущен!')


async def on_shutdown(bot: Bot):
    await notify_admins(bot=bot, text='Бот остановлен!')


async def configure():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_routers(
        start.router,
        help.router,
        cancel.router,
        echo.router,
    )

    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    await set_bot_commands(bot=bot)
    await bot.delete_webhook(drop_pending_updates=True)
    try:
        await dp.start_polling(bot)
    except Exception as e:
         logging.exception(e)
    finally:
        await dp.storage.close()
        await bot.session.close()


def main():
    logging.basicConfig(level=logging.INFO if not DEBUG else logging.DEBUG, stream=sys.stdout)
    asyncio.run(configure())