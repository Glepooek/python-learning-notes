import fileinput

# with open('text.txt', mode='a+') as file:
#     file.write('FUCK YOU\r\n')
#     # file.writelines(['\r\nI love you', '\r\nvery much'])
#     # return to the top of the file before reading, otherwise you'll just read an empty string
#     file.seek(0)
#     # print(file.read())
#     print(file.readlines())
#
# with open('text.txt', mode='a+') as file1:
#     file1.seek(0)
#     while True:
#         char = file1.read(1)
#         if not char:
#             break
#         else:
#             print(char)
#
# with open('text.txt', mode='a+') as file2:
#     file2.seek(0)
#     while True:
#         line = file2.readline()
#         if not line:
#             break
#         else:
#             print(line)

# with fileinput.input('text.txt') as file:
#     for line in file:
#         print(line)

with open('text.txt', mode='a+') as file2:
    file2.seek(0)
    for line in file2:
        print(line)
