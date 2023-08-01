import unittest


def counting_change(amount, coins):
    memo = {}
    return _counting_change(amount, coins, 0, memo)


def _counting_change(amount, coins, i, memo):
    key = (amount, i)

    if key in memo:
        return memo[key]

    if amount == 0:
        return 1

    if i == len(coins):
        return 0

    coin = coins[i]

    total_ways = 0
    for qty in range(0, (amount // coin) + 1):
        remainder = amount - (qty * coin)
        total_ways += _counting_change(remainder, coins, i + 1, memo)

    memo[key] = total_ways
    return memo[key]


class Test(unittest.TestCase):
    def test_case_1(self):
        res = counting_change(4, [1, 2, 3])  # -> 4
        exp = 4
        assert res == exp

    def test_case_2(self):
        res = counting_change(8, [1, 2, 3])  # -> 10
        exp = 10
        assert res == exp

    def test_case_3(self):
        res = counting_change(24, [5, 7, 3])  # -> 5
        exp = 5
        assert res == exp

    def test_case_4(self):
        res = counting_change(13, [2, 6, 12, 10])  # -> 0
        exp = 0
        assert res == exp

    def test_case_5(self):
        res = counting_change(512, [1, 5, 10, 25])  # -> 20119
        exp = 20119
        assert res == exp

    def test_case_6(self):
        res = counting_change(1000, [1, 5, 10, 25])  # -> 142511
        exp = 142511
        assert res == exp

    def test_case_7(self):
        res = counting_change(240, [1, 2, 3, 4, 5, 6, 7, 8, 9])  # -> 1525987916
        exp = 1525987916
        assert res == exp


if __name__ == "__main__":
    unittest.main()
