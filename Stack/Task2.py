from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()
    
    def push(self, no):
        self.container.append(no)
    
    def pop(self):
        return self.container.pop() if not self.is_empty() else None
    
    def peek(self):
        return self.container[-1] if not self.is_empty() else None
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)

def is_match(c1, c2):
    match_dic = {
        '(': ')',
        '{': '}',
        '[': ']'
    }
    return match_dic.get(c1) == c2

def is_balanced(s):
    stack = Stack()
    for c in s:
        if c in "({[":
            stack.push(c)
        elif c in ")}]":
            if stack.size() == 0:
                return False
            if not is_match(stack.pop(), c):
                return False
    return stack.size() == 0

if __name__ == '__main__':
    print(is_balanced("({a+b})"))
    print(is_balanced("))((a+b}{"))
    print(is_balanced("((a+b))"))
    print(is_balanced("((a+g))"))
    print(is_balanced("))"))
    print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))