import unittest


def count_paths(grid):
    memo = {}

    return _count_paths(grid, 0, 0, memo)


def _count_paths(grid, r, c, memo):
    # Create POS for key in memo
    pos = (r, c)

    # If pos found, return stored val
    if pos in memo:
        return memo[pos]

    # check if row out of bounds
    if r == len(grid) or c == len(grid[0]) or grid[r][c] == "X":
        return 0

    # BASE CASE - check if target hit, return 1 if end found
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return 1

    # RECURSIVE CALL - Progress position towards target
    down_count = _count_paths(grid, r + 1, c, memo)
    right_count = _count_paths(grid, r, c + 1, memo)

    memo[pos] = down_count + right_count

    return memo[pos]


class Test(unittest.TestCase):
    def test_case_1(self):
        grid = [
            ["O", "O"],
            ["O", "O"],
        ]
        res = count_paths(grid)  # -> 2
        expected = 2
        assert res == expected

    def test_case_2(self):
        grid = [
            ["O", "O", "X"],
            ["O", "O", "O"],
            ["O", "O", "O"],
        ]

        res = count_paths(grid)  # -> 5

        expected = 5
        assert res == expected

    def test_case_3(self):
        grid = [
            ["O", "O", "O"],
            ["O", "O", "X"],
            ["O", "O", "O"],
        ]

        res = count_paths(grid)  # -> 3

        expected = 3
        assert res == expected

    def test_case_4(self):
        grid = [
            ["O", "O", "O"],
            ["O", "X", "X"],
            ["O", "O", "O"],
        ]
        res = count_paths(grid)  # -> 1

        expected = 1
        assert res == expected

    def test_case_5(self):
        grid = [
            ["O", "O", "X", "O", "O", "O"],
            ["O", "O", "X", "O", "O", "O"],
            ["X", "O", "X", "O", "O", "O"],
            ["X", "X", "X", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O"],
        ]
        res = count_paths(grid)  # -> 0
        expected = 0
        assert res == expected

    def test_case_6(self):
        grid = [
            ["O", "O", "X", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "X"],
            ["X", "O", "O", "O", "O", "O"],
            ["X", "X", "X", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O"],
        ]
        res = count_paths(grid)  # -> 42

        expected = 42
        assert res == expected

    def test_case_7(self):
        grid = [
            ["O", "O", "X", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "X"],
            ["X", "O", "O", "O", "O", "O"],
            ["X", "X", "X", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "X"],
        ]
        res = count_paths(grid)  # -> 0
        expected = 0
        assert res == expected

    def test_case_8(self):
        grid = [
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
        ]
        res = count_paths(grid)  # -> 40116600

        expected = 40116600
        assert res == expected

    def test_case_9(self):
        grid = [
            ["O", "O", "X", "X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "X", "X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "X", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
            ["X", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O", "O"],
            ["X", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "X", "X", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "X", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O"],
            ["X", "X", "X", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "X", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "X", "X", "O", "O", "O", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O"],
            ["O", "O", "O", "O", "O", "O", "O", "O", "X", "O", "O", "O", "O", "O", "O"],
        ]
        res = count_paths(grid)  # -> 3190434
        expected = 3190434
        assert res == expected


if __name__ == "__main__":
    unittest.main()
