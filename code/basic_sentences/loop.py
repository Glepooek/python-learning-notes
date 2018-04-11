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
