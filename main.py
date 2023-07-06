# -*- coding: utf-8 -*-
# @Time    : 2023/4/7
# @Author  : MANKVIS
# @Email   : chzzbeck@gmail.com
# @File    : main.py
# @Software: PyCharm
import os

from fastapi import FastAPI

from app.common.exception import APIException
from app.controller.user import UserController
from app.common.error_handle import http_error_handler, runtime_error_handler

app = FastAPI()

app.include_router(UserController.get_router(), prefix='/api')

app.add_exception_handler(APIException, http_error_handler)
app.add_exception_handler(Exception, runtime_error_handler)

if __name__ == '__main__':
    # 设置 ENV_FOR_DYNACONF 为 development
    os.environ['ENV_FOR_DYNACONF'] = 'development'
    # os.environ['ENV_FOR_DYNACONF'] = 'production'

    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
