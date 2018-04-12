### 循环语句(```loop```)

Python中的循环语句有：for、while。

###### 1、while循环
while循环语句的一般形式如下：

```python
while 判断条件:
    语句
```

例如：

```python
sum = 0
counter = 1
num = 100

while counter <= 100:
    sum += counter
    counter += 1

print(sum)
```

###### 2、while循环使用else语句
while … else语句在条件为false（循环没有被break）时执行else的语句块。修改上面的例子，如：

```python
sum = 0
counter = 1
num = 100

while counter <= 100:
    sum += counter
    counter += 1
else:
    print(sum)
```

###### 3、for循环
for循环可以遍历任何序列的项，```for循环的一大优势就是可以在循环中使用序列解包```。for循环语句的一般形式如下：

```python
for var in sequence:
    语句
```

例如：

```python
languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x)
```

###### 4、for循环使用else语句
for … else语句在for语句执行完毕（循环没有被break）时执行else的语句块。修改上面的例子，如：

```python
languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x)
else:
    print('循环没有被break')
```

###### 5、break和continue语句及循环中的else子句
break语句可以跳出for和while的循环体，即终止循环。
如果从for或while循环中终止，任何循环对应的else子句将不执行。
continue语句用来跳过当前循环中的剩余语句，然后继续进行下一轮循环。

```python
for letter in 'Runoob':
    if letter == 'o':
        break
    print('当前字母 :', letter)


for letter in 'Runoob':
    if letter == 'o':
        continue
    print('当前字母 :', letter)
else:
    print('有continue的for循环可以执行else语句')
```

###### 6、列表推导式
列表推导式是利用其它列表创建新列表的一种方式。

```python
list1 = [x * x for x in range(10)]
print(list1)

# output
[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 列表推导式与if语句结合使用
list2 = [x * x for x in range(10) if x % 3 == 0]
print(list2)

# output
[0, 9, 36, 81]

# 列表推导式中使用多个for语句
list3 = [(x, y) for x in range(3) for y in range(3)]
print(list3)

# output
[(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
```

###### 7、pass语句
pass是空语句，不做任何事情，一般用做占位语句，是为了保持程序结构的完整性。 如下实例：

```python
for letter in 'Runoob':
    if letter == 'o':
        pass
    print('当前字母 :', letter)
else:
    print('pass语句不做任何事情')
```

###### 8、del语句
del语句移除一个对象的引用和名字本身，而不是值本身。当某个值不再使用时，Python解释器会负责内存的回收。

###### 9、使用exec和eval执行和求值字符串
1）exec
exec函数用于执行字符串形式的语句。
2）eval
eval用于计算字符串形式的Python表达式，并且返回结果值。