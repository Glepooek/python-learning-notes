### 迭代器和生成器(```Iterator and Generator```)

>本笔记是在阅读[生成器](https://eastlakeside.gitbooks.io/interpy-zh/content/Generators/)后，
又参考[完全理解Python迭代对象、迭代器、生成器](https://foofish.net/iterators-vs-generators.html)进行的整理。

在学习Python的数据结构时，相关概念容易使人产生混淆：
- 容器（a container）
- 可迭代对象（an iterable）
- 迭代器（an iterator）
- 生成器（a generator）
- 生成器表达式（a generator expression）
- 列表，集合，字典推导式（a {list, set, dict} comprehension）

这些概念的关系，如下图所示：

![相关概念关系图](relationships.png)

###### 1、容器
容器是一种把多个元素组织在一起的数据结构，容器中的元素可以逐个地迭代获取，可以用in, not in
关键字判断元素是否包含在容器中。通常这类数据结构把所有的元素存储在内存中（也有一些特例，并不是所有
的元素都放在内存，比如迭代器和生成器对象）在Python中，常见的容器对象有：
- list, deque, ....
- set, frozensets, ....
- dict, defaultdict, OrderedDict, Counter, ....
- tuple, namedtuple, …
- str

```python
str1 = 'boobar'
list1 = [1, 2, 3, 4]
tuple1 = (1, 2, 3, 4)
set1 = {1, 2, 3, 4}
dic1 = {'12': 'f00', 23: (1, 2, 3, 4)}

if 'b' in str1:
    print('b在str中')

if 2 not in list1:
    print('2不在list中')
else:
    print('2在list中')

if 1 in tuple1:
    print('1在tuple中')

if 3 in set1:
    print('3在set中')

# 通过key判断元素是否在字典中
if '12' in dic1:
    print('12在dic中')
```

尽管绝大多数容器都提供了某种方式来获取其中的每一个元素，但这并不是容器本身提供的能力，
而是可迭代对象赋予了容器这种能力，当然并不是所有的容器都是可迭代的，比如：[Bloom filter](https://zh.wikipedia.org/wiki/%E5%B8%83%E9%9A%86%E8%BF%87%E6%BB%A4%E5%99%A8)。

###### 2、可迭代对象
凡是实现```__iter__```方法，返回一个迭代器的对象都可称之为可迭代对象。
很多容器都是可迭代对象，还有更多的对象同样也是可迭代对象，比如处于打开状态的files，sockets等等。

```python
list1 = [1, 2, 3, 4]

iter1 = list1.__iter__()
iter2 = iter(list1)

print(type(iter1))
print(type(iter2))

# 输出结果
<class 'list_iterator'>
<class 'list_iterator'>
```

当运行如下代码时：

```python
list1 = [1, 2, 3]
for elem in list1:
    ...
```
实际执行情况，如下图所示：

![实际执行情况图](iterable-vs-iterator.png)

```python
from collections import Iterator
from collections import Iterable

class CustomIterator(Iterator):
    """
    自定义迭代器
    """

    def __init__(self, seq):
        self.index = 0
        self.seq = seq

    def __next__(self):
        if self.index > len(self.seq) - 1:
            raise StopIteration
        else:
            self.index += 1
            return self.seq[self.index - 1]

class CustomIterable(Iterable):
    """
    自定义可迭代对象
    """

    def __init__(self, seq):
        self.seq = seq

    def __iter__(self):
        return CustomIterator(self.seq)

# 自定义可迭代对象
print('自定义可迭代对象结果：')
for item in CustomIterable([1, 2, 3, 4, 4, 6]):
    print(item)
```

###### 3、迭代器
任何实现了```__iter__和__next__()（python2中实现next()）```方法的对象都是迭代器，
```__iter__```返回迭代器自身，```__next__```返回容器中的下一个值，如果容器中没有更多元素了，则抛出StopIteration异常。
迭代器内部持有一个状态，该状态用于记录当前迭代所在的位置，以方便下次迭代的时候获取正确的元素。
迭代器有一种具体的迭代器类型，比如list_iterator，set_iterator。
有很多关于迭代器的例子，比如itertools函数返回的都是迭代器对象。

```python
from itertools import count
from itertools import cycle
from itertools import islice

# 生成无限序列
counter = count(start=13, step=12)
print(next(counter))
print(next(counter))

# 从有限序列生成无限序列
colors = cycle(['red', 'black', 'green'])
print(next(colors))
print(next(colors))
print(next(colors))
print(next(colors))

# 从无限的序列中生成有限序列
limited = islice(colors, 0, 4)
for x in limited:
    print(x)
```

自定义一个斐波那契数列迭代器，体会下迭代器的内部执行过程：

```python
class Fib(Iterator):
    """
    自定义斐波那契数列迭代器
    """

    def __init__(self):
        self.prev = 0
        self.curr = 1

    def __iter__(self):
        return self

    def __next__(self):
        value = self.curr
        self.curr += self.prev
        self.prev = value
        return value

limited = islice(Fib(), 0, 10)
for x in limited:
    print(x)
```

###### 4、生成器
生成器其实是一种特殊的迭代器，但它不需要再像上面的类一样重写```__iter__()和__next__()```方法了，只需要一个```yiled```关键字。
生成器一定是迭代器（反之不成立），因此任何生成器也是以一种懒加载的模式生成值。
用生成器来实现斐波那契数列的例子是：

```python
def Fibonacci(num):
    coun, prev, curr = 0, 0, 1
    while coun < num:
        yield curr
        prev, curr = curr, curr + prev
        coun += 1


limited = islice(Fibonacci(100), 0, 10)
for x in limited:
    print(x)
```

###### 5、生成器表达式
生成器表达式是列表推倒式的生成器版本，看起来像列表推导式，但是它返回的是一个生成器对象而不是列表对象。

```python
generator = (x for x in range(10))

print(generator)
print(sum(generator))

# 输出结果
<generator object <genexpr> at 0x0397C060>
45
```

###### 总结
- 容器是一系列元素的集合，str、list、set、dict、file、sockets对象都可以看作是容器，
容器都可以被迭代（用在for，while等语句中），因此他们被称为可迭代对象。
- 可迭代对象实现了```__iter__```方法，该方法返回一个迭代器对象。
- 迭代器持有一个内部状态的字段，用于记录下次迭代返回值，它实现了```__next__和__iter__```方法，
迭代器不会一次性把所有元素加载到内存，而是需要的时候才生成返回结果。
- 生成器是一种特殊的迭代器，它的返回值不是通过return而是用yield。