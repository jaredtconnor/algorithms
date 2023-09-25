import unittest


def max_palin_subsequence(string): 
    pass

class Test(unittest.TestCase):
    def test_case_1(self):
        res = max_palin_subsequence("luwxult") # -> 5 
        exp = 5 
        assert res == exp  

    def test_case_2(self):
        res = max_palin_subsequence("xyzaxxzy") # -> 6
        exp = 6
        assert res == exp  

    def test_case_3(self):
        res = max_palin_subsequence("lol") # -> 3
        exp = 3
        assert res == exp 

    def test_case_4(self):
        res = max_palin_subsequence("boabcdefop") # -> 3
        exp = 3
        assert res == exp   

    def test_case_5(self):
        res = max_palin_subsequence("z") # -> 1
        exp = 1
        assert res == exp   

    def test_case_6(self):
        res = max_palin_subsequence("chartreusepugvicefree") # -> 7
        exp = 7
        assert res == exp  

    def test_case_7(self):
        res = max_palin_subsequence("qwueoiuahsdjnweuueueunasdnmnqweuzqwerty") # -> 15
        exp = 15
        assert res == exp   

    def test_case_8(self):
        res = max_palin_subsequence("enamelpinportlandtildecoldpressedironyflannelsemioticsedisonbulbfashionaxe") # -> 31
        exp = 31
        assert res == exp    

if __name__ == "__main__":
    unittest.main()
