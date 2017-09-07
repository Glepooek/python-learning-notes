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
for循环可以遍历任何序列的项。for循环语句的一般形式如下：

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

###### 6、pass语句
pass是空语句，不做任何事情，一般用做占位语句，是为了保持程序结构的完整性。 如下实例：

```python
for letter in 'Runoob':
    if letter == 'o':
        pass
    print('当前字母 :', letter)
else:
    print('pass语句不做任何事情')
```