from queue import Queue

adj = {
    'A': ['D', 'B'],
    'B': ['A', 'G', 'F'],
    'C': ['D', 'E', 'F'],
    'D': ['A', 'C', 'E'],
    'E': ['D', 'C'],
    'F': ['B', 'C'],
    'G': ['B']
    }

def Breadth_first_search(adj_list):

    visited = {}
    level = {}
    parent = {}
    traversal_output = []

    queue = Queue()

    for node in adj_list.keys():
        visited[node] = False
        parent[node] = None
        level[node] = -1

    s = "A"

    visited[s] = True
    level[s] = 0
    queue.put(s)

    while not queue.empty():

        u = queue.get()
        traversal_output.append(u)

        for v in adj_list[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                level[v] = level[u] + 1
                queue.put(v)

    return traversal_output, visited, level, parent

traversed, visited, level, parent = Breadth_first_search(adj)

v = "G"
path = []
while v is not None:
    path.append(v)
    v = parent[v]

path.reverse()
print(path)