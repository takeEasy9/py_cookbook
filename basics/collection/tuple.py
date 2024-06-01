# -*- coding: utf-8 -*-

"""
@author: takeEasy9
@description: namedtuple
@version: 1.0.0
@since: 2024/5/15 19:59
"""
from collections import namedtuple

"""
namedtuple优点
1.即可使用索引, 也可以使用属性取值
2.相较于普通的tuple给每个位置起了别名，p4[0], p4[1] 等价于p4.x, p4.y
3.相较于定义一个类实现相同功能来说，代码更简洁
"""


class Position:
    """保存坐标的类"""

    def __init__(self, x, y):
        self.x = x
        self.y = y


p1 = Position(1, 2)
p2 = (1, 2)
p3 = {'x': 1, 'y': 2}

Point = namedtuple("Position", ["x", "y"])
p4 = Point(1, 2)
print(p4[0], p4[1])
print(p4.x, p4.y)

# convert to a dictionary
d = p4._asdict()
print(d)

# convert from a dictionary
p5 = Point(**p3)
print(p5)
