from itertools import takewhile
from itertools import dropwhile
from itertools import filterfalse
from itertools import starmap
from itertools import count
from itertools import repeat
from itertools import islice
from itertools import combinations
from itertools import combinations_with_replacement
from itertools import product
from itertools import permutations
from itertools import compress
from itertools import groupby
from itertools import chain

list1 = [1, 3, 5, 6, 2, 4]
list2 = [(1, 2), (3, 4)]

dict2 = {'key1': [1, 2], 'key2': [3, 4]}

if __name__ == '__main__':

    print('takewhile函数执行结果：')
    for value in takewhile(lambda x: x < 5, list1):
        print(value)

    print('dropwhile函数执行结果：')
    for value in dropwhile(lambda x: x < 5, list1):
        print(value)

    print('filterfalse函数执行结果：')
    for value in filterfalse(lambda x: x % 2, range(10)):
        print(value)

    print('starmap函数执行结果：')
    for value in starmap(lambda x, y: x * y, dict2.values()):
        print(value)

    # print('count函数执行结果：')
    # for value in count(start=0, step=5):
    #     print(value)

    print('repeat函数执行结果：')
    for value in repeat(dict2.values(), 5):
        print(value)

    print('islice函数执行结果：')
    for value in islice(dict2.values(), 1, 4, 2):
        print(value)

    print('combinations函数执行结果：')
    for value in combinations('abcd', 2):
        print(value)

    print('product函数执行结果：')
    for value in product('abcd', repeat=3):
        print(value)

    print('permutations函数执行结果：')
    for value in permutations('abcd', 2):
        print(value)

    print('compress函数执行结果：')
    for each in compress('abcd', [1, 0]):
        print(each)

    print('groupby函数执行结果：')
    for key, vale in groupby('aabbbc'):
        print(key, list(vale))

    print('chain函数执行结果：')
    for each in chain('i', 'love', 'python'):
        print(each)
