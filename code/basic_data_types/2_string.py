from string import Template
from math import pi

var1 = 'hello'
var2 = 'I love you'
var3 = 10000

var4 = Template("$key, I love you $value years")
var5 = Template("this book costs $$$key")
var6 = Template("I love ${x}ython")


class Person:
    def __init__(self, name, age):
        self.name, self.age = name, age

    def __str__(self):
        return 'This guy is {self.name},is {self.age} years old'.format(self=self)


if __name__ == "__main__":
    # 乘
    print(var1 * 3)

    full_str = f'{var1},{var2} {var3}年'

    # 成员资格判断
    if var1 in full_str:
        print(full_str)

    # 迭代
    for x in full_str:
        print(x)

    # d = {}
    # d['key'] = 'lff'
    # d['value'] = 10000
    # print(var4.safe_substitute(d))
    # print(var4.safe_substitute(key='lff', value=10000))
    # print(var5.safe_substitute(key=10))
    # print(var6.safe_substitute(x='p'))
    # print('%5d' % 10 + '\n' + '%5d' % -10)

    print(str(Person('kzc', 18)))
