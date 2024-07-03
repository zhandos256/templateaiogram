from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode

from db.query import register_user
from keyboards.inline.menu import inline_menu_keyboard

router = Router()

@router.message(Command('start'))
async def start_msg_handler(msg: types.Message):
    await register_user(
        userid=msg.from_user.id,
        username=msg.from_user.username,
        first_name=msg.from_user.first_name,
        last_name=msg.from_user.last_name
    )
    await msg.answer(
        text='Start',
        reply_markup=await inline_menu_keyboard(),
        parse_mode=ParseMode.HTML
    )