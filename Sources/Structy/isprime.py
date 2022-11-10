import unittest  
from math import sqrt, floor

def isPrime_naive(num): 

    if num < 2: 
        return False

    for i in range(2, num): 

        if num % i == 0: 
            return False   

    return True

def isPrime_sqrt(num):    

    if num < 2: 
        return False

    for i in range(2, floor(sqrt(num) + 1)): 

        if num % i == 0: 
            return False

    return True

class Test(unittest.TestCase):

    test_cases = { 
        (2, True), 
        (3, True), 
        (4, False),
        (5, True), 
        (6, False),  
        (31, True), 
        (2017, True), 
        (2048, False)
    }

    def test_1(self): 

        for num, expected in self.test_cases:   
            assert isPrime_naive(num) == expected 

    def test_2(self): 
        
        for num, expected in self.test_cases: 
            assert isPrime_sqrt(num) == expected


if __name__ == "__main__":
    unittest.main()
