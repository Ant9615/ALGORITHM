'''
push_back에 append 수정(이전엔 insert(-1,num))
'''

import sys

class Deck:
    # initialize list of deck
    def __init__(self):
        self.deck = []
    
    # add component in the 1st location in the deck
    def push_front(self, num):
        self.deck.insert(0,num)
    
    # add component in the last location in the deck
    def push_back(self, num):
        self.deck.append(num)
    
    # delete 1st component in the deck(if it has none, return -1) 
    def pop_front(self):
        if len(self.deck) == 0:
            return -1
        
        res = self.deck[0]
        del self.deck[0]
        return res 
    
    # delete last component in the deck(if it has none, return -1)
    def pop_back(self):
        if len(self.deck) == 0:
            return -1
        
        res = self.deck[-1]
        del self.deck[-1]
        return res
    
    # return the size of deck
    def size(self):
        return len(self.deck)
    
    # check the empty list
    def empty(self):
        if len(self.deck) == 0:
            return 1
        else: 
            return 0
    
    # return first component in the deck(if it has none, return -1)
    def front(self):
        if len(self.deck) == 0:
            return -1
        else: 
            return self.deck[0]
    
    # return last component in the deck(if it has none, return -1)
    def back(self):
        if len(self.deck) == 0:
            return -1
        else:
            return self.deck[-1]
        
n = int(sys.stdin.readline())

decks = Deck()

for _ in range(n):
    word = sys.stdin.readline().split()
    ord = word[0]
    
    if ord == 'push_front':
        val = word[1]
        decks.push_front(val)
        
    elif ord == 'push_back':
        val = word[1]
        decks.push_back(val)
        
    elif ord == 'pop_front':
        print(decks.pop_front())
        
    elif ord == 'pop_back':
        print(decks.pop_back())
        
    elif ord == 'size':
        print(decks.size())
        
    elif ord == 'empty':
        print(decks.empty())
        
    elif ord == 'front':
        print(decks.front())
        
    elif ord == 'back':
        print(decks.back())
    
    else:
        print('unacceptable')