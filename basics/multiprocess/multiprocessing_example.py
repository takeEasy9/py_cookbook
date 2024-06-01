# -*- coding: utf-8 -*-

"""
@author: takeEasy9
@description: multiprocessing
@version: 1.0.0
@since: 2024/5/15 20:00
"""
import multiprocessing
import os

"""两种最基础使用 multiprocessing 的示例"""


def f():
    print(os.getpid())


class MyProcess(multiprocessing.Process):
    """继承multiprocessing.Process, 重写run方法"""
    def run(self) -> None:
        f()


if __name__ == '__main__':
    print(os.getpid())

    p = multiprocessing.Process(target=f)
    p.start()
    p.join()

    p = MyProcess()
    p.start()
    p.join()
