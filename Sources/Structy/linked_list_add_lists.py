import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def add_lists(input1: list, input2: list):

    current1 = input1
    current2 = input2
    dummy = Node(None)
    tail = dummy
    carry = 0

    while current1 is not None and current2 is not None:

        if carry == 0:
            sum = current1.val + current2.val
        else:
            sum = current1.val + current2.val + carry
            carry = 0

        if sum > 9:
            carry = sum // 10
            sum = sum % 10

        result = Node(sum)

        tail.next = result

        current1 = current1.next
        current2 = current2.next
        tail = tail.next

    while current1 is None and current2 is not None:

        if carry == 0:
            sum = current2.val
        else:
            sum = current2.val + carry
            carry = 0

        if sum > 9:
            carry = sum // 10
            sum = sum % 10

        result = Node(sum)

        tail.next = result

        current2 = current2.next
        tail = tail.next

    while current2 is None and current1 is not None:

        if carry == 0:
            sum = current1.val
        else:
            sum = current1.val + carry
            carry = 0

        if sum > 9:
            carry = sum // 10
            sum = sum % 10

        result = Node(sum)

        tail.next = result

        current1 = current1.next
        tail = tail.next

    if carry > 0:
        final_carry = Node(carry)
        tail.next = final_carry
        tail = tail.next

    return dummy.next


def print_list(head):

    res = ""
    current = head

    while current.next is not None:
        res += str(current.val) + " -> "
        current = current.next

    res += str(current.val)

    return res


class Test(unittest.TestCase):
    def test_1(self):

        a1 = Node(1)
        a2 = Node(2)
        a3 = Node(6)

        a1.next = a2
        a2.next = a3
        # 1 -> 2 -> 6

        b1 = Node(4)
        b2 = Node(5)
        b3 = Node(3)
        b1.next = b2
        b2.next = b3
        # 4 -> 5 -> 3

        res = add_lists(a1, b1)
        expected = "5 -> 7 -> 9"

        assert print_list(res) == expected

    def test_2(self):

        a1 = Node(1)
        a2 = Node(4)
        a3 = Node(5)
        a4 = Node(7)

        a1.next = a2
        a2.next = a3
        a3.next = a4
        # 1 -> 4 -> 5 -> 7

        b1 = Node(2)
        b2 = Node(3)

        b1.next = b2
        # 2 -> 3

        res = add_lists(a1, b1)
        expected = "3 -> 7 -> 5 -> 7"

        assert print_list(res) == expected

    def test_3(self):

        a1 = Node(9)
        a2 = Node(3)

        a1.next = a2
        # 9 -> 3

        b1 = Node(7)
        b2 = Node(4)
        b1.next = b2
        # 7 -> 4

        res = add_lists(a1, b1)
        expected = "6 -> 8"
        assert print_list(res) == expected

    def test_4(self):

        a1 = Node(9)
        a2 = Node(9)
        a3 = Node(9)

        a1.next = a2
        a2.next = a3
        # 9 -> 9 -> 9

        b1 = Node(6)
        # 6

        res = add_lists(a1, b1)
        expected = "5 -> 0 -> 0 -> 1"

        assert print_list(res) == expected


if __name__ == "__main__":
    unittest.main()
