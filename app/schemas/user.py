# -*- coding: utf-8 -*-
# @Time    : 2023/7/5
# @Author  : MANKVIS
# @Email   : chzzbeck@gmail.com
# @File    : user.py
# @Software: PyCharm

from pydantic import BaseModel


class UserBase(BaseModel):
    """ 用户基础模型 """
    username: str
    is_active: bool


class UserCreate(UserBase):
    """ 创建用户模型 """
    hashed_password: str


class UserUpdate(UserBase):
    """ 更新用户模型 """
    hashed_password: str


class User(UserBase):
    """ 用户模型 """
    id: int

    class Config:
        orm_mode = True
