class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        count = 0
        left = 0 
        min_index, max_index = -1, -1 
        invalid_index = -1

        for right, num in enumerate(nums):
    
            # If num is out of the valid range Update the last invalid position
            if num < minK or num > maxK:
                invalid_index = right 
          
            if num == minK:
                min_index = right
            
            if num == maxK:
                max_index = right

            valid_start = min(min_index, max_index)

            if valid_start > invalid_index:
                count += valid_start - invalid_index

        return count
        