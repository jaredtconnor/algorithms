import unittest


def fib(n):

    # Base case 0
    if n == 0:
        return 0

    # Base case 1
    if n == 1:
        return 1

    return 0


class Test(unittest.TestCase):
    def test_case_1(self):

        res = fib(0)
        expected = 0
        assert res == expected

    def test_case_2(self):

        res = fib(1)
        expected = 1
        assert res == expected

    def test_case_3(self):

        res = fib(2)
        expected = 1
        assert res == expected

    def test_case_4(self):

        res = fib(3)
        expected = 2
        assert res == expected

    def test_case_5(self):

        res = fib(4)
        expected = 3
        assert res == expected

    def test_case_6(self):

        res = fib(5)
        expected = 5
        assert res == expected

    def test_case_7(self):

        res = fib(35)
        expected = 9227465
        assert res == expected

    def test_case_8(self):

        res = fib(46)
        expected = 1836311903
        assert res == expected


if __name__ == "__main__":
    unittest.main()
