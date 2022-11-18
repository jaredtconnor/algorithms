import unittest


def compress(s):
    
    s += '!'
    res = [] 
    i = 0
    j = 0

    while j < len(s):  
        
        if s[i] == s[j]: # Records the streaks in string
            j+=1 

        else: 
            num =  j - i  

            if num == 1:  # Single occurance of character
                res.append(s[i])
            else:
                res.append(str(num))
                res.append(s[i])

            i = j 

    return ''.join(res) 


class Test(unittest.TestCase):

    test_cases = {  
        ('ccaaatsss', '2c3at3s'),
        ('ssssbbz', '4s2bz'), 
        ('ppoppppp', '2po5p'),  
        ('nnneeeeeeeeeeeezz', '3n12e2z'),
        ('yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy', "127y"), 
    }

    def test_1(self):

        for s, expected in self.test_cases:  
            #print(f"Input: {s} | Output: {compress(s)} | Expected: {expected} | Result {compress(s) == expected}")
            assert compress(s) == expected


if __name__ == "__main__":
    unittest.main()
