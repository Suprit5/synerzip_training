from time import sleep
from threading import *

class A(Thread):
    def run(self):
        for i in range(8):
            print('line 1')
            sleep(1)

class B(Thread):
    def run(self):
        for i in range(8):
            print('line 2')
            sleep(1)

task1=A()
task2=B()

task1.start()
sleep(0.2)
task2.start()

task1.join()
task2.join()
print('Bye')