# Python

记录 Python 一些高级技巧，大部分来自B站Up@码农高天不基础的python合集视频。

[toc]

## 变量

### 变量命名

Python 中合法的变量名是由字母（广义字母，在 Python3  中可以定义中文变量名）、下划线、和数字组成，并且第一个字符不可以是数字。

当变量名包含有效程度更多时，就是一个好的变量名。在变量名与变量长度上做取舍。

```
n = 'Bob' ❌
name = 'Bob' ❌
username = 'Bob' ✅
# ???
the_username_from_my_database_on_aws = 'Bob'
```

Python 中变量命名风格有以下几种：

- lower_underscore， Python 中的 module，variable, function，method 都是使用该命名风格。
- PPER_UNDERSCORE, Python中常量的定义使用该风格。
- CamelCase，Python 类的定义使用大驼峰命名风格。

使用下划线 **_** 来表示未被使用到的变量

```
import random
for _ in range(10):
	print(random.random())
```

**弱私有**：变量以一个下划线开头，单下划线开头的变量，在 from module import  * 时，是不会 import 单下划线开头的 global variable的。

**强私有**：变量以两个下划线开头，Python 在 编译器会对 class 里面对双下划线开头的变量或方法，进行了命名改写（name mangling) ，在命名改写（name mangling)过程中把双下划线开头的变量名称或方法名前增加了一个下划线 class 名，防止在编程中误用强私有变量或方法。

### 变量作用域

全局变量：

局部变量：Python 的局部变量只有 function scope, if 语句定义的变量不会产生新的作用域。

闭包变量：

## 闭包

能从一个函数访问另一个函数中的变量的机制，我们称之为闭包。

```
def f():
	data = []
	def inner(value):
		data.append(value)
		return data
	return inner
g = f()
print(g(1))
print(g(2))
```

Python 闭包实现机制：

Cell Object：Python 中用来保存被多个 scope 所引用的变量的。

当 Python 编译器发现一个函数使用了其他函数的变量时，就会运行 COPY_FREE_VARS，SET_FUNCTION_ATTRIBUTE 将 cell object 保存到闭包函数的 `__closure__` 属性中。

## 迭代器

典型的 Python for loop 结构：

```
lst = [1, 3, 5]
for i in list:
	print(i)
```

for loop 遍历字典

```
dict = {'a': 1， 'b':2}
for d in dict:
	print(d)
```

甚至可以用来遍历文件

```
with open('my.txt') as f:
	for i in f:
		print(i)
```

