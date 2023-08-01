import unittest


def counting_change(amount, coins):
    return None


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
