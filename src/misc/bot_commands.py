from aiogram import Bot
from aiogram.types import BotCommand


async def set_bot_commands(bot: Bot):
    await bot.set_my_commands(
        commands=[
            BotCommand(command="/start", description="Приветсвтенное сообщение"),
            BotCommand(command="/help", description="Получить помощь"),
            BotCommand(command="/menu", description="Показать меню"),
        ]
    )
