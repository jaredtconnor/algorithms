import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def depth_first_values(root: Node):

    if root is None:
        return []

    values = []
    stack = [root]

    while stack:

        current = stack.pop()
        values.append(current.val)

        if current.right is not None:
            stack.append(current.right)

        if current.left is not None:
            stack.append(current.left)

    return values


def depth_first_values_recursive(root: Node):

    # Base case
    if root is None:
        return []

    # Recursive leap of faith
    left_values = depth_first_values_recursive(root.left)
    right_values = depth_first_values_recursive(root.right)

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

        res = depth_first_values(a)
        expected = ["a", "b", "d", "e", "c", "f"]

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
        res = depth_first_values(a)
        expected = ["a", "b", "d", "e", "g", "c", "f"]
        assert res == expected

    def test_case_3(self):

        #     a
        a = Node("a")

        res = depth_first_values(a)
        expected = ["a"]

        assert res == expected

    def test_case_4(self):

        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        a.right = b
        b.left = c
        c.right = d
        d.right = e

        #      a
        #       \
        #        b
        #       /
        #      c
        #       \
        #        d
        #         \
        #          e

        res = depth_first_values(a)
        expected = ["a", "b", "c", "d", "e"]
        assert res == expected

    def test_case_5(self):
        res = depth_first_values(None)
        expected = []
        assert res == expected

    def test_case_6(self):

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

        res = depth_first_values_recursive(a)
        expected = ["a", "b", "d", "e", "c", "f"]

        assert res == expected

    def test_case_7(self):

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
        res = depth_first_values_recursive(a)
        expected = ["a", "b", "d", "e", "g", "c", "f"]
        assert res == expected

    def test_case_8(self):

        #     a
        a = Node("a")

        res = depth_first_values_recursive(a)
        expected = ["a"]

        assert res == expected

    def test_case_9(self):

        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        a.right = b
        b.left = c
        c.right = d
        d.right = e

        #      a
        #       \
        #        b
        #       /
        #      c
        #       \
        #        d
        #         \
        #          e

        res = depth_first_values_recursive(a)
        expected = ["a", "b", "c", "d", "e"]
        assert res == expected

    def test_case_10(self):
        res = depth_first_values_recursive(None)
        expected = []
        assert res == expected


if __name__ == "__main__":
    unittest.main()
