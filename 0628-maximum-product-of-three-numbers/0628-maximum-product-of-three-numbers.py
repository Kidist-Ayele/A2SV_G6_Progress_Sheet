class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        
        nums.sort()

        forward = nums[-1] * nums[-2] * nums[-3]
        backward = nums[0] * nums[1] * nums[-1]
        
       
        return max(forward, backward)