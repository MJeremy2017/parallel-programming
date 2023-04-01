import threading

"""
Since the lock used is an RLock, the same thread can acquire the lock again without blocking, 
allowing _increment_helper to modify the value without causing a deadlock.
"""


class Counter:
    def __init__(self):
        # if it is Lock(), then it will be blocked
        self.lock = threading.RLock()
        self.value = 0

    def increment(self):
        with self.lock:
            self.value += 1
            self._increment_helper()

    def _increment_helper(self):
        with self.lock:
            self.value += 1


if __name__ == '__main__':
    c = Counter()
    c.increment()
    print(c.value)
