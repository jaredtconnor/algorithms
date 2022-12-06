import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def sum_list(head):

    sum = 0
    current = head

    while current is not None:

        sum += current.val
        current = current.next

    return sum


class Test(unittest.TestCase):
    def test_1(self):

        x = Node(38)
        y = Node(4)

        x.next = y

        self.assertEqual(sum_list(x), 42)

    def test_2(self):
        z = Node(100)

        self.assertEqual(sum_list(z), 100)

    def test_3(self):
        self.assertEqual(sum_list(None), 0)


if __name__ == "__main__":
    unittest.main()
