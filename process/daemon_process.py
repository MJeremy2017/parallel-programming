import multiprocessing
import time


def foo(sec):
    print(multiprocessing.current_process().name, "started")
    time.sleep(sec)
    print(multiprocessing.current_process().name, "exited")


if __name__ == '__main__':
    start = time.time()
    p1 = multiprocessing.Process(target=foo, args=(1,), name="process-1")
    p1.daemon = True
    p1.start()

    p2 = multiprocessing.Process(target=foo, args=(3,), name="process-2")
    p2.daemon = False
    p2.start()

    print("running time", time.time() - start)
