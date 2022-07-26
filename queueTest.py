from threading import Thread
from queue import Queue
import time

def thread1(threadname, q):
    #read variable "a" modify by thread 2
    while True:
        a = q.get() #it takes the first value from the queue, and if the queue is empty it waits for a value to be added.
        if a is None: return # Poison pill
        print(a)




def thread2(threadname, q):
    a = 0
    for _ in range(10):
        a += 1
        q.put(a)
        q.put("poop")
        time.sleep(1)
    q.put(None) # Poison pill

queue = Queue()
thread1 = Thread( target=thread1, args=("Thread-1", queue) )
thread2 = Thread( target=thread2, args=("Thread-2", queue) )

thread1.start()
thread2.start()
thread1.join()
thread2.join()
