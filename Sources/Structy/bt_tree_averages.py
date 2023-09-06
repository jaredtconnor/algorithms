import unittest
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def level_averages(root: Node):
    if root is None:
        return []

    levels = []
    stack = [(root, 0)]

    while stack:
        current, level_num = stack.pop()

        if len(levels) == level_num:
            levels.append([current.val])
        else:
            levels[level_num].append(current.val)

        if current.right is not None:
            stack.append((current.right, level_num + 1))

        if current.left is not None:
            stack.append((current.left, level_num + 1))

    avgs = []

    for level in levels:
        avgs.append(sum(level) / len(level))

    return avgs


def level_averages_bfs(root: Node):
    if root is None:
        return []

    levels = []
    queue = deque([(root, 0)])

    while queue:
        current, level_num = queue.popleft()

        if len(levels) == level_num:
            levels.append([current.val])
        else:
            levels[level_num].append(current.val)

        if current.left is not None:
            queue.append((current.left, level_num + 1))

        if current.right is not None:
            queue.append((current.right, level_num + 1))

    avgs = []

    for level in levels:
        avgs.append(sum(level) / len(level))

    return avgs


class Test(unittest.TestCase):
    def test_case_1(self):
        a = Node(3)
        b = Node(11)
        c = Node(4)
        d = Node(4)
        e = Node(-2)
        f = Node(1)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        #       3
        #    /    \
        #   11     4
        #  / \      \
        # 4   -2     1

        res = level_averages(a)
        expected = [3, 7.5, 1]
        assert res == expected

    def test_case_2(self):
        a = Node(5)
        b = Node(11)
        c = Node(54)
        d = Node(20)
        e = Node(15)
        f = Node(1)
        g = Node(3)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        e.left = f
        e.right = g

        #        5
        #     /    \
        #    11    54
        #  /   \
        # 20   15
        #      / \
        #     1  3

        res = level_averages(a)
        expected = [5, 32.5, 17.5, 2]
        assert res == expected

    def test_case_3(self):
        a = Node(-1)
        b = Node(-6)
        c = Node(-5)
        d = Node(-3)
        e = Node(0)
        f = Node(45)
        g = Node(-1)
        h = Node(-2)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        #        -1
        #      /   \
        #    -6    -5
        #   /  \     \
        # -3   0     45
        #     /       \
        #    -1       -2

        res = level_averages(a)
        expected = [-1, -5.5, 14, -1.5]
        assert res == expected

    def test_case_4(self):
        q = Node(13)
        r = Node(4)
        s = Node(2)
        t = Node(9)
        u = Node(2)
        v = Node(42)

        q.left = r
        q.right = s
        r.right = t
        t.left = u
        u.right = v

        #        13
        #      /   \
        #     4     2
        #      \
        #       9
        #      /
        #     2
        #    /
        #   42

        res = level_averages(q)
        expected = [13, 3, 9, 2, 42]
        assert res == expected

    def test_case_5(self):
        res = level_averages(None)
        expected = []
        assert res == expected

    def test_case_6(self):
        a = Node(3)
        b = Node(11)
        c = Node(4)
        d = Node(4)
        e = Node(-2)
        f = Node(1)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        #       3
        #    /    \
        #   11     4
        #  / \      \
        # 4   -2     1

        res = level_averages_bfs(a)
        expected = [3, 7.5, 1]
        assert res == expected

    def test_case_7(self):
        a = Node(5)
        b = Node(11)
        c = Node(54)
        d = Node(20)
        e = Node(15)
        f = Node(1)
        g = Node(3)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        e.left = f
        e.right = g

        #        5
        #     /    \
        #    11    54
        #  /   \
        # 20   15
        #      / \
        #     1  3

        res = level_averages_bfs(a)
        expected = [5, 32.5, 17.5, 2]
        assert res == expected

    def test_case_8(self):
        a = Node(-1)
        b = Node(-6)
        c = Node(-5)
        d = Node(-3)
        e = Node(0)
        f = Node(45)
        g = Node(-1)
        h = Node(-2)

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        #        -1
        #      /   \
        #    -6    -5
        #   /  \     \
        # -3   0     45
        #     /       \
        #    -1       -2

        res = level_averages_bfs(a)
        expected = [-1, -5.5, 14, -1.5]
        assert res == expected

    def test_case_9(self):
        q = Node(13)
        r = Node(4)
        s = Node(2)
        t = Node(9)
        u = Node(2)
        v = Node(42)

        q.left = r
        q.right = s
        r.right = t
        t.left = u
        u.right = v

        #        13
        #      /   \
        #     4     2
        #      \
        #       9
        #      /
        #     2
        #    /
        #   42

        res = level_averages_bfs(q)
        expected = [13, 3, 9, 2, 42]
        assert res == expected

    def test_case_10(self):
        res = level_averages_bfs(None)
        expected = []
        assert res == expected


if __name__ == "__main__":
    unittest.main()
