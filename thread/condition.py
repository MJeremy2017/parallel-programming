import random
import threading
import time
from threading import Thread, Condition

# by default initialize with a Rlock
condition = Condition()
q = []


class Consumer(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        tid = threading.get_ident()
        while True:
            condition.acquire()
            if len(q) == 0:
                print(tid, "no items in queue, waiting ...")
                condition.wait()
            v = q.pop(0)
            print(tid, "Consumed items:", v)
            condition.notify()
            condition.release()
            time.sleep(3)


class Producer(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            condition.acquire()
            if len(q) == 10:
                print("queue is full, waiting ...")
                condition.wait()
            v = random.randint(0, 100)
            q.append(v)
            print("Produced item:", v)
            condition.notify()
            condition.release()
            time.sleep(5)


if __name__ == '__main__':
    c1 = Consumer()
    c2 = Consumer()
    p = Producer()

    c1.start()
    c2.start()
    p.start()
