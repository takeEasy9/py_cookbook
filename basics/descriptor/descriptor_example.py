# -*- coding: utf-8 -*-

"""
@author: takeEasy9
@description: python 描述器
@version: 1.0.0
@since: 2024/5/19 15:39
"""

""""
descriptor: 具有__get__(), __set__(), __delete__()方法中任意一个方法的对象
descriptor是python非常重要的底层机制, Python内部的property，classmethod, staticmethod, super都是描述器
descriptor生效前提：descriptor对象必须是类属性, descriptor对象作为实例属性不会生效
descriptor属性访问查找顺序：
1.__get__(), __set__()都存在, 优先返回__get__()的返回值
2.__get__(), __set__()任意缺失, 在对象的__dict__中查找
3.如果对象的__dict__不存在, 返回__get__()的返回值
4.如果没有_get__()则返回descriptor对象
"""


class Name:
    def __get__(self, instance, owner):
        return "Peter"


class A:
    name = Name()


class AV1:
    def __init__(self):
        # descriptor对象作为实例属性不会生效
        self.name = Name()


obj = A()
# o.name属性访问 等价于调用了 Name的 __get__ 函数
print(obj.name)
print(A.name)
o1 = AV1()
print(o1.name)

# __set__()不存在, 在__dict__中查找
obj1 = A()
obj1.name = "Bob"
print(obj1.__dict__)
print(obj1.name)

# __get__(), __set__()都存在, 优先返回__get__()的返回值
obj2 = A()
obj2.name = "Bob"
Name.__set__ = lambda x, y, z: None
print(obj2.name)
