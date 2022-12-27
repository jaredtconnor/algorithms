import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def add_lists_solution1(input1: list, input2: list):

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


def add_lists(head1: list, head2: list):

    carry = 0
    current1 = head1
    current2 = head2
    dummy = Node(None)
    tail = dummy

    while current1 is not None or current2 is not None or carry == 1:

        val_1 = 0 if current1 is None else current1.val
        val_2 = 0 if current2 is None else current2.val

        sum = val_1 + val_2 + carry
        carry = 1 if sum > 9 else 0
        digit = sum % 10

        tail.next = Node(digit)
        tail = tail.next

        if current1 is not None:
            current1 = current1.next

        if current2 is not None:
            current2 = current2.next

    return dummy.next


def add_lists_recursive(head1: list, head2: list, carry=0):

    # Stopping conidtion
    if head1 is None and head2 is None and carry == 0:
        return None

    val_1 = 0 if head1 is None else head1.val
    val_2 = 0 if head2 is None else head2.val

    sum = val_1 + val_2 + carry
    next_carry = 1 if sum > 9 else 0
    digit = sum % 10

    result = Node(digit)

    next_1 = None if head1 is None else head1.next
    next_2 = None if head2 is None else head2.next

    result.next = add_lists_recursive(next_1, next_2, next_carry)

    return result


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

    def test_5(self):

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

        res = add_lists_recursive(a1, b1)
        expected = "5 -> 7 -> 9"

        assert print_list(res) == expected

    def test_6(self):

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

        res = add_lists_recursive(a1, b1)
        expected = "3 -> 7 -> 5 -> 7"

        assert print_list(res) == expected

    def test_7(self):

        a1 = Node(9)
        a2 = Node(3)

        a1.next = a2
        # 9 -> 3

        b1 = Node(7)
        b2 = Node(4)
        b1.next = b2
        # 7 -> 4

        res = add_lists_recursive(a1, b1)
        expected = "6 -> 8"
        assert print_list(res) == expected

    def test_8(self):

        a1 = Node(9)
        a2 = Node(9)
        a3 = Node(9)

        a1.next = a2
        a2.next = a3
        # 9 -> 9 -> 9

        b1 = Node(6)
        # 6

        res = add_lists_recursive(a1, b1)
        expected = "5 -> 0 -> 0 -> 1"

        assert print_list(res) == expected


if __name__ == "__main__":

    unittest.main()
