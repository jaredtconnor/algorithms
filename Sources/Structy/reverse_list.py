import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list(head):

    res = ""
    current = head

    while current.next is not None:
        res += current.val + " -> "
        current = current.next

    res += current.val

    return res


def reverse_linked_list(head):

    previous = None
    current = head

    if current.next is None:
        return current

    while current is not None:

        next = current.next

        # turn current next pointer to previous
        current.next = previous

        # iterate the temp pointer set
        previous = current
        current = next

    return previous


def reverse_linked_list_recurse(head, prev=None):

    if head is None:
        return prev

    next = head.next
    head.next = prev
    return reverse_linked_list_recurse(next, head)


class Test(unittest.TestCase):
    def test_1(self):

        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f

        self.assertEqual((a, "c"), True)


if __name__ == "__main__":

    print(
        """
    ----------------------
        Iterative solution
    ----------------------
          """
    )

    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    print(f"Starting list: {print_list(a)}")
    print(f"Reversed list: {print_list(reverse_linked_list(a))}")

    print(
        """
    ----------------------
        Recursive solution
    ----------------------
          """
    )
    a = Node("a")
    b = Node("b")
    c = Node("c")
    d = Node("d")
    e = Node("e")
    f = Node("f")

    a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    print(f"Starting list: {print_list(a)}")
    print(f"Reversed list: {print_list(reverse_linked_list_recurse(a))}")
