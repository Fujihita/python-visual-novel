from threading import Timer
from time import sleep

class Test:
    def __init__(self):
        self.flag = True

    def loop(self):
        while self.flag:
            print("Slave 1", self)
            sleep(1.0)

    def stopper(self):
        print("Slave 2: STOP", self)
        self.flag = False

x = Test()
a = Timer(1.0, x.loop)
a.start()
b = Timer(3.0, x.stopper)
b.start()

y = Test()
c = Timer(2.0, y.loop)
c.start()
d = Timer(5.0, y.stopper)
d.start()