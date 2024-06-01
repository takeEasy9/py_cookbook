# -*- coding: utf-8 -*-

"""
@author: takeEasy9
@description: method resolution order: 方法解析顺序
@version: 1.0.0
@since: 2024/5/21 20:45
"""

"""

"""


class A:
    def say(self):
        print("A")


class B(A):
    def say(self):
        print("B")


class M(B):
    pass


m = M()
m.say()
# print(M.__mro__)
print(M.mro())
print(dir(M.__class__))
