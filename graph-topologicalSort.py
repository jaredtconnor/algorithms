from  collections import defaultdict

class Graph: 
    def __init__(self, verticies):
        self.graph = defaultdict(list)
        self.vertices = verticies

    def addEdge(self, u, v): 
        self.graph[u].append(v)



def topologicalsort(graph): 

