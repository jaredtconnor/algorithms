import unittest


def pair_sum_naive(nums, target):

    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):

            if nums[i] + nums[j] == target:
                return (i, j)


def pair_sum(nums, target):

    previous_nums = {}

    for index, num in enumerate(nums):

        complement = target - num

        if complement in previous_nums:

            return (previous_nums[complement], index)

        previous_nums[num] = index


class Test(unittest.TestCase):

    test_cases = {}

    def test_1(self):

        input = [3, 2, 5, 4, 1]
        target = 8
        expected = (0, 2)
        assert pair_sum_naive(input, target) == expected

    def test_2(self):

        input = [3, 2, 5, 4, 1]
        target = 8
        expected = (0, 2)
        assert pair_sum(input, target) == expected


if __name__ == "__main__":
    unittest.main()
