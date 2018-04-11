### 条件控制语句(condition control)

Python条件控制语句是通过一条或多条语句的执行结果（True或者False）来决定执行的代码块。

###### 1、布尔值
False、None、0(各种数据类型的0)、""、[]、()、{}均被解释器看做False。
标准真值0（表示假）和1（表示真）。bool()函数用于将其他类型的值转换为布尔值。

```python
print(True == 1)
print(False == 0)
print(True + False)

#output
True
True
1
```

###### 2、if语句
if语句的一般形式如下：

```python
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
```

###### 3、if语句嵌套
在嵌套if语句中，可以把if...elif...else结构放在另外一个if...elif...else结构中。

```python
if 表达式1:
    if 表达式2:
        语句
    elif 表达式3:
        语句
    else:
        语句
elif 表达式4:
    语句
else:
    语句
```

###### 4、更加复杂的条件
相关内容可参看操作符章节。

1）比较运算符
2）同一性运算符is，判断对象引用是否相同
3）成员资格运算符in
4）序列比较，按序列元素顺序比较
5）布尔运算符

###### 5、断言
要求某个条件必须为真。
关键字assert
