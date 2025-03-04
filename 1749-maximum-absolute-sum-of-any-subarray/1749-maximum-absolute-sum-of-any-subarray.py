class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:

        cur_sum = 0
        cur_max, cur_min = 0, 0
        ans = 0

        for num in nums:
            cur_sum += num
            cur_max = max(cur_max, cur_sum)
            cur_min = min(cur_min, cur_sum)
            ans = max(ans, abs(cur_sum - cur_max), abs(cur_sum - cur_min))

        return ans
        