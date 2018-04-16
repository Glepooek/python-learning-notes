### 魔法方法、属性、迭代器

魔法方法：名称前后都加上两个下划线的方法。这种方法由Python调用，几乎没有直接调用它们的必要。
属性：由property函数构造。
迭代器：使用__iter__来允许迭代器在for循环中使用。

###### 1、构造方法
在Python中，魔法方法__init__是构造方法，在对象被创建后，会立即调用该方法。

```python
class FooBar:
    def __init__(self):
        self.default_value = 4
```

构造函数传参：

```python
class FooBar:
    def __init__(self, value):
        self.default_value = value


if __name__ == "__main__":
    foo = FooBar(5)
    print(foo.default_value)
```

在Python中，魔法方法__del__是析构方法，在对象就要被垃圾回收之前调用。

1）重写一般方法和特殊的构造方法
每个类都可能有一个或多个超类，并从超类里继承行为方式。
当方法被子类的实例调用时，若在子类中没有找到，就会去超类里找。
重写一般方法：在子类中定义一个与超类中同名的方法。
重写构造方法：在子类中定义__init__方法，并调用超类的构造方法，否则对象可能不会被正确的初始化。
调用超类构造方法的两种方式：调用超类未绑定的构造方法，或使用super函数。

2）调用超类未绑定的构造方法
一般在非新式类中使用该方法。
绑定方法：在调用一个实例的方法时，该方法的self参数会被自动绑定到实例上。
未绑定方法：用类直接调用方法，没有实例被绑定，这样便可以自由的提供需要的self参数。

```python
class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("aaaah...")
            self.hungry = False
        else:
            print("No, thanks...")


class SongBird(Bird):
    def __init__(self):
        Bird.__init__(self)
        self.sound = 'squawk'

    def sing(self):
        print(self.sound)


if __name__ == "__main__":
    foo = SongBird()
    foo.eat()
    foo.eat()
```

3）使用super函数

```python
class Bird:
    def __init__(self):
        self.hungry = True

    def eat(self):
        if self.hungry:
            print("aaaah...")
            self.hungry = False
        else:
            print("No, thanks...")


class SongBird(Bird):
    def __init__(self):
        # Bird.__init__(self)
        super(SongBird, self).__init__()
        self.sound = 'squawk'

    def sing(self):
        print(self.sound)


if __name__ == "__main__":
    foo = SongBird()
    foo.eat()
    foo.eat()
```

###### 2、自定义序列或映射
自定义序列或映射有两种方式：

1）重新实现魔法方法
序列和映射是对象的集合，为了实现基本的行为，
如果对象是不可变的，需要使用两个魔法方法（__len__\__getitem__），如果是可变的则需要使用四个（__len__\__getitem__\__setitem__\__delitem__）。

2）子类化列表、字典、字符串
用自定义类继承list，或dict，或string，然后重写部分方法。

###### 3、属性
通过访问器定义的特性被称为属性。

1）property函数
详细内容请参照内置函数：property函数。

2）静态方法和类成员方法
静态方法在定义时不需要self参数，且能够被类本身直接调用。
类方法在定义时需要cls参数，且能够被类对象调用，cls参数是自动绑定到类的。
详细内容请参照```@classmethod```与```@staticmethod```的区别。

3）__getattribute__、__setattr__、__delattr__

###### 4、迭代器和生成器
详细内容参照高级Python：迭代器和生成器(```Iterator and Generator```)


