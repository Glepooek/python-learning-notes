list1 = ['Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose', 'Jim']
if 'Tom' in list1:
    print('call him back')

print(set([x for x in list1 if list1.count(x) > 1]))

student = {'Tom', 'Jim', 'Mary', 'Tom', 'Jack', 'Rose', 'Jim'}
student.add(12)
student.remove('Tom')
print(student)

set1 = set('abracadabra')
set2 = set('alacazam')

print(set1)
print(set2)
print(set1 & set2)
print(set1.intersection(set2))

print(set1 - set2)
print(set1.difference(set2))

print(set1 | set2)
print(set1.union(set2))

print(set1 ^ set2)
print(set1.symmetric_difference(set2))
