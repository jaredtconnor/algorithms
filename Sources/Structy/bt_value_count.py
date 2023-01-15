import unittest
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_value_count(root: Node, target: int):

    # Base case 1
    if root is None:
        return 0

    match = 1 if root.val == target else 0

    left_tree = tree_value_count(root.left, target)
    right_tree = tree_value_count(root.right, target)

    return match + left_tree + right_tree


def tree_value_count_iterative(root: Node, target: int):

    if root is None:
        return 0

    value_cnt = 0
    stack = [root]

    while stack:

        current = stack.pop()

        if current.val == target:
            value_cnt += 1

        if current.right is not None:
            stack.append(current.right)

        if current.left is not None:
            stack.append(current.left)

    return value_cnt


class Test(unittest.TestCase):
    def test_case_1(self):

        a = Node(12)
        b = Node(6)
        c = Node(6)
        d = Node(4)
        e = Node(6)
        f = Node(12)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        #      12
        #    /   \
        #   6     6
        #  / \     \
        # 4   6     12

        res = tree_value_count(a, 6)
        expected = 3

        assert res == expected

    def test_case_2(self):

        a = Node(12)
        b = Node(6)
        c = Node(6)
        d = Node(4)
        e = Node(6)
        f = Node(12)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        #      12
        #    /   \
        #   6     6
        #  / \     \
        # 4  6     12

        res = tree_value_count(a, 12)
        expected = 2
        assert res == expected

    def test_case_3(self):

        a = Node(7)
        b = Node(5)
        c = Node(1)
        d = Node(1)
        e = Node(8)
        f = Node(7)
        g = Node(1)
        h = Node(1)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        #      7
        #    /   \
        #   5     1
        #  / \     \
        # 1   8     7
        #    /       \
        #   1         1

        res = tree_value_count(a, 1)
        expected = 4
        assert res == expected

    def test_case_4(self):

        a = Node(7)
        b = Node(5)
        c = Node(1)
        d = Node(1)
        e = Node(8)
        f = Node(7)
        g = Node(1)
        h = Node(1)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        #      7
        #    /   \
        #   5     1
        #  / \     \
        # 1   8     7
        #    /       \
        #   1         1

        res = tree_value_count(a, 9)  # -> 0
        expected = 0
        assert res == expected

    def test_case_5(self):

        res = tree_value_count(None, 42)
        expected = 0
        assert res == expected

    def test_case_6(self):

        a = Node(12)
        b = Node(6)
        c = Node(6)
        d = Node(4)
        e = Node(6)
        f = Node(12)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        #      12
        #    /   \
        #   6     6
        #  / \     \
        # 4   6     12

        res = tree_value_count_iterative(a, 6)
        expected = 3

        assert res == expected

    def test_case_7(self):

        a = Node(12)
        b = Node(6)
        c = Node(6)
        d = Node(4)
        e = Node(6)
        f = Node(12)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        #      12
        #    /   \
        #   6     6
        #  / \     \
        # 4  6     12

        res = tree_value_count_iterative(a, 12)
        expected = 2
        assert res == expected

    def test_case_8(self):

        a = Node(7)
        b = Node(5)
        c = Node(1)
        d = Node(1)
        e = Node(8)
        f = Node(7)
        g = Node(1)
        h = Node(1)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        #      7
        #    /   \
        #   5     1
        #  / \     \
        # 1   8     7
        #    /       \
        #   1         1

        res = tree_value_count_iterative(a, 1)
        expected = 4
        assert res == expected

    def test_case_9(self):

        a = Node(7)
        b = Node(5)
        c = Node(1)
        d = Node(1)
        e = Node(8)
        f = Node(7)
        g = Node(1)
        h = Node(1)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        #      7
        #    /   \
        #   5     1
        #  / \     \
        # 1   8     7
        #    /       \
        #   1         1

        res = tree_value_count_iterative(a, 9)  # -> 0
        expected = 0
        assert res == expected

    def test_case_10(self):

        res = tree_value_count_iterative(None, 42)
        expected = 0
        assert res == expected


if __name__ == "__main__":
    unittest.main()
