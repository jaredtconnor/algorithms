import unittest


def array_stepper(numbers):
    memo = {}
    return _array_stepper(numbers, 0, memo)


def _array_stepper(numbers, i, memo):
    if i in memo:
        return memo[i]

    # If the current index is at the end of the list
    # we have found a true case
    if i >= len(numbers) - 1:
        return True

    max_steps = numbers[i]

    # Iterate through the remaining of the array
    # recursively calling if we can reach the end of
    # the array with the current index
    for step in range(1, max_steps + 1):
        if _array_stepper(numbers, i + step, memo):
            memo[i] = True
            return memo[i]

    memo[i] = False
    return memo[i]


class Test(unittest.TestCase):
    def test_case_1(self):
        res = array_stepper([2, 4, 2, 0, 0, 1])  # -> True
        exp = True
        assert res == exp

    def test_case_2(self):
        res = array_stepper([2, 3, 2, 0, 0, 1])  # -> False
        exp = False
        assert res == exp

    def test_case_3(self):
        res = array_stepper([3, 1, 3, 1, 0, 1])  # -> True
        exp = True
        assert res == exp

    def test_case_4(self):
        res = array_stepper([4, 1, 5, 1, 1, 1, 0, 4])  # -> True
        exp = True
        assert res == exp

    def test_case_5(self):
        res = array_stepper([4, 1, 2, 1, 1, 1, 0, 4])  # -> False
        exp = False
        assert res == exp

    def test_case_6(self):
        res = array_stepper([1, 1, 1, 1, 1, 0])  # -> True
        exp = True
        assert res == exp

    def test_case_7(self):
        res = array_stepper([1, 1, 1, 1, 0, 0])  # -> False
        exp = False
        assert res == exp

    def test_case_8(self):
        res = array_stepper(
            [
                31,
                30,
                29,
                28,
                27,
                26,
                25,
                24,
                23,
                22,
                21,
                20,
                19,
                18,
                17,
                16,
                15,
                14,
                13,
                12,
                11,
                10,
                9,
                8,
                7,
                6,
                5,
                3,
                2,
                1,
                0,
                0,
                0,
            ]
        )  # -> False
        exp = False
        assert res == exp


if __name__ == "__main__":
    unittest.main()
