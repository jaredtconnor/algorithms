import unittest
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def all_tree_paths(root: Node):

    # Base case 1 - node is None
    if root is None:
        return []

    # Base case 2 - node is leaf
    if root.left is None and root.right is None:
        return [[root.val]]

    paths = []

    # Recursive leap of faith
    left_sub_paths = all_tree_paths(root.left)

    for path in left_sub_paths:
        paths.append([root.val, *path])

    right_sub_paths = all_tree_paths(root.right)

    for path in right_sub_paths:
        paths.append([root.val, *path])

    return paths


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

        res = all_tree_paths(a)  # ->

        expected = [["a", "b", "d"], ["a", "b", "e"], ["a", "c", "f"]]

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
        i = Node("i")

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        e.right = h
        f.left = i

        #         a
        #      /    \
        #     b      c
        #   /  \      \
        #  d    e      f
        #      / \    /
        #     g  h   i

        res = all_tree_paths(a)

        expected = [
            ["a", "b", "d"],
            ["a", "b", "e", "g"],
            ["a", "b", "e", "h"],
            ["a", "c", "f", "i"],
        ]

        assert res == expected

    def test_case_3(self):
        q = Node("q")
        r = Node("r")
        s = Node("s")
        t = Node("t")
        u = Node("u")
        v = Node("v")

        q.left = r
        q.right = s
        r.right = t
        t.left = u
        u.right = v

        #      q
        #    /   \
        #   r     s
        #    \
        #     t
        #    /
        #   u
        #  /
        # v

        res = all_tree_paths(q)  # ->
        expected = [["q", "r", "t", "u", "v"], ["q", "s"]]

        assert res == expected

    def test_case_4(self):

        z = Node("z")

        res = all_tree_paths(z)  # ->
        expected = [["z"]]

        assert res == expected


if __name__ == "__main__":
    unittest.main()
