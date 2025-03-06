class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        wiggle = []
        for right in range(1, len(nums)):
            cur_val = nums[right] - nums[right - 1]
            if wiggle: 
                if wiggle[- 1] * cur_val < 0:
                    wiggle.append(cur_val)
            else:
                if cur_val != 0:
                    wiggle.append(cur_val)
    
        return len(wiggle) + 1




        