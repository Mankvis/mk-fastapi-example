# -*- coding: utf-8 -*-
# @Time    : 2023/7/5
# @Author  : MANKVIS
# @Email   : chzzbeck@gmail.com
# @File    : user.py
# @Software: PyCharm
from typing import Union, List

from fastapi import APIRouter, Depends

from app.schemas.user import UserCreate, UserUpdate
from app.core.depends.service import get_user_service
from app.service.user import UserService
from app.common.response import APIResponse, APICode


class UserController:
    router = APIRouter()

    @staticmethod
    @router.post('/users/', response_model=APIResponse)
    async def create_user(user: UserCreate, user_service: UserService = Depends(get_user_service)):
        user = await user_service.create_user(user)
        return APIResponse(code=APICode.SUCCESS.code, msg=APICode.SUCCESS.msg, data=user)

    @staticmethod
    @router.get('/users/id/{user_id}', response_model=APIResponse)
    async def get_user(user_id: int, user_service: UserService = Depends(get_user_service)):
        user = await user_service.query_user(user_id)
        return APIResponse(code=APICode.SUCCESS.code, msg=APICode.SUCCESS.msg, data=user)

    @staticmethod
    @router.get('/users/username/{username}', response_model=APIResponse)
    async def get_user_by_username(username: str, user_service: UserService = Depends(get_user_service)):
        user = await user_service.query_user_by_username(username)
        return APIResponse(code=APICode.SUCCESS.code, msg=APICode.SUCCESS.msg, data=user)

    @staticmethod
    @router.get('/users', response_model=APIResponse)
    async def get_users(skip: int = 0, limit: int = 100, user_service: UserService = Depends(get_user_service)):
        users = await user_service.query_users(skip, limit)
        return APIResponse(code=APICode.SUCCESS.code, msg=APICode.SUCCESS.msg, data=users)

    @staticmethod
    @router.put('/users/{user_id}', response_model=APIResponse)
    async def update_user(user_id: int, user: UserUpdate, user_service: UserService = Depends(get_user_service)):
        user = await user_service.update_user(user_id, user)
        return APIResponse(code=APICode.SUCCESS.code, msg=APICode.SUCCESS.msg, data=user)

    @staticmethod
    @router.delete('/users/{user_id}')
    async def delete_user(user_id: int, user_service: UserService = Depends(get_user_service)):
        await user_service.delete_user(user_id)
        return APIResponse(code=APICode.SUCCESS.code, msg=APICode.SUCCESS.msg)

    @classmethod
    def get_router(cls):
        return cls.router
