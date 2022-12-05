# implement directed graph

class DirectGraph:
    def __init__(self, edges, n):
        # allocate memory for adjacency list
        self.adjList = [[] for _ in range(n)]
        
        # add edges to directed graph
        for (src,dest) in edges: # src is present node and dest is adjacency node from src
            # allocate src to dest from node of adjacency list
            self.adjList[src].append(dest)
            '''
            the reason adjList index 2 is [0,1]
            : linked 0 to 1, immediately. So component of index 2 mean 0 to 1, therefore, present node is 1 in index 2
            also the reason 2 in index 3, linked 1 to 2, immediately. so index 3 is 2
            
            but, the component of index 2 is [0,1]. It is number of 2 component compare with others
            : edges list의 index 2와 3의 src가 2로 self.adjList[src].append(dest)는 src가 2인 자리에 dest를 삽입
            그래서 adjList의 index 2는 [0,1]이 됨 이후 edges의 4의 component가 (3,2)로 dest 원소인 2가 삽입됨  
            '''
        # print(f'add edges to directed graph: {self.adjList}')

# print adjacency list of graph
def printGraph(graph):
    for src in range(len(graph.adjList)):
        # print present node and all adjacency nodes
        for dest in graph.adjList[src]:
            print(f'({src}->{dest})', end=' ')
        print()

'''
__name__
+ 현재 모듈의 이름을 담고있는 built-in variable
+ 직접 실행된 module의 경우 __main__이라는 값을 가짐
+ 직접 실행되지 않은 import된 모듈은 모듈의 파일명을 가지게 됨
+ 아래 if __name__ == '__main__'은 아래 코드를 직접 실행시켰을 때 실행되길 원하는 코드를 넣어주는 것임
+ 즉, c언어처럼 main function의 선언과 시작을 의미함
    + terminal에서와 같이 직접 call되어 사용될 때는 그 자체 기능을 수행, 
    + 동시에 다른 module에서 필요 함수 등을 제공
'''

if __name__ == '__main__':
    # input: edges of directed graph and number of node(n)
    edges = [(0, 1), (1, 2), (2, 0), (2, 1), (3, 2), (4, 5), (5, 4)] # (src, dest)
    n = 6 # designate label 0 to 5
    
    # consist of graph from given edge list
    graph = DirectGraph(edges,n)
    # print adjacency list of graph
    printGraph(graph)