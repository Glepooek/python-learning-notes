### doctest

doctest是python自带的一个模块。doctest有两种使用方式：一种是嵌入到python源码中，另外一种是放到一个独立文件，如txt文件中。
在python的官方文档中，对doctest是这样介绍的：doctest模块会搜索那些看起来像是python交互式会话中的代码片段，然后尝试执行并验证结果。
doctest的编写过程就像你在一个交互式shell中导入了一个被测试模块，然后一条一条执行被测试模块里面的函数一样。
其实实际上doctest也是这么编写的，写好一个模块之后，在shell中测试这个模块里面的函数，将shell会话中的内容复制粘贴成doctest用例。

###### 1、doctest嵌入源码中
下面的模块只有一个函数，里面嵌入了两个doctest测试用例。

```python
'''
这个例子展示如何在源码中嵌入doctest用例。
'>>>' 开头的行就是doctest测试用例。
不带 '>>>' 的行就是测试用例的输出。
如果实际运行的结果与期望的结果不一致，就标记为测试失败。
'''

def multiply(a, b):
    """
    >>> multiply(4, 3)
    12
    >>> multiply('a', 3)
    'aaa'
    """
    return a * b

if __name__=='__main__':
	import doctest
	doctest.testmod(verbose=True)
```

有两个地方可以放doctest测试用例，一个位置是模块的最开头，另一个位置是函数声明语句的下一行（就像上面的例子这样）。除此之外的其它地方不能放，放了也不会执行。
那个verbose参数，如果设置为True则在执行测试的时候会输出详细信息。默认是False，表示运行测试时，只有失败的用例会输出详细信息，成功的测试用例不会输入任何信息。

执行结果：
```python
liuchunmings-MacBook-Pro:exersice liuchunming$ python unnecessary_math.py
Trying:
    multiply(4, 3)
Expecting:
    12
ok
Trying:
    multiply('a', 3)
Expecting:
    'aaa'
ok
1 items had no tests:
    __main__
1 items passed all tests:
   2 tests in __main__.multiply
2 tests in 2 items.
2 passed and 0 failed.
Test passed.
```

上面启动测试的方式是在__main函数中调用了doctest.testmod()方法。如果__main__函数有其他用途，不方便调用doctest.testmod()方法，那么可以用另外一种执行测试的方法：

```python
$ python -m doctest unnecessary_math.py
$ python -m doctest -v unnecessary_math.py
```

这里 -m 表示引用一个模块，-v 等价于 verbose=True。运行输出与上面基本一样。

###### 2、doctest独立文件
如果不想将doctest测试用例嵌入到python的源码中，则可以建立一个独立的文本文件来保存测试用例。
将doctest测试用例从上面的python源码中剥离出来放到test_unnecessary_math.txt文件里。

```python
这个例子展示如何将doctest用例放到一个独立的文件中。
'>>>' 开头的行就是doctest测试用例。
不带 '>>>' 的行就是测试用例的输出。
如果实际运行的结果与期望的结果不一致，就标记为测试失败。

>>> from unnecessary_math import multiply
>>> multiply(3, 4)
12
>>> multiply('a', 3)
'aaa'
```

注意：from 那一行也要以>>>开头。
在系统的shell中执行：

```python
python -m doctest -v test_unnecessary_math.txt
```