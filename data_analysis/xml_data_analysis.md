### XML数据解析

XML指可扩展标记语言（eXtensible Markup Language），标准通用标记语言的子集。
XML被设计用来传输和存储数据。

python主要有三种方法解析XML:
- SAX(simple API for XML)，不会将xml数据一次性读入内存
- DOM(Document Object Model)，将xml数据一次性读入内存
- ElementTree，不会将xml数据一次性读入内存，提供更高级API

###### 1、SAX
SAX是一种基于事件驱动的API。
利用SAX解析XML文档牵涉到两个部分:解析器和事件处理器。
解析器负责读取XML文档，并向事件处理器发送事件，如元素开始、结束事件；
而事件处理器则负责对事件作出响应，对传递的XML数据进行处理。
在以下情况下可考虑使用SAX解析XML文件：
- 对大型文件进行处理；
- 只需要文件的部分内容，或者只需从文件中得到特定信息；
- 想建立自己的对象模型。

>xml.sax.handler模块中ContentHandler类方法介绍：

1) characters(content)方法

获取标签的值。标签可以是开始标签，也可以是结束标签。
- 从行开始，遇到标签之前，存在字符，content的值为这些字符串。
- 从一个标签，遇到下一个标签之前， 存在字符，content的值为这些字符串。
- 从一个标签，遇到行结束符之前，存在字符，content的值为这些字符串。

2) startDocument()方法

文档启动的时候调用。

3) endDocument()方法

解析器到达文档结尾时调用。

4) startElement(name, attrs)方法

遇到XML开始标签时调用，name是标签的名字，attrs是标签的属性值字典。

5) endElement(name)方法

遇到XML结束标签时调用。

>xml.sax模块相关方法介绍：

1) xml.sax.make_parser([parser_list])

创建一个新的解析器对象并返回，
参数说明:
- parser_list - 可选参数，解析器列表

2) xml.sax.parse(xmlfile, contenthandler[, errorhandler])

创建一个SAX解析器并解析xml文档，
参数说明:
- xmlfile - xml文件名
- contenthandler - 必须是一个ContentHandler的对象
- errorhandler - 如果指定该参数，errorhandler必须是一个SAX ErrorHandler对象

3) xml.sax.parseString(xmlstring, contenthandler[, errorhandler])

创建一个XML解析器并解析xml字符串，
参数说明:
- xmlstring - xml字符串
- contenthandler - 必须是一个ContentHandler的对象
- errorhandler - 如果指定该参数，errorhandler必须是一个SAX ErrorHandler对象

```python
from xml.sax import make_parser
from xml.sax.handler import ContentHandler, feature_namespaces

class MovieHandler(ContentHandler):
    def __init__(self):
        self.CurrentTag = ""
        self.CurrentTagValue = ''

    # 元素开始调用
    def startElement(self, name, attrs):
        self.CurrentTag = name
        if name == 'movie':
            print("*****Movie*****")
            title = attrs["title"]
            print("Title:", title)

    # 元素结束调用
    def endElement(self, name):
        if self.CurrentTag == "type":
            print("Type:", self.CurrentTagValue)
        elif self.CurrentTag == "format":
            print("Format:", self.CurrentTagValue)
        elif self.CurrentTag == "year":
            print("Year:", self.CurrentTagValue)
        elif self.CurrentTag == "rating":
            print("Rating:", self.CurrentTagValue)
        elif self.CurrentTag == "stars":
            print("Stars:", self.CurrentTagValue)
        elif self.CurrentTag == "description":
            print("Description:", self.CurrentTagValue)
        self.CurrentTag = ""

    # 读取字符调用
    def characters(self, content):
        if content:
            self.CurrentTagValue = content

if __name__ == '__main__':
    # 创建一个解析器
    parser = make_parser()
    # turn off namepsaces
    parser.setFeature(feature_namespaces, 0)

    # 重写 ContextHandler
    Handler = MovieHandler()
    parser.setContentHandler(Handler)

    parser.parse("movies.xml")
```

###### 2、DOM
一个DOM的解析器在解析一个XML文档时，一次性读取整个文档，
把文档中所有元素保存在内存中的一个树结构里，之后可以利用DOM提供的不同的函数来读取或修改文档的内容和结构，
也可以把修改过的内容写入xml文件。

```python
from xml.dom.minidom import parse
import xml.dom.minidom

# 使用minidom解析器打开 XML 文档
DOMTree = parse("movies.xml")
collection = DOMTree.documentElement
if collection.hasAttribute("shelf"):
   print ("Root element : %s" % collection.getAttribute("shelf"))

# 在集合中获取所有电影
movies = collection.getElementsByTagName("movie")

# 打印每部电影的详细信息
for movie in movies:
   print ("*****Movie*****")
   if movie.hasAttribute("title"):
      print ("Title: %s" % movie.getAttribute("title"))

   type = movie.getElementsByTagName('type')[0]
   print("Type: %s" % type.childNodes[0].data)
   format = movie.getElementsByTagName('format')[0]
   print("Format: %s" % format.childNodes[0].data)
   rating = movie.getElementsByTagName('rating')[0]
   print("Rating: %s" % rating.childNodes[0].data)
   description = movie.getElementsByTagName('description')[0]
   print("Description: %s" % description.childNodes[0].data)
```

###### 3、ElementTree
ElementTree在 Python 标准库中有两种实现。一种是纯Python实现的xml.etree.ElementTree，
另外一种是C语言实现，速度快一点的xml.etree.cElementTree。

```python
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET
```

Element类型是一种灵活的容器对象，用于在内存中存储结构化数据。
每个element对象都具有以下属性：
- tag：string对象，表示数据代表的种类。
- attrib：dictionary对象，表示附有的属性。
- text：string对象，表示element的内容。
- tail：string对象，表示element闭合之后的尾迹。
- 若干子元素（child elements）。

```python
<tag attrib1=1>text</tag>tail
  1     2        3         4
```

参考：

- [Python官网文档](https://docs.python.org/2/library/xml.etree.elementtree.html)


