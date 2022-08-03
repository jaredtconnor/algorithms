from  collections import defaultdict

class Graph: 
    def __init__(self, verticies):
        self.graph = defaultdict(list)
        self.verticies = verticies

    def addEdge(self, u, v): 
        self.graph[u].append(v)

def topologicalsort(graph): 

    visited = [False] * graph.verticies # Mark all verticies as not visited
    stack = []      # Our stack to store the result/output of the topological search
    
    # Call the recursive helper program to store topological sort in stack
    for current_node in range(graph.verticies): 
        if visited[current_node] == False: 
            topo_helper(graph, current_node, visited, stack)

    return stack

def topo_helper(graph, current_node, visited, result_stack): 

    # First off, mark the current node as visited
    visited[current_node] = True

    # Recursively traverse all adjacent verticies of current node
    for i in graph.graph[current_node]: 
        if visited[i] == False: 
            topo_helper(graph, i, visited, result_stack) 

    # Push current vertex onto stack
    result_stack.insert(0, current_node)


# TESTING: 
test_graph = Graph(5)
test_graph.addEdge(0, 1) 
test_graph.addEdge(0, 3) 
test_graph.addEdge(1, 2) 
test_graph.addEdge(2, 3) 
test_graph.addEdge(2, 4) 
test_graph.addEdge(3, 4) 

print("Topological sort")
print(topologicalsort(test_graph))