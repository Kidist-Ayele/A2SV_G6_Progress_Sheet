class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        def dp(idx, prev):
            if idx == n:
                return 0
            if (idx, prev) in memo:
                return memo[(idx, prev)]
            take = 0
            #take
            if prev == -1 or nums[idx] > nums[prev]:
                take = 1 + dp(idx + 1, idx)

            #not take
            not_take = dp(idx + 1, prev)
            memo[(idx, prev)] = max(take, not_take)
            return memo[(idx, prev)]
        return dp(0, -1)