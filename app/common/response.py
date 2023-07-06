# -*- coding: utf-8 -*-
# @Time    : 2023/7/5
# @Author  : MANKVIS
# @Email   : chzzbeck@gmail.com
# @File    : response.py
# @Software: PyCharm
from enum import Enum
from typing import Optional, Any

from fastapi.responses import JSONResponse

from pydantic import BaseModel


class APIResponse(BaseModel):
    """ API 响应模型 """
    code: int
    msg: str
    data: Optional[Any]

    async def __call__(self, *args, **kwargs):
        return JSONResponse(status_code=self.code, content=self.dict())


class APICode(Enum):
    """ API 响应状态码  """
    RUNTIME_ERROR = {'code': 500, 'msg': 'Runtime Error'}
    SUCCESS = {'code': 200, 'msg': 'Success'}
    INVALID_PARAMS = {'code': 400, 'msg': 'Invalid Params'}
    USER_NOT_FOUND = {'code': 404, 'msg': 'User Not Found'}
    USERNAME_EXISTED = {'code': 200, 'msg': 'Username Existed'}

    @property
    def code(self) -> int:
        return self.value.get('code')

    @property
    def msg(self) -> str:
        return self.value.get('msg')
