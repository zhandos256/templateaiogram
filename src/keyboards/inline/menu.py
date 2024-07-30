from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


async def menu_kb():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text='Change me', callback_data=' '))
    return builder.as_markup()


async def back_menu_kb():
    builder = InlineKeyboardBuilder()
    builder.add(InlineKeyboardButton(text='Меню', callback_data='menu'))
    return builder.as_markup()

