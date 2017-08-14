### 装饰器(```Decorator```)

装饰器本质上是一个Python函数或类，它可以让其他函数或类在不需要做任何代码修改的前提下增加额外功能，
装饰器的返回值也是一个函数或类对象。

###### 1、函数装饰器对函数的修饰
首先来看一个简单的例子：
```python
import time

def log_cost_time(func):
    def wrapper(*args, **kwargs):
        begin = time.clock()
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(str(e))
        finally:
            print('func %s cost %s' % (func.__name__, time.clock() - begin))
    return wrapper

# 函数log_cost_time就是一个装饰器，其作用是打印被装饰函数运行时间。
# 在不改变被装饰对象的同时增加了记录函数执行时间的额外功能。
# complex_func = log_cost_time(complex_func)
@log_cost_time
def wrapped_func(num):
    ret = 0
    for i in range(num):
        ret += i * i
    return ret

if __name__ == '__main__':
    print(wrapped_func(100000))
```

装饰器的语法如下：
```python
@dec
def func():pass
# 等价于 func = dec(func)
```

装饰器是可以嵌套的，如
```python
@dec0
@dec1
def func():pass
# 等价于 func = dec0(dec1(fun))
```

对于被log_cost_time装饰的wrapped_func, 查看一下wrapped_func.__name__，
输出是：“wrapper”。这个是log_cost_time里面inner function（wrapper）的名字，调用者当然希望输出“wrapped_func”，
为了解决这个问题，python提供了两个函数。

1、functools.update_wrapper(wrapper, wrapped[, assigned][, updated])
- 第一个参数，包装函数
- 第二个参数，被包装的函数，即传入的函数
- 第三个参数，默认为（```__doc__, __name__, __module__```)，将被包装函数值直接复制给wrapper
- 第四个参数，默认为(```__dict__```)

2、functools.wraps： update_wrapper的封装

简单修改函数装饰器代码：
```python
from functools import update_wrapper
from functools import wraps

def log_cost_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        import time
        begin = time.time()
        try:
            return func(*args, **kwargs)
        except Exception as e:
                    print(str(e))
        finally:
            print 'func %s cost %s' % (func.__name__, time.time() - begin)
    # return update_wrapper(wrapper, func)
    return wrapper

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
import time
import sys

def log_cost_time(stream):
    def inner_dec(func):
        def wrapper(*args, **kwargs):
            begin = time.clock()
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(str(e))
            finally:
                stream.write('func %s cost %s \n' % (func.__name__, time.clock() - begin))
        return wrapper
    return inner_dec

@log_cost_time(sys.stdout)
def complex_func(num):
    ret = 0
    for i in range(num):
        ret += i * i
    return ret

if __name__ == '__main__':
    print complex_func(100000)
```

###### 2、函数装饰器对类的修饰
```python
def modify(clz):
    clz.__str__ = lambda s: "Haha"
    return clz

@modify
class Widget(object):
    ''' class Widget '''

if __name__ == '__main__':
    w = Widget()
    print(w)
```

###### 3、类装饰器
为了将装饰器定义成一个实例，需要确保它实现了```__call__()```和```__get__()```方法。
例如，下面的代码定义了一个类，它在其他函数上放置一个简单的记录层：
```python
import types
from functools import wraps

class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)
```

可以将它当做一个普通的装饰器来使用，在类里面或外面都可以：
```python
@Profiled
def add(x, y):
    return x + y

class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)
```

decorator在python中用途非常广泛，下面列举几个方面：
- 插入日志、
- 性能测试、
- 事务处理、
- 缓存、
- 权限校验


