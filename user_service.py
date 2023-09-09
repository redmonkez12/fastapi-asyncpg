from sqlmodel import Session, select
from pydantic import BaseModel

from models import User


class CreateUserRequest(BaseModel):
    username: str
    first_name: str
    last_name: str


class UserService:
    def __init__(self, session: Session):
        self.session = session

    async def create(self, data: CreateUserRequest) -> User:
        new_user = User(
            first_name=data.first_name,
            last_name=data.last_name,
            username=data.username,
        )

        self.session.add(new_user)
        await self.session.commit()

        return new_user

    async def get(self, id: int) -> User:
        query = (
            select(User)
            .where(User.user_id == id)
        )

        result = await self.session.execute(query)
        return result.scalars().one()
