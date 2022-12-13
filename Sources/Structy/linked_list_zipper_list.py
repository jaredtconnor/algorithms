import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def zipper_list(head_a: Node, head_b: Node):

    tail = head_a
    current1, current2 = head_a.next, head_b
    count = 0

    while current1 is not None and current2 is not None:

        if count % 2 == 0:

            tail.next = current2
            current2 = current2.next

        else:
            tail.next = current1
            current1 = current1.next

        tail = tail.next
        count += 1

    # section to carry over if one list is null
    if current1 is not None:
        tail.next = current1

    if current2 is not None:
        tail.next = current2

    return head_a


def zipper_list_recursive(head_a: Node, head_b: Node) -> Node:

    if head_a is None and head_b is None:

        return None

    if head_a is None:
        return head_b

    if head_b is None:
        return head_a

    next_1 = head_a.next
    next_2 = head_b.next

    head_a.next = head_b
    head_b.next = zipper_list_recursive(next_1, next_2)

    return head_a


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
        res = zipper_list(a, x)
        assert print_list(res) == expected

    def test_2(self):
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
        res = zipper_list_recursive(a, x)
        assert print_list(res) == expected


if __name__ == "__main__":
    unittest.main()
