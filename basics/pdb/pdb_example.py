# -*- coding: utf-8 -*-

"""
@author: takeEasy9
@description: Pdb
@version: 1.0.0
@since: 2025/3/1 9:39
"""


def g(data):
    return data * data

def f(x):
    breakpoint()
    lst = []
    for i in range(x):
        val = g(i)
        lst.append(val)
    return lst

f(3)