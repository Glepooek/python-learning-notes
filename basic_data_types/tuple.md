### 元组(```Tuple```)

元组创建很简单，只需要在小括号中添加元素，并使用逗号隔开即可。Python元组与列表类似，不同之处在于元组的元素不能修改。

如下实例：
```python
tup1 = ('Google', 'Runoob', 1997, 2000);
tup2 = (1, 2, 3, 4, 5 );
tup3 = "a", "b", "c", "d";
```

###### 1、创建空元组
```python
tup1 = ()
```
元组中只包含一个元素时，需要在元素后面添加逗号，否则括号会被当作运算符使用：
```python
>>> tup1 = (50)
>>> type(tup1)     # 不加逗号，类型为整型
<class 'int'>

>>> tup1 = (50,)
>>> type(tup1)     # 加上逗号，类型为元组
<class 'tuple'>
```

###### 2、访问元组
元组与字符串类似，下标索引从0开始，可以进行截取，组合等。
元组可以使用下标索引来访问元组中的值，如下实例:
```python
tup1 = ('Google', 'Runoob', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )

print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])
以上实例输出结果：
tup1[0]:  Google
tup2[1:5]:  (2, 3, 4, 5)
```

###### 3、修改元组
元组中的元素值是不允许修改的，但我们可以对元组进行连接组合，如下实例:
```python
tup1 = (12, 34.56);
tup2 = ('abc', 'xyz')

# 以下修改元组元素操作是非法的。
# tup1[0] = 100

# 创建一个新的元组
tup3 = tup1 + tup2;
print (tup3)
以上实例输出结果：
(12, 34.56, 'abc', 'xyz')
```


###### 4、删除元组
元组中的元素值是不允许删除的，但可以使用del语句来删除整个元组，如下实例:
```python
tup = ('Google', 'Runoob', 1997, 2000)

print (tup)
del tup;
print ("删除后的元组 tup : ")
print (tup)

# 以上实例元组被删除后，输出变量会有异常信息，输出如下所示：
删除后的元组 tup :
Traceback (most recent call last):
  File "test.py", line 8, in <module>
    print (tup)
NameError: name 'tup' is not defined
```

###### 5、元组运算符
与字符串一样，元组之间可以使用 + 号和 * 号进行运算。这就意味着他们可以组合和复制，运算后会生成一个新的元组。
| Python表达式        | 结果           | 描述  |
| ------------- |:-------------:| -----:|
| len((1, 2, 3)) |:3:| 计算元素个数:|
| (1, 2, 3) + (4, 5, 6)      | (1, 2, 3, 4, 5, 6) | 连接 |
| ('Hi!',) * 4      | ('Hi!', 'Hi!', 'Hi!', 'Hi!')      |   复制 |
| 3 in (1, 2, 3) | True      |    元素是否存在 |
| for x in (1, 2, 3): print x | 1 2 3      |    迭代 |


###### 6、元组索引，截取
因为元组也是一个序列，所以我们可以访问元组中的指定位置的元素，也可以截取索引中的一段元素，如下所示：
元组：
L = ('Google', 'Taobao', 'Runoob')
| Python表达式        | 结果           | 描述  |
| ------------- |:-------------:| -----:|
| L[2]      | 'Runoob!' | 读取第三个元素 |
| L[-2]      | 'Taobao'      |   反向读取；读取倒数第二个元素 |
| L[1:] | ('Taobao', 'Runoob!')      |    截取元素，从第二个开始后的所有元素|

```python
运行实例如下：
>>> L = ('Google', 'Taobao', 'Runoob')
>>> L[2]
'Runoob'
>>> L[-2]
'Taobao'
>>> L[1:]
('Taobao', 'Runoob')
```

###### 7、元组内置函数
Python元组包含了以下内置函数
序号        | 方法及描述
 - |-|
1 |:len(tuple)，计算元组元素个数
2      | max(tuple)，返回元组中元素最大值
3      | min(tuple)，返回元组中元素最小值
4 | tuple(seq)，将列表转换为元组

```python
>>> tuple1 = ('Google', 'Runoob', 'Taobao')
>>> len(tuple1)
3

>>> tuple2 = ('5', '4', '8')
>>> max(tuple2)
'8'

>>> tuple2 = ('5', '4', '8')
>>> min(tuple2)
'4'

>>> list1= ['Google', 'Taobao', 'Runoob', 'Baidu']
>>> tuple1=tuple(list1)
>>> tuple1
('Google', 'Taobao', 'Runoob', 'Baidu')
```
