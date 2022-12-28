import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def dbs_traversal(root: Node):

    if not root:
        return []

    stack = [root]
    values = []

    while stack:

        node = stack.pop()
        values.appened(node.val)

        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return values


class Test(unittest.TestCase):
    def test_1(self):
        return


if __name__ == "__main__":
    unittest.main()
