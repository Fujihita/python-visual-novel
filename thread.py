from threading import Timer
from time import sleep

flag = True

def hello():
    global flag
    flag = False

t = Timer(5.0, hello)
t.start()  # after 30 seconds, "hello, world" will be printed
while flag:
    print(flag)
    sleep(1.0)