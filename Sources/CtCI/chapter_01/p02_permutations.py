import time
import unittest
from collections import defaultdict
from collections import Counter

"""
Chapter 02 - Problem 02 - CTCI 6e pg. 90

Problem Statement: 
    Given two strings write a method to decide
    if one is a permutation of the other

Example:
    ("dog", "god") -> True 
    ("adbc", "abc") -> False 

Solution: 
    If two strings are permutations of eachother, 
    we know they have the same characters, in different
    order. Therefore, if we sort the strings, this will put
    the characters into the same order and then compare the
    two sorted strings. Depending on the sorting algorithm,
    this will be $O(nlog(n))$

"""


def check_permuations(s1: str, s2: str):

    # Check first len of each
    if len(s1) != len(s2):
        return False

    s1 = sorted(s1)
    s2 = sorted(s2)

    for i in range(len(s1)):
        if s1[i] != s2[i]:
            return False

    return True


def check_permuations_reverse_count(s1: str, s2: str):

    # Check first len of each
    if len(s1) != len(s2):
        return False

    hash_map = [0] * 256

    for c in s1:
        hash_map[ord(c)] += 1

    for c in s2:
        if hash_map[ord(c)] == 0:
            return False

        hash_map[ord(c)] -= 1

    return True


class Test(unittest.TestCase):

    test_cases = (
        ("dog", "god", True),
        ("abcd", "bacd", True),
        ("3563476", "7334566", True),
        ("wef34f", "wffe34", True),
        ("dogx", "godz", False),
        ("abcd", "d2cba", False),
        ("2354", "1234", False),
        ("dcw4f", "dcw5f", False),
        ("DOG", "dog", False),
        ("dog ", "dog", False),
        ("aaab", "bbba", False),
    )

    test_functions = [check_permuations, check_permuations_reverse_count]

    def test_cp(self):
        for test_function in self.test_functions:
            for s1, s2, expected in self.test_cases:
                assert test_function(s1, s2) == expected


if __name__ == "__main__":
    unittest.main()
