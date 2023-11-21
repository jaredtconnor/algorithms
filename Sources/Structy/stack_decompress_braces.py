import unittest


def decompress_braces(string):
    pass


class Test(unittest.TestCase):
    def test_1(self):
        res = decompress_braces("2{q}3{tu}v")
        exp = "qqtututuv"
        assert res == exp

    def test_2(self):
        res = decompress_braces("ch3{ao}")
        exp = "chaoaoao"
        assert res == exp

    def test_3(self):
        res = decompress_braces("2{y3{o}}s")
        exp = "yoooyooos"
        assert res == exp

    def test_4(self):
        res = decompress_braces("z3{a2{xy}b}")
        exp = "zaxyxybaxyxybaxyxyb"
        assert res == exp

    def test_5(self):
        res = decompress_braces("2{3{r4{e}r}io}")
        exp = "reeeerreeeerreeeerioreeeerreeeerreeeerio"
        assert res == exp

    def test_6(self):
        res = decompress_braces("go3{spinn2{ing}s}")
        exp = "gospinningingsspinningingsspinningings"
        assert res == exp

    def test_7(self):
        res = decompress_braces("2{l2{if}azu}l")
        exp = "lififazulififazul"
        assert res == exp

    def test_8(self):
        res = decompress_braces("3{al4{ec}2{icia}}")
        exp = "alececececiciaiciaalececececiciaiciaalececececiciaicia"
        assert res == exp


if __name__ == "__main__":
    unittest.main()
