# -*- coding: utf-8 -*-
# @Time    : 2023/7/5
# @Author  : MANKVIS
# @Email   : chzzbeck@gmail.com
# @File    : error_handle.py
# @Software: PyCharm
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.common.exception import APIException, RuntimeException
from app.common.response import APIResponse, APICode


async def http_error_handle(request: Request, exc: APIException) -> JSONResponse:
    """ HTTP 异常处理 """
    return JSONResponse(status_code=exc.code, content=APIResponse(code=exc.code, msg=exc.msg).dict())


async def runtime_error_handle(request: Request, exc: Exception) -> JSONResponse:
    """ 运行时异常处理 """
    return JSONResponse(status_code=APICode.RUNTIME_ERROR.code, content=APIResponse(code=APICode.RUNTIME_ERROR.code, msg=APICode.RUNTIME_ERROR.msg).dict())
