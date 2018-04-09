### 元组(```Tuple```)

元组与列表类似，不同之处在于元组的元素不能修改。元组创建很简单，只需要在小括号中添加元素，并使用逗号隔开即可。

如下实例：

```python
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"

# 元组中嵌套元组
tup4 = ('Google', 'Runoob', 1997, 2000, ('Google', 'Runoob', 1997, 2000))
```

###### 1、创建空元组

```python
# 空元组
tup1 = ()

# 有一个空值的元组
tup2 = (None,)
```

```元组中只包含一个元素时，需要在元素后面添加逗号：```

```python
tup1 = (50)
print(type(tup1))     # 不加逗号，类型为整型
# output: <class 'int'>

tup1 = (50,)
print(type(tup1))     # 加上逗号，类型为元组
# output: <class 'tuple'>
```

###### 2、元组索引，分片

元组与字符串类似，下标索引左边从0开始，右边从-1开始，可以进行索引、分片。
元组：L = ('Google', 'Taobao', 'Runoob!', 1997)

| Python表达式 | 结果 | 描述 |
| :--- |:--- | :---|
| L[2] | 'Runoob!' | 读取第三个元素 |
| L[-2]| 'Runoob!' | 反向读取；读取倒数第二个元素 |
| L[1:]| ('Taobao', 'Runoob!', 1997) | 截取元素，从第二个开始的所有元素|
| L[1:3]| ('Taobao', 'Runoob!') |  截取元素，从第二个开始到第三个元素|
| L[:]| ('Google', 'Taobao', 'Runoob!', 1997) |  截取整个元组|

###### 3、元组运算符

| python表达式 | 结果 | 描述 |
| :--- | :--- | :--- |
| (1, 2, 3) + (4, 5, 6)    | (1, 2, 3, 4, 5, 6) | 连接 |
| ('Hi!',) * 4 | ('Hi!', 'Hi!', 'Hi!', 'Hi!')      |   复制 |
| 3 in (1, 2, 3) | True      |    元素是否存在 |
| for x in (1, 2, 3): print x | 1 2 3      |    迭代 |

###### 4、删除元组

元组中的元素值是不允许删除的，但可以使用del语句来删除整个元组，如下实例:

```python
tup = ('Google', 'Runoob', 1997, 2000)

# 以下删除元组元素操作是非法的。
# del tup[0]

del tup
print(tup)

# 以上实例元组被删除后，输出变量会有异常信息，输出如下所示：
Traceback (most recent call last):
  File "test.py", line 8, in <module>
    print (tup)
NameError: name 'tup' is not defined
```

###### 5、Python内置函数

Python元组包含了以下内置函数

|方法| 描述|
| :--- |:--- |
| len(tuple)|计算元组元素个数|
| max(tuple)|返回元组中元素最大值|
| min(tuple)|返回元组中元素最小值|
| tuple(seq)|将序列转换为元组|

```python
tuple1 = ('Google', 'Runoob', 'Taobao')
print(len(tuple1))
# output: 3

tuple2 = ('5', '4', '8')
print(max(tuple2))
# output: '8'

tuple2 = ('5', '4', '8')
print(min(tuple2))
# output: '4'

list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
tuple1=tuple(list1)
print(tuple1)
# output: ('Google', 'Taobao', 'Runoob', 'Baidu')
```



