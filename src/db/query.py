from sqlalchemy import select

from db.config import async_session
from db.models import User


async def get_all_admins():
    async with async_session() as session:
        query = select(User).filter_by(is_admin=1)
        resutl = await session.execute(query)
        return resutl.scalars().all()
    

async def get_users():
    async with async_session() as session:
        query = select(User).filter_by(is_admin=0)
        resutl = await session.execute(query)
        return resutl.scalars().all()
    

async def get_user_by_id(user_id: int):
    async with async_session() as session:
        query = select(User).filter_by(user_id=user_id)
        result = await session.execute(query)
        return result.scalar_one_or_none()


async def register_user(user_id: int, username):
    async with async_session() as session:
        query = select(User)