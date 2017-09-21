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
