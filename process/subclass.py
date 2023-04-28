from multiprocessing import Process


class MyProcess(Process):
    def __init__(self):
        super().__init__()

    def run(self) -> None:
        print("Running process", self.name)


if __name__ == '__main__':
    for i in range(5):
        p = MyProcess()
        p.start()
        p.join()
