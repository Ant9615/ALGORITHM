'''
reference
https://velog.io/@ash3767/python-Data-Structure

Tree
+ don`t have recurrent structures
+ don`t linking node with linked node
'''

# implement tree

# general form

# class Node: 
#     def __init__(self, data):
#         self.left = None # point to left child node
#         self.right = None # point to right child node
#         self.data = data # save data 
    
#     def print_tree(self):
#         print(f'root: {self.data}')
        
# root = Node(10)
# root.print_tree()


# implement insert
'''
insert: compare with parent node and insert to left or right
'''

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
    def insert_node(self, data):
        if self.data: 
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else: 
                    self.left.insert_node(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else: 
                    self.right.insert_node(data)
        else: 
            self.data = data
            
    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data)
        if self.right:
            self.right.print_tree()        
            
root = Node(10)
root.insert_node(8)
root.insert_node(11)
root.insert_node(3)

root.print_tree()
            