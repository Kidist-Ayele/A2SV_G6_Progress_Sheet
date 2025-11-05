class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def backtrack(idx, cur_sum):
            if (idx, cur_sum) in dp:
                return dp[(idx, cur_sum)]

            if idx == len(nums):
                return 1 if cur_sum == target else 0

            dp[(idx, cur_sum)] = backtrack(idx + 1, cur_sum + nums[idx]) + backtrack(idx + 1, cur_sum - nums[idx])

            return dp[(idx, cur_sum)]
        # backtrack(0, 0)
        # print(dp)
        return backtrack(0, 0)