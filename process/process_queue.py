import random
import time
from multiprocessing import Process, Queue


class Producer(Process):
    def __init__(self, queue: Queue):
        super().__init__()
        self.queue = queue

    def run(self) -> None:
        while True:
            item = random.randint(0, 100)
            self.queue.put(item)
            print(f"{self.name} produced {item}")
            time.sleep(1)


class Consumer(Process):
    def __init__(self, queue: Queue):
        super().__init__()
        self.queue = queue

    def run(self) -> None:
        while True:
            if not self.queue.empty():
                item = self.queue.get()
                print(f"{self.name} consumed {item}")
                time.sleep(1)


if __name__ == '__main__':
    qe = Queue()
    p = Producer(qe)
    c1 = Consumer(qe)
    c2 = Consumer(qe)

    p.start()
    c1.start()
    c2.start()

    p.join()
    c1.join()
    c2.join()
