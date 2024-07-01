from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode

from keyboards.inline.menu import inline_menu_keyboard

router = Router()


@router.message(Command('start'))
async def start_msg_handler(msg: types.Message):
    await msg.answer(
        text='',
        reply_markup=await inline_menu_keyboard(),
        parse_mode=ParseMode.HTML
    )