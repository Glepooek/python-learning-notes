### 避免将可变数据类型作为函数定义中的默认参数

搜索当前页面上的链接，并可选将其附加到另一个提供的列表中，代码如下：

```python
def search_for_links(page, add_to=[]):
    new_links = page.search_for_links()
    add_to.extend(new_links)
    return add_to
```

从表面看，代码没有问题，事实上它也是，而且是可以运行的。
但是这里有个问题，如果给add_to参数提供了一个列表，并让它使用默认值，就会出现一些神奇的事情。

试试下面的代码：

```python
def func(var1, var2=[]):
    var2.append(var1)
    print var2

func(3)
func(4)
func(5)

# 输出结果：
[3]
[3, 4]
[3, 4, 5]
```

输出结果与期望的并不一样。为什么呢？如你所见，每次都使用的是同一个列表，输出为什么会是这样？
在Python中，当编写这样的函数时，这个列表被实例化为函数定义的一部分。
当函数运行时，它并不是每次都被实例化。这意味着，这个函数会一直使用完全一样的列表对象，除非我们提供一个新的对象：

```python
func(3, [4])

# 输出结果
[4, 3]
```

答案正如我们所想的那样。要想得到这种结果，正确的方法是：

```python
def fn(var1, var2=None):
    if not var2:
        var2 = []
    var2.append(var1)
```

或是在第一个例子中：

```python
def search_for_links(page, add_to=None):
    if not add_to:
        add_to = []
    new_links = page.search_for_links()
    add_to.extend(new_links)
    return add_to
```

这将在模块加载的时候移走实例化的内容，以便每次运行函数时都会发生列表实例化。
请注意，对于不可变数据类型，比如元组、字符串、整型，是不需要考虑这种情况的。
这意味着，像下面这样的代码是非常可行的：

```python
def func(message="my message"):
    print message
```