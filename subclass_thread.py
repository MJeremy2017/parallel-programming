from threading import Thread
import time


class MyThread(Thread):
    def __init__(self, name, counter):
        super().__init__(daemon=False)
        self.name = name
        self.counter = counter

    def run(self):
        print("Running", self.name, "\n")
        for i in range(self.counter):
            time.sleep(0.5)
            print(self.name, i)
        print("Exiting", self.name)


if __name__ == "__main__":
    th1 = MyThread("th1", 2)
    th2 = MyThread("th2", 3)

    th1.start()
    th2.start()

    th1.join()
    th2.join()
