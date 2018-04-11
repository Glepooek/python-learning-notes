from copy import deepcopy
from collections import defaultdict

dict1 = {'user': 'runoob', 'num': [1, 2, 3]}
data = [
    ("animal", "bear"),
    ("animal", "duck"),
    ("plant", "cactus"),
    ("vehicle", "speed boat"),
    ("vehicle", "school bus")
]

tup1 = [('name', 'anyu'), ('age', 30)]
dict5 = {'name': 'anyu', 'age': 30}

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

    print('***字典输出结果***')
    print(dict1)
    print(dict2)
    print(dict3)
    print(dict4)

    groups = defaultdict(list)

    for (key, value) in data:
        groups[key].append(value)

    print(groups)

    print("========创建字典=========")
    # 通过元组创建字典
    print(dict(tup1))
    # 通过关键字参数创建字典
    print(dict(name='anyu', age=30))

    print("========字典格式化字符串=========")
    str1 = 'My name is %(name)s, age is %(age)d' % dict5
    print(str1)
    print({}.fromkeys(('name', 'age')))
