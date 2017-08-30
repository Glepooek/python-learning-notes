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


class Fib(object):
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


limited1 = islice(Fib(), 0, 10)
for x in limited1:
    print(x)


def Fibonacci(num):
    coun, prev, curr = 0, 0, 1
    while coun < num:
        yield curr
        prev, curr = curr, curr + prev
        coun += 1


limited2 = islice(Fibonacci(100), 0, 10)
for x in limited2:
    print(x)