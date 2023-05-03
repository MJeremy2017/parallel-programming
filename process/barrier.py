"""
Barrier divides a program into phases as it requires all the processes to reach it before any of them proceeds
"""

import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime


def test_with_barrier(sync: Barrier, serial):
    name = multiprocessing.current_process().name
    sync.wait()
    now = time()
    with serial:
        print("process %s ----> %s" % (name, datetime.fromtimestamp(now)))


if __name__ == '__main__':
    multiprocessing.set_start_method('fork')
    synchronizer = Barrier(2)
    serializer = Lock()
    p1 = Process(name='p1 - test_with_barrier', target=test_with_barrier,
                 args=(synchronizer, serializer))
    p2 = Process(name='p2 - test_with_barrier', target=test_with_barrier,
                 args=(synchronizer, serializer))

    p1.start()
    p2.start()
