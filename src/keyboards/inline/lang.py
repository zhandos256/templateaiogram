from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def lang_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text='Казакша тiл', callback_data='kk'),
        InlineKeyboardButton(text='Русский язык', callback_data='ru'),
        width=2
    )
    builder.add(InlineKeyboardButton(text='Меню', callback_data='menu'))
    return builder.as_markup()