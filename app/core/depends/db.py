# -*- coding: utf-8 -*-
# @Time    : 2023/7/5
# @Author  : MANKVIS
# @Email   : chzzbeck@gmail.com
# @File    : db.py
# @Software: PyCharm
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db.sqlalchemy import SessionLocal


async def get_db_session() -> AsyncSession:
    """ 获取数据库会话 """
    db_session = SessionLocal()
    try:
        yield db_session
    finally:
        await db_session.close()
