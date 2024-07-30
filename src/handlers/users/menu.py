from aiogram import F, Router, types
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import Command


router = Router()


@router.message(Command('menu'))
async def menu_msg_handler(msg: types.Message):
    await msg.answer(
        text='Menu',
        reply_markup=None,
        parse_mode=ParseMode.HTML
    )


@router.callback_query(F.data == 'menu')
async def menu_cb_handler(cb: types.CallbackQuery):
    await cb.message.edit_text(
        text='Menu',
        reply_markup=None,
        parse_mode=ParseMode.HTML
    )
