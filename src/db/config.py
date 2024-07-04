from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import DeclarativeBase

from core.const import DB_URL, POSTGRES_URL

engine = create_async_engine(url=POSTGRES_URL, echo=True)
async_session = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

class Base(DeclarativeBase):
    pass