# -*- coding: utf-8 -*-
# @Time    : 2023/7/5
# @Author  : MANKVIS
# @Email   : chzzbeck@gmail.com
# @File    : service.py
# @Software: PyCharm
from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.depends.db import get_db_session

from app.service.user import UserService


async def get_user_service(db_session: AsyncSession = Depends(get_db_session)) -> UserService:
    """ 获取用户服务类 """
    yield UserService(db_session)
