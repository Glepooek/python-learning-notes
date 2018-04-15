"""
以下是对象实例化的代码
"""

# import copy
# import sys
#
#
# class Point(object):
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     @classmethod
#     def new_object(cls, x, y):
#         return cls(x, y)
#
#
# def make_object(clz, *args, **kwargs):
#     return clz(*args, **kwargs)
#
#
# if __name__ == '__main__':
#     point1 = Point(1, 2)
#     point2 = Point.new_object(3, 4)
#     point3 = make_object(Point, 5, 6)
#     # 通过object.__class__获取到对象的类。获取到类以后，再执行类调用，就又创建了一个新的对象。
#     point4 = point1.__class__(7, 8)
#     # 通过sys.modules[__name__]获取当前模块的所有属性。
#     # 在point8的创建中，直接使用globals函数获取当前模块中的属性。
#     # 获取模块的所有属性以后，可以直接通过类的名称获取到Point这个类对象。
#     # 获取到类对象以后，执行类调用，就创建了一个对象。
#     point8 = getattr(sys.modules[__name__], "Point")(15, 16)
#     point5 = globals()['Point'](9, 10)
#     point6 = copy.deepcopy(point1)
#     point6.x = 11
#     point6.y = 12
#     # eval() 函数用来执行一个字符串表达式，并返回表达式的值。
#     # 存在安全隐患，不建议使用
#     point7 = eval('{}({}, {})'.format('Point', 13, 14))
#
#     print(point7.x)

"""
以下是自定义实现多态的代码
"""


#
# registry = {}
#
#
# class MultiMethod(object):
#     def __init__(self, name):
#         self.name = name
#         self.typemap = {}
#
#     def __call__(self, *args, **kwargs):
#         types = tuple(arg.__class__ for arg in args)
#         func = self.typemap.get(types)
#         if func is None:
#             raise TypeError('no match')
#
#         return func(*args)
#
#     def register(self, types, func):
#         if types in self.typemap:
#             raise TypeError("duplicate registration")
#         self.typemap[types] = func
#
#
# # def multimethod(*types):
# #     def register(func):
# #         name = func.__name__
# #         mm = registry.get(name)
# #         if mm is None:
# #             mm = registry[name] = MultiMethod(name)
# #         mm.register(types, func)
# #         return mm
# #
# #     return register
#
# def multimethod(*types):
#     def register(func):
#         # getattr(x, 'y', z)方法是从x对象中获取属性y的值，
#         # 若x对象中不存在属性y，则返回默认值z，若未设置默认值，则抛出异常
#         func = getattr(func, "__lastreg__", func)
#         name = func.__name__
#         mm = registry.get(name)
#         if mm is None:
#             mm = registry[name] = MultiMethod(name)
#         mm.register(types, func)
#         mm.__lastreg__ = func
#         return mm
#
#     return register
#
#
# @multimethod(int, int)
# @multimethod(int)
# def foo(a, b=10):
#     return a + b
#
#
# @multimethod(str, str)
# def foo(a, b):
#     return a + b
#
#
# if __name__ == '__main__':
#     print(foo(12))
#     print(foo('I', ' love you'))

class Filter:

    def __init__(self):
        self.blocked = []

    def filter(self, seq: list) -> list:
        return [x for x in seq if x not in self.blocked]


class SPAMFilter(Filter):
    def __init__(self):
        self.blocked = ['SPAM']


if __name__ == '__main__':
    s = SPAMFilter()
    if hasattr(s, 'filter') & callable(getattr(s, 'filter')):
        print(s.filter(['SPAM', 1, 2, 4]))
