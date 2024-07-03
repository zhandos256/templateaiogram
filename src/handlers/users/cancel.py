from aiogram import Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.enums.parse_mode import ParseMode

router = Router()

@router.message(Command('cancel'))
async def cancel_handler(msg: types.Message, state: FSMContext):
    st = await state.get_state()
    if st is not None:
        await state.clear()
        await msg.answer(
            text='Операция отменена!',
            reply_markup=None,
            parse_mode=ParseMode.HTML
        )
    else:
        await msg.answer(
            text='Нечего отменять!',
            reply_markup=None,
            parse_mode=ParseMode.HTML
        )