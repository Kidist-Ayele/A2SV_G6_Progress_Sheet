class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        n = len(triangle)
        @cache
        def dp(i, j):
            if i == n - 1:
                return triangle[i][j]

            left = dp(i + 1, j)
            right = dp(i + 1, j + 1)

            return triangle[i][j] + min(left, right)

        return dp(0, 0)