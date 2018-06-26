#coding=utf8
import threading
import time

num = 0

def sum_num(i):
    lock.acquire()
    global num
    time.sleep(1)
    num +=i
    print(num)
    lock.release()

print('%s thread start!'%(time.ctime()))

try:
    lock = threading.Lock()
    list = []
    for i in range(6):
        t = threading.Thread(target=sum_num, args=(i,))
        list.append(t)
        t.start()

    for threadinglist in list:
        threadinglist.join()

except KeyboardInterrupt as e:
    print("you stop the threading")

print('%s thread end!'%(time.ctime()))