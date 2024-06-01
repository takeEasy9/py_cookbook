# -*- coding: utf-8 -*-

"""
@author: takeEasy9
@description: meta_class
@version: 1.0.0
@since: 2024/5/21 20:15
"""

"""
meta class 
"""


class M(type):

    def __new__(mcs, name, bases, _dict):
        return type.__new__(mcs, name, bases, _dict)

    def __init__(cls, name, bases, _dict):
        type.__init__(cls, name, bases, _dict)

    def __call__(cls, *args, **kwargs):
        print("call")
        return type.__call__(cls, *args, **kwargs)


class A(metaclass=M):
    """M 是 A的元类
    等价于
    A = type("A", (), {})
    A = M("A", (), {})
    """
    pass
