import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_levels(root): 

    # Base case
    if root is None:
        return []

    # Recursive leap of faith
    left_values = tree_levels(root.left)
    right_values = tree_levels(root.right)

    return [root.val, *left_values, *right_values]


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

        res = tree_levels(a)  # ->

        expected = [["a"], ["b", "c"], ["d", "e", "f"]]

        assert res == expected


if __name__ == "__main__":
    unittest.main()
