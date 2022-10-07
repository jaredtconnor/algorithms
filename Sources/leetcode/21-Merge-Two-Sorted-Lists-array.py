class Solution:
    def mergeTwoLists(self, nums1, nums2):

        set1 = set(nums1)
        set2 = set(nums2)

        result = []

        for num in set1:
            if num in set2:
                result.append(num)

        return result


if __name__ == "__main__":

    solution = Solution()
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]

    print(solution.mergeTwoLists(nums1, nums2))

