import unittest


def can_concat(s, words):
    memo = {}

    return _can_concat(s, words, memo)


def _can_concat(s, words, memo):
    if s in memo:
        return memo[s]

    # Base case 
    # string is empty 
    # which we can make with nothing so 
    # return True
    if s == "":
        return True

    for word in words:
        if s.startswith(word):
            suffix = s[len(word) :]

            if _can_concat(suffix, words, memo):
                memo[s] = True
                return memo[s]

    memo[s] = False
    return memo[s]


class Test(unittest.TestCase):
    def test_case_1(self):
        res = can_concat("oneisnone", ["one", "none", "is"])  #  -> True
        exp = True
        assert res == exp

    def test_case_2(self):
        res = can_concat("oneisnone", ["on", "e", "is"])  #  -> False
        exp = False
        assert res == exp

    def test_case_3(self):
        res = can_concat("oneisnone", ["on", "e", "is", "n"])  #  -> True
        exp = True
        assert res == exp

    def test_case_4(self):
        res = can_concat("foodisgood", ["is", "g", "ood", "f"])  #  -> True
        exp = True
        assert res == exp

    def test_case_5(self):
        res = can_concat("santahat", ["santah", "hat"])  #  -> False
        exp = False
        assert res == exp

    def test_case_6(self):
        res = can_concat(
            "rrrrrrrrrrrrrrrrrrrrrrrrrrx", ["r", "rr", "rrr", "rrrr", "rrrrr", "rrrrrr"]
        )  #  -> False
        exp = False
        assert res == exp

    def test_case_7(self):
        res = can_concat("fooisgood", ["foo", "is", "g", "ood", "f"])  # -> True
        exp = True
        assert res == exp


if __name__ == "__main__":
    unittest.main()
