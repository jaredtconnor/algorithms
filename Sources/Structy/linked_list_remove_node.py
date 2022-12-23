import unittest


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def remove_node(head: Node, target: str) -> bool:

    # Edge case
    if head.val == target:
        return head.next

    current = head
    prev = None

    while current is not None:

        if current.val == target:
            prev.next = current.next
            break

        prev = current
        current = current.next

    return head


def remove_node_recursive(head: Node, target: str):

    # Base case
    if head is None:
        return

    if head.val == target:
        return head.next

    head.next = remove_node_recursive(head.next, target)

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
        e = Node("e")
        f = Node("f")

        a.next = b
        b.next = c
        c.next = d
        d.next = e
        e.next = f
        # a -> b -> c -> d -> e -> f

        res = remove_node(a, "c")
        expected = "a -> b -> d -> e -> f"

        assert print_list(res) == expected

    def test_2(self):

        x = Node("x")
        y = Node("y")
        z = Node("z")

        x.next = y
        y.next = z
        # x -> y -> z

        res = remove_node(x, "z")  # x -> y`
        expected = "x -> y"

        assert print_list(res) == expected

    def test_3(self):
        q = Node("q")
        r = Node("r")
        s = Node("s")

        q.next = r
        r.next = s
        # q -> r -> s

        res = remove_node(q, "q")  # r -> s`

        expected = "r -> s"
        assert print_list(res) == expected

    def test_4(self):
        node1 = Node("h")
        node2 = Node("i")
        node3 = Node("j")
        node4 = Node("i")

        node1.next = node2
        node2.next = node3
        node3.next = node4
        # h -> i -> j -> i

        res = remove_node(node1, "i")  # h -> j -> i`

        expected = "h -> j -> i"

        assert print_list(res) == expected

    def test_5(self):

        t = Node("t")
        # t

        res = remove_node(t, "t")  # None`
        expected = None

        assert res == expected

    def test_6(self):

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
        # a -> b -> c -> d -> e -> f

        res = remove_node_recursive(a, "c")
        expected = "a -> b -> d -> e -> f"

        assert print_list(res) == expected

    def test_7(self):

        x = Node("x")
        y = Node("y")
        z = Node("z")

        x.next = y
        y.next = z
        # x -> y -> z

        res = remove_node_recursive(x, "z")  # x -> y`
        expected = "x -> y"

        assert print_list(res) == expected

    def test_8(self):
        q = Node("q")
        r = Node("r")
        s = Node("s")

        q.next = r
        r.next = s
        # q -> r -> s

        res = remove_node_recursive(q, "q")  # r -> s`

        expected = "r -> s"
        assert print_list(res) == expected

    def test_9(self):
        node1 = Node("h")
        node2 = Node("i")
        node3 = Node("j")
        node4 = Node("i")

        node1.next = node2
        node2.next = node3
        node3.next = node4
        # h -> i -> j -> i

        res = remove_node_recursive(node1, "i")  # h -> j -> i`

        expected = "h -> j -> i"

        assert print_list(res) == expected

    def test_10(self):

        t = Node("t")
        # t

        res = remove_node_recursive(t, "t")  # None`
        expected = None

        assert res == expected


if __name__ == "__main__":
    unittest.main()
