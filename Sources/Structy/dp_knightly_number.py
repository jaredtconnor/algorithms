from math import prod
import unittest

def knightly_number(n, m, kr, kc, pr, pc):   
    
    memo = {}

    return _knightly_number(n, m, kr, kc, pr, pc, memo)

def _knightly_number(n, m, kr, kc, pr, pc, memo):  

    key = (m, kr, kc) 

    if key in memo: 
        return memo[key]

    if kr < 0 or kr >= n or kc < 0 or kc >= n:
        return 0  
    
    if m == 0: 
        if (kr, kc) == (pr, pc):  
            return 1
        else: 
            return 0
    
    neighbor_positions = [
    ( kr + 2, kc + 1 ),
    ( kr - 2, kc + 1 ),
    ( kr + 2, kc - 1 ),
    ( kr - 2, kc - 1 ),
    ( kr + 1, kc + 2 ),
    ( kr - 1, kc + 2 ),
    ( kr + 1, kc - 2 ),
    ( kr - 1, kc - 2 ),
  ]
    
    count = 0 
    for neighbor_pos in neighbor_positions:   
        neighbor_row, neighbor_col = neighbor_pos 
        count += _knightly_number(n, m - 1, neighbor_row, neighbor_col, pr, pc, memo) 
    
    memo[key] = count
    return memo[key] 

class Test(unittest.TestCase):
    def test_case_1(self):
        res = knightly_number(8, 2, 4, 4, 5, 5) # -> 2
        exp = 2 
        assert res == exp

    def test_case_2(self):
        res = knightly_number(8, 2, 7, 1, 7, 1) # -> 3 
        exp = 3  
        print(f"Returned value is {res} | Expected value is {exp}")
        assert res == exp

    def test_case_3(self):
        res = knightly_number(8, 2, 5, 4, 5, 4) # -> 8
        exp = 8  
        assert res == exp

    def test_case_4(self):
        res = knightly_number(8, 3, 5, 2, 4, 4) # -> 21
        exp = 21 
        assert res == exp

    def test_case_5(self):
        res = knightly_number(20, 6, 18, 7, 10, 15) # -> 60
        exp = 60 
        assert res == exp

    def test_case_6(self):
        res = knightly_number(20, 12, 8, 3, 9, 14) # -> 98410127
        exp = 98410127 
        assert res == exp

    def test_case_7(self):
        res = knightly_number(8, 2, 0, 0, 1, 1) # -> 0
        exp = 0 
        assert res == exp

if __name__ == "__main__":
    unittest.main()
