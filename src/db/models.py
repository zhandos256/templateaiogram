from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column


from db.config import Base


class User(Base):
    __tablename__ = 'Users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    created: Mapped[datetime] = mapped_column(DateTime, default=datetime.today())
    userid: Mapped[int] = mapped_column(Integer, unique=True)
    username: Mapped[str] = mapped_column(String(length=32), default='-')
    first_name: Mapped[str] = mapped_column(String(length=255), default='-')
    last_name: Mapped[str] = mapped_column(String(length=255), default='-')
    language: Mapped[str] = mapped_column(String(length=2), default='ru')
    is_admin: Mapped[int] = mapped_column(Integer, default=0)
    subscription: Mapped[int] = mapped_column(Integer, default=0)
