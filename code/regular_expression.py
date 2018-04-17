import re

def double(matched):
    value = int(matched.group('value'))
    key = matched.group('key')
    return ''.join([str(value * 4), str(key * 2)])

s = 'A24G4HFD567 ds89a2'
pattern = '(?P<value>\d+) (?P<key>ds\d*)'
print(re.search(pattern, s).group(1))
print(re.search(pattern, s).group(2))

print(re.sub(pattern, double, s))


