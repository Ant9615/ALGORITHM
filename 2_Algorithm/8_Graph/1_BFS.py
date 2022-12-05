'''
if start node is no.3, search all adjacent nodes through start node and search to other adjacent nodes

Questions
- why use queue?
- what is dequeue?
'''

from queue import Queue


class Graph:
    def __init__(self, v_num): # v_num: number of vertices
        self.adj_list = [[] for _ in range(v_num)]
        self.visited = [False for _ in range(v_num)]
    
    # implemet to adjacency list 
    def add_edge(self, u, v): # u, v: edge from u to v
        self.adj_list[u].append(v) # node u to v(edge)
        self.adj_list[v].append(u) # node v to u(edge)
        
    def init_visited(self):
        for i in range(len(self.visited)):
            # visited: check the visited -> if visited eaach node, return the true othersise false
            # default is false
            self.visited[i] = False

    def bfs(self, v):
        q = Queue() # create queue
        
        self.init_visited() # initialize visited list
        q.put(v) # put first node to queue
        self.visited[v] = True # visited first node
        
        while not q.empty():
            # dequeue to visited node, why use the dequeue?
            v = q.get() 
            
            print(v, end='=')
            # visited list of adjacency node
            # adj_v is adjacency node of node v
            adj_v = self.adj_list[v]
            for u in adj_v:
                if not self.visited[u]:
                    q.put(u) 
                    self.visited[u] =True
                    