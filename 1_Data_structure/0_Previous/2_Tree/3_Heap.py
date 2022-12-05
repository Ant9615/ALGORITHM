'''
<<Previous summerized>>
Property of Heap
+ complete binary tree
    + tree의 구성이 모두 binary tree로 구성되어 있음

+ component value의 대소 관계는 오로지 parent node와 child node 간에만 성립
    + sibling에는 대소관계가 없음

+ 가장 높은 또는 낮은 priority를 가지는 node가 항상 root node에 오게 되는 특징이 있음
    + priority queue와 같은 추상적인 structure를 구현할 수 있음

+ max heap: parent node의 key value가 child node의 key value보다 항상 큼
+ min heap: max heap의 반대(child node의 key value보다 항상 작음)

+ time complexity: O(log n)
    + component의 insert나 delete가 일어날 때 전체 component의 반만큼의 값과 비교
    
Example
input: natural number x
output: return maximum and delete it
* initialize none list
----------------------------------------------------------------

Heap
+ based on complete binary serch tree that find maximum or minimum quickly
+ max heap: key of parent > key of child
+ min heap: key of parent < key of child
    + not compare with sibling
+ in heap property, the higher priority of node is located in root
-> it can implement to priority queue
+ time complexity
    + insert, delete: O(log n)

Reference
https://daimhada.tistory.com/108

change code refer to
https://velog.io/@gnwjd309/python-heap 
https://data-newbie.tistory.com/846 
'''

# max heap
class MaxHeap:
    def __init__(self):
        self.queue = []
            
    def insert(self, n):
        # add preliminary component for insert to last
        self.queue.append(n)
        last_ind = len(self.queue)-1
        
        # compare with nodes while go to the parent
        while 0 <= last_ind:
            parent_ind = self.parent(last_ind)
            if 0 <= parent_ind and self.queue[parent_ind] < self.queue[last_ind]:
                self.swap(last_ind, parent_ind)
                last_ind = parent_ind
            else:
                break
    
    def delete(self):
        last_ind = len(self.queue)-1
        if last_ind < 0: 
            return -1
        self.swap(0,last_ind)
        maxv = self.queue.pop()
        self.maxheapify(0) # restoring from the root
        print(maxv)
        return maxv
    
    # the function to restore while compare with child from preliminary root
    def maxheapify(self, i):
        left_ind = self.leftchild(i)
        right_ind = self.rightchild(i)
        max_ind = i
        
        if left_ind <= len(self.queue)-1 and self.queue[max_ind] < self.queue[left_ind]:
            max_ind = left_ind
        if right_ind <= len(self.queue)-1 and self.queue[max_ind] < self.queue[right_ind]:
            max_ind = right_ind
            
        if max_ind != i:
            self.swap(i, max_ind)
            self.maxheapify(max_ind)
    
    def parent(self, index):
        return (index-1)//2

    def leftchild(slef, index):
        return index*2+1        
        
    def rightchild(self, index):
        return index*2+2
    
    def swap(self, i, parent_ind):
        self.queue[i] = self.queue[parent_ind] = self.queue[parent_ind], self.queue[i]
   
    def printHeap(self):
        print(self.queue)


if __name__ == "__main__":
    mh = MaxHeap()
    mh.insert(5)
    mh.insert(8)
    mh.insert(11)
    mh.insert(3)
    mh.insert(2)
    mh.insert(9)
    mh.printHeap()
    mh.delete()
    mh.printHeap()
    mh.delete()
    mh.printHeap()
    mh.delete()
    mh.printHeap()
    mh.delete()
    mh.printHeap()
    mh.delete()
    mh.printHeap()
    mh.delete()
        
        