# -*- coding: utf-8 -*-

"""
@author: takeEasy9
@description: 迭代器
@version: 1.0.0
@since: 2024/5/9 20:36
"""


class NodeIter:
    """iterator必须有 __next__ 方法, 保证被next函数作用时,
        可以返回下一个iterable里的值
    """
    def __init__(self, node):
        self.curr_node = node

    def __next__(self):
        if self.curr_node is None:
            raise StopIteration
        node, self.curr_node = self.curr_node, self.curr_node.next
        return node

    def __iter__(self):
        """
        返回iterator本身，以满足官方文档要求：一个iterator也是iterable
        """
        return self


class Node:
    """iterable是个容器，可以提供iterator
       所以iterable 对象 必须有 __iter__ 方法, 返回迭代器对象
    """
    def __init__(self, name):
        self.name = name
        self.next = None

    def __iter__(self):
        return NodeIter(self)


node1 = Node("node1")
node2 = Node("node2")
node3 = Node("node3")
node1.next = node2
node2.next = node3
"""for in 结构中要求对象必须是iterable的对象
或者是sequence, 有__getItem__ 方法
"""
for node in node1:
    print(node.name)
