from itertools import count
from itertools import cycle
from itertools import islice

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


def fibonacci(num):
    coun, prev, curr = 0, 0, 1
    while coun < num:
        yield curr
        prev, curr = curr, curr + prev
        coun += 1


if __name__ == '__main__':
    # 生成无限序列
    counter = count(start=13, step=12)
    print('生成无限序列结果：')
    print(next(counter))
    print(next(counter))

    # 从有限序列生成无限序列
    colors = cycle(['red', 'black', 'green'])
    print('从有限序列生成无限序列结果：')
    print(next(colors))
    print(next(colors))
    print(next(colors))
    print(next(colors))

    # 从无限的序列中生成有限序列
    limited = islice(colors, 0, 4)
    print('从无限的序列中生成有限序列结果：')
    for x in limited:
        print(x)

    # 自定义可迭代对象
    print('自定义可迭代对象结果：')
    for item in CustomIterable([1, 2, 3, 4, 4, 6]):
        print(item)

    # 自定义迭代器
    limited1 = islice(Fib(), 0, 10)
    print('自定义迭代器结果：')
    for x in limited1:
        print(x)

    # 生成器
    limited2 = islice(fibonacci(100), 0, 10)
    print('生成器结果：')
    for x in limited2:
        print(x)
