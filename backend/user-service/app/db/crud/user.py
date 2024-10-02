from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from uuid import UUID
from app.db.models import User
from app.schemas.user import UserCreate, UserUpdate


class UserCRUD:
    def __init__(self, session: AsyncSession) -> None:
        self.session = session
        
    async def get_user(self, user_id: UUID):
        result = await self.session.execute(select(User).filter(User.id == user_id))
        return result.scalars().first()

    async def get_user_by_email(self, email: str):
        result = await self.session.execute(select(User).filter(User.email == email))
        return result.scalars().first()

    async def create_user(self, user_data: UserCreate):
        user = User(**user_data.dict())  # Преобразуем Pydantic-модель в словарь
        self.session.add(user)
        await self.session.commit()
        await self.session.refresh(user)
        return user

    async def update_user(self, user_id: UUID, user_data: UserUpdate):
        user = await self.get_user(user_id)
        if user:
            if user_data.is_verified:
                user.is_verified = user_data.is_verified
            if user_data.is_google_authenticated:
                user.is_google_authenticated = user_data.is_google_authenticated
            if user_data.new_password:
                user.password = user_data.new_password
            await self.session.commit()
            await self.session.refresh(user)
        return user

    async def delete_user(self, user_id: UUID):
        user = await self.get_user(user_id)
        if user:
            await self.session.delete(user)
            await self.session.commit()
        return user