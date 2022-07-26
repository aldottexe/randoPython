from time import sleep
import threading

num = 0
def counter():
    global num
    i = 0
    while i <= 20:
        i += 1
        num = i
        sleep(1)

if __name__ == "__main__":
    c = threading.Thread(target=counter)
    c.start()
    sleep(10)
    print(num)