### JSON数据解析

JSON (JavaScript Object Notation) 是一种轻量级的数据交换格式，是JavaScript的一个子集。
Python3 中可以使用json模块来对JSON数据进行编解码，它包含了两个函数：
- json.dumps(): 对包含JSON文档的字符串、字节、字节数组进行编码。
- json.dump():对包含JSON文档的文件进行编码。
- json.loads(): 对包含JSON文档的字符串、字节、字节数组进行解码。
- json.load():对包含JSON文档的文件进行解码。
在json的编解码过程中，python的原始类型与json类型会相互转换，具体的转化对照如下：

###### Python编码为JSON类型转换对应表：

|Python|JSON |
| :--- | :--- |
|dict|	object|
|list, tuple|array|
|str|string|
|int, float, int- & float-derived Enums| number|
|True|	true|
|False|	false|
|None|	null|

###### JSON解码为Python类型转换对应表：

|JSON  |Python|
| :--- | :--- |
|object|dict|
|array|	list|
|string	|str|
|integer| int|
|number| float|
|true| True|
|false|	False|
|null|	None|


