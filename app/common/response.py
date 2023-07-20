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


class APIResponseModel(BaseModel):
    """ API 响应模型 """
    code: int
    msg: str
    data: Optional[Any]


class APIResponse(JSONResponse):
    """
    API 响应，继承自JSONResponse，请求状态码全部为200，通过code区分业务
    """
    def __init__(self, code: int, msg: str, data: Optional[Any] = None):
        super().__init__(status_code=200, content=APIResponseModel(code=code, msg=msg, data=data).dict(exclude_none=True))


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
