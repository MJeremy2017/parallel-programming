import asyncio
from asyncio import Future


async def total(future: Future):
    s = 0
    for i in range(100):
        s += i
    await asyncio.sleep(2)
    future.set_result(f"total got result {s}")


async def factorial(future: Future):
    s = 1
    for i in range(1, 12):
        s *= i
    await asyncio.sleep(1)
    future.set_result(f"factorial got result {s}")


def call_back(future: Future):
    result = future.result()
    print(result)


async def main():
    future1 = Future()
    future2 = Future()

    future1.add_done_callback(call_back)
    future2.add_done_callback(call_back)

    task_total = asyncio.create_task(total(future1))
    task_factorial = asyncio.create_task(factorial(future2))

    await task_total
    await task_factorial


if __name__ == '__main__':
    asyncio.run(main())
