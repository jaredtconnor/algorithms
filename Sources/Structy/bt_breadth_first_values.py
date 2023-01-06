import unittest
from collections import deque

# double ended queue


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def breadth_first_values(root: Node):

    if root is None:
        return []

    values = []
    queue = deque([root])

    while queue:

        current = queue.popleft()
        values.append(current.val)

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

    return values


def breadth_first_values_recursive(root: Node):

    # Base case
    if root is None:
        return []

    # Recursive leap of faith
    left_values = breadth_first_values_recursive(root.left)
    right_values = breadth_first_values_recursive(root.right)

    return [root.val, *left_values, *right_values]


class Test(unittest.TestCase):
    def test_case_1(self):

        #      a
        #    /   \
        #   b     c
        #  / \     \
        # d   e     f

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

        res = breadth_first_values(a)
        expected = ["a", "b", "c", "d", "e", "f"]

        assert res == expected

    def test_case_2(self):

        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        g = Node("g")
        h = Node("h")

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        #      a
        #    /   \
        #   b     c
        #  / \     \
        # d   e     f
        #    /
        #   g

        res = breadth_first_values(a)
        expected = ["a", "b", "c", "d", "e", "f", "g", "h"]
        assert res == expected

    def test_case_3(self):

        #     a
        a = Node("a")

        res = breadth_first_values(a)
        expected = ["a"]

        assert res == expected

    def test_case_4(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        x = Node("x")

        a.right = b
        b.left = c
        c.left = x
        c.right = d
        d.right = e

        #      a
        #       \
        #        b
        #       /
        #      c
        #    /  \
        #   x    d
        #         \
        #          e

        res = breadth_first_values(a)
        expected = ["a", "b", "c", "x", "d", "e"]
        assert res == expected

    def test_case_5(self):
        res = breadth_first_values(None)
        expected = []

        assert res == expected


if __name__ == "__main__":
    unittest.main()
