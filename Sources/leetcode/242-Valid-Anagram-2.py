class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)


string_1 = "race"
string_2 = "care"

solution = Solution()

result = solution.isAnagram(string_1, string_2)

print(f"These two strings are anagrams: {result}")
