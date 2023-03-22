import unittest


def sum_possible(amount, numbers):

    memo = {}

    return _sum_possible(amount, numbers, memo)


def _sum_possible(amount, numbers, memo):

    if amount in memo:
        return memo[amount]

    if amount < 0:
        return False

    if amount == 0:
        return True

    for num in numbers:
        if _sum_possible(amount - num, numbers, memo) is True:

            memo[amount] = True
            return True

    memo[amount] = False
    return False


class Test(unittest.TestCase):
    def test_case_1(self):

        res = sum_possible(8, [5, 12, 4])  # -> True, 4 + 4
        expected = True
        assert res == expected

    def test_case_2(self):

        res = sum_possible(15, [6, 2, 10, 19])  # -> False
        expected = False
        assert res == expected

    def test_case_3(self):

        res = sum_possible(13, [6, 2, 1])  # -> True
        expected = True
        assert res == expected

    def test_case_4(self):

        res = sum_possible(103, [6, 20, 1])  # -> True
        expected = True
        assert res == expected

    def test_case_5(self):

        res = sum_possible(12, [])  # -> False
        expected = False
        assert res == expected

    def test_case_6(self):

        res = sum_possible(12, [12])  # -> True
        expected = True
        assert res == expected

    def test_case_7(self):

        res = sum_possible(0, [])  # -> True
        expected = True
        assert res == expected

    def test_case_8(self):

        res = sum_possible(271, [10, 8, 265, 24])  # -> False
        expected = False
        assert res == expected

    def test_case_9(self):

        res = sum_possible(2017, [4, 2, 10])  # -> False
        expected = False
        assert res == expected

    def test_case_10(self):

        res = sum_possible(13, [3, 5])  # -> true
        expected = True
        assert res == expected


if __name__ == "__main__":
    unittest.main()
