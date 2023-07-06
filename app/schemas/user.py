# -*- coding: utf-8 -*-
# @Time    : 2023/7/5
# @Author  : MANKVIS
# @Email   : chzzbeck@gmail.com
# @File    : user.py
# @Software: PyCharm

from typing import Optional
from pydantic import BaseModel


class UserCreate(BaseModel):
    """ 创建用户模型 """
    username: str
    hashed_password: str


class UserUpdate(BaseModel):
    """ 更新用户模型 """
    username: Optional[str]
    hashed_password: Optional[str]
    is_active: Optional[bool]


class UserInDB(BaseModel):
    """ 数据库用户模型 """
    id: int
    username: str
    hashed_password: str
    is_active: bool

    class Config:
        orm_mode = True


class UserOut(BaseModel):
    """ 输出用户模型 """
    id: int
    username: str
    is_active: bool

    class Config:
        orm_mode = True
