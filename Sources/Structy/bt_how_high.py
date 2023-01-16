import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def how_high(root: Node):

    # Base case 1
    if root is None:
        return -1

    # Base case 2 - Root node
    if root.left is None and root.right is None:
        return 0

    height = max(how_high(root.left), how_high(root.right))

    return


class Test(unittest.TestCase):
    def test_case_1(self):

        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        #      a
        #    /   \
        #   b     c
        #  / \     \
        # d   e     f
        res = how_high(a)  # -> 2
        expected = 2

        assert res == expected

    def test_case_2(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        g = Node("g")

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g

        #      a
        #    /   \
        #   b     c
        #  / \     \
        # d   e     f
        #    /
        #   g

        res = how_high(a)  # -> 3
        expected = 3
        assert res == expected

    def test_case_3(self):
        a = Node("a")
        c = Node("c")

        a.right = c

        #      a
        #       \
        #        c

        res = how_high(a)  # -> 1
        expected = 1

        assert res == expected

    def test_case_4(self):

        a = Node("a")
        res = how_high(a)  # -> 0

        expected = 0
        assert res == expected

    def test_case_5(self):

        res = how_high(None)  # -> -1
        expected = -1
        assert res == expected


if __name__ == "__main__":
    unittest.main()
