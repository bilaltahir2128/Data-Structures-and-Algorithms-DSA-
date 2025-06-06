import threading
import time 

from collections import deque

class Queue:
    def __init__(self):
        self.buffer=deque()

    def enqueue(self,x):
        return self.buffer.appendleft(x)
    
    def dequeue(self):
        if len(self.buffer)==0:
            print("Queue is empty.")
            return
        
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)
    
queue=Queue()

def order(orders):
    for order in orders:
        print("Placing order for :",order)
        queue.enqueue(order)
        time.sleep(0.5)

def serve():
    
    while not queue.is_empty():
        odr=queue.dequeue()
        print("Serving order:",odr)
        time.sleep(2)


if __name__=='__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1=threading.Thread(target=order,args=(orders,))
    t2=threading.Thread(target=serve)

    t1.start()
    time.sleep(1)
    t2.start()


    