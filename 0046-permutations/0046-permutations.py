class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(index):
            if index == len(nums):
                ans.append(nums[:])
                return
            
            for i in range(index, len(nums)):

                nums[index], nums[i] = nums[i], nums[index]
                backtrack(index + 1)
                nums[index], nums[i] = nums[i], nums[index]
                        

        backtrack(0)
        return ans

        