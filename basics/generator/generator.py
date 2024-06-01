# -*- coding: utf-8 -*-

"""
@author: takeEasy9
@description: 生成器
@version: 1.0.0
@since: 2024/5/9 21:22
"""

"""
  生成器是一种特殊的迭代器，可以使用在for in 结构中，也可以对迭代器使用 next 函数，生成器惰性求值，
  直到对生成器使用next函数时才开始运行函数。
  生成器高级用法：send
"""


def gen(num):
    """简单的生成器函数"""
    while num > 0:
        yield num
        num -= 1
    # python 编译器会对生成器返回作特殊处理，而不是返回 None
    return


# 生成器对象
g = gen(5)
first = next(g)
for i in g:
    print(i)


def gen_v2(num):
    """可以使用send的生成器函数"""
    while num > 0:
        # yield 结果赋值
        tmp = yield num
        if tmp is not None:
            num = tmp
        num -= 1
    return


g2 = gen_v2(5)
first = next(g2)  # 等价于 first = g2.send(None)
print(f"first: {first}")
print(f"send: {g2.send(10)}")
for i in g2:
    print(i)
