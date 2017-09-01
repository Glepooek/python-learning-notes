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

    print('***列表输出结果***')
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    print(list5)
