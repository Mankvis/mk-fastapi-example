# -*- coding: utf-8 -*-
# @Time    : 2023/7/5
# @Author  : MANKVIS
# @Email   : chzzbeck@gmail.com
# @File    : error_handle.py
# @Software: PyCharm
from starlette.requests import Request
from starlette.responses import JSONResponse

from app.common.exception import APIException
from app.common.response import APIResponse, APICode
from app.core.config.settings import settings


async def http_error_handler(request: Request, exc: APIException) -> JSONResponse:
    """ HTTP 异常处理 """
    return APIResponse(code=exc.code, msg=exc.msg)


async def runtime_error_handler(request: Request, exc: Exception) -> JSONResponse:
    """ 运行时异常处理 """
    # 当在开发环境时，返回详细的错误信息
    if settings.debug:
        return APIResponse(code=APICode.RUNTIME_ERROR.code, msg=str(exc))
    else:
        return APIResponse(code=APICode.RUNTIME_ERROR.code, msg=APICode.RUNTIME_ERROR.msg)
