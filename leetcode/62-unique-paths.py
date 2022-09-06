class Solution:
    def unique_paths(self, m: int, n: int) -> int:

        # create the main structure
        dp = [[0] * n for i in range(m)]

        for i in range(m):
            dp[i][0] = 1

        for i in range(n):
            dp[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):

                dp[i][j] = dp[i-1][j] + dp[i][j-1]

        return dp[m-1][n-1]
