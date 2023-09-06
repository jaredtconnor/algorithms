import unittest
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_sum(root: Node):
    if root is None:
        return 0

    sum = 0
    stack = [root]

    while stack:
        current = stack.pop()
        sum += current.val

        if current.right is not None:
            stack.append(current.right)

        if current.left is not None:
            stack.append(current.left)

    return sum


def tree_sum_recursive(root: Node):
    if root is None:
        return 0

    left_values = tree_sum_recursive(root.left)
    right_values = tree_sum_recursive(root.right)

    return root.val + left_values + right_values


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

        res = tree_sum(a)  # -> 21
        expected = 21

        assert res == expected

    def test_case_2(self):
        a = Node(1)
        b = Node(6)
        c = Node(0)
        d = Node(3)
        e = Node(-6)
        f = Node(2)
        g = Node(2)
        h = Node(2)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        #      1
        #    /   \
        #   6     0
        #  / \     \
        # 3   -6    2
        #    /       \
        #   2         2

        res = tree_sum(a)  # -> 10
        expected = 10

        assert res == expected

    def test_case_3(self):
        res = tree_sum(None)  # -> 0
        expected = 0

        assert res == expected

    def test_case_4(self):
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

        res = tree_sum_recursive(a)  # -> 21
        expected = 21

        assert res == expected

    def test_case_4(self):
        a = Node(1)
        b = Node(6)
        c = Node(0)
        d = Node(3)
        e = Node(-6)
        f = Node(2)
        g = Node(2)
        h = Node(2)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        #      1
        #    /   \
        #   6     0
        #  / \     \
        # 3   -6    2
        #    /       \
        #   2         2

        res = tree_sum_recursive(a)  # -> 10
        expected = 10

        assert res == expected

    def test_case_5(self):
        res = tree_sum_recursive(None)  # -> 0
        expected = 0

        assert res == expected


if __name__ == "__main__":
    unittest.main()
