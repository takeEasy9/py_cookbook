# -*- coding: utf-8 -*-

"""
@author: takeEasy9
@description: python dict
@version: 1.0.0
@since: 2024/5/15 19:59
"""
import weakref

"""
weakref.WeakValueDictionary 当字典里的值，只用字典保持对其的引用时，将其从字典中删除
相对应的有 weakref.WeakKeyDictionary
Python 中不是每个对象都支持弱引用，如 int, str
如果一个class 定义了 __slot__ 就不支持弱引用了，如果=要支持弱引用， 需要在__slot__中增加__weakref__这一项
"""
# players = {}
players = weakref.WeakValueDictionary()


class Player:
    def __init__(self):
        for i in range(1000):
            if i not in players:
                self.id = i
            players[self.id] = self


def game():
    p1 = Player()
    p2 = Player()


for _ in range(2):
    game()

print(players)
