import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_linked_list(input: list):

    dummy = Node(None)
    tail = dummy

    for value in input:

        tail.next = Node(str(value))
        tail = tail.next

    return dummy.next


def create_linked_list_recursive(input: list):

    # Base Case - if input is end
    if len(input) == 0:
        return None

    head = Node(str(input[0]))

    head.next = create_linked_list_recursive(input[1:])

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

        res = create_linked_list(["h", "e", "y"])
        expected = "h -> e -> y"

        assert print_list(res) == expected

    def test_2(self):

        res = create_linked_list([1, 7, 1, 8])
        expected = "1 -> 7 -> 1 -> 8"

        assert print_list(res) == expected

    def test_3(self):

        res = create_linked_list(["a"])
        expected = "a"

        assert print_list(res) == expected

    def test_4(self):

        res = create_linked_list([])
        expected = None

        assert res == expected

    def test_5(self):

        res = create_linked_list_recursive(["h", "e", "y"])
        expected = "h -> e -> y"

        assert print_list(res) == expected

    def test_6(self):

        res = create_linked_list_recursive([1, 7, 1, 8])
        expected = "1 -> 7 -> 1 -> 8"

        assert print_list(res) == expected

    def test_7(self):

        res = create_linked_list_recursive(["a"])
        expected = "a"

        assert print_list(res) == expected

    def test_8(self):

        res = create_linked_list_recursive([])
        expected = None

        assert res == expected


if __name__ == "__main__":
    unittest.main()
