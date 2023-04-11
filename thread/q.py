import random
import time
from threading import Thread
from queue import Queue
from utils import get_now


class Consumer(Thread):
    def __init__(self, queue: Queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            v = self.queue.get()
            print(get_now(), self.name, "consumed item", v)
            self.queue.task_done()  # to unblock join() method from Queue


class Producer(Thread):
    def __init__(self, queue: Queue):
        super().__init__()
        self.queue = queue

    def run(self):
        while True:
            v = random.randint(0, 100)
            self.queue.put(v)
            print(get_now(), self.name, "Produced item:", v)
            time.sleep(1)


if __name__ == '__main__':
    q = Queue()
    c1 = Consumer(q)
    c2 = Consumer(q)
    p1 = Producer(q)
    p2 = Producer(q)

    c1.start()
    c2.start()
    p1.start()
    p2.start()


