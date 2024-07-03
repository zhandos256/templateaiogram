from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.enums.parse_mode import ParseMode

router = Router()

@router.message(Command('menu'))
async def menu_msg_handler(msg: types.Message):
    await msg.answer(
        text='',
        reply_markup=None,
        parse_mode=ParseMode.HTML
    )


@router.callback_query(F.data == 'menu_callback_data')
async def menu_cb_handler(cb: types.CallbackQuery):
    await cb.message.edit_text(
        text='',
        reply_markup=None,
        parse_mode=ParseMode.HTML
    )
