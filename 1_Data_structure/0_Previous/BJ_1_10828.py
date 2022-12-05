#  https://alpyrithm.tistory.com/38 <- 클래스 부분 보기

import sys

# for stack
class Stck:
    # initalizes the list of stack
    def __init__(self):
        self.stack = []
    
    # push
    def push(slef, num):
        slef.stack.append(num)
        
    # pop
    def pop(self):
        if len(self.stack) == 0:
            return -1
        
        res = self.stack[-1]
        del self.stack[-1]
        return res
    
    # size of stack list
    def size(self): 
        return len(self.stack)
    
    # if list of stack is empty return 1, otherwise return 0
    def empty(self):
        if len(self.stack) == 0:
            return 1
        else: 
            return 0
    
    # if list of stack is empty return -1 and otherwise return last component in stack list
    def top(self):
        if len(self.stack) == 0:
            return -1
        else:
            return self.stack[-1]
        

n = int(sys.stdin.readline())

stacks = Stck()

for _ in range(n):
    word = sys.stdin.readline().split()
    ord = word[0]
    
    if ord == 'push':
        val = word[1]
        stacks.push(val)
    
    elif ord == 'pop':
        print(stacks.pop())
    
    elif ord == 'size':
        print(stacks.size())
        
    elif ord == 'empty':
        print(stacks.empty())
    elif ord == 'top':
        print(stacks.top())
    else: 
        print("unacceptable")
        
