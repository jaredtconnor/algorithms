import unittest

"""
Hi, here's your problem today. This problem was recently asked by Amazon:

Given an integer, reverse the digits.
Do not convert the integer into a string and reverse it.

Here's some examples and some starter code.

def reverse_integer(num):
  # Fill this in.

print(reverse_integer(135))
# 531

print(reverse_integer(-321))
# -123

######
Solution:
Input:  num
(1) Initialize rev_num = 0
(2) Loop while num > 0
     (a) Multiply rev_num by 10 and add remainder of num
          divide by 10 to rev_num
               rev_num = rev_num*10 + num%10;
     (b) Divide num by 10
(3) Return rev_num

"""


def reverse_integer(num: int):

    rev = 0

    if num < 0:
        num = num * -1
        while num > 0:

            a = num % 10
            rev = rev * 10 + a
            num = num // 10

        return rev * -1

    else:
        while num > 0:

            a = num % 10
            rev = rev * 10 + a
            num = num // 10

        return rev


class Test(unittest.TestCase):

    test_cases = [(135, 531), (-321, -123)]

    test_functions = [reverse_integer]

    def test_1(self):

        for test_function in self.test_functions:
            for test, expected in self.test_cases:
                self.assertEqual(
                    test_function(test), expected,
                    f"Testing {test} | result {expected}"
                )


if __name__ == "__main__":
    unittest.main()
