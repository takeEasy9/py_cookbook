# -*- coding: utf-8 -*-

"""
@author: takeEasy9
@description: python frame
@version: 1.0.0
@since: 2024/5/26 19:08
"""
import inspect
import sys

from objprint import op


def f():
    frame = inspect.currentframe()
    # 等价于 frame = sys._getframe()
    op(frame, honor_existing=False, depth=2)
    # 拿到当前调用该函数的名称
    print(frame.f_back.f_code.co_name)
    # 拿到当前调用该函数的局部变量
    print(frame.f_back.f_locals)
    # 拿到该函数在哪一行被调用
    print(frame.f_back.f_lineno)


def g():
    a = 3
    b = 4
    f()


g()
