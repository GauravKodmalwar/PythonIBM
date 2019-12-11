import threading
x = 0

def increment():
    global x
    x += 1


def thread_task(lock):
    for _ in range(100000):
        lock.acquire()
        increment()
        lock.release()

def main_task():
    global x
    x = 0

    lock = threading.Lock()

    t1 = threading.Thread(target=thread_task, args=(lock,))
    t2 = threading.Thread(target=thread_task, args=(lock,))
    #t3 = threading.Thread(target=thread_task, args=(lock,))
    #t4 = threading.Thread(target=thread_task, args=(lock,))

    # start threads
    t1.start()
    t2.start()
    #t3.start()
    #t4.start()

    # wait until threads finish their job
    #t4.join()
    t1.join()
    t2.join()
    #t3.join()

for i in range(10):
    main_task()
    print("Iteration {0}: x = {1}".format(i, x))