from xml.sax import make_parser
from xml.sax.handler import ContentHandler, feature_namespaces
from xml.dom.minidom import parse
import xml.dom.minidom
import xml.etree.cElementTree as cet
from html.parser import HTMLParser


class MovieHandler(ContentHandler):
    def __init__(self):
        super(MovieHandler, self).__init__()
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


class DOMAnalysisXML(object):
    def analysis(self):
        DOMTree = xml.dom.minidom.parse("movies.xml")
        collection = DOMTree.documentElement
        if collection.hasAttribute("shelf"):
            print("Root element : %s" % collection.getAttribute("shelf"))

        # 在集合中获取所有电影
        movies = collection.getElementsByTagName("movie")

        # 打印每部电影的详细信息
        for movie in movies:
            print("*****Movie*****")
            if movie.hasAttribute("title"):
                print("Title: %s" % movie.getAttribute("title"))

            type = movie.getElementsByTagName('type')[0]
            print("Type: %s" % type.childNodes[0].data)
            format = movie.getElementsByTagName('format')[0]
            print("Format: %s" % format.childNodes[0].data)
            rating = movie.getElementsByTagName('rating')[0]
            print("Rating: %s" % rating.childNodes[0].data)
            description = movie.getElementsByTagName('description')[0]
            print("Description: %s" % description.childNodes[0].data)


if __name__ == '__main__':
    # # 创建一个解析器
    # parser = make_parser()
    # # turn off namepsaces
    # parser.setFeature(feature_namespaces, 0)
    #
    # # 重写 ContextHandler
    # Handler = MovieHandler()
    # parser.setContentHandler(Handler)

    # parser.parse("movies.xml")

    # DOMAnalysisXML().analysis()

    tree = cet.parse("movies.xml")
    root = tree.getroot()
    for child in root:
        print(child.tag)
