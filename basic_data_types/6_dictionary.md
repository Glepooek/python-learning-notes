### 字典(```Dictionary```)

字典是一种可变容器，且可存储任意类型对象。
字典的每个键值对的键值用冒号(:)分割，每个键值对间用逗号(,)分割，整个字典包括在花括号({})中 ,格式如下所示：

```python
d = {key1 : value1, key2 : value2 }
```

值可以取任何数据类型，但键必须是不可变数据类型，如数字、字符串或元组。
不允许同一个键出现两次，若创建时同一个键被赋值两次，后一个值会被记住。
一个简单的字典实例：

```python
dict = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
```

###### 1、访问字典的值
把相应的键放入字典名后的方括弧内来访问字典的值。若用不存在的键访问值，则会报错。

```python
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])

# 以上实例输出结果：
dict['Name']:  Runoob
dict['Age']:  7
```

###### 2、修改字典的值
```python
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

dict['Age'] = 8;            # 更新Age
dict['School'] = "菜鸟教程"  # 添加信息

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

# 以上实例输出结果：
dict['Age']:  8
dict['School']:  菜鸟教程
```

###### 3、删除字典键/值对
能删除字典的单一键/值对，也能清空全部键/值对。删除字典用del命令。

```python
dict = {'Name': 'Runoob', 'Age': 7, 'Class': 'First'}

del dict['Name'] # 删除键 'Name'
dict.clear()     # 清空字典
del dict         # 删除字典
```

###### 4、Python内置函数及字典内置函数

| 函数 | 描述 |
| :--- | :--- |
|len(dict) | 计算字典元素个数|
|str(dict) | 输出字典，以可打印的字符串表示|
|type(variable) | 返回输入的变量类型，如果变量是字典就返回字典类型|
|dict.clear() |删除字典内所有元素|
|dict.copy() |返回一个字典的浅复制。深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用|
|dict.fromkeys() |创建一个新字典，以序列seq中元素做字典的键，value为字典所有键对应的初始值|
|dict.get(key, default=None) |返回指定键的值，如果值不在字典中返回default值|
|key in dict |如果键在字典dict里返回true，否则返回false|
|dict.items() |以列表形式返回可遍历的键/值对元组数组|
|dict.keys() |以列表形式返回一个字典所有的键|
|dict.values() |以列表形式返回字典中的所有值|
|dict.setdefault(key, default=None) |如果键不存在于字典中，将会添加键并将值设为default，并返回default值;如果存在，则返回键对应的值|
|dict.update(dict2) |把字典dict2的键/值对更新到dict里|
|pop(key[,default]) |删除字典给定键key所对应的值，返回值为被删除的值。key值必须给出。若给出的key不存在，则返回default值|
|popitem() |随机删除字典中的一对键/值并以元组形式返回该键/值对|

```python
from copy import deepcopy

dict1 = {'user': 'runoob', 'num': [1, 2, 3]}

if __name__ == '__main__':
    # 浅拷贝: 引用对象
    dict2 = dict1
    # 浅拷贝：深拷贝父对象（一级目录），子对象（二级目录）不拷贝，还是引用
    dict3 = dict1.copy()
    # 深拷贝
    dict4 = deepcopy(dict1)

    # 修改 data 数据
    dict1['user'] = 'root'
    dict1['num'].remove(1)

    print(dict1)
    print(dict2)
    print(dict3)
    print(dict4)

    # 输出结果
    {'user': 'root', 'num': [2, 3]}
    {'user': 'root', 'num': [2, 3]}
    {'user': 'runoob', 'num': [2, 3]}
    {'user': 'runoob', 'num': [1, 2, 3]}
```

