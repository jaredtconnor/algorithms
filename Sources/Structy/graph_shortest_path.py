import unittest


def shortest_path(graph):

    visited = set()

    current_max = 0

    return current_max


class Test(unittest.TestCase):
    def test_case_1(self):
        edges = [
            ['w', 'x'],
            ['x', 'y'],
            ['z', 'y'],
            ['z', 'v'],
            ['w', 'v']
        ]

        res = shortest_path(edges, 'w', 'z')  # -> 2
        expected = 2
        assert res == expected

    def test_case_2(self):

        edges = [
            ['w', 'x'],
            ['x', 'y'],
            ['z', 'y'],
            ['z', 'v'],
            ['w', 'v']
        ]

        res = shortest_path(edges, 'y', 'x')  # -> 1
        expected = 1

        assert res == expected

    def test_case_3(self):

        edges = [
            ['a', 'c'],
            ['a', 'b'],
            ['c', 'b'],
            ['c', 'd'],
            ['b', 'd'],
            ['e', 'd'],
            ['g', 'f']
        ]

        res = shortest_path(edges, 'a', 'e')  # -> 3
        expected = 3

        assert res == expected

    def test_case_4(self):
        edges = [
            ['a', 'c'],
            ['a', 'b'],
            ['c', 'b'],
            ['c', 'd'],
            ['b', 'd'],
            ['e', 'd'],
            ['g', 'f']
        ]

        res = shortest_path(edges, 'e', 'c')  # -> 2
        expected = 2
        assert res == expected

    def test_case_5(self):

        edges = [
            ['a', 'c'],
            ['a', 'b'],
            ['c', 'b'],
            ['c', 'd'],
            ['b', 'd'],
            ['e', 'd'],
            ['g', 'f']
        ]

        res = shortest_path(edges, 'b', 'g')  # -> -1
        expected = -1
        assert res == expected

    def test_case_6(self):

        edges = [
            ['c', 'n'],
            ['c', 'e'],
            ['c', 's'],
            ['c', 'w'],
            ['w', 'e'],
        ]

        res = shortest_path(edges, 'w', 'e')  # -> 1
        expected = 1

        assert res == expected

    def test_case_7(self):

        edges = [
            ['c', 'n'],
            ['c', 'e'],
            ['c', 's'],
            ['c', 'w'],
            ['w', 'e'],
        ]

        res = shortest_path(edges, 'n', 'e')  # -> 2
        expected = 2
        assert res == expected

    def test_case_8(self):

        edges = [
            ['m', 'n'],
            ['n', 'o'],
            ['o', 'p'],
            ['p', 'q'],
            ['t', 'o'],
            ['r', 'q'],
            ['r', 's']
        ]

        res = shortest_path(edges, 'm', 's')  # -> 6
        expected = 6
        assert res == expected


if __name__ == "__main__":
    unittest.main()
