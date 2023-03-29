from threading import Thread
from time import sleep
import sys

print(sys.implementation)


class MyThread(Thread):
    def __init__(self):
        super().__init__(daemon=False)
        self.msg = "Hello thread"

    def run(self):
        for i in range(10):
            print(self.msg)
            sleep(1)
        print("Thread Ended")


print("Process Started")
t = MyThread()
t.start()
print("Process Ended")
