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

```python
# 用于检查对象是否可调用，返回True也可能调用失败，但是返回False一定不可调用
callable(func)
```

2）判断对象类型是否是FunctionType

```python
type(func) is FunctionType
# 或者
isinstance(func, FunctionType)
```

3）判断对象是否实现__call__方法

```python
hasattr(func, '__call__')
```

###### 2、记录函数
为函数添加注释。用fun_name.__doc__获取函数的文档内容。也可通过help函数获取更加详细的信息。

```python
help(fibs)
```

###### 3、函数的参数
def语句中函数名后面的变量通常叫函数的形式参数，而调用函数时传入的值是实际参数。
无论参数是不可变类型（数字、字符串、元组），还是可变类型（列表），在函数内部为参数```赋予新值```不会改变外部任何变量的值。
不可变类型参数在函数内部是不允许修改的，但是可变类型参数可以被修改。当可变类型参数在函数内部被修改后，外部变量的值也被修改了
（解决方案是传入一个深度拷贝的参数）。

```python
names = ['Mr. Entity', 'Mrs. Thing']


def change_name(name):
    name[0] = 'Mr. Gumby'
    print(name)


if __name__ == "__main__":
    print(names)
    change_name(names)
    print(names)

# output
['Mr. Entity', 'Mrs. Thing']
['Mr. Gumby', 'Mrs. Thing']
['Mr. Gumby', 'Mrs. Thing']

from copy import deepcopy

names = ['Mr. Entity', 'Mrs. Thing', [1, 3, 4]]


def change_name(name):
    name[0] = 'Mr. Gumby'
    name[2][0] = 'lff'
    print(name)


if __name__ == "__main__":
    print(names)
    # change_name(names[:])
    # change_name(names.copy())
    change_name(deepcopy(names))
    print(names)

# output
['Mr. Entity', 'Mrs. Thing', [1, 3, 4]]
['Mr. Gumby', 'Mrs. Thing', ['lff', 3, 4]]
['Mr. Entity', 'Mrs. Thing', [1, 3, 4]]
```

1）关键字参数和默认值

使用参数名提供的参数叫关键字参数，主要作用在于可以明确每个参数的作用。
关键字参数最厉害的地方在于可以在函数中给参数提供默认值，这样在调用时，可以不提供参数值，或者提供部分参数值，或者全部提供参数值。
位置参数和关键字参数可以混合使用，但位置参数要放在关键字参数前面。

```python
def greet(name, sex='male'):
    if sex == 'male':
        greetings = 'hello Mr. %s' % name
    else:
        greetings = 'hello Mrs. %s' % name
    print(greetings)

# call
greet(name='nayu')
greet(sex='male', name='nayu')

# output
hello Mr. nayu
hello Mr. nayu
```

2）任意数量参数

在某些情况下需要使函数能够接收任意数量的参数。
在参数前加*，能使函数接收任意数量的普通参数（非关键字参数），*将参数收集起来放在元组中，在函数内以元组的形式使用参数。
在参数前加**，能使函数接收任意数量的关键字参数，**将参数收集起来放在字典中，在函数内以字典的形式使用函数。

*参数与普通参数联合使用，*收集除普通参数外的所有参数。
**参数与普通参数联合使用，**收集所有关键字参数。
*参数、**参数与普通参数联合使用，*收集除普通参数、关键字参数外的所有参数，**收集所有关键字参数。

**参数必须在*参数、普通参数的后面。当普通参数在*参数后时，在调用时普通参数需要使用关键字。

```python
def print_params(*params, name='', **title):
    print(params)
    print(name)
    print(title)

# call
print_params(1, 2, 3, 4, title='anyu')

#output
(1, 2, 3, 4)

{'title': 'anyu'}
```

3）在```调用函数```时用*参数、**参数分解元组、字典

在调用函数时用*参数、**参数分解元组、字典，是在定义函数时使用*参数、**参数收集参数放在元组、字典中的逆过程。

```python
def test_args(arg1, arg2, arg3):
    print('arg1:%s, arg2:%s, arg3:%s,' % (arg1, arg2, arg3))

# call
temp = (1, 2, 3)
temp1 = {'arg1': 1, 'arg2': 2, 'arg3': 3}
test_args(*temp)
test_args(**temp1)

# output
arg1:1, arg2:2, arg3:3,
arg1:1, arg2:2, arg3:3,
```

###### 4、作用域
全局作用域————全局变量；局部作用域————局部变量
每创建一个函数就会创建一个新的局部作用域，对局部作用域中的局部变量进行操作，并不会影响全局作用域中的变量（即使他们名称一样）。

1）在函数内部访问局部变量
一般来说，在函数内部读取全局变量的值是没有问题的，如果局部变量和全局变量同名的话就不能直接访问，因为全局变量会被局部变量屏蔽。
如果非要这样做的话，可以使用globals函数获取全局变量值（locals函数获取所有局部变量）。

```python
age = 1

def calculate():
    age = globals()['age'] + 3
    print(age)
```

在函数内部不仅可以读取全局变量的值，还可以使全局变量重新引用其他新值。只要在函数内将全局变量用global声明即可。

```python
age = 1

def calculate():
    global age
    age += 3

# call
calculate()
print(age)

# output
4
```

2）嵌套作用域
Python函数时可以嵌套的，即可在函数内部定义函数。

```python
def multiplier(factor):
    def multiply_by_factor(number):
        return factor * number

    return multiply_by_factor

# call
double = multiplier(3)
print(double(5))

triple = multiplier(6)
print(triple(2))
```

类似multiply_by_factor函数存储子封闭作用域的行为叫做闭包。
```在嵌套作用域中，外部作用域的变量一般来说是不能进行重新绑定的，但是只要在内部作用域中用nonlocal对变量进行声明后，可以对外部作用域的变量进行赋值。```

```python
def multiplier(factor):
    temp = 5

    def multiply_by_factor(number):
        nonlocal temp
        temp += 2
        return factor * number

    return multiply_by_factor
```

###### 5、递归
函数可以调用自身。
