"""
Resource protection: Semaphores can be used to protect a shared resource, such as a file or a database,
from concurrent access. By limiting the number of threads that can access the
resource at the same time, semaphores can help prevent race conditions and other concurrency-related issues.

Thread synchronization: Semaphores can be used to synchronize the execution of
multiple threads, especially in cases where one thread depends on the completion of
another thread. For example, a producer-consumer problem can be solved using a semaphore
 to coordinate the access of the producer and consumer threads to a shared buffer.

Throttling: Semaphores can be used to limit the rate at which threads can access
a particular resource. For example, a web server can use a semaphore to limit
the number of concurrent connections it accepts to avoid overwhelming the server.
"""

import threading
import random

sema = threading.Semaphore(0)
item = 0


def consumer():
    print("consumer waiting ...")
    sema.acquire()
    print("consumed item", item)


def producer():
    global item
    print("producing ...")
    item = random.randint(0, 1000)
    print("produced item", item)
    sema.release()


if __name__ == '__main__':
    for i in range(5):
        t1 = threading.Thread(target=consumer)
        t2 = threading.Thread(target=producer)

        t1.start()
        t2.start()
        t1.join()
        t2.join()

        print("done iteration", i)
