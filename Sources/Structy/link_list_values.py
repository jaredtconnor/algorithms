import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def linked_list_values(head):

    vals = []

    current = head

    while current is not None:
        vals.append(current.val)
        current = current.next

    return vals


class Test(unittest.TestCase):
    def test_1(self):

        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        linked_list_values(a)


if __name__ == "__main__":
    unittest.main()
