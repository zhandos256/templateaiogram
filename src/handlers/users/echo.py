from aiogram import Router, types
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.context import FSMContext

router = Router()


@router.message()
async def echo_msg_handler(msg: types.Message, state: FSMContext):
    st = await state.get_state()
    if st is not None:
        pass
    else:
        await msg.answer(
            text='Извините, я не смог понять ваше сообщение. Используйте команду /help, чтобы увидеть доступные команды.',
            reply_markup=None,
            parse_mode=ParseMode.HTML
        )
