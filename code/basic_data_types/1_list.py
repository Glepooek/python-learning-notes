from copy import deepcopy

list1 = [12, 'niubi', 'hah', [1, 2, 3]]
name = list("Perl")
numbers = [1, 5]
full_numbers = [1, 2, 3, 4, 5]

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

    print('***拷贝列表输出结果***')
    print(list1)
    print(list2)
    print(list3)
    print(list4)
    print(list5)

    # del list1
    print('***分片赋值输出结果***')
    name[1:] = list("ython")
    print(name)
    numbers[1:1] = [4, 2, 3, 9]
    print(numbers)
    full_numbers[1:4] = []
    print(full_numbers)

    print('***排序输出结果***')
    # numbers.sort()
    # print(numbers)

    list1 = ["google", 'niubi', 'hah', 'python']
    list1.sort(key=len, reverse=True)
    print(list1)
