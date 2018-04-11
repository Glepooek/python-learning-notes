### 其他语句

###### 1、import语句
import语句用于导入模块或模块中的函数。

```python
# 导入模块
import somemodule

# 导入模块下的某个函数
from somemodule import somefunction

# 导入模块下的多个函数
from somemodule import somefunction, anotherfunction, yetanotherfunction

# 导入模块下所有函数
from somemodule import *

# 导入的模块或函数均可以取别名，这在导入同名的函数时非常有用
from module1 import open as open1
from module2 import open as open2
```

###### 2、赋值语句

1)序列解包

```python
# 同时进行多个赋值
x, y, z = 1, 2, 3

# 交换变量
x, y = y, x
```

上面代码示例中所做的事情就是序列解包，即将多个值的序列解开，放到变量的序列中。

```python
values = (1, 2, 3)
x, y, z = values
```

当函数或方法返回元组（或者其他序列或可迭代对象）时，该特性非常有用。
```所解包的序列中元素的数量必须要与赋值符号（=）左边的变量数量完全一致。```

2）链式赋值
同时将同一个值赋值给多个变量。

```python
x = y = somefuncetion()

# 链式赋值的坑
# 链式赋值是从左到右开始赋值的
s = [1, 2, 3, 4, 5, 6]
i = 0
i = s[i] = 3

print(i)
print(s)

# output
3
[1, 2, 3, 3, 5, 6]
```

3）增量赋值
将运算符放在赋值运算符=的左边，如：

```python
x = 2
x += 1
x *= 3

# 其他数据类型也适用，只要二元运算符支持该类型
foo = 'anyu'
foo *= 2
print(foo)

# output
anyuanyu
```

###### 3、语句块
用缩进来创建语句块。
用冒号来标识语句块的开始，块中的每个语句都具有相同的缩进量，当回退到和已经闭合的块一样的缩进量时，就表示当前块结束了。


