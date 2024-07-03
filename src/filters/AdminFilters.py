from typing import Any

from aiogram import types
from aiogram.filters import BaseFilter

from db.query import get_all_users

class IsAdminMsg(BaseFilter):
    async def __call__(self, msg: types.Message):
        users = await get_all_users()
        if users is not None:
            return True if msg.from_user.id in [user.userid for user in users if user.is_admin] else False


class IsAdminCb(BaseFilter):
    async def __call__(self, cb: types.CallbackQuery):
        users = await get_all_users()
        if users is not None:
            return True if cb.from_user.id in [user.userid for user in users if user.is_admin] else False