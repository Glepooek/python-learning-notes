# while True:
#     num = int(input("输入一个数字："))
#     if num % 2 == 0:
#         if num % 3 == 0:
#             print("你输入的数字可以整除 2 和 3")
#         else:
#             print("你输入的数字可以整除 2，但不能整除 3")
#     else:
#         if num % 3 == 0:
#             print("你输入的数字可以整除 3，但不能整除 2")
#         else:
#             print("你输入的数字不能整除 2 和 3")

# list1 = ["I", "love", "Python"]
# list2 = list1
# list3 = list1[:]
#
# print(id(list1))
# print(id(list2))
# print(list1 is list2)
# print(list1 == list2)
#
# print(id(list3))
# print(list1 is list3)
# print(list1 == list3)

a = 2570
b = 2570
# 在命令行中执行下面的语句返回的是false，而在pycharm中返回的是true
print(a is b)
print(a == b)
