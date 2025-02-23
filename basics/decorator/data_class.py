# -*- coding: utf-8 -*-

"""
@author: takeEasy9
@description: dataclass decorator
@version: 1.0.0
@since: 2025/2/22 21:22
"""
from dataclasses import dataclass, field
from typing import ClassVar


class NormalPerson:
    """Python 具有 name 和 age 类普通的写法"""
    def __init__(self, name, age):
        self.name = name
        self.age = age


@dataclass
class Person:
    """使用 @dataclass 的写法"""
    name: str
    age: int
    # 使用 field 定义 dataclass 的 field 行为
    height: int = field(default=0, compare=False)
    # 使用 ClassVar 设置类变量
    people_num = ClassVar[int] = 0

    def __post_init__(self):
        """ init 方法执行后被调用"""
        Person.people_num += 1


p = Person('Alice', 18)
print(p)
