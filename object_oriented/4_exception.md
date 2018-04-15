### 异常

###### 1、什么是异常
Python用异常对象来表示异常情况。
程序遇到错误后会引发异常，如果异常对象并未被处理或捕获，程序就会用回溯（traceback）终止执行。

###### 2、自动引发异常
1）raise语句
使用raise语句引发异常。

2）自定义异常类
如果要使用特殊的错误处理方式，可以自定义异常类。

```python
class CustomException(Exception):
    pass
```

###### 3、捕获异常
使用try...except来捕获异常。
1）多个except子句，每个子句用于捕获不同类型的异常
2）用一个except子句捕获多个异常，将多个异常类型作为元组列出

```python
def test_exception():
    try:
        x = input('Enter the first number:')
        y = input('Enter the second number:')

        print(x / y)
    except (ZeroDivisionError, TypeError, NameError):
        # 处理这些异常
        raise
```

3）捕获异常对象，以便打印或记录异常日志

```python
def test_exception():
    try:
        x = input('Enter the first number:')
        y = input('Enter the second number:')

        print(x / y)
    except (ZeroDivisionError, TypeError, NameError) as e:
        # 处理这些异常，打印或记录日志
        print(e)
```

4）捕获所有异常

```python
def test_exception():
    try:
        x = input('Enter the first number:')
        y = input('Enter the second number:')

        print(x / y)
    except Exception as e:
        # 处理这些异常，打印或记录日志
        print(e)
```

###### 4、else子句
try...except...else，else子句只有在没有异常捕获时才会进入。

###### 5、finally子句
try...finally，try...except...finally，try...except...else...finally。
finally子句不管try是否有异常，不管except有没有将异常捕获，最终都会被执行。

