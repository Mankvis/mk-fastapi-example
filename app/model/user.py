# -*- coding: utf-8 -*-
# @Time    : 2023/7/5
# @Author  : MANKVIS
# @Email   : chzzbeck@gmail.com
# @File    : user.py
# @Software: PyCharm

from sqlalchemy import Column, BigInteger, String, Boolean

from app.core.db.sqlalchemy import Base


class UserModel(Base):
    """ 用户表 """
    # __tablename__ 表名
    __tablename__ = 'user'
    # id 字段，primary_key=True 为主键，autoincrement=True 自增，index=True 索引
    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)
    # username 字段，nullable=False 不为空，unique=True 唯一
    username = Column(String(32), unique=True, nullable=False, index=True)
    # hashed_password 字段，nullable=False 不为空
    hashed_password = Column(String(255), nullable=False)
    # is_active 字段，default=True 默认为 True
    is_active = Column(Boolean, default=True)
