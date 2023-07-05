# -*- coding: utf-8 -*-
# @Time    : 2023/4/7
# @Author  : MANKVIS
# @Email   : chzzbeck@gmail.com
# @File    : main.py
# @Software: PyCharm
import os

from fastapi import FastAPI

from app.controller.user import UserController

app = FastAPI()

app.include_router(UserController.get_router(), prefix='/api')

if __name__ == '__main__':
    # 设置 ENV_FOR_DYNACONF 为 development
    os.environ['ENV_FOR_DYNACONF'] = 'development'
    # os.environ['ENV_FOR_DYNACONF'] = 'production'

    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True)
