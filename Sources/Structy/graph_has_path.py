import unittest


def has_path(graph, src, dest):

    if src == dest:
        return True

    for neighbor in graph[src]:
        if has_path(graph, neighbor, dest) is True:
            return True

    return False


class Test(unittest.TestCase):
    def test_case_1(self):

        graph = {
            "f": ["g", "i"],
            "g": ["h"],
            "h": [],
            "i": ["g", "k"],
            "j": ["i"],
            "k": [],
        }

        res = has_path(graph, "f", "k")  # True
        expected = True
        assert res == expected


if __name__ == "__main__":
    unittest.main()
