import add_task

if __name__ == '__main__':
    # submit the tasks
    result = add_task.add.delay(5, 5)
    print("got result", result.get())
