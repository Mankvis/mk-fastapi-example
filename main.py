# -*- coding: utf-8 -*-
# @Time    : 2023/4/7
# @Author  : MANKVIS
# @Email   : chzzbeck@gmail.com
# @File    : main.py
# @Software: PyCharm
import os

from fastapi import FastAPI

from app.common.exception import APIException, RuntimeException
from app.controller.user import UserController
from app.common.error_handle import http_error_handle, runtime_error_handle

app = FastAPI()

app.include_router(UserController.get_router(), prefix='/api')

app.add_exception_handler(APIException, http_error_handle)
app.add_exception_handler(Exception, runtime_error_handle)

if __name__ == '__main__':
    # 设置 ENV_FOR_DYNACONF 为 development
    os.environ['ENV_FOR_DYNACONF'] = 'development'
    # os.environ['ENV_FOR_DYNACONF'] = 'production'

    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)

# 在 FastAPI 的路由中，我指定response_model=APIResponse，这样就可以统一返回格式了。但是在APIResponse.data中会返回用户信息，我想要屏蔽掉用户的密码，怎么办呢？因为封装了APIResponse，所以我们可以在APIResponse中指定response_model_exclude={'hashed_password'}，这样是无效的
#