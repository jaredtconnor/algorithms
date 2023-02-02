from collections import deque


def breadth_first_search(graph, start):

    queue = deque([start])

    while len(queue) > 0:

        current = queue[0]
        print(current)

        queue.popleft()

        for neighbor in graph[current]:
            queue.append(neighbor)


if __name__ == "__main__":
    #    unittest.main()

    graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}

    breadth_first_search(graph, "a")
