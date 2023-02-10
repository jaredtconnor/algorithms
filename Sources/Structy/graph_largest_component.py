import unittest


def largest_component(graph):

    visited = set()

    current_max = 0

    for node in graph:

        connected_node_size = size_connected(graph, node, visited, 0)

        if connected_node_size > current_max:
            current_max = connected_node_size

    return current_max


def size_connected(graph, current, visited, count):

    if current in visited:
        return count + 0

    visited.add(current)

    for neighbor in graph[current]:
        count += size_connected(graph, neighbor, visited, count)

    # Only returns true if node never
    # visited
    return 1


class Test(unittest.TestCase):
    def test_case_1(self):

        res = largest_component(
            {
                0: [8, 1, 5],
                1: [0],
                5: [0, 8],
                8: [0, 5],
                2: [3, 4],
                3: [2, 4],
                4: [3, 2],
            }
        )
        expected = 4

        assert res == expected

    def test_case_2(self):

        res = largest_component(
            {1: [2], 2: [1, 8], 6: [7], 9: [8], 7: [6, 8], 8: [9, 7, 2]}
        )

        expected = 6
        assert res == expected

    def test_case_3(self):

        res = largest_component(
            {3: [], 4: [6], 6: [4, 5, 7, 8], 8: [6], 7: [6], 5: [6], 1: [2], 2: [1]}
        )  # -> 5

        expected = 5
        assert res == expected

    def test_case_4(self):

        res = largest_component({})  # -> 0
        expected = 0
        assert res == expected

    def test_case_5(self):
        res = largest_component(
            {0: [4, 7], 1: [], 2: [], 3: [6], 4: [0], 6: [3], 7: [0], 8: []}
        )  # -> 3
        expected = 3
        assert res == expected


if __name__ == "__main__":
    unittest.main()
