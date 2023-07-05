# -*- coding: utf-8 -*-
# @Time    : 2023/7/5
# @Author  : MANKVIS
# @Email   : chzzbeck@gmail.com
# @File    : sqlalchemy.py
# @Software: PyCharm
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base

from app.core.config.settings import settings

# 创建异步数据库引擎
# echo=True 会打印所有的 SQL 语句
# future=True 会启用 SQLAlchemy 的异步功能
async_engine = create_async_engine(settings.mysql.url, echo=True, future=True)

# 创建异步数据库会话
# expire_on_commit=False 会关闭自动提交，这样就可以在事务中使用 session.commit() 了
# class_=AsyncSession 会启用 SQLAlchemy 的异步功能
SessionLocal = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)

# 创建基本映射类
Base = declarative_base()
