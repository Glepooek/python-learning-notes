### 集合(```Set```)

集合（set）是一个无序不重复元素的序列。
基本功能是进行成员关系测试和删除重复元素，以及集合运算。
可以使用大括号```{ }```或者```set()```函数创建集合。
注意，创建一个空集合必须用```set()```而不是```{ }```，因为```{ }```是用来创建一个空字典。

###### 1、关系测试

```python
student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose'}
if 'Tom' in student:
    print('call him back')
```

###### 2、删除重复元素
```python
student = ['Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose', 'Jim']
print(set([x for x in student if student.count(x) > 1]))

# 输出结果
{'Jim', 'Tom'}

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose', 'Jim'}
print(student)

# 输出结果
{'Tom', 'Jack', 'Rose', 'Jim', 'Mary'}
```

###### 3、集合运算
交集(&)：以属于A且属于B的元素为元素的集合成为A与B的交（集）
差集(-)：以属于A而不属于B的元素为元素的集合成为A与B的差（集）
并集(|)：以属于A或属于B的元素为元素的集合成为A与B的并（集）
对称差集(^)：以属于A而不属于B，属于B而不属于A的元素为元素的集合成为A与B的对称差（集）

```python
set1 = set('abracadabra')
set2 = set('alacazam')

print(set1)
print(set2)
print(set1 & set2)
print(set1.intersection(set2))

print(set1 - set2)
print(set1.difference(set2))

print(set1 | set2)
print(set1.union(set2))

print(set1 ^ set2)
print(set1.symmetric_difference(set2))

# 输出结果
{'r', 'd', 'b', 'a', 'c'}
{'m', 'l', 'a', 'z', 'c'}
{'a', 'c'}
{'a', 'c'}
{'d', 'r', 'b'}
{'d', 'r', 'b'}
{'r', 'm', 'd', 'l', 'b', 'a', 'z', 'c'}
{'r', 'm', 'd', 'l', 'b', 'a', 'z', 'c'}
{'r', 'm', 'd', 'l', 'b', 'z'}
{'r', 'm', 'd', 'l', 'b', 'z'}
```
