### setuptools

作为Python标准的打包及分发工具，setuptools可以说相当地简单易用。只需写一个简短的setup.py安装文件，就可以将Python应用打包。

###### 1、第一个安装文件
接下来编写安装文件，假设项目名为setup-demo，包名为myapp，目录结构如下：

```python
setup-demo/
  ├ setup.py         # 安装文件
  └ myapp/           # 源代码
      ├ __init__.py
```

一个最基本的setup.py文件如下：

```python
from setuptools import setup

setup(
    name='MyApp',         # 应用名
    version='1.0',        # 版本号
    packages=['myapp']    # 包括在安装包内的Python包
)
```

###### 2、执行安装文件
有了上面的setup.py文件，就可以打各种包，也可以将应用安装在本地Python环境中。

1）创建egg包

```python
$ python setup.py bdist_egg
```

该命令会在当前目录下的”dist”目录内创建一个egg文件，名为”MyApp-1.0-py2.7.egg”。
文件名格式就是”应用名-版本号-Python版本.egg”，我本地Python版本是2.7。
同时你会注意到，当前目录多了”build”和”MyApp.egg-info”子目录来存放打包的中间结果。

2）创建tar.gz包

```python
$ python setup.py sdist --formats=gztar
```

同上例类似，只不过创建的文件类型是tar.gz，文件名为”MyApp-1.0.tar.gz”。

3）安装应用

```python
$ python setup.py install
```

该命令会将当前的Python应用安装到当前Python环境的”site-packages”目录下，这样其他程序就可以像导入标准库一样导入该应用的代码。

4）开发方式安装

```python
$ python setup.py develop
```

如果应用在开发过程中会频繁变更，每次安装还需要先将原来的版本卸掉，很麻烦。
使用”develop”开发方式安装的话，应用代码不会真的被拷贝到本地Python环境的”site-packages”目录下，而是在”site-packages”目录里创建一个指向当前应用位置的链接。
这样如果当前位置的源码被改动，就会马上反映到”site-packages”里。

###### 3、引入非Python文件
上例中，我们只会将”myapp”包下的源码打包，如果我们还想将其他非Python文件也打包，比如静态文件（JS，CSS，图片），应该怎么做呢？
这时我们要在项目目录下添加一个”MANIFEST.in”文件夹。假设我们把所有静态文件都放在”static”子目录下，现在的项目结构如下：

```python
setup-demo/
  ├ setup.py         # 安装文件
  ├ MANIFEST.in      # 清单文件
  └ myapp/           # 源代码
      ├ static/      # 静态文件目录
      ├ __init__.py
      ...
```

我们在清单文件”MANIFEST.in”中，列出想要在包内引入的目录路径：

```python
recursive-include myapp/static *
recursive-include myapp/xxx *
```

“recursive-include”表明包含子目录。还有一件事要做，就是在”setup.py”中将” include_package_data”参数设为True：

```python
#coding:utf8
from setuptools import setup

setup(
    name='MyApp',         # 应用名
    version='1.0',        # 版本号
    packages=['myapp'],   # 包括在安装包内的Python包
    include_package_data=True    # 启用清单文件MANIFEST.in
)
```

之后再次打包或者安装，”myapp/static”目录下的所有文件都会被包含在内。如果你想排除一部分文件，可以在setup.py中使用”exclude_package_date”参数，比如：

```python
setup(
    ...
    include_package_data=True,    # 启用清单文件MANIFEST.in
    exclude_package_date={'':['.gitignore']}
)
```

上面的代码会将所有”.gitignore”文件排除在包外。
如果上述”exclude_package_date”对象属性不为空，比如”{‘myapp’:[‘.gitignore’]}”，就表明只排除”myapp”包下的所有”.gitignore”文件。

###### 4、自动安装依赖
我们的应用会依赖于第三方的Python包，虽然可以在说明文件中要求用户提前安装依赖包，但毕竟很麻烦，用户还有可能装错版本。
其实我们可以在setup.py文件中指定依赖包，然后在使用setuptools安装应用时，依赖包的相应版本就会被自动安装。
让我们来修改上例中的setup.py文件，加入”install_requires”参数：

```python
from setuptools import setup

setup(
    name='MyApp',         # 应用名
    version='1.0',        # 版本号
    packages=['myapp'],   # 包括在安装包内的Python包
    include_package_data=True,    # 启用清单文件MANIFEST.in
    exclude_package_date={'':['.gitignore']},
    install_requires=[    # 依赖列表
        'Flask>=0.10',
        'Flask-SQLAlchemy>=1.5,<=2.1'
    ]
)
```

上面的代码中，我们声明了应用依赖Flask 0.10及以上版本，和Flask-SQLAlchemy 1.5及以上、2.1及以下版本。
setuptools会先检查本地有没有符合要求的依赖包，如果没有的话，就会从PyPI中获得一个符合条件的最新的包安装到本地。

如果应用依赖的包无法从PyPI中获取怎么办，我们需要指定其下载路径：

```python
setup(
    ...
    install_requires=[    # 依赖列表
        'Flask>=0.10',
        'Flask-SQLAlchemy>=1.5,<=2.1'
    ],
    dependency_links=[    # 依赖包下载路径
        'http://example.com/dependency.tar.gz'
    ]
)
```

路径应指向一个egg包或tar.gz包，也可以是个包含下载地址（一个egg包或tar.gz包）的页面。个人建议直接指向文件。

###### 5、自动搜索Python包
之前我们在setup.py中指定了”packages=[‘myapp’]”，说明将Python包”myapp”下的源码打包。如果我们的应用很大，Python包很多怎么办。
大家看到这个参数是一个列表，我们当然可以将所有的源码包都列在里面，但肯定很多人觉得这样做很傻。
的确，setuptools提供了”find_packages()”方法来自动搜索可以引入的Python包：

```python
from setuptools import setup, find_packages

setup(
    name='MyApp',               # 应用名
    version='1.0',              # 版本号
    packages=find_packages(),   # 包括在安装包内的Python包
    include_package_data=True,   # 启用清单文件MANIFEST.in
    exclude_package_date={'':['.gitignore']},
    install_requires=[          # 依赖列表
        'Flask>=0.10',
        'Flask-SQLAlchemy>=1.5,<=2.1'
    ]
)
```

这样当前项目内所有的Python包都会自动被搜索到并引入到打好的包内。
”find_packages()”方法可以限定你要搜索的路径，比如使用”find_packages(‘src’)”就表明只在”src”子目录下搜索所有的Python包。

###### 6、补充
1）zip_safe参数
决定应用是否作为一个zip压缩后的egg文件安装在当前Python环境中，还是作为一个以.egg结尾的目录安装在当前环境中。
因为有些工具不支持zip压缩文件，而且压缩后的包也不方便调试，所以建议将其设为False：”zip_safe=False”。

2）描述信息
部分参数提供了更多当前应用的细节信息，对打包安装并无任何影响，比如：

```python
setup(
    ...
    author = "Billy He",
    author_email = "billy@bjhee.com",
    description = "This is a sample package",
    license = "MIT",
    keywords = "hello world example",
    url = "http://example.com/HelloWorld/",   # 项目主页
    long_description=__doc__,   # 从代码中获取文档注释
)
```


