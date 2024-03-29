import unittest


def longest_path(graph):

    distance = {}

    # Locate terminal nodes
    for node in graph:

        if len(graph[node]) == 0:
            distance[node] = 0

    for node in graph:
        traverse_distance(graph, node, distance)

    return max(distance.values())


def traverse_distance(graph, current, distance):

    if current in distance:
        return distance[current]

    max_path = 0
    for neighbor in graph[current]:
        path = traverse_distance(graph, neighbor, distance)

        if path > max_path:
            max_path = path

    distance[current] = 1 + max_path
    return distance[current]


class Test(unittest.TestCase):
    def test_case_1(self):

        graph = {"a": ["c", "b"], "b": ["c"], "c": []}

        res = longest_path(graph)  # -> 2
        expected = 2
        assert res == expected

    def test_case_2(self):

        graph = {
            "a": ["c", "b"],
            "b": ["c"],
            "c": [],
            "q": ["r"],
            "r": ["s", "u", "t"],
            "s": ["t"],
            "t": ["u"],
            "u": [],
        }

        res = longest_path(graph)  # -> 4
        expected = 4
        assert res == expected

    def test_case_3(self):

        graph = {
            "h": ["i", "j", "k"],
            "g": ["h"],
            "i": [],
            "j": [],
            "k": [],
            "x": ["y"],
            "y": [],
        }

        res = longest_path(graph)  # -> 2
        expected = 2
        assert res == expected

    def test_case_4(self):

        graph = {
            "a": ["b"],
            "b": ["c"],
            "c": [],
            "e": ["f"],
            "f": ["g"],
            "g": ["h"],
            "h": [],
        }

        res = longest_path(graph)  # -> 3
        expected = 3
        assert res == expected


if __name__ == "__main__":
    unittest.main()
