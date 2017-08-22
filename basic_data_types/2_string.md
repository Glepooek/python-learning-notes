### 字符串\(`String`\)

字符串是Python中最常用的数据类型。在Python3中，所有的字符串都是`Unicode字符串`。  
Python不支持单字符类型，单字符在Python也是作为一个字符串使用。  
使用单引号号\('\)、双引号\("\)或三引号\('''、"""\)来创建字符串，  
其中三引号允许一个字符串跨多行，字符串中可以包含`换行符、制表符以及其他特殊字符`。如：

```python
var1 = 'Google'
var2 = "Runoob"

str = '''这是一个多行字符串的实例
多行字符串可以使用制表符
TAB ( \t )。
也可以使用换行符 [ \n ]。
'''
```

###### 1、创建空字符串

```python
var1 = ''
var2 = ""
var3 = ''''''
var4 = """"""
```

###### 2、字符串索引，截取

字符串下标索引左边从0开始，右边从-1开始，可以进行索引、截取、组合等。  
L = 'Google'

| Python表达式 | 结果 | 描述 |
| :--- | :--- | :--- |
| L\[2\] | 'o' | 读取第三个元素 |
| L\[-2\] | 'l' | 反向读取；读取倒数第二个元素 |
| L\[1:\] | 'oogle' | 截取元素，从第二个开始的所有元素 |
| L\[1:3\] | 'oo' | 截取元素，从第二个开始到第三个元素 |

###### 3、连接字符串

字符串中的元素值是不允许修改的，但可以对字符串进行连接组合，如下实例:

```python
var1 = 'Google'
var2 = 'runoob'

# 以下修改字符串元素操作是非法的
# var1[0] = 'g'

# 创建一个新的字符串
var3 = var1 + var2
print(var3)

# 以上实例输出结果：
Googlerunoob
```

###### 4、删除字符串

字符串中的元素值是不允许删除的，但可以使用del语句来删除整个字符串，如下实例:

```python
var1 = 'Google'

# 以下删除字符串元素操作是非法的
# del var1[0]

del var1
print(var1)

# 以上实例元组被删除后，输出变量会有异常信息，输出如下所示：
Traceback (most recent call last):
  File "test.py", line 8, in <module>
    print (var1)
NameError: name 'tup' is not defined
```

###### 5、Python转义字符

在字符串中使用特殊字符时，python用反斜杠\(\)转义字符。如下表：

| 转义字符 | 描述 |
| :--- | :--- |
| `\(在行尾时)` | 续行符 |
| `\\` | 反斜杠符号 |
| \' | 单引号 |
| \" | 双引号 |
| \a | 响铃 |
| \b | 退格\(Backspace\) |
| \e | 转义 |
| \000 | 空 |
| \n | 换行 |
| \v | 纵向制表符 |
| \t | 横向制表符 |
| \r | 回车 |
| \f | 换页 |
| \oyy | 八进制数，yy代表的字符，例如：\o12代表换行 |
| \xyy | 十六进制数，yy代表的字符，例如：\x0a代表换行 |
| \other | 其它的字符以普通格式输出 |

###### 6、字符串运算符

| 操作符 | 描述 |
| :--- | :--- |
| + | 字符串连接 |
| \* | 重复输出字符串 |
| \[\] | 通过索引获取字符串中字符 |
| \[:\] | 截取字符串中的一部分 |
| in | 成员运算符，如果字符串中包含给定的字符返回True |
| not in | 成员运算符，如果字符串中不包含给定的字符返回True |
| r/R | 原始字符串，所有字符都是按照字面意思来使用，没有特殊字符。  |
| % | 格式字符串 |

###### 7、字符串格式化

1）%格式化操作

Python2.6之前的版本中使用`%`对字符串进行格式化操作。

```python
str1 = 'I love %s' % ('python')
print(str1)
# output:
I love python

str2 = "我叫 %s 今年 %d 岁!" % ('小明', 10)
print(str2)
# output:
我叫 小明 今年 10 岁!

str3 = '这是测试数据：%.*f' % (5, 20)
print(str3)
# output:
这是测试数据：20.00000
```

Python字符串格式化符号:

| 符号  | 描述 |
| :---  | :--- |
|  %c	| 格式化字符及其ASCII码|
|  %s	| 格式化字符串|
|  %d	| 格式化整数|
|  %u	| 格式化无符号整型|
|  %o	| 格式化无符号八进制数|
|  %x	| 格式化无符号十六进制数|
|  %X	| 格式化无符号十六进制数（大写）|
|  %f	| 格式化浮点数字，可指定小数点后的精度|
|  %e	| 用科学计数法格式化浮点数|
|  %E	| 作用同%e，用科学计数法格式化浮点数|
|  %g	| 指数(e)或浮点数 (根据显示长度)|
|  %G	| 指数(E)或浮点数 (根据显示长度)|
|  %p	| 用十六进制数格式化变量的地址|

格式化操作符辅助指令:

| 符号  | 描述 |
| :---  | :--- |
|*	|定义宽度或者小数点精度|
|-	|用做左对齐|
|+	|在正数前面显示加号( + )|
|```<sp>```|在正数前面显示空格|
|#	|在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')|
|0	|显示的数字前面填充'0'而不是默认的空格|
|%	|'%%'输出一个单一的'%'|
|(var)|	映射变量(字典参数)|
|m.n.|m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)|

2）str.format()

Python2.6开始，新增了一种格式化字符串的函数str.format\(\)，它增强了字符串格式化的功能。
基本语法是通过`{}和:`来代替以前的`%`。

通过位置

字符串的format函数可以接受无限个参数，参数位置可以不按顺序，可以不用参数或者每个参数用多次，
不过2.6不能为空{}，2.7才可以。

```python
'{0},{1}'.format('kzc',18)
#output:
'kzc,18'

'{},{}'.format('kzc',18)
#output:
'kzc,18'

'{1},{0},{1}'.format('kzc',18)
#output:
'18,kzc,18'
```

通过关键字参数

```python
'{name},{age}'.format(age=18,name='kzc')
#output:
'kzc,18'

dict1 = {'age': 18, 'name': 'kzc'}
print('{dict1[name]},{dict1[age]}'.format(dict1=dict1))
#output:
'kzc,18'

args=['lu']
kwargs = {'name1': 'Kevin', 'name2': 'Tom'}
print('hello {name1} {} i am {name2}'.format(*args, **kwargs))
#output:
hello Kevin lu i am Tom
```

通过对象属性

```python
class Person:
    def __init__(self,name,age):
        self.name,self.age = name,age
        def __str__(self):
            return 'This guy is {self.name},is {self.age} old'.format(self=self)

print(str(Person('kzc',18)))
#output:
'This guy is kzc,is 18 old'
```

通过下标

```python
p=['kzc',18]
print('{0[0]},{0[1]}'.format(p))
#output:
'kzc,18'

p=['kzc',18]
print('{p[0]},{p[1]}'.format(p = p))
#output:
'kzc,18'
```

格式限定符,它有着丰富的的“格式限定符”（语法是{}中带:号）

填充与对齐

| 数字 | 格式 | 描述 |
| :--- | :---| :--- |
|5	|{:0>2}|数字补零 (填充左边, 宽度为2)
|5	|{:x<4}| 数字补x (填充右边, 宽度为4)
|10	|{:x^4}|数字补x (填充左右两边, 宽度为4)
|13	|{:10}|	右对齐 (默认, 宽度为10)
|13	|{:<10}|左对齐 (宽度为10)
|13	|{:^10}|中间对齐 (宽度为10)

格式转换
主要就是进制了，b、d、o、x分别是二进制、十进制、八进制、十六进制。

| 数字 | 格式 |输出 | 描述 |
| :--- | :--- |:--- | :--- |
|3.1415926|	{:.2f}|	3.14|	保留小数点后两位|
|3.1415926|	{:+.2f}| +3.14|	带符号保留小数点后两位|
|-1|	{:+.2f}|	-1.00|	带符号保留小数点后两位|
|2.71828|	{:.0f}|	3|	不带小数|
|1000000|	{:,}|	1,000,000|	以逗号分隔的数字格式|
|0.25|	{:.2%}|	25.00%|	百分比格式|
|1000000000|	{:.2e}|	1.00e+09|	指数记法|
|25|	{0:b}|	11001	|转换成二进制|
|25|	{0:d}|	25	|转换成十进制|
|25|	{0:o}|	31	|转换成八进制|
|25|	{0:x}|	19	|转换成十六进制|


###### 8、字符串常用内置函数

| 方法 | 描述 |
| :--- | :--- |
| capitalize\(\) | 将字符串的第一个字符转换为大写 |
| lower\(\) | 转换字符串中所有大写字符为小写 |
| upper\(\) | 转换字符串中的小写字母为大写 |
| swapcase\(\) | 将字符串中大写转换为小写，小写转换为大写 |
| title\(\) | 返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写\(见istitle\(\)\) |
| islower\(\) | 如果字符串中包含至少一个区分大小写的字符，并且所有这些\(区分大小写的\)字符都是小写，则返回True，否则返回False |
| isupper\(\) | 如果字符串中包含至少一个区分大小写的字符，并且所有这些\(区分大小写的\)字符都是大写，则返回True，否则返回False |
| istitle\(\) | 如果字符串是标题化的\(见title\(\)\)则返回True，否则返回False |
| startswith\(str, beg=0,end=len\(string\)\) | 检查字符串是否是以str开头，是则返回True，否则返回False。如果beg 和end指定值，则在指定范围内检查。 |
| endswith\(str, beg=0, end=len\(string\)\) | 检查字符串是否以str结束，如果beg或者end指定则检查指定的范围内是否以str结束，如果是，返回True,否则返回False |
| center\(width, fillchar\) | 返回一个指定的宽度width居中的字符串，fillchar为填充的字符，默认为空格。 |
| zfill \(width\) | 返回长度为width的字符串，原字符串右对齐，前面填充0 |
| ljust\(width\[, fillchar\]\) | 返回一个原字符串左对齐,并使用fillchar填充至长度width的新字符串，fillchar默认为空格。 |
| rjust\(width,\[, fillchar\]\) | 返回一个原字符串右对齐,并使用fillchar\(默认空格）填充至长度 width 的新字符串 |
| strip\(\[chars\]\) | 在字符串上执行lstrip\(\)和 rstrip\(\) |
| lstrip\(\) | 截掉字符串左边的空格或指定字符。 |
| rstrip\(\) | 截掉字符串字符串末尾的空格 |
| len\(string\) | 返回字符串长度 |
| count\(str, beg= 0,end=len\(string\)\) | 返回str在string里面出现的次数，如果beg或者end指定则返回指定范围内str出现的次数 |
| bytes.decode\(encoding="utf-8", errors="strict"\) | Python3中没有 decode 方法，但我们可以使用 bytes 对象的 decode\(\) 方法来解码给定的 bytes 对象，这个 bytes 对象可以由 str.encode\(\) 来编码返回。 |
| encode\(encoding='UTF-8',errors='strict'\) | 以 encoding 指定的编码格式编码字符串，如果出错默认报一个ValueError 的异常，除非 errors 指定的是'ignore'或者'replace' |
| find\(str, beg=0 end=len\(string\)\) | 检测str是否包含在字符串中，如果beg和end指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回-1 |
| index\(str, beg=0, end=len\(string\)\) | 跟find\(\)方法一样，只不过如果str不在字符串中会报一个异常 |
| rfind\(str, beg=0,end=len\(string\)\) | 类似于find\(\)函数，不过是从右边开始查找 |
| rindex\( str, beg=0, end=len\(string\)\) | 类似于index\(\)，不过是从右边开始 |
| replace\(old, new \[, max\]\) | 把 将字符串中的str1替换成str2,如果 max 指定，则替换不超过 max 次。 |
| split\(str="", num=string.count\(str\)\) | num=string.count\(str\)\) 以 str 为分隔符截取字符串，如果 num 有指定值，则仅截取 num 个子字符串 |
| splitlines\(\[keepends\]\) | 按照行\('\r', '\r\n', \n'\)分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。 |
| join\(seq\) | 以指定字符串作为分隔符，将 seq 中所有的元素\(的字符串表示\)合并为一个新的字符串 |
| max\(str\) | 返回字符串str中最大的字母。 |
| min\(str\) | 返回字符串str中最小的字母。 |
| isalnum\(\) | 如果字符串至少有一个字符并且所有字符都是字母或数字则返 回True,否则返回False |
| isalpha\(\) | 如果字符串至少有一个字符并且所有字符都是字母则返回True, 否则返回 False |
| isdigit\(\) | 如果字符串只包含数字则返回True，否则返回False |
| isnumeric\(\) | 如果字符串中只包含数字字符，则返回True，否则返回 False |
| isdecimal\(\) | 检查字符串是否只包含十进制字符，如果是返回true，否则返回false。 |
| isspace\(\) | 如果字符串中只包含空白，则返回True，否则返回False |
| maketrans\(\) | 创建字符映射的转换表。第一个参数是字符串，表示需要转换的字符，第二个参数是字符串，表示转换的目标。 |
| translate\(table, deletechars=""\) | 根据str给出的表\(包含256个字符\)转换string的字符, 要过滤掉的字符放到deletechars参数中 |
| expandtabs\(tabsize=8\) | 把字符串string中的tab符号转为空格，tab符号默认的空格数是8。 |



