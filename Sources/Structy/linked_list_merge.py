import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def merge_lists(head_a: Node, head_b: Node):

    current1 = head_a
    current2 = head_b
    dummy = Node()

    while current1 and current2:

        if current1.val < current2.val:
            current1.next = current1


def print_list(head):

    res = ""
    current = head

    while current.next is not None:
        res += current.val + " -> "
        current = current.next

    res += current.val

    return res


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

        expected = "a -> x -> b -> y -> c -> z"
        res = merge_lists(a, x)
        assert print_list(res) == expected


if __name__ == "__main__":
    unittest.main()
