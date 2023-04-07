import random
import time
from threading import Thread, Event

q = []
event = Event()


class Consumer(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            if len(q) == 0:
                event.wait()
                continue
            v = q.pop(0)
            print(self.name, "Consumed items:", v)
            time.sleep(2)


class Producer(Thread):
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            v = random.randint(0, 100)
            q.append(v)
            print(self.name, "Produced item:", v)
            event.set()  # condition.notifyAll()
            event.clear()
            time.sleep(2)


if __name__ == '__main__':
    c1 = Consumer()
    c2 = Consumer()
    p1 = Producer()
    p2 = Producer()

    c1.start()
    c2.start()
    p1.start()
    p2.start()
