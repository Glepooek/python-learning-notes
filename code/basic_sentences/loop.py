sum = 0
counter = 1
num = 100

while counter <= 100:
    sum += counter
    counter += 1
else:
    print(sum)

languages = ["C", "C++", "Perl", "Python"]
for x in languages:
    print(x)
else:
    print('循环没有被break')

for letter in 'Runoob':
    if letter == 'o':
        continue
    print('当前字母 :', letter)
else:
    print('有continue的for循环可以执行else语句')

for letter in 'Runoob':
    if letter == 'o':
        pass
    print('当前字母 :', letter)
else:
    print('pass语句不做任何事情')

# 下面是错误的示范
# strings = 'I love you'
# for index, str1 in enumerate(strings):
#     if 'I' in str1:
#         strings[index] = 'xxx'

list1 = [x * x for x in range(10)]
print(list1)

list2 = [x * x for x in range(10) if x % 3 == 0]
print(list2)

list3 = [(x, y) for x in range(3) for y in range(3)]
print(list3)

# 高效匹配名字首字母相同的男女孩
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)

print([b + '+' + g for b in boys for g in letterGirls[b[0]]])
