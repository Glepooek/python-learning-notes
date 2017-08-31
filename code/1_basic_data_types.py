from copy import deepcopy
from collections import defaultdict

list1 = [12, 'niubi', 'hah', [1, 2, 3]]
dict1 = {'user': 'runoob', 'num': [1, 2, 3]}

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

    print('***列表输出结果***')
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    print(list5)

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

    data = [
        ("animal", "bear"),
        ("animal", "duck"),
        ("plant", "cactus"),
        ("vehicle", "speed boat"),
        ("vehicle", "school bus")
    ]

    groups = defaultdict(list)

    for (key, value) in data:
        groups[key].append(value)

    print(groups)
