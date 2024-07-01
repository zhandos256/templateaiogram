from datetime import datetime

from sqlalchemy import Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from db.config import Base


class User(Base):
    __tablename__ = 'Users'

    id: Mapped[int] =  mapped_column(Integer, primary_key=True, autoincrement=True)
    created: Mapped[datetime] =  mapped_column(DateTime, default=datetime.today())
    user_id: Mapped[int] =  mapped_column(Integer, unique=True, nullable=False)
    username: Mapped[str] =  mapped_column(String, default='-')
    first_name: Mapped[str] =  mapped_column(Integer, default='-')
    last_name: Mapped[str] =  mapped_column(Integer, default='-')
    language: Mapped[str] =  mapped_column(String, default='ru')
    phone: Mapped[int] = mapped_column(Integer, nullable=False)
    is_admin: Mapped[int] = mapped_column(Integer, default=0)