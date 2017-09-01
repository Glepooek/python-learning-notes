### itertools模块

itertools模块中的内置函数用于创建高效迭代器。

###### 1、itertools.takewhile(predicate,iterable)
返回所有满足predicate为true的iterable的连续元素，直到predicate为false，后续元素不再被返回。例如：

```python
from itertools import takewhile

for value in takewhile(lambda x: x < 5, [1, 3, 5, 6]):
    print value

# 输出结果:
1
3
```

###### 2、itertools.dropwhile(predicate, iterable)
直到predicate为false，就返回iterable后续数据， 否则drop掉 例如：

```python
from itertools import dropwhile

for each in dropwhile(lambda x: x<5, [2,1,6,8,2,1]):
    print each

# 输出结果:
6
8
2
1
```

###### 3、itertools.filterfasle(predicate,iterable)
返回predicate为False的元素，如果predicate为None,则返回所有iterable中为False的项 例如：

```python
from itertools import filterfalse

for value in filterfalse(lambda x: x % 2, range(10)):
    print value

# 输出结果:
0
2
4
6
8
```

###### 4、itertools.starmap(function,iterable)
返回一个迭代器，该迭代器的值是所有function(iter)的返回值，function(iter)函数的参数iter为iterable的元素。例如：

```python
from itertools import starmap

for value in starmap(lambda x, y: x * y, [(1, 2), (3, 4)]):
    print value

# 输出结果:
2
12
```

###### 5、itertools.repeat(object,[,times])
返回一个迭代器，该迭代器的值为重复返回的object对象，如果指定了times,则返回times次 例如：

```python
from itertools import repeat
for value in repeat('a', 2):
    print value

# 输出结果:
a
a
```

###### 6、itertools.cycle(iterable)
无限迭代iterable中的元素 例如：

```python
from itertools import cycle

for each in cycle('ab'):
    print each

# 输出结果:
a
b
a
b
.
.
```

###### 8、itertools.count(start=0,step=1)
返回以start开始，step递增的序列，无限递增 例如：

```python
from itertools import count

for each in count(start=0, step=2):
    print each

# 输出结果:
1
2
3
.
.
```

###### 9、itertools.islice(iterable, start,stop[,step])
相当于迭代器方式的切片操作。例如：

```python
from itertools import islice

for value in islice('abcdefg', 1, 4, 2):
    print value

# 输出结果:
b
d
```

###### 10、itertools.combinations(iterable, r)
返回指定长度的"组合" 例如：

```python
from itertools import combinations

for each in combinations('abc', 2):
    print each

# 输出结果:
('a', 'b')
('a', 'c')
('b', 'c')
```

###### 11、itertools.combinations_with_replacement(iterable, r)
返回指定长度的"组合"，组合内元素可重复 例如：

```python
from itertools import combinations_with_replacement

for each in combinations_with_replacement('abc', 2):
    print each

# 输出结果:
('a', 'a')
('a', 'b')
('a', 'c')
('b', 'b')
('b', 'c')
('c', 'c')
```

###### 12、itertools.product(*iterable[,repeat])
返回指定长度的所有组合，可理解为笛卡尔乘积 例如：

```python
from itertools import product

for each in product('abc', repeat=2):
    print each

# 输出结果:
('a', 'a')
('a', 'b')
('a', 'c')
('b', 'a')
('b', 'b')
('b', 'c')
('c', 'a')
('c', 'b')
('c', 'c')
```

###### 13、itertools.permutations(iterable[,r])
返回长度为r的排列 例如：

```python
from itertools import permutations

for value in permutations('abc', 2):
    print value

# 输出结果:
('a', 'b')
('a', 'c')
('b', 'a')
('b', 'c')
('c', 'a')
('c', 'b')
```

###### 14、itertools.compress(data,selector)
返回selector为True的data对应元素 例如：

```python
from itertools import compress

for each in compress('abcd', [1, 0, 1, 0]):
    print each

# 输出结果:
a
c
```

###### 15、itertools.groupby(iterable[,key])
返回一组（key,itera）,key为iterable的值，itera为等于key的所有项 例如:

```python
from itertools import groupby

for key, value in groupby('aabbbc'):
    print(key, list(value))

# 输出结果:
a ['a', 'a']
b ['b', 'b', 'b']
c ['c']
```

###### 16、itertools.chain(*iterable)
将多个序列中的元素连续返回。 例如：

```python
from itertools import chain

for value in chain('i', 'love', 'python'):
    print(value)

# 输出结果:
i
l
o
v
e
p
y
t
h
o
n
```



