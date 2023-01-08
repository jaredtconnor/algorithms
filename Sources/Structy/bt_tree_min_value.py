import unittest
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_min_value(root: Node):

    if root is None:
        return None

    stack = [root]
    min_val = root.val

    while stack:

        current = stack.pop()

        if current.val < min_val:
            min_val = current.val

        if current.right is not None:
            stack.append(current.right)

        if current.left is not None:
            stack.append(current.left)

    return min_val


## def tree_min_value(root: Node, min_val: int):

##  if root is None:
##     return


class Test(unittest.TestCase):
    def test_case_1(self):

        a = Node(3)
        b = Node(11)
        c = Node(4)
        d = Node(4)
        e = Node(-2)
        f = Node(1)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        #       3
        #    /    \
        #   11     4
        #  / \      \
        # 4   -2     1

        res = tree_min_value(a)  # -> -2
        expected = -2

        assert res == expected

    def test_case_2(self):

        a = Node(5)
        b = Node(11)
        c = Node(3)
        d = Node(4)
        e = Node(14)
        f = Node(12)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        #       5
        #    /    \
        #   11     3
        #  / \      \
        # 4   14     12

        res = tree_min_value(a)  # -> 3
        expected = 3
        assert res == expected

    def test_case_3(self):

        a = Node(-1)
        b = Node(-6)
        c = Node(-5)
        d = Node(-3)
        e = Node(-4)
        f = Node(-13)
        g = Node(-2)
        h = Node(-2)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        #        -1
        #      /   \
        #    -6    -5
        #   /  \     \
        # -3   -4   -13
        #     /       \
        #    -2       -2

        res = tree_min_value(a)  # -> -13
        expected = -13
        assert res == expected

    def test_case_4(self):
        a = Node(42)
        #        42

        res = tree_min_value(a)  # -> 42
        expected = 42
        assert res == expected


if __name__ == "__main__":
    unittest.main()
