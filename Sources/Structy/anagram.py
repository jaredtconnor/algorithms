import unittest
from collections import Counter


def anagram_hashmap(s1, s2):

    if len(s1) != len(s2):
        return False

    s1map = {}
    s2map = {}

    # Populate the hash maps
    # make sure to use get()
    # to have safe retrieval
    for i in range(len(s1)):
        s1map[s1[i]] = 1 + s1map.get(s1[i], 0)
        s2map[s2[i]] = 1 + s2map.get(s2[i], 0)

    # Check each map and see if same value
    for c in s1map:
        if s1map[c] != s2map.get(c, 0):
            return False

    return True


def anagram_sorted(s1, s2):

    return sorted(s1) == sorted(s2)


def anagram_solution(s1, s2):
    return build_map(s1) == build_map(s2)


def anagram_counter(s1, s2):
    return Counter(s1) == Counter(s2)


def build_map(s):
    """
    Input: a string
    Output: a dict containing the amount of each char in string

    O(n) complexity over the input string
    """

    count_map = {}

    for c in s:
        if c not in count_map:
            count_map[c] = 0

        count_map[c] += 1

    return count_map


class Test(unittest.TestCase):

    test_cases = {
        ("restful", "fluster", True),  # -> True`
        ("cats", "tocs", False),  # -> False`
        ("monkeyswrite", "newyorktimes", True),  # -> True`
        ("paper", "reapa", False),  # -> False`
        ("elbow", "below", True),  # -> True`
        ("tax", "taxi", False),  # -> False`
        ("taxi", "tax", False),  # -> False`
        ("night", "thing", True),  # -> True`
        ("abbc", "aabc", False),  # -> False`
        ("po", "popp", False),  # -> false`
        ("pp", "oo", False),  # -> false`
    }

    def test_1(self):

        for input_1, input_2, expected in self.test_cases:
            assert anagram_hashmap(input_1, input_2) == expected

    def test_2(self):

        for input_1, input_2, expected in self.test_cases:
            assert anagram_sorted(input_1, input_2) == expected

    def test_3(self):

        for input_1, input_2, expected in self.test_cases:
            assert anagram_solution(input_1, input_2) == expected

    def test_4(self):

        for input_1, input_2, expected in self.test_cases:
            assert anagram_counter(input_1, input_2) == expected


if __name__ == "__main__":
    unittest.main()
