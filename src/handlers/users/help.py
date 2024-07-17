from aiogram import F, Router, types
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import Command

router = Router()


@router.message(Command('help'))
async def help_msg_handler(msg: types.Message):
    await msg.answer(
        text='Help',
        reply_markup=None,
        parse_mode=ParseMode.HTML
    )


@router.callback_query(F.data == 'help_callback_data')
async def help_cb_handler(cb: types.CallbackQuery):
    await cb.message.edit_text(
        text='Help',
        reply_markup=None,
        parse_mode=ParseMode.HTML
    )
