import unittest
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def path_finder_inefficient(root: Node, target: str):
    # Base case 1 - root == target
    if root.val == target:
        return [root.val]

    # Base case 2 - node is None
    elif root is None:
        return None

    left_path = path_finder_inefficient(root.left, target)
    right_path = path_finder_inefficient(root.right, target)

    if left_path is not None:
        result = [root.val, *left_path]
    elif right_path is not None:
        result = [root.val, *right_path]
    else:
        result = None

    return result


def path_finder(root: Node, target: str):
    result = _path_finder(root, target)

    if result is None:
        return None
    else:
        return result[::-1]


def _path_finder(root: Node, target: str):
    # Base case 2 - node is None
    if root is None:
        return None

    # Base case 1 - root == target
    if root.val == target:
        return [root.val]

    left_path = _path_finder(root.left, target)
    if left_path is not None:
        left_path.append(root.val)
        return left_path

    right_path = _path_finder(root.right, target)
    if right_path is not None:
        right_path.append(root.val)
        return right_path

    return None


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

        res = path_finder(a, "e")
        expected = ["a", "b", "e"]

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

        res = path_finder(a, "p")  # -> None
        expected = None

        assert res == expected

    def test_case_3(self):
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

        res = path_finder(a, "c")  # -> ['a', 'c']
        expected = ["a", "c"]

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

        res = path_finder(a, "h")
        expected = ["a", "c", "f", "h"]

        assert res == expected

    def test_case_5(self):
        x = Node("x")

        res = path_finder(x, "x")
        expected = ["x"]

        assert res == expected

    def test_case_6(self):
        res = path_finder(None, "x")  # -> None
        expected = None

        assert res == expected


if __name__ == "__main__":
    unittest.main()
