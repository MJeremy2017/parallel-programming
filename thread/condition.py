import random
import time
from threading import Thread, Condition

# by default initialize with a Rlock
condition = Condition()
q = []


class Consumer(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            condition.acquire()
            if len(q) == 0:
                print(self.name, "no items in queue, waiting ...")
                condition.wait()
            else:
                v = q.pop(0)
                print(self.name, "Consumed items:", v)
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
                print(self.name, ": queue is full, waiting ...")
                condition.wait()
            v = random.randint(0, 100)
            q.append(v)
            print(self.name, "Produced item:", v)
            condition.notify()
            condition.release()
            time.sleep(5)


if __name__ == '__main__':
    c1 = Consumer()
    c2 = Consumer()
    p1 = Producer()
    p2 = Producer()

    c1.start()
    c2.start()
    p1.start()
    p2.start()
