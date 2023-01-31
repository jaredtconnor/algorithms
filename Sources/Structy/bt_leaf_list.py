import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def leaf_list(root: Node):

    if root is None:
        return []

    leafs = []
    stack = [root]

    while stack:

        current = stack.pop()

        if current.left is None and current.right is None:
            leafs.append(current.val)

        if current.right is not None:
            stack.append(current.right)

        if current.left is not None:
            stack.append(current.left)

    return leafs


def leaf_list_recursive(root: Node):

    leafs = []

    _leaf_list_recursive(root, leafs)

    return leafs


def _leaf_list_recursive(root: Node, leaf_list):

    # Base case 1
    if root is None:
        return

    # Base case 2 - leaf
    if root.left is None and root.right is None:
        leaf_list.append(root.val)

    # Recursive leap of faith
    if root.left is not None:
        _leaf_list_recursive(root.left, leaf_list)

    if root.right is not None:
        _leaf_list_recursive(root.right, leaf_list)


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

        res = leaf_list(a)
        expected = ["d", "e", "f"]
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
        #    /       \
        #   g         h

        res = leaf_list(a)
        expected = ["d", "g", "h"]
        assert res == expected

    def test_case_3(self):

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

        res = leaf_list(a)
        expected = [20, 1, 3, 54]
        assert res == expected

    def test_case_4(self):
        x = Node("x")

        res = leaf_list(x)
        expected = ["x"]
        assert res == expected

    def test_case_5(self):

        res = leaf_list(None)
        expected = []
        assert res == expected

    def test_case_6(self):
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

        res = leaf_list_recursive(a)
        expected = ["d", "e", "f"]
        assert res == expected

    def test_case_7(self):

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

        res = leaf_list_recursive(a)
        expected = ["d", "g", "h"]
        assert res == expected

    def test_case_8(self):

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

        res = leaf_list_recursive(a)
        expected = [20, 1, 3, 54]
        assert res == expected

    def test_case_9(self):
        x = Node("x")

        res = leaf_list_recursive(x)
        expected = ["x"]
        assert res == expected

    def test_case_10(self):

        res = leaf_list_recursive(None)
        expected = []
        assert res == expected


if __name__ == "__main__":
    unittest.main()
