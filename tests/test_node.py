# -*- coding: utf-8 -*-

"""
@author: takeEasy9
@description: unittest example
@version: 1.0.0
@since: 2024/5/18 9:22
"""
import unittest
from typing import Iterable

from basics.iterator.iterator import Node

"""
1.测试文件必须以 test_开头
2.常用的验证函数
        assertEqual
        assertTrue
        assertRaises: 验证是否抛出指定异常
3. setup、tearDown在每个testcase之前或之后执行一段逻辑
setUpClass、tearDownClass在每个 testclass 之前或之后执行一段逻辑
4. 通过 unittest.skipIf 使testcase在某些情况下不运行
5. 通过控制unittest command line 指定要运行的testcase 
如 python -m unittest tests.test_node.TestNode.test_init
"""


class TestNode(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("start")

    @classmethod
    def tearDownClass(cls) -> None:
        print("end")

    def setUp(self) -> None:
        print("start")

    def tearDown(self) -> None:
        print("end")

    def test_init(self):
        n = Node('node1')
        self.assertEqual(n.name, 'node1')

    def test_iter(self):
        n = Node('node1')
        iterator = n.__iter__()
        self.assertTrue(isinstance(iterator, Iterable))
