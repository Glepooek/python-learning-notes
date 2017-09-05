registry = {}


class MultiMethod(object):
    def __init__(self, name):
        self.name = name
        self.typemap = {}

    def __call__(self, *args, **kwargs):
        types = tuple(arg.__class__ for arg in args)
        func = self.typemap.get(types)
        if func is None:
            raise TypeError('no match')

        return func(*args)

    def register(self, types, func):
        if types in self.typemap:
            raise TypeError("duplicate registration")
        self.typemap[types] = func


# def multimethod(*types):
#     def register(func):
#         name = func.__name__
#         mm = registry.get(name)
#         if mm is None:
#             mm = registry[name] = MultiMethod(name)
#         mm.register(types, func)
#         return mm
#
#     return register

def multimethod(*types):
    def register(func):
        # getattr(x, 'y', z)方法是从x对象中获取属性y的值，
        # 若x对象中不存在属性y，则返回默认值z，若未设置默认值，则抛出异常
        func = getattr(func, "__lastreg__", func)
        name = func.__name__
        mm = registry.get(name)
        if mm is None:
            mm = registry[name] = MultiMethod(name)
        mm.register(types, func)
        mm.__lastreg__ = func
        return mm

    return register


@multimethod(int, int)
@multimethod(int)
def foo(a, b=10):
    return a + b


@multimethod(str, str)
def foo(a, b):
    return a + b


if __name__ == '__main__':
    print(foo(12))
    print(foo('I', ' love you'))
