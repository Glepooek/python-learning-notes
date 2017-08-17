import re

# 将匹配的数字乘于 2
def double(matched):
    value = int(matched.group('value'))
    return str(value * 2)

s = 'A24G4HFD567'
print(re.sub('(?P<value>\d+)', double, s))


pattern = '(?P<value>\d+)'
print(re.sub(pattern, double, s))
