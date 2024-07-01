from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import InlineKeyboardButton


async def inline_menu_keyboard():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text='', callback_data=''))
    return builder.as_markup()