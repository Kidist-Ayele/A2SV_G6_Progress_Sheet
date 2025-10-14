class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        @cache
        def dp(left, right):
            if left >= n or right >= m:
                return 0
            if text1[left] == text2[right]:
                return 1 + dp(left + 1, right + 1)

            take_left = dp(left + 1, right)
            take_right = dp(left, right + 1)
            return max(take_left, take_right)

        return dp(0, 0)
        