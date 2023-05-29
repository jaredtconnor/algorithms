import unittest


def non_adjacent_sum(nums):
    memo = {}
    return _non_adjacent_sum(nums, 0, memo)


def _non_adjacent_sum(nums, i, memo):
    if i in memo:
        return memo[i]

    if i >= len(nums):
        return 0

    include_branch = nums[i] + _non_adjacent_sum(nums, i + 2, memo)
    exclude_branch = _non_adjacent_sum(nums, i + 1, memo)

    memo[i] = max(include_branch, exclude_branch)
    return memo[i]


class Test(unittest.TestCase):
    def test_case_1(self):
        nums = [2, 4, 5, 12, 7]
        res = non_adjacent_sum(nums)  # -> 16
        expected = 16
        assert res == expected

    def test_case_2(self):
        nums = [7, 5, 5, 12]
        res = non_adjacent_sum(nums)  # -> 19
        expected = 19
        assert res == expected

    def test_case_3(self):
        nums = [7, 5, 5, 12, 17, 29]
        res = non_adjacent_sum(nums)  # -> 48
        expected = 48
        assert res == expected

    def test_case_4(self):
        nums = [
            72,
            62,
            10,
            6,
            20,
            19,
            42,
            46,
            24,
            78,
            30,
            41,
            75,
            38,
            23,
            28,
            66,
            55,
            12,
            17,
            9,
            12,
            3,
            1,
            19,
            30,
            50,
            20,
        ]
        res = non_adjacent_sum(nums)  # -> 488

        expected = 488
        assert res == expected

    def test_case_5(self):
        nums = [
            72,
            62,
            10,
            6,
            20,
            19,
            42,
            46,
            24,
            78,
            30,
            41,
            75,
            38,
            23,
            28,
            66,
            55,
            12,
            17,
            83,
            80,
            56,
            68,
            6,
            22,
            56,
            96,
            77,
            98,
            61,
            20,
            0,
            76,
            53,
            74,
            8,
            22,
            92,
            37,
            30,
            41,
            75,
            38,
            23,
            28,
            66,
            55,
            12,
            17,
            72,
            62,
            10,
            6,
            20,
            19,
            42,
            46,
            24,
            78,
            42,
        ]
        res = non_adjacent_sum(nums)  # -> 1465
        expected = 1465
        assert res == expected


if __name__ == "__main__":
    unittest.main()
