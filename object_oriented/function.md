### 函数(```function```)
函数（可能包含参数）能够执行某种行为并返回一个值。

###### 1、创建函数
使用def语句创建函数。

```python
# 函数均有返回值。在不需要函数返回值时，函数返回的是None
def fibs(num):
    pass
```

使用如下方法判断函数是否可调用：

1）使用内置的callable函数

callable(func)
用于检查对象是否可调用，返回True也可能调用失败，但是返回False一定不可调用

2）判断对象类型是否是FunctionType

type(func) is FunctionType
# 或者
isinstance(func, FunctionType)


3）判断对象是否实现__call__方法

hasattr(func, '__call__')

###### 2、记录函数
为函数添加注释。用fun_name.__doc__获取函数的文档内容。也可通过help函数获取更加详细的信息。

```python
help(fibs)
```

###### 3、函数的参数
def语句中函数名后面的变量通常叫函数的形式参数，而调用函数时传入的值是实际参数。


