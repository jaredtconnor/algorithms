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


def linked_list_values_recurse(head):

    vals = []
    _linked_list_values_fill_values(head, vals)
    return vals


def _linked_list_values_fill_values(head, vals):

    if head is None:
        return

    vals.append(head.val)
    _linked_list_values_fill_values(head.next, vals)


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
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        expected = ["a", "b", "c", "d"]
        res = linked_list_values(a)
        assert res == expected

    def test_2(self):

        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        expected = ["a", "b", "c", "d"]
        res = linked_list_values_recurse(a)
        assert res == expected


if __name__ == "__main__":
    unittest.main()
