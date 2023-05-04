"""
Manage shared objects
"""

import multiprocessing


def worker(d, key, value):
    d[key] = value


if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    dct = mgr.dict()
    jobs = [multiprocessing.Process(target=worker, args=(dct, i, 2 * i)) for i in range(10)]
    for j in jobs:
        j.start()

    for j in jobs:
        j.join()

    print(dct)
