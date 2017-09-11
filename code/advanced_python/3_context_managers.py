from contextlib import contextmanager


class File(object):
    """
    用类实现上下文管理器
    """

    # 用固定集合来分配空间，避免随意增加属性
    __slots__ = ['file_obj']

    def __init__(self, file_name, mode):
        self.file_obj = open(file_name, mode, encoding='utf-8')

    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        if type or value or traceback:
            print(type, value, traceback)
        self.file_obj.close()
        return True


@contextmanager
def open_file(file_name, mode):
    """
    用生成器实现的上下文管理器

    :param file_name: 文件名
    :param mode: 读写模式
    :return:
    """
    file = None

    try:
        file = open(file_name, mode, encoding='utf-8')
        yield file
    except Exception as e:
        print(repr(e))
    finally:
        if file:
            file.close()


if __name__ == '__main__':
    # with File('demo.text', 'w') as opened_file:
    # opened_file.write('{}{}'.format('hello', '用类实现上下文管理器'))
    # opened_file.undefined_function('hello')

    with open_file('demo1.text', 'w') as opened_file:
        opened_file.write('{}{}'.format('hello', '用生成器实现的上下文管理器'))
        # opened_file.undefined_function('hello')
