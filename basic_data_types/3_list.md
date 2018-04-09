### 列表(```List```)

列表是最常用的Python数据类型之一，列表的数据项不需要具有相同的类型。列表数据项在一个方括号内，由逗号分隔。
列表下标索引左边从0开始，右边从-1开始。
创建一个列表，只要把逗号分隔的不同的数据项使用方括号括起来即可。如下所示：

```python
list1 = ['Google', 'Runoob', 1997, 2000]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]

# 列表中嵌套列表
list4 = [['a', 'b', 'c'], [1, 2, 3]]
```

###### 1、创建空列表
```python
# 空列表
list1 = []
# 有一个空值的列表
list2 = [None]
```

###### 2、列表索引，分片

列表下标索引左边从0开始，右边从-1开始，可以进行索引、分片。

L = ['Google', 'Runoob', 1997, 2000]

| Python表达式 | 结果 | 描述 |
| :--- | :--- | :--- |
| L[2] | 1997 | 读取第三个元素 |
| L[-2] | 1997 | 反向读取；读取倒数第二个元素 |
| L[1:] | ['Runoob', 1997, 2000] | 截取元素，从第二个开始的所有元素 |
| L[1:3] | ['Runoob', 1997] | 截取元素，从第二个开始到第三个元素 |
| L[:] | ['Google', 'Runoob', 1997, 2000] | 截取整个列表，生成新列表。浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用|

###### 3、列表运算符

| python表达式 | 结果 | 描述 |
| :--- | :--- | :--- |
| [1, 2, 3] + [4, 5, 6]    | [1, 2, 3, 4, 5, 6] | 连接 |
| ['Hi!'] * 4 | ['Hi!', 'Hi!', 'Hi!', 'Hi!']      |   复制 |
| 3 in [1, 2, 3] | True      |    元素是否存在 |
| for x in [1, 2, 3]: print x | 1 2 3      |    迭代 |

字符串、列表、元组迭代也可以这样：
```python
list1 = [12, 'niubi', 'hah']

# 遍历 [start,end)，间隔为 span，
# 当 span>0 时顺序遍历, 当 span<0 时，逆着遍历。
# start 不输入则默认为 0，end 不输入默认为长度。
print(list1[::-1])

# 输出结果
['hah', 'niubi', 12]
```

###### 4、列表元素赋值
```python
list1 = ['Google', 'Runoob', 1997, 2000]

list1[2] = 2001
print(list1)

# 输出结果
['Google', 'Runoob', 2001, 2000]
```

###### 5、删除列表或列表元素
```python
list1 = ['Google', 'Runoob', 1997, 2000]

del list1[2]
# del list1

print(list1)

# 输出结果
['Google', 'Runoob', 2000]
```

###### 6、分片赋值
```python
# 分片赋值可以一次为多个元素赋值。可以使用与原序列不等长的序列将分片替换。
name = list("Perl")
name[1:] = list("ython")
print(name)

# 分片赋值可以插入多个新元素
numbers = [1,5]
numbers[1:1] = [2,3,4]
print(numbers)

# 分片赋值可以删除多个元素
full_numbers = [1,2,3,4,5]
full_numbers[1:4] =[]
print(full_numbers)
```

###### 7、Python内置函数

| 函数 | 描述 |
| :--- | :--- |
|len(list) |返回列表元素个数|
|max(list) |返回列表元素最大值|
|min(list) |返回列表元素最小值|
|list(seq) |将元组转换为列表|

###### 8、列表函数

| 函数 | 描述 |
| :--- | :--- |
|list.append(obj) |在列表末尾追加元素|
|list.count(obj) |统计某个元素在列表中出现的次数|
|list.extend(seq) |在列表末尾一次性追加另一个序列中的所有元素来扩展原来的列表|
|list.index(obj) |从列表中找出某个值的第一个匹配项的索引位置|
|list.insert(index, obj) |将元素插入列表指定索引处|
|list.pop(index) |移除列表中指定索引处的元素（默认最后一个元素），并且返回该元素的值|
|list.remove(obj) |移除列表中某个值的第一个匹配项|
|list.reverse() |反向列表中元素|
|list.sort([func]) |对原列表进行排序|
|list.clear() |清空列表|
|list.copy() |复制列表，浅拷贝|

```python
from copy import deepcopy

list1 = [12, 'niubi', 'hah', [1, 2, 3]]

if __name__ == '__main__':
    # 浅拷贝:引用对象
    list2 = list1
    # 浅拷贝:深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
    list3 = list1[:]
    # 浅拷贝:深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
    list4 = list1.copy()
    # 深拷贝
    list5 = deepcopy(list1)

    list1[0] = 0
    list1[3][2] = 'change'

    print(list1)
    print(list2)
    print(list3)
    print(list4)
    print(list5)

    #输出结果
    [0, 'niubi', 'hah', [1, 2, 'change']]
    [0, 'niubi', 'hah', [1, 2, 'change']]
    [12, 'niubi', 'hah', [1, 2, 'change']]
    [12, 'niubi', 'hah', [1, 2, 'change']]
    [12, 'niubi', 'hah', [1, 2, 3]]
```