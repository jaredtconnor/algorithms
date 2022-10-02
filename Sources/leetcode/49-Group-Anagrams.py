from collections import defaultdict


class Solution:

    def groupAnagrams(self, strs: list[int]) -> list[list[str]]:

        result = defaultdict(list)

        for s in strs:  # For each string in the array of strings
            count = [0] * 26  # a .... z but null values

            for c in s:  # For each character in each strings
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(s) 

        return result.values()
