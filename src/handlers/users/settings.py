from aiogram import F, Router, types
from aiogram.enums.parse_mode import ParseMode

from keyboards.inline.settings import settings_kg


router = Router()


@router.callback_query(F.data == 'settings')
async def menu_cb_handler(cb: types.CallbackQuery):
    await cb.message.edit_text(
        text='Настройки бота',
        reply_markup=await settings_kg(),
        parse_mode=ParseMode.HTML
    )