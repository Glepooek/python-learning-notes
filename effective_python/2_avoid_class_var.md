### 避免将可变数据类型作为类变量

思考以下代码：
```python
class URLCatcher(object):
    urls = []
    def add_url(self, url):
        self.urls.append(url)
```

这段代码看起来非常正常。有一个储存URL的对象。当调用add_url方法时，它会添加一个给定的URL到存储中。
看起来非常正确吧？现在来看看实际是怎样的：

```python
catcher_one = URLCatcher()
catcher_one.add_to('http://www.baidu.com')

catcher_two = URLCatcher()
catcher_two.add_to('http://www.google.com')

print(catcher_one.urls)
print(catcher_two.urls)

# 输出结果
['http://www.baidu.com', 'http://www.google.com']
['http://www.baidu.com', 'http://www.google.com']
```

从结果可以看出。虽然实例化了两个单独的对象，但是这两个对象都有这两个URL。这是因为创建类定义时，URL列表将被实例化。该类所有的实例使用相同的列表。在有些时候这种情况是有用的，但大多数时候希望每个对象有一个单独的储存。
为此，修改代码为：

```python
class URLCatcher(object):
    def __init__(self):
        self.urls = []

    def add_url(self, url):
        self.urls.append(url)
```

现在，当创建对象时，URL列表被实例化。当实例化两个单独的对象时，它们将分别使用两个单独的列表。
