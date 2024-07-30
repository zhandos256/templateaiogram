from aiogram import Router, types
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import Command

from db.query import register_user
from keyboards.inline.menu import menu_kb


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
        reply_markup=await menu_kb(),
        parse_mode=ParseMode.HTML
    )
