class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        target = total // 2
        memo =[ [-1] * (len(nums) + 1) for _ in range(sum(nums) + 1)]
        # memo[sub1][idx]
        def dp(i, sub1):
            if i == len(nums):
                return sub1 == target
            if memo[sub1][i] == -1:
                add = dp(i + 1, sub1 + nums[i])
                dont_add = dp(i + 1, sub1)
                memo[sub1][i] = add or dont_add
            return memo[sub1][i]
        return dp(0, 0)
        