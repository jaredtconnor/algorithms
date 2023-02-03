import unittest


def has_path(graph, src, dest):

    stack = [src]

    while len(stack) > 0:

        current = stack[-1]

        if current == dest:
            return True

        stack.pop()

        for neighbor in graph[current]:
            stack.append(neighbor)

    return False


def has_path_recursive(graph, src, dest):

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

    def test_case_2(self):

        graph = {
            "f": ["g", "i"],
            "g": ["h"],
            "h": [],
            "i": ["g", "k"],
            "j": ["i"],
            "k": [],
        }

        res = has_path(graph, "f", "j")
        expected = False
        assert res == expected

    def test_case_3(self):

        graph = {
            "f": ["g", "i"],
            "g": ["h"],
            "h": [],
            "i": ["g", "k"],
            "j": ["i"],
            "k": [],
        }

        res = has_path(graph, "i", "h")  # True
        expected = True
        assert res == expected

    def test_case_4(self):

        graph = {
            "v": ["x", "w"],
            "w": [],
            "x": [],
            "y": ["z"],
            "z": [],
        }

        res = has_path(graph, "v", "w")  # True
        expected = True
        assert res == expected

    def test_case_5(self):

        graph = {
            "v": ["x", "w"],
            "w": [],
            "x": [],
            "y": ["z"],
            "z": [],
        }

        res = has_path(graph, "v", "z")  # False
        expected = False
        assert res == expected

    def test_case_6(self):

        graph = {
            "f": ["g", "i"],
            "g": ["h"],
            "h": [],
            "i": ["g", "k"],
            "j": ["i"],
            "k": [],
        }

        res = has_path_recursive(graph, "f", "k")  # True
        expected = True
        assert res == expected

    def test_case_7(self):

        graph = {
            "f": ["g", "i"],
            "g": ["h"],
            "h": [],
            "i": ["g", "k"],
            "j": ["i"],
            "k": [],
        }

        res = has_path_recursive(graph, "f", "j")
        expected = False
        assert res == expected

    def test_case_8(self):

        graph = {
            "f": ["g", "i"],
            "g": ["h"],
            "h": [],
            "i": ["g", "k"],
            "j": ["i"],
            "k": [],
        }

        res = has_path_recursive(graph, "i", "h")  # True
        expected = True
        assert res == expected

    def test_case_9(self):

        graph = {
            "v": ["x", "w"],
            "w": [],
            "x": [],
            "y": ["z"],
            "z": [],
        }

        res = has_path_recursive(graph, "v", "w")  # True
        expected = True
        assert res == expected

    def test_case_10(self):

        graph = {
            "v": ["x", "w"],
            "w": [],
            "x": [],
            "y": ["z"],
            "z": [],
        }

        res = has_path_recursive(graph, "v", "z")  # False
        expected = False
        assert res == expected


if __name__ == "__main__":
    unittest.main()
