class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
      
        for i in range(n):
            index = abs(nums[i]) - 1

            if 0 <= index < n: 

                if nums[index] > 0:
                    nums[index] *= - 1
                else:
                    nums[index] = -(n + 1)

        for i in range(n):
            if nums[i] >= 0:
                return i + 1

        return n + 1
            

