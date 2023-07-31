import unittest
import math


def summing_squares(n):

    memo = {}
    return _summing_squares(n, memo)


def _summing_squares(n, memo):

    # DP Memo check
    if n in memo:
        return memo[n]

    # Base case
    if n == 0:
        return 0

    # Set really large at init
    min_squares = float("inf")

    for i in range(1, math.floor(math.sqrt(n)) + 1):
        square = i * i

        # Returns the min_squares required to reach
        num_squares = 1 + _summing_squares(n - square, memo)

        min_squares = min(num_squares, min_squares)

    memo[n] = min_squares
    return memo[n]


class Test(unittest.TestCase):
    def test_case_1(self):
        res = summing_squares(8)
        exp = 2
        assert res == exp

    def test_case_2(self):
        res = summing_squares(12)
        exp = 3
        assert res == exp

    def test_case_3(self):
        res = summing_squares(1)
        exp = 1
        assert res == exp

    def test_case_4(self):
        res = summing_squares(31)
        exp = 4
        assert res == exp

    def test_case_5(self):
        res = summing_squares(50)
        exp = 2
        assert res == exp

    def test_case_6(self):
        res = summing_squares(68)
        exp = 2
        assert res == exp

    def test_case_7(self):
        res = summing_squares(87)
        exp = 4
        assert res == exp


if __name__ == "__main__":
    unittest.main()
