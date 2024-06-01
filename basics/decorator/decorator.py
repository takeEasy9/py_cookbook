# -*- coding: utf-8 -*-

"""
@author: takeEasy9
@description: 装饰器
@version: 1.0.0
@since: 2024/5/9 21:49
"""

import time


def timeit(f):
    """不带参数的装饰器, 参数是函数,返回值也是函数"""

    def wrapper(*args, **kwargs):
        """
        *args, **kwargs 变长参数，以支持装饰任意函数
        """
        start = time.time()
        ret = f(*args, **kwargs)
        print(time.time() - start)
        return ret

    return wrapper


@timeit  # 等价于 my_func = timeit(my_func)
def my_func(x):
    time.sleep(x)


my_func(1)


def timeit_v2(iteration):
    """带参数的装饰器, 参数是函数,返回值也是函数"""

    def inner(f):
        def wrapper(*args, **kwargs):
            """
            *args, **kwargs 变长参数，以支持装饰任意函数
            """
            start = time.time()
            for _ in range(iteration):
                ret = f(*args, **kwargs)
            print(time.time() - start)
            return ret

        return wrapper

    return inner


@timeit_v2(1000)  # 等价于 double = timeit_v2(1000)(double)
def double(x):
    return x * 2


double(2)

"""类装饰"""


class Timer:
    """不带参数的类装饰器"""

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        """__call__将类的实例对象变为callable"""
        start = time.time()
        ret = self.func(*args, **kwargs)
        print(f"Time: {time.time() - start}")
        return ret


@Timer  # 等价于 add = Timer(add)
def add(a, b):
    return a + b


print(add(2, 3))


class Timer_v2:
    """不带参数的类装饰器"""

    def __init__(self, prefix):
        self.prefix = prefix

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            start = time.time()
            ret = func(*args, **kwargs)
            print(f"{self.prefix}{time.time() - start}")
            return ret

        return wrapper


@Timer_v2(prefix="curr_time:")  # 等价于 add = Timer_v2(prefix="curr_time:")(add)
def add(a, b):
    return a + b


print(add(2, 3))


def add_str(cls):
    """装饰类的装饰"""

    def __str__(self):
        return str(self.__dict__)

    cls.__str__ = __str__
    return cls


@add_str  # 等价于 MyObject = add_str(MyObject)
class MyObject:
    def __init__(self, a, b):
        self.a = a
        self.b = b


o = MyObject(1, 2)
print(o)

"""在class内部定义一个装饰器"""


class Decorators:

    def log_function(self, func):
        def wrapper(*args, **kwargs):
            print(f"function start!")
            print(f"args: {args}")
            ret = func(*args, **kwargs)
            print(f"function end!")
            return ret

        return wrapper


d = Decorators()


@d.log_function
def fib(n):
    if n <= 1:
        return 0
    return fib(n - 1) + fib(n - 2)


fib(3)

"""在class内部定义一个装饰器作为类方法, 解决装饰器使用需要实例化对象的问题"""


class Decorators_v2:
    @classmethod
    def log_function(cls, func):
        def wrapper(*args, **kwargs):
            print(f"function start!")
            print(f"args: {args}")
            ret = func(*args, **kwargs)
            print(f"function end!")
            return ret

        return wrapper


@Decorators_v2.log_function
def fib(n):
    if n <= 1:
        return 0
    return fib(n - 1) + fib(n - 2)


fib(5)

"""在class内部定义一个装饰器作为静态方法, 解决装饰器使用需要实例化对象的问题"""


class Decorators_v3:
    @staticmethod
    def log_function(func):
        def wrapper(*args, **kwargs):
            print(f"function start!")
            print(f"args: {args}")
            ret = func(*args, **kwargs)
            print(f"function end!")
            return ret

        return wrapper


@Decorators_v3.log_function
def fib(n):
    if n <= 1:
        return 0
    return fib(n - 1) + fib(n - 2)


fib(6)

"""将装饰器封装到类里, 在类里使用装饰器"""


class Decorators_v4:

    def log_function(func):
        def wrapper(*args, **kwargs):
            print(f"function start!")
            print(f"args: {args}")
            ret = func(*args, **kwargs)
            print(f"function end!")
            return ret

        return wrapper

    @log_function
    def fib(self, n):
        if n <= 1:
            return 0
        return fib(n - 1) + fib(n - 2)

    log_function = staticmethod(log_function)

