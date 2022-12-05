'''
https://velog.io/@jjaa9292/Python%EC%9E%90%EB%A3%8C%EA%B5%AC%EC%A1%B0-6.%EA%B7%B8%EB%9E%98%ED%94%84
https://daekyoulibrary.tistory.com/entry/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC%EC%9D%84-%ED%86%B5%ED%95%B4-%EA%B5%AC%ED%98%84%ED%95%9C-DFS%EC%99%80-BFS

'''


# understand mean about each code following document above 
class Graph: 
    def __init__(self, v_num):
        self.adj_list = [[] for _ in range(v_num)]
        self.visited = [False for _ in range(v_num)]
    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)
        
    def init_visited(self):
        for i in range(len(self.visited)):
            self.visited[i] = False
    
    def recursion_dfs(self,v):
        print(v, end=' ')
        self.visited[v] = True
        
        adj_v = self.adj_list[v]
        for u in adj_v:
            if not self.visited[u]:
                self.recursion_dfs(u)
        # where use this function below       
        def dfs(self,v):
            self.init_visited()
            self.recursion_dfs(v)
    
    '''implement using stack and loop''' 
    
    # def stack_loop_def(self,v): 
    #     s = Stack()
    #     self.init_visited()
        
    #     s.push(v)
    #     self.visited[v] = True
        
    #     print(v, end=' ')
        
    #     is_visited = False
        
    #     while not s.empty():
    #         is_visited = False
    #         v = s.peak()
            
    #         adj_v = self.adj_list[v]
    #         for u in adj_v:
    #             if not self.visited[u]:
    #                 s.push(u)
    #                 self.visited[u] = True
    #                 is_visited = True
    #                 break
    #     if not is_visited:
    #         s.pop()
    
    '''if didn't linking between node using recursion'''
    # def dfs_all(self):
    #     self.init_visited()
        
    #     for i in range(len(self.visited)):
    #         if not self.visited[i]:
    #             self.recursion_dfs(i)