### 上下文管理器(```Context Managers```)

上下⽂管理器允许在有需要的时候，精确地分配和释放资源。
使⽤上下⽂管理器最⼴泛的案例就是with语句。
想象下你有两个需要结对执⾏的相关操作，然后还要在它们中间放置⼀段代码。
上下⽂管理器就是专门让你做这种事情的。 举个例⼦：

```python
with open('some_file', 'w') as opened_file:
    opened_file.write('Hello!')
```
上⾯这段代码打开了⼀个⽂件，往⾥⾯写⼊了⼀些数据，然后关闭该⽂件。如果在往⽂件
写数据时发⽣异常，它也会尝试去关闭⽂件。上⾯那段代码与这⼀段是等价的：

```python
file = open('some_file', 'w')
try:
    file.write('Hello!')
finally:
    file.close()
```

与第⼀个例⼦对⽐时，可以看到，通过使⽤with语句，许多样板代码(boilerplate code)
被消掉了。这就是with语句的主要优势，它确保⽂件会被关闭，⽽不⽤关注嵌套代码如何退出。
上下⽂管理器的⼀个常见⽤例，是资源的加锁和解锁，以及关闭已打开的⽂件（就像我已经展⽰给你看的）。
让我们看看如何来实现我们⾃⼰的上下⽂管理器。这会让我们更完全地理解在这些场景背后都发⽣着什么。

###### 基于类的实现
⼀个上下⽂管理器的类，最起码要定义__enter__和__exit__⽅法。
现在来构造自己的开启⽂件的上下⽂管理器，并学习下基础知识。

```python
class File(object):
    def __init__(self, file_name, mode):
        self.file_obj = open(file_name, mode)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()
```

通过定义__enter__和__exit__⽅法，可以在with语句⾥使⽤它：

```python
with File('demo.txt', 'w') as opened_file:
    opened_file.write('hello!')
```

__exit__函数接受三个参数。 这些参数对于每个上下⽂管理器类中的__exit__⽅法都是必须的。
来看看在底层都发⽣了什么。
- 1. with语句先暂存了File类的__exit__⽅法
- 2. 然后它调⽤File类的__enter__⽅法
- 3. __enter__⽅法打开⽂件并返回给with语句
- 4. 打开的⽂件句柄被传递给opened_file参数
- 5. 在with语句内opened_file参数使⽤.write()来写⽂件
- 6. with语句调⽤之前暂存的__exit__⽅法
- 7. __exit__⽅法关闭了⽂件


###### 处理异常
直到现在还没有谈到__exit__⽅法的这三个参数：type, value和traceback。
在第4步和第6步之间，如果发⽣异常，Python会将异常的type,value和traceback传递给__exit__⽅法。
它让__exit__⽅法来决定如何关闭⽂件以及是否需要其他步骤。在案例中，我们并没有注意它们。
那如果我们的⽂件对象抛出⼀个异常呢？ 举个例⼦，尝试访问⽂件对象的⼀个不⽀持的⽅法：

```python
with File('demo.txt', 'w') as opened_file:
    opened_file.undefined_function('Hello!')
```

我们来列⼀下， 当异常发⽣时， with语句会采取哪些步骤。
- 1. 它把异常的type,value和traceback传递给__exit__⽅法
- 2. 它让__exit__⽅法来处理异常
- 3. 如果__exit__返回的是True， 那么这个异常就被优雅地处理了。
- 4. 如果__exit__返回的是True以外的任何东西，那么这个异常将被with语句抛出。
在案例中，__exit__⽅法返回的是None(如果没有return语句那么⽅法会返回None)。因此，with语句抛出了那个异常。

```python
Traceback (most recent call last):
  File "E:/PycharmProjects/python-gitbook/code/advanced_python/3_context_managers.py", line 15, in <module>
    opened_file.undefined_function('hello')
AttributeError: '_io.TextIOWrapper' object has no attribute 'undefined_function'
```

我们尝试下在__exit__⽅法中处理异常：

```python
class File(object):
    def __init__(self, file_name, method):
        self.file_obj = open(file_name, method)

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
         # 记录日志
         print(type, value, traceback)
         self.file_obj.close()
         return True

with File('demo.txt', 'w') as opened_file:
    opened_file.undefined_function()

# Output:
<class 'AttributeError'> '_io.TextIOWrapper' object has no attribute 'undefined_function' <traceback object at 0x02AFFD28>
```

我们的__exit__⽅法返回了True,因此没有异常会被with语句抛出。
这还不是实现上下⽂管理器的唯⼀⽅式。 还有⼀种⽅式， 我们会在下⼀节中⼀起看看。


###### 基于⽣成器的实现
还可以⽤装饰器(decorators)和⽣成器(generators)来实现上下⽂管理器。
Python有个contextlib模块专门⽤于这个⽬的。我们可以使⽤⼀个⽣成器函数来实现⼀个上下⽂管理器，⽽不是使⽤⼀个类。
让我们看⼀个例⼦：

```python
from contextlib import contextmanager

@contextmanager
def open_file(name):
    f = open(name, 'w')
    yield f
    f.close()
```

这个实现⽅式看起来更加直观和简单。 然⽽， 这个⽅法需要关于⽣成器、 yield
和装饰器的⼀些知识。 在这个例⼦中我们还没有捕捉可能产⽣的任何异常。 它的⼯作⽅式
和之前的⽅法⼤致相同。
让我们小小地剖析下这个⽅法。
- 1. Python解释器遇到了yield关键字。因为这个缘故它创建了⼀个⽣成器而不是⼀个普通的函数。
- 2. 因为这个装饰器，contextmanager会被调⽤并传⼊函数名（open_file）作为参数。
- 3. contextmanager函数返回⼀个以GeneratorContextManager对象封装过的⽣成器。
- 4. 这个GeneratorContextManager被赋值给open_file函数，我们实际上是在调⽤GeneratorContextManager对象。
那现在我们既然知道了所有这些，我们可以⽤这个新⽣成的上下⽂管理器了， 像这样：

```python
with open_file('some_file') as f:
    f.write('hello!'）
```

对上面的例子进行异常处理，修改上例为：

```python
@contextmanager
def open_file(file_name, mode):
    file = None

    try:
        file = open(file_name, mode, encoding='utf-8')
        yield file
    except Exception as e:
        print(repr(e))
    finally:
        if file:
            file.close()
```

