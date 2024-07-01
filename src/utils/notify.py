import logging
import asyncio

from aiogram import Bot

from db.query import get_all_admins, get_users


async def notify_admins(bot: Bot, text: str):
    admins = [admin.user_id for admin in await get_all_admins()]
    for admin in admins:
        try:
            await bot.send_message(chat_id=admin, text=text)
            await asyncio.sleep(.05)
        except Exception as e:
            logging.exception(e)


async def notify_users(bot: Bot, text: str):
    users = [admin.user_id for admin in await get_users()]
    for user in users:
        try:
            await bot.send_message(chat_id=user, text=text)
            await asyncio.sleep(.05)
        except Exception as e:
            logging.exception(e)