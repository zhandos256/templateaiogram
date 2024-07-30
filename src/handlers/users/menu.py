from aiogram import F, Router, types
from aiogram.enums.parse_mode import ParseMode
from aiogram.filters import Command

from keyboards.inline.menu import menu_kb


router = Router()


@router.message(Command('menu'))
async def menu_msg(msg: types.Message):
    templtae = [
        'Шаблонное приветствие\n',
        'Поменяй меня на другой текст\n',
        'Исходники - https://github.com/zhandos256/templateaiogram\n'
    ]
    await msg.answer(
        text='\n'.join(templtae),
        reply_markup=await menu_kb(),
        parse_mode=ParseMode.HTML
    )


@router.callback_query(F.data == 'menu')
async def menu_cb(call: types.CallbackQuery):
    templtae = [
        'Шаблонное приветствие\n',
        'Поменяй меня на другой текст\n',
        'Исходники - https://github.com/zhandos256/templateaiogram\n',
    ]
    await call.message.edit_text(
        text='\n'.join(templtae),
        reply_markup=await menu_kb(),
        parse_mode=ParseMode.HTML
    )
