class WDG:
    def __init__(self, edges, n):
        # represent to list of adjacency(generate size of n list)
        self.adjlist = [None] * n
        
        # allocate memory about adjacency list(about each component)
        for i in range(n):
            self.adjlist[i]=[]
        
        # add edges to directed graph
        for (src,dest,weight) in edges:
            # allocate node in adjacency list src to dest
            self.adjlist[src].append((dest,weight))
            
def printgraph(graph):
    for src in range(len(graph.adjlist)):
        for (dest,weight) in graph.adjlist[src]:
            print(f'({src} -> {dest},{weight})', end=' ')
        print()
        
if __name__ == '__main__':
    # input: edge of weighted and binary graph 
    # (src, dest, weight) -> src to dest is weight
    edges = [(0, 1, 6), (1, 2, 7), (2, 0, 5), (2, 1, 4), (3, 2, 10),
            (4, 5, 1), (5, 4, 3)]
    
    # number of node
    n = 6
    
    graph = WDG(edges, n)
    
    printgraph(graph)