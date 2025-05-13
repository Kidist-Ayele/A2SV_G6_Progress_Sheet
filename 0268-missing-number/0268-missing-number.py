class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #Arthmetic Sum
        return (len(nums) * (len(nums) + 1)// 2) - sum(nums)
       