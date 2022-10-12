import unittest
import time
from collections import defaultdict

"""
Chapter 04 - Problem 03 - CTCI 6e pg. 91

Problem Statement:

Example:

Solution:

"""


def create_hash_map(string: str):

    map = {}

    for i in string:
        if i in map:
            map[i] += 1
        else:
            map[i] = 1

    return map


def checkMaxOneOdd(table):

    foundOdd = False

    for i in table:
        if table[i] % 2 == 1:

            if foundOdd:
                return False

            foundOdd = True

    return True


def palindrome_permutation(string: str):

    map = create_hash_map(string)

    return checkMaxOneOdd(map)


class Test(unittest.TestCase):

    test_cases = [
        ("aba", True),
        ("aab", True),
        ("abba", True),
        ("aabb", True),
        ("a-bba", True),
        ("a-bba!", True),
        ("Tact Coa", True),
        ("jhsabckuj ahjsbckj", True),
        ("Able was I ere I saw Elba", True),
        ("So patient a nurse to nurse a patient so", False),
        ("Random Words", False),
        ("Not a Palindrome", False),
        ("no x in nixon", True),
        ("azAZ", True),
    ]
    testable_functions = [
        palindrome_permutation,
    ]

    def test_1(self):

        assert palindrome_permutation("a-baa!") == True

        # for f in self.testable_functions:
        # for [test_string, expected] in self.test_cases:
        # assert f(test_string) == expected


if __name__ == "__main__":
    unittest.main()
