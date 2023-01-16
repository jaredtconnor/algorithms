import unittest
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def bottom_right_value(root: Node):

    if root is None:
        return None

    queue = deque([root])

    while queue:

        current = queue.popleft()
        previous = current

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

    return previous.val


class Test(unittest.TestCase):
    def test_case_1(self):
        a = Node(3)
        b = Node(11)
        c = Node(10)
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
        #   11     10
        #  / \      \
        # 4   -2     1

        res = bottom_right_value(a)  # -> 1
        expected = 1
        assert res == expected

    def test_case_2(self):
        a = Node(-1)
        b = Node(-6)
        c = Node(-5)
        d = Node(-3)
        e = Node(-4)
        f = Node(-13)
        g = Node(-2)
        h = Node(6)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        e.right = h

        #        -1
        #      /   \
        #    -6    -5
        #   /  \     \
        # -3   -4   -13
        #     / \
        #    -2  6

        res = bottom_right_value(a)  # -> 6
        expected = 6
        assert res == expected

    def test_case_3(self):
        a = Node(-1)
        b = Node(-6)
        c = Node(-5)
        d = Node(-3)
        e = Node(-4)
        f = Node(-13)
        g = Node(-2)
        h = Node(6)
        i = Node(7)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        e.right = h
        f.left = i

        #        -1
        #      /   \
        #    -6    -5
        #   /  \     \
        # -3   -4   -13
        #     / \    /
        #    -2  6  7

        res = bottom_right_value(a)  # -> 7
        expected = 7
        assert res == expected

    def test_case_4(self):

        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")

        a.left = b
        a.right = c
        b.right = d
        d.left = e
        e.right = f

        #      a
        #    /   \
        #   b     c
        #    \
        #     d
        #    /
        #   e
        #  /
        # f

        res = bottom_right_value(a)  # -> 'f'
        expected = "f"
        assert res == expected

    def test_case_5(self):

        a = Node(42)
        #      42

        res = bottom_right_value(a)  # -> 42
        expected = res
        assert res == expected


if __name__ == "__main__":
    unittest.main()
