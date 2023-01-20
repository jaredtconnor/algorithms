import unittest 
from collections import deque


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def tree_levels_dfs(root: Node ):

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
    
    return levels  


def tree_levels_bfs(root: Node):  

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
    
    return levels  


def tree_levels_recursive(root: None): 
    
    levels = []

    fill_levels(root, levels, 0)
        
    return levels

def fill_levels(current, levels, level_num):
    
    # Base case 
    if current is None: 
        return 

    if len(levels) == level_num: 
        levels.append([current.val]) 
    else: 
        levels[level_num].append(current.val)

    fill_levels(current.left, levels, level_num + 1)
    fill_levels(current.right, levels, level_num + 1)

class Test(unittest.TestCase):
    def test_case_1(self):

        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        #      a
        #    /   \
        #   b     c
        #  / \     \
        # d   e     f

        res = tree_levels_dfs(a)  # ->

        expected = [["a"], ["b", "c"], ["d", "e", "f"]]

        assert res == expected

    def test_case_2(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        g = Node("g")
        h = Node("h")
        i = Node("i")

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        e.right = h
        f.left = i

        #         a
        #      /    \
                #     b      c
        #   /  \      \
                #  d    e      f
        #      / \    /
        #     g  h   i

        res = tree_levels_dfs(a)  # ->
        expected = [["a"], ["b", "c"], ["d", "e", "f"], ["g", "h", "i"]]

        assert res == expected

    def test_case_3(self):

        q = Node("q")
        r = Node("r")
        s = Node("s")
        t = Node("t")
        u = Node("u")
        v = Node("v")

        q.left = r
        q.right = s
        r.right = t
        t.left = u
        u.right = v

        #      q
        #    /   \
                #   r     s
        #    \
                #     t
        #    /
        #   u
        #  /
        # v

        res = tree_levels_dfs(q)

        expected = [["q"], ["r", "s"], ["t"], ["u"], ["v"]]

        assert res == expected

    def test_case_4(self):

        res = tree_levels_dfs(None)
        expected = []

        assert res == expected

    def test_case_5(self):

        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        #      a
        #    /   \
        #   b     c
        #  / \     \
        # d   e     f

        res = tree_levels_bfs(a)  # ->

        expected = [["a"], ["b", "c"], ["d", "e", "f"]]

        assert res == expected

    def test_case_6(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        g = Node("g")
        h = Node("h")
        i = Node("i")

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        e.right = h
        f.left = i

        #         a
        #      /    \
                #     b      c
        #   /  \      \
                #  d    e      f
        #      / \    /
        #     g  h   i

        res = tree_levels_bfs(a)  # ->
        expected = [["a"], ["b", "c"], ["d", "e", "f"], ["g", "h", "i"]]

        assert res == expected

    def test_case_7(self):

        q = Node("q")
        r = Node("r")
        s = Node("s")
        t = Node("t")
        u = Node("u")
        v = Node("v")

        q.left = r
        q.right = s
        r.right = t
        t.left = u
        u.right = v

        #      q
        #    /   \
                #   r     s
        #    \
                #     t
        #    /
        #   u
        #  /
        # v

        res = tree_levels_bfs(q)

        expected = [["q"], ["r", "s"], ["t"], ["u"], ["v"]]

        assert res == expected

    def test_case_8(self):

        res = tree_levels_bfs(None)
        expected = []

        assert res == expected

    
    def test_case_9(self):

        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f

        #      a
        #    /   \
        #   b     c
        #  / \     \
        # d   e     f

        res = tree_levels_recursive(a)  # ->

        expected = [["a"], ["b", "c"], ["d", "e", "f"]]

        assert res == expected

    def test_case_10(self):
        a = Node("a")
        b = Node("b")
        c = Node("c")
        d = Node("d")
        e = Node("e")
        f = Node("f")
        g = Node("g")
        h = Node("h")
        i = Node("i")

        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        e.right = h
        f.left = i

        #         a
        #      /    \
                #     b      c
        #   /  \      \
                #  d    e      f
        #      / \    /
        #     g  h   i

        res = tree_levels_recursive(a)  # ->
        expected = [["a"], ["b", "c"], ["d", "e", "f"], ["g", "h", "i"]]

        assert res == expected

    def test_case_11(self):

        q = Node("q")
        r = Node("r")
        s = Node("s")
        t = Node("t")
        u = Node("u")
        v = Node("v")

        q.left = r
        q.right = s
        r.right = t
        t.left = u
        u.right = v

        #      q
        #    /   \
            #   r     s
        #    \
                #     t
        #    /
        #   u
        #  /
        # v

        res = tree_levels_recursive(q)

        expected = [["q"], ["r", "s"], ["t"], ["u"], ["v"]]

        assert res == expected

    def test_case_12(self):

        res = tree_levels_recursive(None)
        expected = []

        assert res == expected


if __name__ == "__main__":
    unittest.main()
