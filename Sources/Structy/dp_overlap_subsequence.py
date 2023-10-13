import unittest


def overlap_subsequence(string_1, string_2): 
    memo = {}
    return _overlap_subsequence(string_1, string_2, 0, 0, memo)


def _overlap_subsequence(string_1, string_2, i, j, memo):  

    pair = (i, j) 

    # Base cases - if the index of either string 
    # is longer than the len of each string
    # could also use: 
    # if i == len(string_1) or j ==  len(string_2):
    if len(string_1) - i == 0 or len(string_2) - j == 0: 
        return 0 

    if pair in memo: 
        return memo[pair]

    if string_1[i] == string_2[j]: 
        memo[pair] = 1 + _overlap_subsequence(string_1, string_2, i+1, j+1, memo)

    else: 
        right_path = _overlap_subsequence(string_1, string_2, i+1, j, memo)
        left_path = _overlap_subsequence(string_1, string_2, i, j+1, memo) 

        memo[pair] = max(right_path, left_path)

    return memo[pair]

class Test(unittest.TestCase):
    def test_case_1(self):
        res = overlap_subsequence("dogs", "daogt") # -> 3
        exp = 3
        assert res == exp

    def test_case_2(self):
        res = overlap_subsequence("xcyats", "criaotsi") # -> 4
        exp = 4
        assert res == exp

    def test_case_3(self):
        res = overlap_subsequence("xfeqortsver", "feeeuavoeqr") # -> 5
        exp = 5
        assert res == exp

    def test_case_4(self): 
        res = overlap_subsequence("kinfolklivemustache", "bespokekinfolksnackwave") # -> 11
        exp = 11
        assert res == exp

    def test_case_5(self):
        res = overlap_subsequence(
          "mumblecorebeardleggingsauthenticunicorn",
          "succulentspughumblemeditationlocavore"
        ) # -> 15
        exp = 15
        assert res == exp

if __name__ == "__main__":
    unittest.main()
