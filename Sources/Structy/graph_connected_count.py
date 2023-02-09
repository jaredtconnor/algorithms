import unittest


def connected_components_count(graph):

    visited = set()

    count = 0
    for node in graph:
        if explore(graph, node, visited) is True:
            count += 1

    return count


def explore(graph, current, visited):

    if current in visited:
        return False

    visited.add(current)

    for neighbor in graph[current]:
        explore(graph, neighbor, visited)

    # Only returns true if node never
    # visited
    return True


class Test(unittest.TestCase):
    def test_case_1(self):

        res = connected_components_count(
            {
                0: [8, 1, 5],
                1: [0],
                5: [0, 8],
                8: [0, 5],
                2: [3, 4],
                3: [2, 4],
                4: [3, 2],
            }
        )  # -> 2

        expected = 2
        assert res == expected

    def test_case_2(self):

        res = connected_components_count(
            {1: [2], 2: [1, 8], 6: [7], 9: [8], 7: [6, 8], 8: [9, 7, 2]}
        )  # -> 1

        expected = 1
        assert res == expected

    def test_case_3(self):

        res = connected_components_count(
            {3: [], 4: [6], 6: [4, 5, 7, 8], 8: [6], 7: [6], 5: [6], 1: [2], 2: [1]}
        )  # -> 3

        expected = 3
        assert res == expected

    def test_case_4(self):

        res = connected_components_count({})
        # -> 0

        expected = 0
        assert res == expected

    def test_case_5(self):

        res = connected_components_count(
            {0: [4, 7], 1: [], 2: [], 3: [6], 4: [0], 6: [3], 7: [0], 8: []}
        )
        # -> 5
        expected = 5
        assert res == expected


if __name__ == "__main__":
    unittest.main()
