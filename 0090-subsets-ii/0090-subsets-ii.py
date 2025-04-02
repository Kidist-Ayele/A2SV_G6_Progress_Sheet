class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()

        ans = []
        path = []

        def backtrack(index):
            
            ans.append(path[:])

            for i in range(index,len(nums)):
                if i > index and nums[i] == nums[i - 1]:
                    continue

                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return ans
        