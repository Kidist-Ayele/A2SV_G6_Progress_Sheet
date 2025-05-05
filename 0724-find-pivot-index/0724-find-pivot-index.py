class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l_s, r_s = 0, sum(nums)

        for i, num in enumerate(nums):
            r_s -= num

            if l_s == r_s:
                return i
            
            l_s += num
            
        return -1