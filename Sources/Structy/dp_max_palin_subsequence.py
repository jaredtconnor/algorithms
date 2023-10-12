import unittest


def max_palin_subsequence(string):
    memo = {}
    return _max_palin_subsequence(string, 0, len(string) - 1, memo)


def _max_palin_subsequence(string, i, j, memo):
    pair = (i, j)

    # Base cases
    # 1 - if the len of string is 1
    if i == j:
        return 1

    # 2 - if the len of string is 0 or if the indicies cross
    if i > j:
        return 0

    if pair in memo:
        return memo[pair]

    if string[i] == string[j]:
        # Need to make recursive leap of faith
        # Should return the max palindrome in the string
        # need to add 2 to the result to represent the two
        # matching chars that we just matched
        memo[pair] = 2 + _max_palin_subsequence(string, i + 1, j - 1, memo)

    else:
        right_branch = _max_palin_subsequence(string, i + 1, j, memo)
        left_branch = _max_palin_subsequence(string, i, j - 1, memo)
        memo[pair] = max(right_branch, left_branch)

    return memo[pair]


class Test(unittest.TestCase):
    def test_case_1(self):
        res = max_palin_subsequence("luwxult")  # -> 5
        exp = 5
        assert res == exp

    def test_case_2(self):
        res = max_palin_subsequence("xyzaxxzy")  # -> 6
        exp = 6
        assert res == exp

    def test_case_3(self):
        res = max_palin_subsequence("lol")  # -> 3
        exp = 3
        assert res == exp

    def test_case_4(self):
        res = max_palin_subsequence("boabcdefop")  # -> 3
        exp = 3
        assert res == exp

    def test_case_5(self):
        res = max_palin_subsequence("z")  # -> 1
        exp = 1
        assert res == exp

    def test_case_6(self):
        res = max_palin_subsequence("chartreusepugvicefree")  # -> 7
        exp = 7
        assert res == exp

    def test_case_7(self):
        res = max_palin_subsequence("qwueoiuahsdjnweuueueunasdnmnqweuzqwerty")  # -> 15
        exp = 15
        assert res == exp

    def test_case_8(self):
        res = max_palin_subsequence(
            "enamelpinportlandtildecoldpressedironyflannelsemioticsedisonbulbfashionaxe"
        )  # -> 31
        exp = 31
        assert res == exp


if __name__ == "__main__":
    unittest.main()
