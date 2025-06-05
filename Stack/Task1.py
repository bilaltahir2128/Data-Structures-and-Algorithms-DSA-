
from collections import deque

class Stack:

    def __init__(self):
        self.container=deque()

    def push(self,no):
        return self.container.append(no)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def size(self):
        return len(self.container)
    def reverse(self,s):
        stack=Stack()
        for c in s:
            stack.push(c)

        revstr=''
        while stack.size()!=0:
            revstr +=stack.pop()
        return revstr

def main():
    s=("We will conquere COVID-19")
    stack=Stack()
    print("Reversed String: ",stack.reverse(s))
if __name__=='__main__':
    main()
    

