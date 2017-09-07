### 条件控制语句(condition control)

Python条件控制语句是通过一条或多条语句的执行结果（True或者False）来决定执行的代码块。

###### 1、if语句
if语句的一般形式如下：

```python
if condition_1:
    statement_block_1
elif condition_2:
    statement_block_2
else:
    statement_block_3
```

###### 2、if语句嵌套
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
