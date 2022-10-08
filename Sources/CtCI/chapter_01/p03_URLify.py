import unittest

"""
Chapter 01 - Problem 03 - CTCI 6e pg. 90

Problem Statement:
    Write a method to replace all spaces in a string with "%20". You may
    assume that the string has sufficient space at the end to hold
    the additional character.

Example:
    input: "Mr John Smith      ", 13
    output: "Mr%20John%20Smth"

Solution:
    - Count the number of spaces in the string
    - Define a new index equal to the true length plus 2 * num_spaces
    - Start from the back of the array
        - When we see a space, replace it piecemeal with '%20'
        - If no spaces, copy the original character
"""


def URLify_algo(string: str, length: int):

    # Need to convert to list b/c python strings
    # are immutable
    char_list = list(string)
    new_index = len(char_list)

    for i in reversed(range(length)):
        if char_list[i] == " ":

            # Replace with correct chars
            char_list[new_index - 3:new_index] = "%20"
            new_index -= 3

        else:
            # Move character
            char_list[new_index - 1] = char_list[i]
            new_index -= 1

    return "".join(char_list[new_index:])


def URLify_python(string: str, length: int):
    return string[:length].replace(" ", "%20")


class Test(unittest.TestCase):

    test_cases = {
        ("much ado about nothing      ", 22): "much%20ado%20about%20nothing",
        ("Mr John Smith       ", 13): "Mr%20John%20Smith",
        (" a b    ", 4): "%20a%20b",
        (" a b       ", 5): "%20a%20b%20",
    }

    def test_urlify_1(self):
        for args, expected in self.test_cases.items():

            actual = URLify_algo(*args)
            print(f"Actual result {actual}")
            assert actual == expected, f"Failed {URLify_algo.__name__} for {[*args]}"

    def test_urlify_2(self):
        for args, expected in self.test_cases.items():

            actual = URLify_python(*args)
            assert actual == expected, f"Failed {URLify_python.__name__} for {[*args]}"


if __name__ == "__main__":
    unittest.main()
