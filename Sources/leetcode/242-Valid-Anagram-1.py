class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # Check if the original lens are the same
        if len(s) != len(t):
            return False

        # Define the hashmaps
        countS = {}
        countT = {}

        # Populate the hashmaps
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # Confirm if the hashmaps are identical
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True
