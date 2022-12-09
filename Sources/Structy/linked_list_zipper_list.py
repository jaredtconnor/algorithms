import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def zipper_list(head_a: Node, head_b: Node):

    return


class Test(unittest.TestCase):
    def test_1(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")

        a.next = b
        b.next = c
        # a -> b -> c

        x = Node("x")
        y = Node("y")
        z = Node("z")
        x.next = y
        y.next = z
        # x -> y -> z

        zipper_lists(a, x)
        # a -> x -> b -> y -> c -> z`


if __name__ == "__main__":
    unittest.main()
