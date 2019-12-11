import threading
x = 0

def increment():
    global x
    x += 1


def thread_task():
    for _ in range(100000):
        increment()

def main_task():
    global x
    x = 0

    t1 = threading.Thread(target=thread_task)
    t2 = threading.Thread(target=thread_task)

    # start threads
    t1.start()
    t2.start()

    # wait until threads finish their job
    t1.join()
    t2.join()

for i in range(10):
    main_task()
    print("Iteration {0}: x = {1}".format(i, x))