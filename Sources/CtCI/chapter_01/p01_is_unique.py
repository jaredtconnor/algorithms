import time
import unittest
from collections import defaultdict
from collections import Counter

"""
Chapter 01 - Problem 01 - CTCI 6e pg. 90

Problem Statement:
    Implement an algorithm to determine if a string has all unique
    characters. What if you cannot use additional data structures?


Example:
    "alex" -> True
    "aalex" -> False

Solution:


"""


def is_unique_python(input_text: str):
    return len(set(input_text)) == len(input_text)


def is_unique_no_datastruct(input_text: str):
    sorted_text = sorted(input_text)

    last_char = None

    for char in sorted_text:
        if char == last_char:
            return False
        last_char = char

    return True


class Test(unittest.TestCase):
    test_cases = [
        ("abcd", True),
        ("s4fad", True),
        ("", True),
        ("23ds2", False),
        ("hb 627jh=j ()", False),
        ("".join([chr(val) for val in range(128)]), True),
        # unique 128 chars
        ("".join([chr(val // 2) for val in range(129)]), False),
        # non-unique 129 chars
    ]

    test_functions = [is_unique_python, is_unique_no_datastruct]

    def test_is_unique_chars(self):
        num_runs = 1000
        function_runtimes = defaultdict(float)

        for _ in range(num_runs):
            for text, expected in self.test_cases:
                for is_unique_chars in self.test_functions:
                    start = time.perf_counter()
                    assert (
                        is_unique_chars(text) == expected
                    ), f"{is_unique_chars.__name__} failed for value: {text}"
                    function_runtimes[is_unique_chars.__name__] += (
                        time.perf_counter() - start
                    ) * 1000

        print(f"\n{num_runs} runs")
        for function_name, runtime in function_runtimes.items():
            print(f"{function_name}: {runtime:.1f}ms")


if __name__ == "__main__":
    unittest.main()
