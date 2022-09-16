from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: list[int]) -> list[list[str]]:

        result = defaultdict(list)  # Mapping charCount to list of Anagrams

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1

            result[tuple(count)].append(s)

        return result.values()
