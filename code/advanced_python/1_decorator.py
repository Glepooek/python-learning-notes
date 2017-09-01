# 函数装饰器
from functools import wraps
from functools import update_wrapper
import time


def log_cost_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        begin = time.clock()
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(str(e))
        finally:
            print('func %s cost %s' % (func.__name__, time.clock() - begin))

    # return update_wrapper(wrapper, func)
    return wrapper


@log_cost_time
def wrapped_func(num):
    ret = 0
    for i in range(num):
        ret += i * i
    return ret


# 类装饰器
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


@Profiled
def add(x, y):
    return x + y


class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)


def modify(clz):
    clz.__str__ = lambda s: "Haha"
    return clz


@modify
class Widget(object):
    ''' class Widget '''


if __name__ == '__main__':
    print(wrapped_func(100))
    print(wrapped_func.__name__)

    print(add(1, 2))
    print(add.ncalls)

    s = Spam()
    print(s.bar(3))
    print(s.bar.ncalls)

    w = Widget()
    print(w)
