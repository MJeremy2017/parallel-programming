import multiprocessing
import time


def foo(i):
    print("function called in process", i)
    time.sleep(4)


if __name__ == '__main__':
    start = time.time()
    ps = []
    # starting new process has a lot overhead
    for i in range(5):
        p = multiprocessing.Process(target=foo, args=(i,))
        ps.append(p)
        p.start()

    for p in ps:
        p.join()

    print("running time", time.time() - start)
