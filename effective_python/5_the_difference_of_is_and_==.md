### is和==的区别

在Python中会用到对象之间比较，可以用==，也可以用is。但是它们的区别是什么呢？
- is 比较的是两个实例对象是不是完全相同，即它们是不是同一个对象，占用的内存地址是否相同（比较id是否相同即可）。
- == 比较的是两个对象的内容是否相等，即内存地址可以不一样，内容一样即可。默认会调用对象的__eq__()方法。

可以通过如下例子来区分比较下：
```python
list1 = ["I", "love", "Python"]
list2 = list1
list3 = list1[:]

print(id(list1))
print(id(list2))
print(list1 is list2)
print(list1 == list2)

print(id(list3))
print(list1 is list3)
print(list1 == list3)

# 输出结果
50937408
50937408
True
True

50983320
False
True
```

