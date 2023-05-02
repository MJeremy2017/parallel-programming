import multiprocessing
import time


def create_items(pipe: multiprocessing.Pipe):
    sender, receiver = pipe
    for i in range(10):
        sender.send(i)
        time.sleep(.5)
    sender.send(None)
    sender.close()


def receive_items(pipe: multiprocessing.Pipe):
    sender, receiver = pipe
    while True:
        item = receiver.recv()
        if item is None:
            break
        print("received item: ", item)
    receiver.close()


if __name__ == '__main__':
    pipe1 = multiprocessing.Pipe(True)

    p1 = multiprocessing.Process(target=create_items, args=(pipe1,))
    p11 = multiprocessing.Process(target=create_items, args=(pipe1,))
    p2 = multiprocessing.Process(target=receive_items, args=(pipe1,))

    p1.start()
    p11.start()
    p2.start()
