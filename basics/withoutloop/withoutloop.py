# -*- coding: utf-8 -*-

"""
@author: takeEasy9
@description: 比较常用的python中替代for loop的方式
@version: 1.0.0
@since: 2024/5/18 10:47
"""
from timeit import timeit

"""
python内置一些函数，帮助我们在不使用用for loop情况下实现相同的功能
max/min: 求最大/最小值
all/any: 符合条件的是否存在
filter: 过滤符合条件的元素, 返回的是生成器
map: 遍历元素，并对元素做操作, 返回的也是生成器
zip: 合并两个列表，返回的也是生成器
"""


def with_for_v1():
    lst = []
    for i in range(100):
        lst.append(i)
    return lst


def without_for_v1():
    """列表推导式"""
    return [i for i in range(100)]


print(f"with_v1: {timeit(with_for_v1, number=10000)}")
print(f"without_for_v1: {timeit(without_for_v1, number=10000)}")

lst = [i for i in range(100)]


def with_for_v2():
    """普通地求列表中的最大值"""
    max_num = 0
    for num in lst:
        if num > max_num:
            max_num = num
    return max_num


def without_for_v2():
    """使用内置的max函数求最大值"""
    return max(lst)


print(f"with_v2: {timeit(with_for_v2, number=10000)}")
print(f"without_for_v2: {timeit(without_for_v2, number=10000)}")


def with_for_v3():
    """all/any"""
    for num in lst:
        if num > 50:
            return True
    return False


def without_for_v3():
    """all/any使用时推荐使用generator"""
    return any(num > 50 for num in lst)


print(f"with_v3: {timeit(with_for_v3, number=10000)}")
print(f"without_for_v3: {timeit(without_for_v3, number=10000)}")


def good(n):
    return n >= 60


def with_for_v4():
    """过滤list符合条件的元素"""
    ret = []
    for num in lst:
        if num >= 60:
            ret.append(num)
    return ret


def without_for_v4():
    """使用内置filter"""
    # 等价写法 filter(lambda n: n >= 60, lst)
    return filter(good, lst)


print(f"with_v4: {timeit(with_for_v4, number=10000)}")
print(f"without_for_v4: {timeit(without_for_v4, number=10000)}")


def change(n):
    return n * 2


def with_for_v5():
    """map的等价实现"""
    ret = []
    for num in lst:
        if num >= 60:
            ret.append(change(num))
    return ret


def without_for_v5():
    """使用内置 map 函数, map函数可以接受多个参数
    map(lambda n1, n2: n1 + n2, lst1, lst2)
    """
    # 等价写法 map(lambda n: n * 2, lst)
    return map(change, lst)


print(f"with_v5: {timeit(with_for_v5, number=10000)}")
print(f"without_for_v5: {timeit(without_for_v5, number=10000)}")

lst2 = [i for i in range(100)]


def with_for_v6():
    """zip的等价实现"""
    ret = []
    for i in range(min(len(lst), len(lst2))):
        ret.append((lst[i], lst2[i]))
    return ret


def without_for_v6():
    """zip合并列表"""
    return zip(lst, lst2)


print(f"with_v6: {timeit(with_for_v6, number=10000)}")
print(f"without_for_v6: {timeit(without_for_v6, number=10000)}")
