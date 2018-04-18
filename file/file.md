### 文件和素材

###### 1、打开文件
open函数用来代开文件，语法如下：

```python
# 打开文件并返回流
open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
```

参数file为必选参数，传入文件名或文件路径。其他参数为可选参数。

1）文件模式mode
参数mode的默认值为'r'，如果要想向文件内写入内容，则必须显式提供模式参数。

|值| 描述|
| :--- |:--- |
| 'r'  |  打开以读取 (默认)|
| 'w'  |  打开写入，先截断文件|
| 'x'  |  创建新的文件，并打开写入|
| 'a'  |  如果文件存在，打开写入，并追加到文件尾部|
| 'b'  |  二进制模式|
| 't'  |  文本模式 (默认)|
| '+'  |  读、写模式，可以和其他任何模式联合使用|
| 'U'  |  通用换行符模式 (不建议使用)|

2）缓冲buffering
参数buffering控制着文件的缓冲。
- buffering = 0，无（关闭）缓冲；
- buffering = 1，有缓冲；
- buffering > 1，数字代表缓冲区的大小；
- buffering <= -1，代表使用默认的缓冲区大小。

###### 2、基本文件方法

1）读和写
文件或流最重要的能力是提供或者接受数据。
用file.write()（会增加新行）和file.read()（可设置读取的最大字符数）方法写入和读取数据。

```python
with open('text.txt', mode='a+') as file:
    file.write('FUCK YOU\r\n')
    # return to the top of the file before reading, otherwise you'll just read an empty string
    file.seek(0)
    print(file.read())
```

2）读写行
- file.readline()，读取单独一行（不设置参数，从当前位置开始直到一个换行符出现，也读取换行符）或读取最大字节数（设置参数）。
- file.readlines()，读取所有的行并将其作为列表返回。
- file.writelines()，将字符串列表写入文件（不增加新行）。

3）关闭文件
使用file.close()方法关闭文件，或可使用with语句来自动关闭文件。

```python
with open('text.txt', mode='a+') as file:
    file.write('FUCK YOU\r\n')
```

###### 3、对文件内容进行迭代
1）按字节处理

```python
with open('text.txt', mode='a+') as file:
    file.seek(0)
    while True:
        char = file.read(1)
        if not char:
            break
        else:
            print(char)
```

2）按行处理

```python
with open('text.txt', mode='a+') as file2:
    file2.seek(0)
    while True:
        line = file2.readline()
        if not line:
            break
        else:
            print(line)
```

3）读取所有内容
file.read()或file.readlines()

4）使用fileinput模块读取文件
fileinput.input()读取文件后，返回一个可迭代对象，可实现懒惰迭代。

```python
with fileinput.input('text.txt') as file:
    for line in file:
        print(line)
```

5）文件迭代器

```python
with open('text.txt', mode='a+') as file:
    file.seek(0)
    for line in file:
        print(line)
```