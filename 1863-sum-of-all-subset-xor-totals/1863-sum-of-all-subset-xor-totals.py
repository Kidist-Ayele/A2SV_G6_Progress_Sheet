class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def dfs(idx, total):
            if idx == len(nums):
                return total

            #take
            take = dfs(idx + 1, total ^ nums[idx])

            # not take
            not_take = dfs(idx + 1, total)

            return take + not_take

        return dfs(0, 0)
        