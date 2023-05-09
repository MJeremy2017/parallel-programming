"""
Await allows the program to continue executing other `tasks`
while waiting for the awaited coroutine or function to complete.
"""

import asyncio
import time


async def coroutine1(q):
    print("Coroutine 1: Hello")
    await asyncio.sleep(1)
    print("Coroutine 1: World")
    await q.put("Result from coroutine 1")


async def coroutine2():
    print("Coroutine 2: Start")
    await asyncio.sleep(2)
    print("Coroutine 2: End")


async def coroutine3(q):
    result = await q.get()
    print(f"Coroutine 3: Received `{result}`")
    await asyncio.sleep(3)
    print("Coroutine 3: Done")


async def main():
    # create task would run in async way
    q = asyncio.Queue()
    task1 = asyncio.create_task(coroutine1(q))
    task2 = asyncio.create_task(coroutine2())
    task3 = asyncio.create_task(coroutine3(q))

    await asyncio.gather(task1, task2, task3)
    print("Ended")


async def main2():
    # this will run in sequential way
    q = asyncio.Queue()
    await coroutine1(q)
    await coroutine3(q)
    await coroutine2()
    print("Ended")


if __name__ == '__main__':
    # tasks = [asyncio.Task(coroutine1()),
    #          asyncio.Task(coroutine2())]
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(asyncio.wait(tasks))
    # loop.close()
    start = time.time()
    asyncio.run(main())
    print("Time taken", time.time() - start)
