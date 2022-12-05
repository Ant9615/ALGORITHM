
import sys

class Queue:
    # initialize list of queue
    def __init__(self):
        self.queues = []
    
    # push
    def push(self,num):
        self.queues.append(num)
    
    # if don`t have components return -1, otherwise delete last component and return
    def pop(self):
        if len(self.queues) == 0:
            return -1
        res = self.queues[0]
        del self.queues[0]
        return res
    
    # size of queue list
    def size(self): 
        return len(self.queues)
    
    # if queue list is empty return 1, otherwise return 0
    def empty(self):
        if len(self.queues) == 0:
            return 1
        else: 
            return 0
    
    # if queue list is empty return -1, otherwise return first component in queue list
    def front(self):
        if len(self.queues) == 0:
            return -1
        else:
            return self.queues[0]
    
    # if queue list is empty return -1, otherwise return last component in queue list
    def back(self):
        if len(self.queues) == 0:
            return -1
        else: 
            return self.queues[-1]
        


n = int(sys.stdin.readline())

queues = Queue()

for _ in range(n):
    word = sys.stdin.readline().split()
    ord = word[0]
    
    if ord == 'push':
        val = word[1]
        queues.push(val)
    
    elif ord == 'pop':
        print(queues.pop())
        
    elif ord == 'size':
        print(queues.size())
        
    elif ord == 'empty':
        print(queues.empty())
        
    elif ord == 'front':
        print(queues.front())
    
    elif ord == 'back':
        print(queues.back())
    
    else: 
        print("unacceptable")