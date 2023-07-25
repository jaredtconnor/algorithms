import unittest

def summing_squares(n):
    return None


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
        exp = 24
        assert res == exp


if __name__ == "__main__":
    unittest.main()
