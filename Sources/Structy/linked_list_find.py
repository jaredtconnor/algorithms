import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def linked_list_find(head, target):

    current = head

    while current is not None:

        if current.val == target:
            return True

        current = current.next

    return False


def linked_list_find_recurse(head, target):

    # base case 1 - end of list
    if head is None:
        return False

    elif head.val == target:
        return True

    return linked_list_find_recurse(head.next, target)


class Test(unittest.TestCase):
    def test_1(self):

        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        self.assertEqual(linked_list_find(a, "c"), True)

    def test_2(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        self.assertEqual(linked_list_find(a, "d"), True)

    def test_3(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")

        a.next = b
        b.next = c
        c.next = d

        self.assertEqual(linked_list_find(a, "q"), False)

    def test_4(self):
        node1 = Node("jason")
        node2 = Node("leneli")

        node1.next = node2

        self.assertEqual(linked_list_find(node1, "jason"), True)

    def test_5(self):
        node1 = Node(42)

        self.assertEqual(linked_list_find(node1, 42), True)

    def test_6(self):
        node1 = Node(42)

        self.assertEqual(linked_list_find(node1, 50), False)


if __name__ == "__main__":
    unittest.main()
