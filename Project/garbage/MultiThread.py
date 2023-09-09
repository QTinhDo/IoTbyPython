from threading import Thread
import time
# <name_thread> = Thread(target = <funtion>)
# <name_thread>.start()

def printName(text): 
    while True:
        print("DEVIOT")
        print(text)
        time.sleep(5)

def printAddress():
    while True:
        print("HANOI")
        time.sleep(10)

thread1 = Thread(target = printName,args=("Hello"))
thread1.start()
thread2 = Thread(target= printAddress)
thread2.start()

while True:
    print("My thread !!")
    time.sleep(1)