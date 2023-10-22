import unittest


def quickest_concat(s, words):  

    memo = {}

    result = _quickest_concat(s, words, memo)  

    if result == float("inf"): 
        return -1 
    else: 
        return result


def _quickest_concat(s, words, memo):  

    if s in memo: 
        return memo[s]

    if s == "": 
        return 0
   
    min_words = float("inf")
    for word in words: 

        if s.startswith(word):
            suffix = s[len(word): ]

            attempt = 1 + _quickest_concat(suffix, words, memo)  
            min_words = min(attempt, min_words)

    memo[s] = min_words
    return memo[s]

class Test(unittest.TestCase):
    def test_case_1(self):

        res = quickest_concat('caution', ['ca', 'ion', 'caut', 'ut']) # -> 2
        exp = 2 
        assert res == exp

    def test_case_2(self):
        res = quickest_concat('caution', ['ion', 'caut', 'caution']) # -> 1
        exp = 1 
        assert res == exp

    def test_case_3(self):
        res = quickest_concat('respondorreact', ['re', 'or', 'spond', 'act', 'respond']) # -> 4
        exp = 4 
        assert res == exp

    def test_case_4(self):
        res = quickest_concat('simchacindy', ['sim', 'simcha', 'acindy', 'ch']) # -> 3
        exp = 3 
        assert res == exp

    def test_case_6(self):   
        res = quickest_concat('simchacindy', ['sim', 'simcha', 'acindy']) # -> -1
        exp = -1 
        assert res == exp

    def test_case_7(self): 
        res = quickest_concat('uuuuuu', ['u', 'uu', 'uuu', 'uuuu']) # -> 2
        exp = 2 
        assert res == exp

    def test_case_8(self): 
        res = quickest_concat('rongbetty', ['wrong', 'bet']) # -> -1
        exp = -1
        assert res == exp 

    def test_case_9(self): 
        res = quickest_concat('uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu', ['u', 'uu', 'uuu', 'uuuu', 'uuuuu']) # -> 7
        exp = 7
        assert res == exp 

if __name__ == "__main__":
    unittest.main()
