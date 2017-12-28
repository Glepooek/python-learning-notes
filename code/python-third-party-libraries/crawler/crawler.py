import logging
import os
import re
import time
from urllib.parse import urlparse

import pdfkit
import requests
from bs4 import BeautifulSoup


class Crawler(object):
    """
    爬虫基类
    """

    html_template = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
        </head>
        <body>
        {content}
        </body>
        </html>
        """

    def __init__(self, pdf_name, start_url):
        """
        初始化
        :param pdf_name: 待保存成的pdf的名称
        :param start_url: 待解析的url，即爬虫入口
        """
        self.pdf_name = pdf_name
        self.start_url = start_url
        self.domain_name = '{uri.scheme}://{uri.netloc}'.format(uri=urlparse(start_url))

    @staticmethod
    def request(url: str, **kwargs) -> requests.Response:
        """
        网络请求
        :param url: 接受请求的url
        :return: response对象
        """
        return requests.get(url, **kwargs)

    def parse_menu(self, response):
        """
        从response对象中解析出所有目录对应的url
        :param response: response对象
        :return: 经过处理的url
        """
        raise NotImplementedError

    def parse_body(self, response):
        """
        从response对象中解析出正文
        :param response: response对象
        :return: 经过处理的html正文
        """
        raise NotImplementedError

    def parse(self):
        htmls = []
        start = time.time()

        options = {
            'page-size': 'Letter',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
            'custom-header': [
                ('Accept-Encoding', 'gzip')
            ],
            'cookie': [
                ('cookie-name1', 'cookie-value1'),
                ('cookie-name2', 'cookie-value2'),
            ],
            'outline-depth': 10,
        }

        try:
            for index, url in enumerate(self.parse_menu(self.request(self.start_url))):
                html = self.parse_body(self.request(url))
                file_name = '.'.join([str(index), 'html'])
                with open(file_name, 'wb') as file:
                    file.write(html)
                htmls.append(file_name)

            if len(htmls) > 0:
                pdfkit.from_file(htmls, '{}{}'.format(self.pdf_name, '.pdf'), options=options)
            else:
                logging.info('没有需要转换的html文件')
        except Exception as e:
            logging.error('解析错误', exc_info=True)
        finally:
            for html in htmls:
                os.remove(html)
            total_time = time.time() - start
            print('解析html并转换为pdf文件总共花费：{}秒'.format(total_time))


class LiaoxuefengCrawler(Crawler):
    def parse_menu(self, response):
        """
        从response对象中解析出所有目录对应的url
        :param response: response对象
        :return: 经过处理的url
        """

        try:
            soup = BeautifulSoup(response.content, 'html.parser')
            menu_tags = soup.find_all(class_="uk-nav uk-nav-side")

            if len(menu_tags) > 1:
                menu_tag = menu_tags[1]
                for li in menu_tag.find_all('li'):
                    url = li.a.get('href')
                    if not url.startswith('https'):
                        url = ''.join([self.domain_name, url])
                    yield url

        except Exception as e:
            logging.error('解析错误', exc_info=True)

    def parse_body(self, response):
        """
        从response对象中解析出正文
        :param response: response对象
        :return: 经过处理的html正文
        """

        try:
            soup = BeautifulSoup(response.content, 'html.parser')
            body = soup.find(class_="x-wiki-content x-main-content")

            # 在正文中插入标题
            title = soup.find('h4').get_text()
            title_tag = soup.new_tag('h1')
            title_tag.string = title
            center_tag = soup.new_tag('center')
            center_tag.insert(1, title_tag)
            body.insert(0, center_tag)

            html = str(body)
            # body中的img标签的src相对路径的改成绝对路径
            pattern = '(<img .*?src=\")(.*?)(\")'

            def func(m):
                if not m.group(2).startswith('https'):
                    return ''.join([m.group(1), self.domain_name, m.group(2), m.group(3)])
                else:
                    return ''.join([m.group(1), m.group(2), m.group(3)])

            html = re.compile(pattern).sub(func, html)
            html = self.html_template.format(content=html)
            html = html.encode('utf-8')

            return html
        except Exception as e:
            logging.error('解析错误', exc_info=True)


class LiuzhijunCrawler(Crawler):
    def parse_menu(self, response):
        """
        从response对象中解析出所有目录对应的url
        :param response: response对象
        :return: 经过处理的url
        """

        try:
            soup = BeautifulSoup(response.content, 'html.parser')
            menu_tag = soup.find(class_="container content archive")

            for h2 in menu_tag.find_all('h2'):
                dl = h2.next_sibling.next_sibling
                for dd in dl.find_all('dd'):
                    url = dd.a.get('href')
                    if not url.startswith('https'):
                        url = ''.join([self.domain_name, url])
                    yield url

        except Exception as e:
            logging.error('解析错误', exc_info=True)

    def parse_body(self, response):
        """
        从response对象中解析出正文
        :param response: response对象
        :return: 经过处理的html正文
        """

        try:
            soup = BeautifulSoup(response.content, 'html.parser')
            body = soup.find(class_="container content")

            # 在正文中插入标题
            title = soup.find(class_="header-title").get_text()
            title_tag = soup.new_tag('h1')
            title_tag.string = title
            center_tag = soup.new_tag('center')
            center_tag.insert(1, title_tag)
            body.insert(0, center_tag)

            html = str(body)
            # body中的img标签的src相对路径的改成绝对路径
            pattern = '(<img .*?src=\")(.*?)(\")'

            def func(m):
                if not m.group(2).startswith('https'):
                    if m.group(2).startswith('..'):
                        return ''.join([m.group(1), self.domain_name, m.group(2)[2:], m.group(3)])
                else:
                    return ''.join([m.group(1), m.group(2), m.group(3)])

            html = re.compile(pattern).sub(func, html)
            html = self.html_template.format(content=html)
            html = html.encode('utf-8')

            return html
        except Exception as e:
            logging.error('解析错误', exc_info=True)


if __name__ == '__main__':
    # start_url = '''https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000'''
    # crawler = LiaoxuefengCrawler('Python3教程', start_url)
    # crawler.parse()

    start_url = 'https://foofish.net/categories.html'
    crawler = LiuzhijunCrawler('Python3之禅', start_url)
    crawler.parse()
