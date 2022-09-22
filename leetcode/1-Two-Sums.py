class Solution:
    def TwoSums_naive(self, nums: list[int], target: int) -> list[int]:

        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return [-1, -1]

    def TwoSums_dict(self, nums: list[int], target: int) -> list[int]:

        for i, num in enumerate(nums):
            hashmaps = i

        for i, num in enumerate(nums):
            second_num = target - num
            if second_num in hashmaps.keys():
                return [hashmaps[second_num], i]
