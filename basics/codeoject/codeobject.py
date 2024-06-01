# -*- coding: utf-8 -*-

"""
@author: takeEasy9
@description: python code object
@version: 1.0.0
@since: 2024/5/27 21:27
"""


def f():
    pass


code = f.__code__
# 二进制表示的字节码
print(code.co_code)
# 函数名称
print(code.co_name)
# 函数在哪个文件定义的
print(code.co_filename)
# bytecode 对应源代码行数映射
print(code.co_lnotab)


def f1(a, b=3, *args, **kwargs):
    print(a + b)


def f2(a, b=3, /, *args, **kwargs):
    """ '/': python 中 positional only arguments 语法
    '/'之前的参数都是 positional only arguments
    """
    print(a + b)


def f3(a, *, b=3, **kwargs):
    """'*': python 中 keyword only arguments 语法
    '*'之后所有的参数都是 keyword only arguments
     """
    print(a + b)


code = f1.__code__
# 函数参数相关
# number of arguments (not including keyword
# only arguments, * or ** args)
print(code.co_argcount)
# number of positional only arguments
print(code.co_posonlyargcount)
# number of keyword only arguments (not including ** arg)
print(code.co_kwonlyargcount)


def f4(a, b):
    return a + b


code = f4.__code__

print(f"nlocals: {code.co_nlocals}")
print(f"varnames: {code.co_varnames}")
print(f"names: {code.co_names}")
# 被其他scope引用的变量
print(f"cellvars: {code.co_cellvars}")
# 变量来自其他的scope
print(f"freevars: {code.co_freevars}")
# 函数中的常量
print(f"consts: {code.co_consts}")
