### 高效使用字典清单

字典（dict）对象是Python最常用的数据结构，在Python中的重要性不言而喻，这里整理了几个关于高效使用字典的清单，
助你代码更加Pythonic。

1、用in关键字检查key是否存在

```python
if 'name' in dict:
    pass
```

2、用get方法获取字典中的值

关于获取字典中的值，一种简单的方式就是用dict[x]访问该元素，但是这种情况在key不存在时会报KeyError错误，
当然可以先用in操作检查key是否在字典中再获取，不过这种方式不符合Python之禅中说的：

>Simple is better than complex.
Flat is better than nested.

好的代码应该是简单易懂的，扁平的代码结构更加可读。可以使用get方法来代替if … else

```python
bad

d = {'name': 'python'}
if 'name' in d:
    print(d['hello'])
else:
    print('default')

good

print(d.get("name", "default"))
```

3、用setdefault方法为字典中不存在的key设置缺省值

```python
data = [
        ("animal", "bear"),
        ("animal", "duck"),
        ("plant", "cactus"),
        ("vehicle", "speed boat"),
        ("vehicle", "school bus")
    ]
```

在做分类统计时，希望把同一类型的数据归到字典中的某种类型中，比如上面代码，
把相同类型的事物用列表的形式重新组装，得到新的字典:

```python
groups = {}

>>>
{'plant': ['cactus'],
 'animal': ['bear', 'duck'],
 'vehicle': ['speed boat', 'school bus']}
 ```

普通的方式就是先判断key是否已经存在，如果不存在则要先用列表对象进行初始化，
再执行后续操作。而更好的方式就是使用字典中的setdefault方法。

```python
bad

for (key, value) in data:
    if key in groups:
        groups[key].append(value)
    else:
        groups[key] = [value]

good

groups = {}
for (key, value) in data:
    groups.setdefault(key, []).append(value)
```

setdefault的作用是：
- 如果 key 存在于字典中，那么直接返回对应的值，等效于 get 方法
- 如果 key 不存在字典中，则会用 setdefault 中的第二个参数作为该 key 的值，再返回该值。

4、用defaultdict方法初始化字典对象

如果不希望dict[x]在x不存在时报错，除了在获取元素时使用get方法之外，
另外一种方式是用collections模块中的defaultdict，在初始化字典的时候指定一个函数，
其实defaultdit是dict的子类。

```python
from collections import defaultdict

groups = defaultdict(list)
for (key, value) in data:
    groups[key].append(value)
```

当 key不存在于字典中时，list函数将被调用并返回一个空列表赋值给dict[key]，这样就不用担心调用dict[key]会报错了。

5、用fromkeys方法将列表转换成字典

```python
keys = {'a', 'e', 'i', 'o', 'u' }
value = []
d = dict.fromkeys(keys, value)
print(d)

>>>
{'i': [], 'u': [], 'e': [],
 'a': [], 'o': []}
```

6、用字典实现switch … case语句

Python中没有switch … case语句，这个问题Python之父龟叔表示这个语法过去没有，
现在没有，以后也不会有。因为Python简洁的语法完全可以用if … elif实现。如果有太多的分支判断，
还可以使用字典来代替。

```python
bad

if arg == 0:
    return 'zero'
elif arg == 1:
    return 'one'
elif arg == 2:
    return "two"
else:
    return "nothing"

good

data = {
    0: "zero",
    1: "one",
    2: "two",
}

data.get(arg, "nothing")
```

7、使用 iteritems 迭代字典中的元素

python提供了几种方式迭代字典中的元素，第一种是使用 items 方法：

```python
d = {
    0: "zero",
    1: "one",
    2: "two",
}

for k, v in d.items():
    print(k, v)
```

items 方法返回的时（key ,value）组成的列表对象，这种方式的弊端是迭代超大字典的时候，内存瞬间会扩大两倍，
因为列表对象会一次性把所有元素加载到内存，更好的方式是使用iteritems。

```python
for k, v in d.iteritems():
    print(k, v)
```

iteritems返回的是迭代器对象，迭代器对象具有惰性加载的特性，只有真正需要的时候才生成值，
这种方式在迭代过程中不需要额外的内存来装载这些数据。
注意Python3中，只有items方法了，它等价于 Python2 中的 iteritems，而 iteritems 这个方法名被移除了。

8、使用字典推导式

```python
bad

numbers = [1,2,3]
d = dict([(number,number*2) for number in numbers])

good

numbers = [1, 2, 3]
d = {number: number * 2 for number in numbers}
```

