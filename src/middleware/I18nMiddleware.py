from typing import Any, Dict

from aiogram.types import TelegramObject
from aiogram.utils.i18n import I18n, I18nMiddleware

from core.const import LOCALES_DIR
from db.query import get_user_lang

class CustomI18nMiddleware(I18nMiddleware):
    async def get_locale(self, event: TelegramObject, data: Dict[str, Any]) -> str:
        user = data['event_from_user']
        userid = int(user.id)
        res = await get_user_lang(userid=userid)
        return res if res else 'ru'
    

i18n = I18n(path=LOCALES_DIR, default_locale='ru', domain='messages')
i18n_middleware = CustomI18nMiddleware(i18n=i18n)