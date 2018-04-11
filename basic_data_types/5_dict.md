### 字典(```dict```)

字典是一种可变容器，且可存储任意类型对象。
字典的每个键值对的键值用冒号(:)分割，每个键值对间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：

```python
d = {key1 : value1, key2 : value2 }
```

值可以取任何数据类型，但键必须是不可变数据类型，如数字、字符串或元组。
不允许同一个键出现两次，若创建时同一个键被赋值两次，后一个值会被记住。
一个简单的字典实例：

```python
dic = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}

# 空字典
dic = {}
```

###### 1、访问字典的值
把相应的键放入字典名后的方括弧内来访问字典的值。若用不存在的键访问值，则会报错。

```python
dic = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print ("dic['Name']: ", dic['Name'])
print ("dic['Age']: ", dic['Age'])

# 以上实例输出结果：
dic['Name']:  Runoob
dic['Age']:  7
```

###### 2、修改字典的值
```python
dic = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

dic['Age'] = 8;            # 更新Age
dic['School'] = "菜鸟教程"  # 添加信息

print ("dic['Age']: ", dic['Age'])
print ("dic['School']: ", dic['School'])

# 以上实例输出结果：
dic['Age']:  8
dic['School']:  菜鸟教程
```

###### 3、删除字典键/值对
能删除字典的单一键/值对，也能清空全部键/值对。删除字典用del命令。

```python
dic = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

del dic['Name'] # 删除键 'Name'
dic.clear()     # 清空字典
del dic         # 删除字典
```

###### 4、字典的格式化字符串
如果使用仅以字符串为键的字典，在每个转换说明符%后面，加上用圆括号括起来的键，后面再加上格式符%及字典名，来达到字典格式化字符串的目的。

```python
dict5 = {'name': 'anyu', 'age': 30}
str1 = 'My name is %(name)s, age is %(age)d' % dict5
print(str1)

# output
My name is anyu, age is 30
```

###### 5、Python内置函数或表达式

| 函数 | 描述 |
| :--- | :--- |
|len(dic) | 计算字典元素个数|
|str(dic) | 输出字典，以可打印的字符串表示|
|type(variable) | 返回输入的变量类型，如果变量是字典就返回字典类型|
|dict() | 可通过序列或关键字参数创建字典|
|key in dict |检查键是否在字典中|

###### 6、字典函数

| 函数 | 描述 |
| :--- | :--- |
|dict.clear() |删除字典内所有元素|
|dict.copy() |返回一个字典的浅复制。深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用|
|dict.fromkeys() |创建一个新字典，以序列seq中元素做字典的键，所有键对应的初始值为None或设定的default值|
|dict.setdefault(key, default=None) |如果键不存在于字典中，将会添加键并将值设为default，并返回default值;如果存在，则返回键对应的值|
|dict.get(key, default=None) |返回指定键的值，如果值不在字典中返回None或设定的default值|
|dict.items() |以列表形式返回可遍历的键/值对元组|
|dict.keys() |以列表形式返回一个字典所有的键|
|dict.values() |以列表形式返回字典中的所有值|
|dict.update(dic2) |把字典dic2的键/值对更新到dic里，若有相同的键，则会进行覆盖|
|dict.pop(key[,default]) |删除字典给定键key所对应的值，返回值为被删除的值。key值必须给出。若给出的key不存在，则返回default值|
|dict.popitem() |随机删除字典中的一对键/值，并以元组形式返回该键/值对|


```python
from copy import deepcopy

dic1 = {'user': 'runoob', 'num': [1, 2, 3]}

if __name__ == '__main__':
    # 浅拷贝: 引用对象
    dic2 = dic1
    # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
    dic3 = dic1.copy()
    # 深拷贝
    dic4 = deepcopy(dic1)

    # 修改 data 数据
    dic1['user'] = 'root'
    dic1['num'].remove(1)

    print(dic1)
    print(dic2)
    print(dic3)
    print(dic4)

    # 输出结果
    {'user': 'root', 'num': [2, 3]}
    {'user': 'root', 'num': [2, 3]}
    {'user': 'runoob', 'num': [2, 3]}
    {'user': 'runoob', 'num': [1, 2, 3]}
```

