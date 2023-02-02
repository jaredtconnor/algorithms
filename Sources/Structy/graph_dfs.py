def depth_first_search(graph, start):

    stack = [start]

    while len(stack) > 0:

        current = stack[-1]
        print(current)
        stack.pop()

        for neighbor in graph[current]:
            stack.append(neighbor)


def depth_first_search_recursive(graph, current):

    print(current)

    # implicit base case
    for neighbor in graph[current]:

        depth_first_search_recursive(graph, neighbor)


if __name__ == "__main__":
    #    unittest.main()

    graph = {"a": ["b", "c"], "b": ["d"], "c": ["e"], "d": ["f"], "e": [], "f": []}

    print(f"----- Depth First Search -----")
    depth_first_search(graph, "a")

    print(f"\n----- Depth First Search Recursive -----")
    depth_first_search_recursive(graph, "a")
