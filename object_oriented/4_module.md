### 模块

1）一个.py文件就是一个模块。
2）定义模块的目的是实现代码重用。
3）在模块中可以增加仅在当前模块使用的测试代码。
```python
def test():
    # 语句块

# 在当前模块中使用
# 在当前模块中，__name__的值为'__main__'；在导入模块中，__name__的值为模块名。
if __name__ == '__main__':
    test()
```

4）配置Python环境变量。

```python
# 执行如下代码，用于告诉解析器在那查找自己编写的模块，然后导入模块即可
import sys
sys.path.extend(['E:\PycharmProjects\python-gitbook\code'])
```
通过配置环境变量可取代以上操作。
设置环境变量时，变量名为PYTHONPATH，变量值为自己编写的模块的路径。

5）包
为了更好的组织模块，可以将其分组为包。
模块放在包中时，包就是模块所在的目录，为使Python将其作为包对待，必须包含一个名为__init__.py的文件。

6）使用dir函数包含的内容，如函数、变量、类等。
```python
import logger

logger_content = [n for n in dir(logger) if not n.startswith('_')]
print(logger_content)
```

7）__all__变量
__all__变量在模块内被定义并设置，
其定义模块的公有接口，即告诉解析器，从模块导入所有名字（from copy import *）时只能导入在__all__变量中设置的名字。

8）help()函数可以获取模块、模块中类、函数、变量的相关文档信息。也可以使用模块.__doc__获取文档。


