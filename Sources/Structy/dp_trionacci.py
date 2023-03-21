import unittest


def tribonacci(n):

    memo = {}

    return _trib(n, memo)


def _trib(n, memo):

    if n in memo:
        return memo[n]

    if n == 0:
        return 0

    if n == 1 or n == 2:
        return 1

    memo[n] = +_trib(n - 3, memo) + _trib(n - 2, memo) + _trib(n - 1, memo)

    return memo[n]


class Test(unittest.TestCase):
    def test_case_1(self):

        res = tribonacci(0)
        expected = 0
        assert res == expected

    def test_case_2(self):

        res = tribonacci(1)
        expected = 0
        assert res == expected

    def test_case_3(self):

        res = tribonacci(2)
        expected = 1
        assert res == expected

    def test_case_4(self):

        res = tribonacci(2)
        expected = 1
        assert res == expected

    def test_case_5(self):

        res = tribonacci(5)
        expected = 4
        assert res == expected

    def test_case_6(self):

        res = tribonacci(7)
        expected = 13
        assert res == expected

    def test_case_7(self):

        res = tribonacci(14)
        expected = 927
        assert res == expected

    def test_case_8(self):

        res = tribonacci(20)
        expected = 35890
        assert res == expected

    def test_case_9(self):

        res = tribonacci(37)
        expected = 1132436852
        assert res == expected

    def test_case_10(self):

        res = tribonacci(37)
        expected = 1132436852
        assert res == expected


if __name__ == "__main__":
    # unittest.main()

    res = tribonacci(14)
    expected = 0

    print(f"Res is {res}")
