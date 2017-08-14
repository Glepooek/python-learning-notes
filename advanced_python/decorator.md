### 装饰器(```Decorator```)

一般来说，装饰器是一个函数，接受一个函数（或者类）作为参数，返回值也是也是一个函数（或者类）。

###### 1、装饰器对函数的修饰，在不改变被装饰对象的同时增加额外功能
首先来看一个简单的例子：
```python
def log_cost_time(func):
    def wrapped(*args, **kwargs):
        import time
        begin = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            print 'func %s cost %s' % (func.__name__, time.time() - begin)
    return wrapped

# 函数log_cost_time就是一个装饰器，其作用是打印被装饰函数运行时间。
# 在不改变被装饰对象的同时增加了记录函数执行时间的额外功能。
@log_cost_time
def complex_func(num):
    ret = 0
    for i in xrange(num):
        ret += i * i
    return ret
#complex_func = log_cost_time(complex_func)

if __name__ == '__main__':
    print complex_func(100000)
```

装饰器的语法如下：
```python
@dec
def func():pass

# 等价于 func = dec(func)。
```

装饰器是可以嵌套的，如
```python
@dec0
@dec1
def func():pass

# 等价于 func = dec0(dec1(fun))。
```

装饰器也有“副作用”，对于被log_cost_time装饰的complex_calc, 查看一下complex_func.__name__，
输出是：“wrapped”。这个是log_cost_time里面inner function（wrapped）的名字，调用者当然希望输出“complex_func”，
为了解决这个问题，python提供了两个函数。

1、functools.update_wrapper(wrapper, wrapped[, assigned][, updated])
第三个参数，将wrapped的值直接复制给wrapper，默认为（__doc__, __name__, __module__)
第四个参数，updated，默认为(__dict__)

2、functools.wraps： update_wrapper的封装

简单改改代码：
```python
from functools import wraps
def log_cost_time(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        import time
        begin = time.time()
        try:
            return func(*args, **kwargs)
        finally:
            print 'func %s cost %s' % (func.__name__, time.time() - begin)
    return wrapped

# 查看complex_func.__name__ 输出就是 “complex_func”
```

装饰器也是可以带参数的，基本语法为：
```python
@dec(dec_args)
def func(*args, **kwargs):pass

# 等价于 func = dec(dec_args)(*args, **kwargs)
```

将上面的代码略微修改一下：
```python
def log_cost_time(stream):
    def inner_dec(func):
        def wrapped(*args, **kwargs):
            import time
            begin = time.time()
            try:
                return func(*args, **kwargs)
            finally:
                stream.write('func %s cost %s \n' % (func.__name__, time.time() - begin))
        return wrapped
    return inner_dec

import sys
@log_cost_time(sys.stdout)
def complex_func(num):
    ret = 0
    for i in xrange(num):
        ret += i * i
    return ret

if __name__ == '__main__':
    print complex_func(100000)
```

###### 2、装饰器对类的修饰（```decorator修改了被装饰的对象```）
举个例子，修改类的__str__方法，代码很简单。
```python
def Haha(clz):
    clz.__str__ = lambda s: "Haha"
    return clz

<a href="http://www.jobbole.com/members/cxh1527">@Haha</a>
class Widget(object):
    ''' class Widget '''

if __name__ == '__main__':
    w = Widget()
    print w
```

decorator在python中用途非常广泛，下面列举几个方面：
- 修改被装饰对象的属性或者行为
- 处理被函数对象执行的上下文，比如设置环境变量，加log之类
- 处理重复的逻辑，比如有N个函数都可能抛出异常，可以写一个catchall的decorator，作用于所用可能抛出异常的函数
- 框架代码，如flask， bottle等等，让使用者很方便就能使用框架，本质上也避免了重复代码。


另外staticmethod和classmethod是两个经常在代码中用到的装饰器，
如果对pyc反编译，得到的代码一般也都是 func = staticmthod(func)这种模式。
当然，@符号的形式更受欢迎些，至少可以少拼写一次函数名。


