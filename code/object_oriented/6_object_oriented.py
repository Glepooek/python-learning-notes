import copy
import sys


class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def new_object(cls, x, y):
        return cls(x, y)


def make_object(clz, *args, **kwargs):
    return clz(*args, **kwargs)


if __name__ == '__main__':
    point1 = Point(1, 2)
    point2 = Point.new_object(3, 4)
    point3 = make_object(Point, 5, 6)
    # 通过object.__class__获取到对象的类。获取到类以后，再执行类调用，就又创建了一个新的对象。
    point4 = point1.__class__(7, 8)
    # 通过sys.modules[__name__]获取当前模块的所有属性。
    # 在point8的创建中，直接使用globals函数获取当前模块中的属性。
    # 获取模块的所有属性以后，可以直接通过类的名称获取到Point这个类对象。
    # 获取到类对象以后，执行类调用，就创建了一个对象。
    point8 = getattr(sys.modules[__name__], "Point")(15, 16)
    point5 = globals()['Point'](9, 10)
    point6 = copy.deepcopy(point1)
    point6.x = 11
    point6.y = 12
    # eval() 函数用来执行一个字符串表达式，并返回表达式的值。
    # 存在安全隐患，不建议使用
    point7 = eval('{}({}, {})'.format('Point', 13, 14))

    print(point7.x)
