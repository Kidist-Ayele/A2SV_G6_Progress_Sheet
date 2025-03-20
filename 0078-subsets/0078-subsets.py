class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        ans = []

        def backtrack(index):
            if index >= len(nums):
                ans.append(res[:])
                return

            res.append(nums[index])
            backtrack(index + 1)

            res.pop()
            backtrack(index + 1)
        backtrack(0)
        return ans


        