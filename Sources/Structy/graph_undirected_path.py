import unittest


def build_graph(edges):

    graph = {}

    for edge in edges:

        a, b = edge

        if a not in graph:
            graph[a] = []

        if b not in graph:
            graph[b] = []

        graph[a].append(b)
        graph[b].append(a)

    return graph


def has_path(graph, src, dest, visited):

    # Base case 1 - stopping condition
    if src == dest:
        return True

    # Base case 2 - visited node already
    if src in visited:
        return False

    # Add current node to visited
    visited.add(src)

    for neighbor in graph[src]:
        if has_path(graph, neighbor, dest, visited) is True:
            return True

    return False


def undirected_path(edges, node_a, node_b):

    graph = build_graph(edges)
    visited = set()

    return has_path(graph, node_a, node_b, visited)


class Test(unittest.TestCase):
    def test_case_1(self):
        edges = [("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")]

        res = undirected_path(edges, "j", "m")  # -> True
        expected = True
        assert res == expected

    def test_case_2(self):

        edges = [("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")]

        res = undirected_path(edges, "m", "j")  # -> True
        expected = True
        assert res == expected

    def test_case_3(self):

        edges = [("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")]

        res = undirected_path(edges, "l", "j")  # -> True
        expected = True
        assert res == expected

    def test_case_4(self):
        edges = [("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")]

        res = undirected_path(edges, "k", "o")  # -> False
        expected = False
        assert res == expected

    def test_case_5(self):

        edges = [("i", "j"), ("k", "i"), ("m", "k"), ("k", "l"), ("o", "n")]

        res = undirected_path(edges, "i", "o")  # -> False
        expected = False
        assert res == expected

    def test_case_6(self):

        edges = [
            ("b", "a"),
            ("c", "a"),
            ("b", "c"),
            ("q", "r"),
            ("q", "s"),
            ("q", "u"),
            ("q", "t"),
        ]

        res = undirected_path(edges, "a", "b")  # -> True
        expected = True
        assert res == expected

    def test_case_7(self):

        edges = [
            ("b", "a"),
            ("c", "a"),
            ("b", "c"),
            ("q", "r"),
            ("q", "s"),
            ("q", "u"),
            ("q", "t"),
        ]

        res = undirected_path(edges, "a", "c")  # -> True
        expected = True
        assert res == expected

    def test_case_8(self):

        edges = [
            ("b", "a"),
            ("c", "a"),
            ("b", "c"),
            ("q", "r"),
            ("q", "s"),
            ("q", "u"),
            ("q", "t"),
        ]

        res = undirected_path(edges, "r", "t")  # -> True
        expected = True
        assert res == expected

    def test_case_9(self):

        edges = [
            ("b", "a"),
            ("c", "a"),
            ("b", "c"),
            ("q", "r"),
            ("q", "s"),
            ("q", "u"),
            ("q", "t"),
        ]

        res = undirected_path(edges, "r", "b")  # -> False
        expected = False
        assert res == expected

    def test_case_10(self):
        edges = [
            ("s", "r"),
            ("t", "q"),
            ("q", "r"),
        ]

        res = undirected_path(edges, "r", "t")
        # -> True
        expected = True
        assert res == expected


if __name__ == "__main__":
    unittest.main()
