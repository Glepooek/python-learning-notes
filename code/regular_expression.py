import re

pattern = '.?'
list1 = ['a', 'ab', 'aab', 'aabb', 'abb', 'abbbb']

print(re.search(pattern, 'abbbbab'))
