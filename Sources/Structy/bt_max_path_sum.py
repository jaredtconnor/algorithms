import unittest
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def max_path_sum(root: Node):

    if root is None:
        return float("-inf")

    # Base case
    if root.left is None and root.right is None:
        return root.val

    max_left = max_path_sum(root.left)
    max_right = max_path_sum(root.right)

    return root.val + max(max_left, max_right)


class Test(unittest.TestCase):
    def test_case_1(self):

        #       3
        #    /    \
        #   11     4
        #  / \      \
        # 4   -2     1

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

        res = max_path_sum(a)  # -> 18
        expected = 18

        assert res == expected

    def test_case_2(self):
        a = Node(5)
        b = Node(11)
        c = Node(54)
        d = Node(20)
        e = Node(15)
        f = Node(1)
        g = Node(3)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        e.left = f
        e.right = g

        #        5
        #     /    \
        #    11    54
        #  /   \
        # 20   15
        #      / \
        #     1  3

        res = max_path_sum(a)  # -> 59
        expected = 59

        assert res == expected

    def test_case_3(self):

        a = Node(-1)
        b = Node(-6)
        c = Node(-5)
        d = Node(-3)
        e = Node(0)
        f = Node(-13)
        g = Node(-1)
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
        # -3   0    -13
        #     /       \
        #    -1       -2

        res = max_path_sum(a)  # -> -8
        expected = -8
        assert res == expected

    def test_case_4(self):

        a = Node(42)

        res = max_path_sum(a)  # -> 42
        expected = 42


if __name__ == "__main__":
    unittest.main()
