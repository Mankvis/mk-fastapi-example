# -*- coding: utf-8 -*-
# @Time    : 2023/7/5
# @Author  : MANKVIS
# @Email   : chzzbeck@gmail.com
# @File    : user.py
# @Software: PyCharm
from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession

from app.schemas.user import UserCreate, User, UserUpdate
from app.repository.user import UserRepository


class UserService:
    """ 用户服务类 """

    def __init__(self, db_session: AsyncSession):
        self.user_repository = UserRepository(db_session)

    async def create_user(self, user: UserCreate) -> User:
        return await self.user_repository.create_user(user)

    async def query_user(self, user_id: int) -> User:
        return await self.user_repository.query_user(user_id)

    async def query_user_by_username(self, username: str) -> User:
        return await self.user_repository.query_user_by_username(username)

    async def query_users(self, skip: int = 0, limit: int = 100) -> Sequence[User]:
        return await self.user_repository.query_users(skip, limit)

    async def update_user(self, user_id: int, user: UserUpdate) -> User:
        return await self.user_repository.update_user(user_id, user)

    async def delete_user(self, user_id: int) -> None:
        return await self.user_repository.delete_user(user_id)
