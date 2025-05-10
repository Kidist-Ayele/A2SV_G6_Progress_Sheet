class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cur_ones = 0
        ans = 0
        for num in nums:
            if num == 1:
                cur_ones += 1
            else:
                ans = max(ans, cur_ones)
                cur_ones = 0
        ans = max(ans, cur_ones)
        return ans
        