Python for loop 实现背后涉及到两个核心概念：可迭代对象（iterable）与迭代器（iterator）。 Python 官方文档  [Glossary — Python 3.13.2 documentation](https://docs.python.org/3/glossary.html) 给出二者的定义。

可迭代对象（iterable）:如果一个类定义了  `__iter__()`或 `__getitem__()`方法，那这个类的对象就是可迭代（iterable）的。可迭代对象（iterable）更像是一个 container，一个数据保存者，是无状态的，使用内置方法 iter( ) 方法可以返回一个迭代器（iterator）。

迭代器（iterator）：实现了`__next()__`方法的对象，有状态，使用内置方法 next( ) 方法可以返回可迭代对象里的下一个值，没有值时抛出`StopIteration`，Python 官方文档中要求迭代器（iterator）也要是可迭代的，需要实现`__iter__()`方法。

**迭代器示例**：[使用 iterator 实现链表结构](./basics/iterator/iterator.py)

## 生成器

生成器函数：Python 在编译时发现函数定义中有 yield 关键字时，会将该函数视为一个生成器函数，调用一个生成器函数会返回一个生成器对象，当对一个生成器对象使用 next 函数时，才开始真正运行函数本体。

生成器对象：Python 生成器（generator）本身就是一个特殊的迭代器（iterator），可以在 for loop 结构中使用生成器，也可以使用 next() 函数，生成器与迭代器的用法几乎一样。

生成器高级用法 `send()` 函数：

```
def gen(num):
	while(num > 0):
		tmp = yield num
		if tmp is not None:
			num = tmp
		num -= 1
g = gen(5)
g = gen(5)
first = next(g)
print(f'first: {first}')
print(f'send: {g.send(10)}')
```

next() 和 send(None) 是等价的。

生成器示例：[生成器](./basics/generator/generator.py)

## 装饰器

Python 中一起皆对象，函数也是一个普通对象，可以作为函数参数和返回值。

函数装饰器：输入与输出都是函数的函数。示例：[@timeit](./basics/decorator/decorator.py)

函数装饰器工厂：带参数的函数装饰器。示例：[@timeit_v2](./basics/decorator/decorator.py)

用作装饰器的类：示例：[@Timer ](./basics/decorator/decorator.py)

类装饰器：输入与输出都是类的函数。示例：[@add_str ](./basics/decorator/decorator.py)

如何将一组装饰器封装到类里：示例：[@Decorators_v4 ](./basics/decorator/decorator.py)

### @dataclass 装饰器

`@dataclass` (装饰器)[[dataclasses — Data Classes — Python 3.13.2 documentation](https://docs.python.org/3/library/dataclasses.html#module-contents)]默认会自动为类生成 `__repr__` 、`__eq__`方法，`@dataclass` 装饰器参数如下：

```
@dataclasses.dataclass(*, init=True, repr=True, eq=True, order=False, unsafe_hash=False, frozen=False, match_args=True, kw_only=False, slots=False, weakref_slot=False)
```

order : 设置为 True， 会自动为生成比大小的方法，比大小方法是按字段顺序依次比较，遇到第一个能区分结果的字段时，就停止比较。

### @staticmethod 装饰器

@staticmethod 用来装饰类的静态方法（staticmethod），静态方法除了第一个参数像实例方法或类方法那样是 self 或  cls， 在使用上与定义在类外面的正常函数是一样的，类的静态方法更多的是把这个函数放到了这个类的命名空间下面，让这个函数从属于这个类，它的意义是提供了一个更好的封装，当我们想把一个函数绑定在一个类上，而不是类的实例对象时，可以使用静态方法。

静态方法既可以通过类来调用，也可以通过类的实例对象调用。

###  @classmethod 装饰器

classmethod 与 staticmethod 一样可以实现将函数绑定类上，而不是这个类的实例对象上，区别在于 classmethod 第一个 argument 是这个 class，classmethod 无论在类上调用还是在类的实例对象上调用，第一个 argument cls 都是 class。

@classmethod 与 @staticmethod 实现机制类似，以较简单的 @staticmethod 实现机制做说明。

@staticmethod 装饰的函数本身是一个 staticmethod object， 访问 staticmethod object 时返回被装饰的函数，其背后的机制就是**描述器（descriptor）**。

## 描述器

描述器（descriptor）：任何定义了 `__get__()`、`__set__()` 或 `__delete__()` 方法的对象。当**类的某个属性**是描述符时，使用 `a.b` 来获取、设置或删除属性时，会在 `a` 所属类的字典中查找名为 `b` 的对象，但如果 `b` 是一个描述符，则会调用相应的描述符方法， 在**实例对象**上描述器不会生效。

描述器实现机制：

LOAD_ATTR --> PyObject_GetAttr(Python 属性访问查找逻辑)

如果`__get__()`、`__set__()`方法都有，优先使用描述器（descriptor），如果不是的话，先在自己的`__dict__`里面找，如果`__dict__`不存在，就尝试使用 描述器（descriptor）的`__get__()`方法。

## 全局解释器锁

GIL(Global Interpreter Lock): 全局解释器锁。

Python 设计者为了解决多个线程同时尝试去读或写 python object 的数据竞争冒险问题，决定给 Python 设计一个全局的锁（GIL）。通过 GIL，Python可以保证每一个 bytecode 都是拿到线程锁的， bytecode 的执行不会被其他线程打断。

GIL 优点：

- 设计简单有效，相较于每一个 object 都实现一个自己的锁要简单非常多。
- 由于只有一个锁，避免了死锁问题。
- 单线程程序或没法并行的多线程程序，全局锁的性能是非常优秀的，运行时只需要获取一次锁，避免多次获取锁的性能损失。
- 给 Python 代码 写 c extension 变得简单，在 c 代码里修改 Python object 时，不用考虑线程的竞争冒险问题。
- 历史原因：上个世纪90年代，多核 CPU 不存在，多线程存在的意义，不会因为某一个线程的计算量过大，导致其他任务没有机会执行。

GIL 缺点：

- 进入 21世纪后，多核 CPU 开始普及，导致 Python 的多线程没有办法利用多核来提高自己的运算速度。为了解决这个问题，可以使用 mutiprocessing（多进程）来解决这个问题，利用多进程来使用 CPU 的多个核心，使用多进程可以避开 GIL 这个问题。
- GIL 地存在，Python 多线程编程还是要**加锁**来保证结果的正确性。

PEP 703 Python 将3.13 中试验性地移除 GIL，没有 GIL 的版本 单线程性能下降约 30%，4 个线程达到两倍的速度，没办法达到4倍或3倍多的速度。

## 单元测试

在Python 中做单元测试推荐使用 Python 自带的测试框架 unittest。

测试文件代码全部放到根目录下的 tests 这个模块下，在根目录下执行 `python -m unittest`， Python 会自动运行测试代码。

```
import unittest
# 测试类要继承 unittest.TestCase
class TestNode(unittest.TestCase):
		#测试方法以 test_ 开头
	    def test_iter(self):
        n = Node('node1')
        iterator = n.__iter__()
        # 以相应的 assert 方法判断结果是否符合预期
        self.assertTrue(isinstance(iterator, Iterable))
```

unittest 实例：[unittest](./tests/test_node.py)

`python -m unittest` 后面可以指定测试代码 module、测试类，测试类的方法，来单独运行某些测试 case。

使用coveragepy计算单元测试的覆盖率：`coverage run -m unittest`

上面这条命令产生一个 .coverage 文件，这个文件里以二进制的形式保存着我们的覆盖率数据，使用 `coverage report` 读取覆盖率数据，使用  `coverage report -m` 查看没有被单元测试覆盖到的行。

使用 `coverage html` 命令，会生成 htmlcov 文件夹，使用 `python -m http.server --directory htmlcov/` 运行一个 http server，在浏览器上访问对应地址，在对应的源文件上显示哪些行被覆盖到了，哪些行没有被覆盖。

coverage 常用参数：

- --source：指定要测试的库，示例：`coverage run --source objprint -m unitest`。
- --omit：忽略某些源文件测试覆盖率，示例：`coverage run --source objprint --omit=*/objprint/executing/* -m unitest`。

有时 coverage 命令行参数复杂，不好记忆，这时可以使用 .coveragerc 文件，将coverage 命令配置保存到  .coveragerc 文件。 .coveragerc 文件相当于 coverage 的 configuration 文件，当需要比较复杂的自定义配置的时候， .coveragerc 文件提供了一种比较好的方式来保存这个配置。

利用 Github actions 自动运行 unit test, 产生一个 XML report，最后使用这个 codedev action，将生成的 XML report 上传到 codedev 上去，codedev 网站会为开源项目免费生成测试率报告。

Github actions 配置文件：

```
name: Generate coverage report
run: |
    coverage run --source objprint --parallel-mode --m unittest
    coverage combine
    coverage xml -i
env:
COVERAGE_RUN: True
name: Upload report to Codecov
uses: codecov/codecov-action@v3
with:
	file: ./coverage.xml	
```

## Pdb(Python debugger)

pdb 是 Python 官方提供的命令行 debugger，提供了暂停程序和检视程序状态这两项核心功能。

暂停程序：

可以修改源代码时，在源代码中想要暂停的地方加入 breakpoint()，通过 Python 命令运行代码时，会进入 Pdb 命令行界面。 

 Pdb 命令行常用命令：

- p： 代表 print， 可以打印变量。
- w 或 where：查看当前调用栈。
- l 或 lst：查看当前位置附近的源代码，默认打印当前行前后的11行代码，再输入一个 l ，它会往下再翻11行，l .(l 后跟点，回到当前行)， ll(longlst) 显示当前这个函数的全部代码。
- u 或 up：改变当前帧。
- d 或 down：往下调整栈帧。
- n 或 next：运行下一行程序。
- s：step，单步调试。s 与 n 只有在有函数调用时才有区别。
- retval：通过 retval 命令拿到返回值。
- until：until 9, 运行直到行数大于行数 9 。
- c 或 continue：程序继续执行。
- b 或 break：在无法对源代码进行修改的前提下设置断点，如 b 5，表示在对应的文件地第 5 行设置了断点。b inspect.currentframe()，表示在 currentframe() 函数里设置断点。b 和 break 命令是等价的，break 后什么都不加，会列出当前所有断点。
- clear：clear 命令用来删除断点，clear 1 表示删除 编号为 1 的断点。
- q 或 quit：退出 Pdb 。

## Python 类(class)

### class 背后的机制和原理

当我们定义一个 class 时，首先相当于运行了所有在这个 class 里面的代码，然后把产生的所有局部变量的名字和其对应值都保存到这个 class 的 `__dict__`里面，然后建立一个 type，然后把这个 type 赋值给了这个 class 的名字的变量。

使用type动态创建类，type函数接受三个参数，第一个是类的名字，第二是这个类的父类，第三是存储类属性的 dictionary。

```
#class A：
#	name = 'AAA'
#	def f(self):
#		print(1)
def f(self):
	print(1)
d = {
'name': 'AAA',
 'f': f
}
A = type('A', (), d)
```

### MRO(Method Resolution Order)

MRO 即方法解析顺序（Method Resolution Order）。它是 Python 用于在多重继承情况下确定调用方法和属性时查找顺序的一种机制。

```
# 获取类 M 的 MRO
print(M.__mro__)
print(M.mro())
```

Python MRO 从 Python 2.3 开始使用 1996年提出的 C3 线性化算法用作 MRO 算法。

C3 线性化算法满足三个属性：

- local precedence order:  局部优先顺序，当 class 继承了多个父类时，优先使用写在前面的 class，除了 这个类外，这个类的所有的子类也要保证这个顺序。
- monotonicity：单调性，任何一个 class 使用方法必须来自它的直接父类，不可以直接跳过父类往上寻找。
- extended precedence graph：extended precedence graph 是描述子类和父类之间的继承关系。

### class里定义的函数是怎么变成方法的？

```
class A：
	def f(self, data):
		print(self.name)
		print(data)
o = A()
print(A.f) # function
print(o.f) # bound method
```

上述示例中，A.f 就是一个非常普通的 function，o.f 已经变成 bound method，而所谓的 bound method 就是这个函数上绑定了一个对象，o.f 实际上就是返回了一个绑定在 o 自己本身上面的一个 method，当调用 o.f 时不需要给出 self 这个参数，在调用 o.f 时把自己这个 object 作为第一个参数传进去，o.f 不再是在 class A 定义的 f 函数。

当我们在 class A 里面定义了这个函数 f 的时候，实际上产生了一个 function object , 然后 这个 function object 保存到 class A 的 `__dict__` 里面，在 o.f调用时由于 f 这个名字并不在 o 的 `__dict__` 里面，所以会在 class A 里寻找 f 属性，从 class A 的  `__dict__` 取出 f 这个属性，这时 f 还是一个 function object。

在使用读取属性，顺着 MRO 从类里拿到一个 attribute 的时候，首先会检查属性有没有 descriptor `__get__` 函数，如果有 `__get__` 函数，返回的不再是这个 attribute，而是这个 attribute 调用 descriptor `__get__`函数的返回值。o.f 在属性查找过程中在 class A 中查找，返回的并不是 A.f，而是 A.f  `__get__`函数的返回值，这个返回值是一个绑定了调用对象 o 的方法的 object，因此在调用 o.f 时只需要传入 self 之后的内容，o.f会自动地把self 对应的 object 补到第一个参数地位置。

了解上述原理后，可以解决在动态给对象或类增加函数或方法时，需不需要写 self 参数，调用时要不要传递 self 参数。

```
class A:
	pass
def f(self, data):
    print(self.name)
    print(data)
# A.f = f
# o = A()
# o.f('hello') 因为在类上定义 f 函数, 在调用 f 函数时, 会自动把 function 转换为 绑定在对象 o 上的 method, 不需要传入 self 参数

o = A()
o.f = f
# o.f('hello') 由于 f 定义在对象上，存在了对象的 __dict__ 里面, 在调用时就不再会通过 descriptor get 函数返回绑定对象的 method, 需要在调用时传入 self 参数。
# 正确调用 f 
o.f(o, 'hello')

```

小测试：

```
class FuncDescr:
	def __get(self, *args):
		def f(self, data):
    		print(self.name)
    		print(data)
    	return f
class A:
	f = FuncDescr()
o = A()
o.name = 'Bob'
# 下面调用 f 函数, 哪个是对的?
o.f('hello')
o.f(o, 'hello')
```

### metaclass

A 指定元类为M，而不是继承这样的写法，这时我们称 M 为 A 的元类。

```
class M(type):
	def __new__(cls, name, bases, dict):
		return type.__new__(cls, name, bases, dict)
class A(metaclass=M)：# 等价于 A = M('A', (), {})
	pass
```

使用元类可以使类创建过程更加灵活，metaclass 一般是用来解决继承没办法解决的问题的。

```
class M(type):
	def __new__(cls, name, bases, dict):
		return type.__new__(cls, name, bases, dict)
	def __init__(cls, name, bases, dict):
		return type.__init__(cls, name, bases, dict)
    def __call__(cls, *args, **kwargs):
    	# 创建 A 实例时被调用
    	return type.__call__(cls, *args, **kwargs)
class A(metaclass=M)：
	pass
```

