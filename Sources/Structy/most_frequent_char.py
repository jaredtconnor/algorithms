import unittest
from collections import Counter


def most_frequent_char(s):

    map = build_map(s)

    max_count = -1
    for key, value in zip(map.keys(), map.values()):

        if value > max_count:
            max_char = key
            max_count = value

    return max_char


def most_frequent_char_solution(s):

    map = build_map(s)

    most_frequent = None

    for c in s:
        if most_frequent is None or map[c] > map[most_frequent]:
            most_frequent = c

    return most_frequent


def most_frequent_char_counter(s):

    map = Counter(s)

    most_frequent = None

    for c in s:
        if most_frequent is None or map[c] > map[most_frequent]:
            most_frequent = c

    return most_frequent


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
        ("bookeeper", "e"),
        ("david", "d"),
        ("abby", "b"),
        ("mississippi", "i"),
        ("potato", "o"),
        ("eleventennine", "e"),
        ("riverbed", "r"),
    }

    def test_1(self):

        for input, expected in self.test_cases:
            assert most_frequent_char(input) == expected

    def test_2(self):

        for input, expected in self.test_cases:
            assert most_frequent_char_solution(input) == expected

    def test_3(self):

        for input, expected in self.test_cases:
            assert most_frequent_char_counter(input) == expected


if __name__ == "__main__":
    unittest.main()
    # print(most_frequent_char("bookeeper"))
