import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def longest_streak(head: Node) -> bool:

    return res


def longest_streak_recursive(head, prev_val=None):

    return is_univalue_list_recursive_solution(head.next, head.val)


def is_univalue_list_recursive(head: Node) -> bool:

    res = True
    val = head.val

    res = _is_univalue_list_check(head, val)

    return res


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

    def test_4(self):

        a = Node(7)
        b = Node(7)
        c = Node(7)

        a.next = b
        b.next = c  # 7 -> 7 -> 7

        expected = True
        res = is_univalue_list_recursive(a)  # True

        assert res == expected

    def test_5(self):

        a = Node(7)
        b = Node(7)
        c = Node(4)

        a.next = b
        b.next = c
        # 7 -> 7 -> 4

        expected = False
        res = is_univalue_list_recursive(a)  # False`

        assert res == expected

    def test_6(self):

        z = Node("z")  # z

        expected = True
        res = is_univalue_list_recursive(z)  # True
        assert res == expected


if __name__ == "__main__":
    unittest.main()
