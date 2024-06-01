# -*- coding: utf-8 -*-

"""
@author: takeEasy9
@description: atexit module
@version: 1.0.0
@since: 2024/5/18 7:19
"""
import atexit

"""
atexit 用来在python进程退出时运行某些函数
用法示例：atexit.register(f)
也可以把atexit.register当作装饰器来使用
"""


def f():
    print("exiting")


atexit.register(f)


def f_v2():
    print("v2_exiting")


atexit.register(f_v2)
atexit.register(f_v2)
atexit.register(f_v2)
# unregister移除所有的注册的相同的函数,
atexit.unregister(f_v2)


class MyFunc:

    def __call__(self, *args, **kwargs):
        print("v3_exiting")

    def __eq__(self, other):
        if isinstance(other, MyFunc):
            return True
        return False


f0 = MyFunc()
atexit.register(f0)

f1 = MyFunc()
# unregister 使用 == 判断是否相同, 而不是 is
atexit.unregister(f1)