# -*- coding: utf-8 -*-

"""
@author: takeEasy9
@description: python try finally
@version: 1.0.0
@since: 2024/5/18 11:35
"""
"""
finally：对于sys.exit(0) ctr+ c, finally都能执行
finally不能能执行场景: SIGTERM(kill -15 PID), SIGKILL(kill -9 PID), os._exit(0), segfault


"""
# python 普通的try catch
try:
    raise StopIteration("停止迭代")
except Exception as e:
    print(e)
finally:
    # finally 保证即使发生异常，也能执行
    print("finally 代码执行")


try:
    raise ValueError("值错误")
finally:
    # finally 保证即使发生异常，也能执行
    print("finally 代码执行")
