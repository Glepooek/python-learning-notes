### 面向对象基础

Pyhton被称为面向对象语言，创建对象是Pyhton的核心概念。

###### 1、面向对象的三大特性：多态、封装、继承
1）多态
多态意味着就算不知道变量所引用的对象类型是什么，还是能对它进行操作，而它也会根据对象（或类）类型的不同而表现出不同行为。
多态的使用不仅限于方法，很多内建运算符（如+，**）和函数（如len()）都有多态的性质。
唯一能毁掉多态的就是使用函数显示的检查类型，如type、isinstance、issubclass函数等。

```python
# 自定义实现多态

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
```

2）封装
封装是对全局作用域中其他区域隐藏多余信息的原则。

3）继承

###### 2、类和类型
类（对象的抽象），对象（类的实例），子类（方法重载、覆盖），父类（超类）

1）创建类
```python
# self是对于对象自身的引用
class Person:
    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def greet(self):
        print("hello, I'm %s" % self.name)
```

2）特性、函数和方法
self参数是方法和函数的区别。
方法将它的第一个参数绑定到所属的实例上。
也可以将特性（方法名）绑定到没有self参数的普通函数上。
在定义方法或特性时，在其名字前加```双下划线```即可将其定义为私有的。

3）类命名空间
4）指定超类
将超类的类型写在class语句后的圆括号内。

```python
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
    print(s.filter(['SPAM', 1, 2, 4]))
```

5）调查继承
用issubclass内置函数判断一个类是否是另一个类的子类。
用isinstance内置函数检查一个对象是否是一个类的实例。
获取已知类的基类可以直接使用该类的特性__bases__。
获取对象所属的类可以直接使用该类的特性__class__。

6）多个超类
Python支持多重继承。
当使用多重继承时，若多个超类中存在相同名字的不同方法，要注意超类的顺序：先继承的超类中的方法会重写后继承的超类中的方法。
如果超类共享一个超类，那么查找给定方法或特性时访问超类的顺序称为MRO。

7）接口和内省



