import concurrent.futures
import time


def evaluate(item):
    i = 0
    for _ in range(10000000):
        i += 1
    print("result", i * item)


if __name__ == '__main__':
    A = list(range(10))
    start_time = time.time()
    for item in A:
        evaluate(item)
    print("Sequential execution in " + str(time.time() - start_time), "seconds")

    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        for item in A:
            executor.submit(evaluate, item)
    print("Thread pool execution in " + str(time.time() - start_time), "seconds")

    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=5) as executor:
        for item in A:
            executor.submit(evaluate, item)
    print("Process pool execution in " + str(time.time() - start_time), "seconds")
