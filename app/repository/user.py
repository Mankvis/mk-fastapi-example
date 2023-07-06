# -*- coding: utf-8 -*-
# @Time    : 2023/7/5
# @Author  : MANKVIS
# @Email   : chzzbeck@gmail.com
# @File    : user.py
# @Software: PyCharm

from typing import Sequence

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

from app.schemas.user import UserCreate, UserUpdate, UserInDB
from app.model.user import UserModel


class UserRepository:
    """ 用户仓库类 """

    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def create_user(self, user: UserCreate) -> UserModel:
        """ 创建用户 """
        db_user = UserModel(username=user.username, hashed_password=user.hashed_password)
        self.db_session.add(db_user)
        await self.db_session.commit()
        await self.db_session.refresh(db_user)
        return db_user

    async def query_user(self, user_id: int) -> UserModel:
        """ 根据id查询用户 """
        stmt = select(UserModel).where(UserModel.id == user_id)
        result = await self.db_session.execute(stmt)
        return result.scalars().first()

    async def query_user_by_username(self, username: str) -> UserModel:
        """ 根据username查询用户"""
        stmt = select(UserModel).where(UserModel.username == username)
        result = await self.db_session.execute(stmt)
        return result.scalars().first()

    async def query_users(self, skip: int = 0, limit: int = 100) -> Sequence[UserModel]:
        """ 查询用户列表 """
        stmt = select(UserModel).offset(skip).limit(limit)
        result = await self.db_session.execute(stmt)
        return result.scalars().all()

    async def update_user(self, user_id: int, user: UserUpdate) -> UserModel:
        """ 更新用户 """
        stmt = update(UserModel).where(UserModel.id == user_id).values(**user.dict(exclude_unset=True))
        await self.db_session.execute(stmt)
        await self.db_session.commit()
        stmt = select(UserModel).where(UserModel.id == user_id)
        result = await self.db_session.execute(stmt)
        return result.scalars().first()

    async def delete_user(self, user_id: int) -> None:
        """ 删除用户（物理删除） """
        smtm = delete(UserModel).where(UserModel.id == user_id)
        await self.db_session.execute(smtm)
        await self.db_session.commit()
