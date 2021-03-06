### 基础语法

1、编码

默认情况下，Python3源码文件以UTF-8编码，所有字符串都是unicode字符串。
当然也可以为源码文件指定不同的编码，以如下注释方式修改编码：
```python
# -*- coding: cp-1252 -*-
```

2、标识符定义
- 标识符由有字母、数字和下划线组成
- 第一个字符必须是字母或下划线'_'
- 标识符对大小写敏感
- 关键字不能被用作任何标识符名称

以下划线开头的标识符是有特殊意义的。
以单下划线开头，如```_foo```， 代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用 from xxx import * 而导入；
以双下划线开头，如```__foo```，代表类的私有成员；
以双下划线开头和结尾的，形如```__foo__```，代表Python里特殊方法专用的标识，如```__init__() ```代表类的构造函数。

Python的标准库提供了一个keyword模块，可以输出当前版本的所有关键字：
```python
>>> import keyword
>>> keyword.kwlist
['False', 'None', 'True', 'and', 'as', 'assert', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
```

3、行与缩进

python最具特色的就是使用缩进来表示代码块，不需要使用大括号({})。
缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数，若缩进数空格数不一致将会报错。
```python
if True:
	print ("True")
else:
	print ("False")
```

4、同一行显示多条语句

在同一行中显示多条语句，语句之间使用分号(;)分割。
```python
import sys; x = 'runoob'; sys.stdout.write(x + '\n')
```

5、多行语句

Python语句中一般以新行作为语句的结束符，但可以使用斜杠（\）将一行的语句分为多行显示，如下所示：
```python
total = item_one + \
        item_two + \
        item_three
```

语句中包含 [], {} 或 () 就不需要使用多行连接符。
```python
days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
```

6、变量和赋值

>参考文章：
- [图解Python变量与赋值](https://foofish.net/python-variable.html)

在python中,“变量”的严格叫法是“名字(name)”，也可以理解为标签，就像我们人的姓名一样，名字就是挂在人身上的一个标签。
变量本身没有类型信息，真正的信息都在对象身上。给变量赋值就是相当于给对象贴标签。

```python
# 定义变量a，并赋值为1。
# Python会先分配内存，用于创建并存放对象1，然后为对象1贴上标签a
# 创建变量a并不用分配内存
a = 1

# 为对象1贴上标签b
# 创建变量b并不用分配内存
b = a
```
