import threading
import time

shared_resource_with_lock = 0
shared_resource_without_lock = 0
N = 100000
lock = threading.Lock()


def lock_increment():
    global shared_resource_with_lock
    for i in range(N):
        lock.acquire()
        shared_resource_with_lock += 1
        lock.release()
    time.sleep(1)
    print("done lock incrementing")


def lock_decrement():
    global shared_resource_with_lock
    for i in range(N):
        lock.acquire()
        shared_resource_with_lock -= 1
        lock.release()
    print("done lock decrementing")


def increment():
    global shared_resource_without_lock
    for i in range(N):
        shared_resource_without_lock += 1
    print("done unlock incrementing")


def decrement():
    global shared_resource_without_lock
    for i in range(N):
        shared_resource_without_lock -= 1
    print("done unlock decrementing")


if __name__ == '__main__':
    th1 = threading.Thread(target=lock_increment)
    th2 = threading.Thread(target=lock_decrement)
    th3 = threading.Thread(target=increment)
    th4 = threading.Thread(target=decrement)

    th1.start()
    th2.start()
    th3.start()
    th4.start()

    th1.join()
    th2.join()
    th3.join()
    th4.join()

    print("lock variable", shared_resource_with_lock)
    print("unlock variable", shared_resource_without_lock)
