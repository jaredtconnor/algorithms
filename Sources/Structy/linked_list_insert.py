import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def insert_node(head: Node, value: str, index: int):

    if index == 0:
        new_head = Node(value)
        new_head.next = head
        return new_head

    count = 0
    current = head

    while current is not None:

        if count == (index - 1):

            temp = current.next
            to_add = Node(value)
            to_add.next = temp
            current.next = to_add
            break

        count += 1
        current = current.next

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

        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        res = insert_node(a, "x", 2)
        expected = "a -> b -> x -> c -> d"

        assert print_list(res) == expected

    def test_2(self):

        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d
        # a -> b -> c -> d

        res = insert_node(a, "v", 3)
        expected = "a -> b -> c -> v -> d"

        assert print_list(res) == expected

    def test_3(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        # a -> b -> c -> d

        res = insert_node(a, "m", 4)
        expected = "a -> b -> c -> d -> m"

        assert print_list(res) == expected

    def test_4(self):

        a = Node("a")
        b = Node("b")
        a.next = b
        # a -> b

        res = insert_node(a, "z", 0)
        expected = "z -> a -> b"

        assert print_list(res) == expected


if __name__ == "__main__":
    unittest.main()
