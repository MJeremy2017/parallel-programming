"""
- Use map() when you want the main process to wait for the results and have no other tasks to perform in parallel.
- Use map_async() when you want the main process to continue executing other tasks while waiting
for the results from the worker processes


You would use apply() when you have a single task that takes a long time to complete,
and you want to offload this task to a separate process, allowing your main process
to continue executing other tasks in parallel.
"""
import multiprocessing
import time


def mirror(v):
    time.sleep(.5)
    return v


if __name__ == '__main__':
    start = time.time()
    pool = multiprocessing.Pool(4)

    results = pool.map_async(mirror, list(range(100)))
    pool.close()  # close the pool so that no new tasks can be submitted
    pool.join()  # optional
    print(results.get())
    print('time taken', time.time() - start)
