from aiogram import F, Router, types
from aiogram.enums.parse_mode import ParseMode

from db.query import update_user_lang
from keyboards.inline.lang import lang_kb
from keyboards.inline.menu import back_menu_kb


router = Router()


@router.callback_query(F.data == 'lang')
async def menu_cb_handler(cb: types.CallbackQuery):
    await cb.message.edit_text(
        text='Язык интерфейса',
        reply_markup=await lang_kb(),
        parse_mode=ParseMode.HTML
    )


@router.callback_query(F.data.in_(['kk', 'ru']))
async def menu_cb_handler(cb: types.CallbackQuery):
    if F.data == 'kk':
        await update_user_lang(userid=cb.from_user.id, value='kk')
    else:
        await update_user_lang(userid=cb.from_user.id, value='ru')
    await cb.message.edit_text(
        text='✅ Язык интерфейса обновлен',
        reply_markup=await back_menu_kb(),
        parse_mode=ParseMode.HTML
    )