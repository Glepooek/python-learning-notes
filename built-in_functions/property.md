### property

property() 函数的作用是在新式类中返回属性值。

##### 语法
property([fget[, fset[, fdel[, doc]]]])

##### 参数
fget -- 获取属性值的函数
fset -- 设置属性值的函数
fdel -- 删除属性值函数
doc -- 属性描述信息

##### 返回值
返回新式类属性。


```python
class BuiltinFunctionDemo:
    """
    内置函数Demo
    """

    def __init__(self):
        self._name = None

    """
    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = value

    def del_name(self):
        del self._name

    name = property(get_name, set_name, del_name, "姓名")
    """

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

test = BuiltinFunctionDemo()
test.name = 'anyu'
print(test.name)
```
