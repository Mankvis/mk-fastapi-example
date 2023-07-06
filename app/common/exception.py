# -*- coding: utf-8 -*-
# @Time    : 2023/7/5
# @Author  : MANKVIS
# @Email   : chzzbeck@gmail.com
# @File    : exception.py
# @Software: PyCharm


class APIException(Exception):
    """ API 异常类 """

    def __init__(self, code, msg):
        self.code = code
        self.msg = msg

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}(error_code={self.code!r}, error_msg={self.msg!r})"


class RuntimeException(Exception):

    def __init__(self, code, msg, **kwargs):
        self.code = code
        self.msg = msg
        self.kwargs = kwargs

    def __repr__(self) -> str:
        class_name = self.__class__.__name__
        return f"{class_name}(error_code={self.code!r}, error_msg={self.msg!r}, kwargs={self.kwargs!r})"

