"""
Await allows the program to continue executing other `tasks`
while waiting for the awaited coroutine or function to complete.
"""

import asyncio


async def coroutine1():
    print("Coroutine 1: Hello")
    await asyncio.sleep(1)
    print("Coroutine 1: World")


async def coroutine2():
    print("Coroutine 2: Start")
    await asyncio.sleep(2)
    print("Coroutine 2: End")


async def main():
    task1 = asyncio.create_task(coroutine1())
    task2 = asyncio.create_task(coroutine2())

    await task1
    await task2
    print("Ended")


if __name__ == '__main__':
    asyncio.run(main())
