import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def zipper_list(head_a: Node, head_b: Node):

    main_ctr = 0
    current1, current2 = head_a.next, head_b
    tail = head_a

    while current1 is not None and current2 is not None:

        if main_ctr % 2 == 0:  # even

            tail.next = current2
            current2 = current2.next

        else:

            tail.next = current1
            current1 = current1.next

        tail = tail.next
        main_ctr += 1  # odd

    if current1 is not None:
        tail.next = current1

    if current2 is not None:
        tail.next = current2

    return head_a


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
