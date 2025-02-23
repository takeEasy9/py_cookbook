# -*- coding: utf-8 -*-

"""
@author: takeEasy9
@description: python 闭包实现机制
@version: 1.0.0
@since: 2024/5/8 21:52
"""

"""
 闭包简单描述：能一个函数里去读取其他函数中的变量的机制叫做闭包
 实现机制：cell object 保存被访问的局部变量
 注意：在内层函数作用域中对外层函数同名变量时，如果不使用nonlocal关键字，
 则把变量认为是内层函数的局部变量
"""


def f():
    data = []

    def inner(value):
        data.append(value)
        return data

    return inner


g = f()
# g两次调用使用的是同一个data
print(g(1))
print(g(2))
# 证明data保存在cell object中
print(g.__closure__)
print(hex(id(g(3))))


def f_v2():
    data = []

    def inner(value):
        data.append(value)
        return data

    """
     对data变量重新赋值, 证明闭包都实现机制不是对变量的简单复制
    """
    data = [0]
    return inner


g_v2 = f_v2()
# 即使对data变量重新赋值, g两次调用使用的也是是同一个data
print(g_v2(1))
print(g_v2(2))


def fab_outer():
    a = 0
    b = 1

    def fab_inner():
        nonlocal a
        nonlocal b
        a, b = b, a + b
        return a

    return fab_inner


fab = fab_outer()
print(fab())
print(fab())
