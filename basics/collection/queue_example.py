# -*- coding: utf-8 -*-

"""
@author: takeEasy9
@description: 队列
@version: 1.0.0
@since: 2024/5/15 19:58
"""
import queue
import threading

"""
queue FIFO 线性数据结构
1.有序地安排任务, 利用实现bfs(宽度优先遍历)
2.多线程producer-consumer模型
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def bfs(root):
    q = queue.Queue()
    q.put(root)
    while not q.empty():
        # 相较于list的pop操作, queue的get与pop操作都是常数时间的
        node = q.get()
        print(node.data)
        if node.left:
            q.put(node.left)
        if node.right:
            q.put(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.right = Node(5)
bfs(root)


def consumer(q):
    while True:
        # 阻塞操作
        item = q.get()
        print("Consumer: ", item)
        q.task_done()


def producer(q):
    for i in range(10):
        q.put(i)


print("producer-consumer")
q = queue.Queue()
#
t1 = threading.Thread(target=consumer, args=(q,), daemon=True)
t2 = threading.Thread(target=consumer, args=(q,), daemon=True)
t1.start()
t2.start()

producer(q)
# join 等待consumer完成
q.join()
