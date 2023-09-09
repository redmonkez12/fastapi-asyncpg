from database import async_session
from user_service import UserService


async def get_user_service():
    async with async_session() as session:
        async with session.begin():
            yield UserService(session)
