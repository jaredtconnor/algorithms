import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def is_univalue_list(head: Node) -> bool:

    return false


def is_univalue_list_recursive(head: Node) -> bool:

    return head


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

        a = Node(7)
        b = Node(7)
        c = Node(7)

        a.next = b
        b.next = c  # 7 -> 7 -> 7

        expected = True
        res = is_univalue_list(a)  # True

        assert res == expected

    def test_2(self):

        a = Node(7)
        b = Node(7)
        c = Node(4)

        a.next = b
        b.next = c
        # 7 -> 7 -> 4

        expected = False
        res = is_univalue_list(a)  # False`

        assert res == expected

    def test_3(self):

        z = Node("z")  # z

        expected = True
        res = is_univalue_list(z)  # True
        assert res == expected


if __name__ == "__main__":
    unittest.main()
