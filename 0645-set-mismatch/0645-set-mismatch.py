class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        i = 0 
        n = len(nums)

        while i < n:
            position = nums[i] - 1

            if nums[i] != nums[position]:
                nums[i], nums[position] = nums[position], nums[i]
            else:
                i += 1

      
        for i in range(n):
            if nums[i] != i + 1:
                return [nums[i], i + 1]
     
        