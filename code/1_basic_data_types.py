list1 = [12, 'niubi', 'hah', [1, 2, 3]]

# 浅拷贝
list2 = list1[:]
list3 = list1.copy()

# list2[3][2] = 5
del list2[3]

print(list3)
print(list2)
print(list1)

# 翻转列表对象
print(list1[::-1])

class URLCatcher(object):
    def __init__(self):
        self.urls = []

    def add_url(self, url):
        return self.urls.append(url)


catcher_one = URLCatcher()
catcher_one.add_url('http://www.baidu.com')

catcher_two = URLCatcher()
catcher_two.add_url('http://www.google.com')

print(catcher_one.urls)
print(catcher_two.urls)


def add_url(var, urls=None):
    if not urls:
        urls = []
    urls.append(var)
    return urls


print(add_url('http://www.baidu.com'))
print(add_url('http://www.google.com'))


list4 = [12, 'niubi', 'hah']
list5 = list4.copy()
del list5[1]

print(list4)
print(list5)
