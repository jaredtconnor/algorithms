import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def longest_streak(head: Node) -> int:

    current = head
    prev_val = None
    max_streak = 0
    current_streak = 0

    while current is not None:

        if prev_val is None:
            prev_val = current.val

        if prev_val == current.val:
            current_streak += 1

        if current_streak > max_streak:
            max_streak = current_streak

        current = current.next

    return max_streak


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
        a = Node(5)
        b = Node(5)
        c = Node(7)
        d = Node(7)
        e = Node(7)
        f = Node(6)

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f

        # 5 -> 5 -> 7 -> 7 -> -> 7 -> 6
        res = longest_streak(a)  # 3
        expected = 3
        assert res == expected

    def test_2(self):

        a = Node(3)
        b = Node(3)
        c = Node(3)
        d = Node(3)
        e = Node(9)
        f = Node(9)

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f
        # 3 -> 3 -> 3 -> 3 -> 9 -> 9

        res = longest_streak(a)  # 4
        expected = 4

        assert res == expected

    def test_3(self):

        a = Node(9)
        b = Node(9)
        c = Node(1)
        d = Node(9)
        e = Node(9)
        f = Node(9)

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f
        # 9 -> 9 -> 1 -> 9 -> 9 -> 9

        res = longest_streak(a)  # 3
        expected = 3
        assert res == expected

    def test_4(self):
        a = Node(5)
        b = Node(5)

        a.next = b  # 5 -> 5

        res = longest_streak(a)  # 2
        expected = 2

        assert res == expected

    def test_5(self):
        a = Node(4)
        # 4

        res = longest_streak(a)  # 1
        expected = 1

        assert res == expected

    def test_6(self):

        res = longest_streak(None)  # 0
        expected = 0
        assert res == expected


if __name__ == "__main__":
    unittest.main()
