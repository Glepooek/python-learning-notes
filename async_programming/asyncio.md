### 异步IO（```asyncio```）

>参考文章：
- [Python黑魔法---异步IO（asyncio）协程](http://python.jobbole.com/87310/)
- [还在疑惑并发和并行?](https://laike9m.com/blog/huan-zai-yi-huo-bing-fa-he-bing-xing,61/)
- [全局解释器锁](https://zh.wikipedia.org/wiki/%E5%85%A8%E5%B1%80%E8%A7%A3%E9%87%8A%E5%99%A8%E9%94%81)

asyncio的相关概念：
- coroutine 协程：协程对象，指一个使用async关键字定义的函数，它的调用不会立即执行函数，
而是会返回一个协程对象。协程对象需要注册到事件循环，由事件循环调用。
- event_loop 事件循环：程序开启一个无限的循环，调用run_until_complete把一些协程函数注册到事件循环上。
当满足事件发生的时候，调用相应的协程函数。
- task 任务：一个协程对象就是一个原生可以挂起的函数，任务则是对协程进一步封装，其中包含任务的各种状态。
- future： 代表将来执行或没有执行的任务的结果。它和task上没有本质的区别
- async/await 关键字：python3.5 用于定义协程的关键字，async定义一个协程，await用于挂起阻塞的异步调用接口。

###### 1、定义一个协程
通过async关键字定义一个协程（coroutine），协程也是一种对象。协程不能直接运行，
需要把协程注册到事件循环（loop），由后者在适当的时候调用协程。
asyncio.get_event_loop方法可以创建一个事件循环，然后使用run_until_complete将协程注册到事件循环，
并启动事件循环。

```python
import time
import asyncio

now = lambda: time.time()

async def do_some_work(x):
    print('Waiting: ', x)

if __name__ == '__main__':
    start = now()
    coroutine = do_some_work(2)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(coroutine)
    print('TIME: ', now() - start)
```

###### 2、定义一个任务
协程对象不能直接运行，在注册事件循环的时候，其实是run_until_complete方法将协程包装成为了一个任务
（task）对象。所谓task对象是Future类的子类，保存了协程运行后的状态，用于未来获取协程的结果。

```python
import time
import asyncio

now = lambda: time.time()

async def do_some_work(x):
    print('Waiting: ', x)

if __name__ == '__main__':
    start = now()

    coroutine = do_some_work(2)
    loop = asyncio.get_event_loop()
    # task = asyncio.ensure_future(coroutine, loop=loop)
    task = loop.create_task(coroutine)

    print(task)
    loop.run_until_complete(task)
    print(task)
    print('TIME: ', now() - start)

# 输出结果
<Task pending coro=<do_some_work() running at E:\PycharmProjects\python-gitbook\code\async_programming\2_asyncio.py:7>>
Waiting:  2
<Task finished coro=<do_some_work() done, defined at E:\PycharmProjects\python-gitbook\code\async_programming\2_asyncio.py:7> result=None>
TIME:  0.0029735565185546875
```

###### 3、为任务绑定回调
绑定回调，在task执行完毕的时候可以获取执行的结果，回调的```最后一个参数```是future对象，
通过该对象可以获取协程返回值。如果回调需要多个参数，可以通过偏函数导入。

```python
import time
import asyncio
import functools

now = lambda: time.time()

async def do_some_work(x):
    print('Waiting: ', x)
    return 'Done after {}s'.format(x)

def callback(t,future):
    print('Callback: ', future.result())

if __name__ == '__main__':
    start = now()
    coroutine = do_some_work(2)
    loop = asyncio.get_event_loop()
    # task = asyncio.ensure_future(coroutine, loop=loop)
    task = loop.create_task(coroutine)

    # task.add_done_callback(callback)
    task.add_done_callback(functools.partial(callback, 2))

    loop.run_until_complete(task)

    print('TIME: ', now() - start)
```

回调一直是很多异步编程的恶梦，程序员更喜欢使用同步的编写方式写异步代码，以避免回调的恶梦。
回调中使用了future对象的result方法。在前面不绑定回调的例子中，可以看到task有fiinished状态。
在那个时候，可以直接调用task的result方法获取返回结果。

```python
import time
import asyncio

now = lambda: time.time()

async def do_some_work(x):
    print('Waiting: ', x)
    return 'Done after {}s'.format(x)

if __name__ == '__main__':
    start = now()
    coroutine = do_some_work(2)
    loop = asyncio.get_event_loop()
    # task = asyncio.ensure_future(coroutine, loop=loop)
    task = loop.create_task(coroutine)

    loop.run_until_complete(task)

    print(task.result())
    print('TIME: ', now() - start)
```

###### 4、阻塞和await
使用async可以定义协程对象，使用await可以针对耗时的操作进行挂起，就像生成器里的yield一样，
函数让出控制权。协程遇到await，事件循环将会挂起该协程，执行别的协程，
直到其他的协程也挂起或者执行完毕，再进行下一个协程的执行。协程的目的也是让这些IO操作异步化。
耗时的操作一般是一些IO操作，例如网络请求，文件读取等。下面使用asyncio.sleep函数来模拟IO操作。

```python
import time
import asyncio

now = lambda: time.time()

async def do_some_work(x):
    print('Waiting: ', x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)


if __name__ == '__main__':
    start = now()
    coroutine = do_some_work(4)
    loop = asyncio.get_event_loop()
    task = loop.create_task(coroutine)
    loop.run_until_complete(task)

    print(task.result())
    print('TIME: ', now() - start)
```

###### 5、并发和并行
asyncio实现并发，就需要多个协程来完成任务，每当有任务阻塞的时候就await，
然后其他协程继续工作。创建多个协程的列表，然后将这些协程注册到事件循环中。

```python
import time
import asyncio
import functools

now = lambda: time.time()

async def do_some_work(x):
    print('Waiting: ', x)
    await asyncio.sleep(x)
    return 'Done after {}s'.format(x)

if __name__ == '__main__':
    start = now()
    coroutine1 = do_some_work(1)
    coroutine2 = do_some_work(2)
    coroutine3 = do_some_work(4)

    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(coroutine1),
             loop.create_task(coroutine2),
             loop.create_task(coroutine3)]

    loop.run_until_complete(asyncio.gather(*tasks))
    # loop.run_until_complete(asyncio.wait(tasks))

    for task in tasks:
        print(task.result())
    print('TIME: ', now() - start)

# 输出结果
Waiting:  1
Waiting:  2
Waiting:  4
Done after 1s
Done after 2s
Done after 4s
TIME:  4.00682520866394
```

###### 6、协程嵌套
