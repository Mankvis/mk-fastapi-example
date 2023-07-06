# -*- coding: utf-8 -*-
# @Time    : 2023/7/5
# @Author  : MANKVIS
# @Email   : chzzbeck@gmail.com
# @File    : user.py
# @Software: PyCharm
from typing import Sequence
from pydantic import parse_obj_as

from sqlalchemy.ext.asyncio import AsyncSession

from app.common.exception import APIException
from app.common.response import APICode
from app.schemas.user import UserCreate, UserUpdate, UserOut
from app.repository.user import UserRepository


class UserService:
    """ 用户服务类 """

    def __init__(self, db_session: AsyncSession):
        self.user_repository = UserRepository(db_session)

    async def create_user(self, user: UserCreate) -> UserOut:
        db_user = await self.user_repository.query_user_by_username(user.username)
        if db_user is not None:
            raise APIException(APICode.USERNAME_EXISTED.code, APICode.USERNAME_EXISTED.msg)
        return parse_obj_as(UserOut, await self.user_repository.create_user(user))

    async def query_user(self, user_id: int) -> UserOut:
        db_user = await self.user_repository.query_user(user_id)
        return parse_obj_as(UserOut, db_user)

    async def query_user_by_username(self, username: str) -> UserOut:
        db_user = await self.user_repository.query_user_by_username(username)
        if db_user is None:
            raise APIException(APICode.USER_NOT_FOUND.code, APICode.USER_NOT_FOUND.msg)
        return parse_obj_as(UserOut, db_user)

    async def query_users(self, skip: int = 0, limit: int = 100) -> Sequence[UserOut]:
        return parse_obj_as(Sequence[UserOut], await self.user_repository.query_users(skip, limit))

    async def update_user(self, user_id: int, user: UserUpdate) -> UserOut:
        cur_user = await self.user_repository.query_user(user_id)
        if cur_user is None:
            raise APIException(APICode.USER_NOT_FOUND.code, APICode.USER_NOT_FOUND.msg)
        return parse_obj_as(UserOut, await self.user_repository.update_user(user_id, user))

    async def delete_user(self, user_id: int) -> None:
        return await self.user_repository.delete_user(user_id)
