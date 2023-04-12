"""
CPython GIL(Global interpreter Lock) allows only one thread to be executed at a time. So there is no advantages
to create multiple threads when the code is executed seamlessly without breaks.
"""

from threading import Thread


class ThreadsObject(Thread):
    def run(self):
        function_to_run()


class NonThreadsObject(object):
    def run(self):
        function_to_run()


def non_threaded(num_iter):
    funcs = []
    for i in range(int(num_iter)):
        funcs.append(NonThreadsObject())
    for i in funcs:
        i.run()


def threaded(num_threads):
    funcs = []
    for i in range(int(num_threads)):
        funcs.append(ThreadsObject())
    for i in funcs:
        i.start()
    for i in funcs:
        i.join()


def function_to_run():
    a, b = 0, 0
    for i in range(10000):
        a, b = b, a+b


def show_results(func_name, results):
    print("%s %4.6f seconds" % (func_name, results))


if __name__ == "__main__":
    from timeit import Timer

    repeat = 100
    number = 1  # execute the main statement `number` of times
    num_threads = [1, 2, 4, 8]
    print('Starting tests')
    for i in num_threads:
        t = Timer(f"non_threaded({i})", "from __main__ import non_threaded")
        best_result = min(t.repeat(repeat=repeat, number=number))
        show_results("non_threaded (%s iters)" % i, best_result)

        t = Timer(f"threaded({i})", "from __main__ import threaded")
        best_result = min(t.repeat(repeat=repeat, number=number))
        show_results("threaded (%s threads)" % i, best_result)

    print('Iterations complete')
