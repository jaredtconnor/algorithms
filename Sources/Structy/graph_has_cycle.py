import unittest


def has_cycle(graph):

    visiting = set()
    visited = set()

    for node in graph:

        if cycle_detect(graph, node, visiting, visited) is True:
            return True

    return False


def cycle_detect(graph, node, visiting, visited):

    if node in visited:
        return False

    if node in visiting:
        return True

    visiting.add(node)

    for neighbor in graph[node]:
        if cycle_detect(graph, neighbor, visiting, visited) is True:
            return True

    visiting.remove(node)
    visited.add(node)

    return False


class Test(unittest.TestCase):
    def test_case_1(self):

        res = has_cycle(
            {
                "a": ["b"],
                "b": ["c"],
                "c": ["a"],
            }
        )  # -> True
        expected = True
        assert res == expected

    def test_case_2(self):
        res = has_cycle(
            {
                "a": ["b", "c"],
                "b": ["c"],
                "c": ["d"],
                "d": [],
            }
        )  # -> False
        expected = False
        assert res == expected

    def test_case_3(self):

        res = has_cycle(
            {
                "a": ["b", "c"],
                "b": [],
                "c": [],
                "e": ["f"],
                "f": ["e"],
            }
        )  # -> True
        expected = True
        assert res == expected

    def test_case_4(self):

        res = has_cycle(
            {
                "q": ["r", "s"],
                "r": ["t", "u"],
                "s": [],
                "t": [],
                "u": [],
                "v": ["w"],
                "w": [],
                "x": ["w"],
            }
        )  # -> False
        expected = False
        assert res == expected

    def test_case_5(self):
        res = has_cycle(
            {
                "a": ["b"],
                "b": ["c"],
                "c": ["a"],
                "g": [],
            }
        )  # -> True
        expected = True
        assert res == expected

    def test_case_6(self):
        res = has_cycle(
            {
                "a": ["b"],
                "b": ["c"],
                "c": ["d"],
                "d": ["b"],
            }
        )  # -> True
        expected = True
        assert res == expected


if __name__ == "__main__":
    unittest.main()
