from typing import Any 

class FixedQueue:
    class Empty(Exception):
        # 비어있을 때 dequeue 또는 peak할 때 내보내는 예외처리
        pass
    
    class Full(Exception):
        # 가득 차 있을때 inqueue할 때 내보내는 예외처리
        pass
    
    def __init__(self, capa: int) -> None:
        self.no = 0 # number of current data
        self.front = 0 # cursor of front element
        self.rear = 0 # cursor of back element
        self.capa = capa # size of queue
        self.que = [None] * capa # entity of queue
        
    def __len__(self) -> int:
        # return the number of all data in the queue
        return self.no
    
    def is_empty(self) -> bool:
        # check the empty in the queue 
        return self.no <= 0
    
    def is_full(self) -> bool:
        # check the full in the full
        return self.no >= self.capa
    
    def enque(self, x:Any) -> Any:
        # if full in the queue, try the exception
        if self.is_full():
            raise FixedQueue.Full
        self.que[self.rear] = x
        self.rear += 1
        self.no += 1
        # if same rear with capa, return rear index to 0(in-front of index) 
        if self.rear == self.capa:
            self.rear = 0
            
    def dequeue(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        x = self.que[self.front]
        self.front += 1 
        self.no -= 1
        # if same front with capa, return front index to 0(in-front of index) 
        if self.front == self.capa:
            self.front = 0
        return x 
    
    def peek(self) -> Any:
        if self.is_empty():
            raise FixedQueue.Empty
        return self.que[self.front]
    
    def find(self, value: Any) -> Any:
        for i in range(self.no):
            idx = (i + self.front) % self.capa
            if self.que[idx] == value:
                return idx
        return -1
    
    def count(self, value: Any) -> bool:
        c=0
        for i in range(self.no):
            idx = (i+self.front) % self.capa
            if self.que[idx] == value:
                c+=1
        return c
    