import unittest


def min_change(amount, coins):

    memo = {}

    min_coins = _min_change(amount, coins, memo)

    if min_coins == float("inf"):
        return -1

    return min_coins


def _min_change(amount, coins, memo):

    if amount in memo:
        return memo[amount]

    # Base case:
    if amount == 0:
        return 0

    if amount < 0:
        return float("inf")

    # returns the min amount of coins
    min_coins = float("inf")

    for coin in coins:

        num_coins = 1 + _min_change(amount - coin, coins, memo)

        if num_coins < min_coins:
            min_coins = num_coins

    memo[amount] = min_coins
    return min_coins


class Test(unittest.TestCase):
    def test_case_1(self):

        res = min_change(8, [1, 5, 4, 12])  # -> 2
        expected = 2
        assert res == expected

    def test_case_2(self):

        expected = min_change(13, [1, 9, 5, 14, 30])  # -> 5
        res = 5
        assert res == expected

    def test_case_3(self):

        expected = min_change(23, [2, 5, 7])  # -> 4
        res = 4
        assert res == expected

    def test_case_4(self):

        expected = min_change(102, [1, 5, 10, 25])  # -> 6
        res = 6
        assert res == expected

    def test_case_5(self):

        expected = min_change(200, [1, 5, 10, 25])  # -> 8
        res = 8
        assert res == expected

    def test_case_6(self):

        expected = min_change(2017, [4, 2, 10])  # -> -1
        res = -1
        assert res == expected

    def test_case_7(self):

        expected = min_change(271, [10, 8, 265, 24])  # -> -1
        res = -1
        assert res == expected

    def test_case_8(self):

        expected = min_change(0, [4, 2, 10])  # -> 0
        res = 0
        assert res == expected

    def test_case_9(self):

        expected = min_change(0, [])  # -> 0
        res = 0
        assert res == expected


if __name__ == "__main__":
    unittest.main()
