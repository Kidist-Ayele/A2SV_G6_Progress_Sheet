class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        ROWS = m
        COLS = n
        dp = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        dp[1][1] = 1

        for i in range(1, ROWS + 1):
            for j in range(1, COLS + 1):
                if i == 1 and j == 1:
                    continue
                dp[i][j] = dp[i -1][j] + dp[i][j - 1]
        return dp[ROWS][COLS]