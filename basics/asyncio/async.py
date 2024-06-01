# -*- coding: utf-8 -*-

"""
@author: takeEasy9
@description: python 协程
@version: 1.0.0
@since: 2024/5/13 17:01
"""
import asyncio
import time

"""
python asyncio 基于eventloop, 同时运行的任务只能有一个
"""


async def main():
    print("hello")
    await asyncio.sleep(1)
    print("world!")


# 调用main方法返回coroutine
asyncio.run(main())
print("main ended")


async def say_after(delay, what):
    await asyncio.sleep(delay)
    print(what)


async def main_v2():
    """多个任务示例"""
    print(f"started at {time.strftime('%X')}")
    await say_after(1, "hello")
    await say_after(2, "world!")
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main_v2())
print("main_v2 ended")


async def main_v3():
    """create_task"""
    task1 = asyncio.create_task(say_after(1, "hello"))
    task2 = asyncio.create_task(say_after(2, "world!"))

    print(f"started at {time.strftime('%X')}")
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main_v3())
print("main_v3 ended")


async def say_after_v2(delay, what):
    """有返回值的 async 函数"""
    await asyncio.sleep(delay)
    return f"{what} - {delay}"


async def main_v4():
    """await 获取返回值"""
    task1 = asyncio.create_task(say_after_v2(1, "hello"))
    task2 = asyncio.create_task(say_after_v2(2, "world!"))

    print(f"started at {time.strftime('%X')}")
    ret1 = await task1
    ret2 = await task2
    print(ret1)
    print(ret2)
    print(f"finished at {time.strftime('%X')}")


asyncio.run(main_v4())
print("main_v4 ended")


async def main_v5():
    """async gather函数 获取多个task返回值"""
    task1 = asyncio.create_task(say_after_v2(1, "hello"))
    task2 = asyncio.create_task(say_after_v2(2, "world!"))

    print(f"started at {time.strftime('%X')}")
    ret = await asyncio.gather(task1, task2)
    print(ret)
    print(f"finished at {time.strftime('%X')}")

asyncio.run(main_v5())
print("main_v5 ended")