import unittest


def max_path_sum(grid):
    memo = {}

    return _max_path_sum(grid, 0, 0, memo)


def _max_path_sum(grid, r, c, memo):
    # Create POS for key in memo
    pos = (r, c)

    # If pos found, return stored val
    if pos in memo:
        return memo[pos]

    # check if row out of bounds
    if r == len(grid) or c == len(grid[0]) or grid[r][c] == "X":
        return float("-inf")

    # BASE CASE - check if target hit, return 1 if end found
    if r == len(grid) - 1 and c == len(grid[0]) - 1:
        return grid[r][c]

    # RECURSIVE CALL - Progress position towards target
    down_sum = _max_path_sum(grid, r + 1, c, memo)
    right_sum = _max_path_sum(grid, r, c + 1, memo)

    max_sum = max(down_sum, right_sum)

    memo[pos] = grid[r][c] + max_sum

    return memo[pos]


class Test(unittest.TestCase):
    def test_case_1(self):
        grid = [
            [1, 3, 12],
            [5, 1, 1],
            [3, 6, 1],
        ]
        res = max_path_sum(grid)  # -> 18
        exp = 18
        assert res == exp

    def test_case_2(self):
        grid = [
            [1, 2, 8, 1],
            [3, 1, 12, 10],
            [4, 0, 6, 3],
        ]
        res = max_path_sum(grid)  # -> 36
        exp = 36
        assert res == exp

    def test_case_3(self):
        grid = [
            [1, 2, 8, 1],
            [3, 10, 12, 10],
            [4, 0, 6, 3],
        ]
        res = max_path_sum(grid)  # -> 39
        exp = 39
        assert res == exp

    def test_case_4(self):
        grid = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        res = max_path_sum(grid)  # -> 27
        exp = 27
        assert res == exp

    def test_case_5(self):
        grid = [
            [1, 1, 3, 1, 1, 1, 1, 4, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 2, 1, 1, 6, 1, 1, 5, 1, 1, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 5, 1, 1, 1, 1, 0, 1, 1, 1, 1],
            [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [2, 1, 1, 1, 1, 8, 1, 1, 1, 1, 1, 1, 1],
            [2, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 9, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 8, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 42, 1, 1, 1, 1, 1, 1, 1, 8, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ]
        res = max_path_sum(grid)  # -> 82
        exp = 82
        assert res == exp


if __name__ == "__main__":
    unittest.main()
