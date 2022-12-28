import unittest


def five_sort(nums):

    i = 0
    j = len(nums) - 1

    while i < j:

        if nums[j] == 5:
            j -= 1

        elif nums[i] == 5:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

        else:
            i += 1

    return nums


class Test(unittest.TestCase):

    test_case_1 = [12, 5, 1, 5, 12, 7]
    res_1 = [12, 7, 1, 12, 5, 5]
    test_case_2 = [5, 2, 5, 6, 5, 1, 10, 2, 5, 5]
    res_2 = [2, 2, 10, 6, 1, 5, 5, 5, 5, 5]

    def test_1(self):

        assert five_sort(self.test_case_1) == self.res_1

    def test_2(self):

        assert five_sort(self.test_case_2) == self.res_2


if __name__ == "__main__":
    unittest.main()
