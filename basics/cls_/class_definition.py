# -*- coding: utf-8 -*-

"""
@author: takeEasy9
@description: python 类定义
@version: 1.0.0
@since: 2024/5/21 19:37
"""

"""
class 定义
动态定义一个类：类名、父类、__dict__
def f(self):
    print(self)
    
d = {
    "name: "AAA",
    "f"： f,
    }
class A 的等价定义
A = type("A", (), d)
"""


class A:
    name = ""

    def f(self):
        print(self)
