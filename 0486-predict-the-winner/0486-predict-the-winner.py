class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        def dp(i, j):
            if i == j:
                return nums[i]

            winner = max(nums[i] - dp(i + 1, j), nums[j] - dp(i, j - 1))
            return winner
        n = len(nums)
        

        return dp(0, n - 1) >= 0
