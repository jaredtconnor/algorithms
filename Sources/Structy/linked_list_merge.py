import unittest


class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None


def merge_lists(head_a: Node, head_b: Node) -> Node:
    dummy = Node()  # Create a dummy node to link
    tail = dummy  # Maintain a tail
    current1 = head_a
    current2 = head_b

    # Iterate over both lists
    while current1 and current2:
        # Point tail to the lowest of either list
        if current1.val < current2.val:
            tail.next = current1
            current1 = current1.next

        else:
            tail.next = current2
            current2 = current2.next

        # Re-point tail to tail.next
        tail = tail.next

    # If any list is complete after Iterate,
    # point the rest of the list to that list
    if current1 is not None:
        tail.next = current1

    if current2 is not None:
        tail.next = current2

    # Must return dummy next to get rid of extra
    # dummy node
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
        a = Node(5)
        b = Node(7)
        c = Node(10)
        d = Node(12)
        e = Node(20)
        f = Node(28)

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f
        # 5 -> 7 -> 10 -> 12 -> 20 -> 28

        q = Node(6)
        r = Node(8)
        s = Node(9)
        t = Node(25)
        q.next = r
        r.next = s
        s.next = t
        # 6 -> 8 -> 9 -> 25

        res = merge_lists(a, q)
        expected = "5 -> 6 -> 7 -> 8 -> 9 -> 10 -> 12 -> 20 -> 25 -> 28"
        print(f"Expected: {expected} \n Result: {print_list(res)}")
        assert print_list(res) == expected


if __name__ == "__main__":
    unittest.main()
