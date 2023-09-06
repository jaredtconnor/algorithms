import unittest
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_includes(root: Node, target: str):
    if root is None:
        return False

    queue = deque([root])

    while queue:
        current = queue.popleft()

        if current.val == target:
            return True

        if current.left is not None:
            queue.append(current.left)

        if current.right is not None:
            queue.append(current.right)

    return False


def tree_includes_recursive(root: Node, target: str):
    if root is None:
        return False

    if root.val == target:
        return True

    left_values = tree_includes_recursive(root.left, target)
    right_values = tree_includes_recursive(root.right, target)

    if left_values or right_values:
        result = True
    else:
        result = False

    return result


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

        res = tree_includes(a, "e")  # -> True
        expected = True
        assert res == expected

    def test_case_2(self):
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
        res = tree_includes(a, "a")  # -> True
        expected = True

        assert res == expected

    def test_case_3(self):
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

        res = tree_includes(a, "n")  # -> False
        expected = False

        assert res == expected

    def test_case_4(self):
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
        #    /       \
        #   g         h

        res = tree_includes(a, "f")  # -> True
        expected = True

        assert res == expected

    def test_case_5(self):
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
        #    /       \
        #   g         h

        res = tree_includes(a, "p")  # -> False
        expected = False

        assert res == expected

    def test_case_6(self):
        res = tree_includes(None, "b")  # -> False
        expected = False

        assert res == expected

    def test_case_7(self):
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

        res = tree_includes_recursive(a, "e")  # -> True
        expected = True
        assert res == expected

    def test_case_8(self):
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
        res = tree_includes_recursive(a, "a")  # -> True
        expected = True

        assert res == expected

    def test_case_9(self):
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

        res = tree_includes_recursive(a, "n")  # -> False
        expected = False

        assert res == expected

    def test_case_10(self):
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
        #    /       \
        #   g         h

        res = tree_includes_recursive(a, "f")  # -> True
        expected = True

        assert res == expected

    def test_case_11(self):
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
        #    /       \
        #   g         h

        res = tree_includes_recursive(a, "p")  # -> False
        expected = False

        assert res == expected

    def test_case_12(self):
        res = tree_includes_recursive(None, "b")  # -> False
        expected = False

        assert res == expected


if __name__ == "__main__":
    unittest.main()
