from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def lang_kb():
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Казакша тiл", callback_data="kk"),
        InlineKeyboardButton(text="Русский язык", callback_data="ru"),
        width=2,
    )
    builder.row(InlineKeyboardButton(text="Меню", callback_data="menu"), width=1)
    return builder.as_markup()
