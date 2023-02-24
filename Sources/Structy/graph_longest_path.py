import unittest


def longest_path(graph):

    visited = set()

    current_max = 0

    for node in graph:

        connected_node_size = size_connected(graph, node, visited)

        if connected_node_size > current_max:
            current_max = connected_node_size

    return current_max


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
