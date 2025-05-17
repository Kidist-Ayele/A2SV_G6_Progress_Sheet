class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        left, temp, res = 0, nums[0], 1

        for right in range(1, len(nums)):
            while left < right and (temp & nums[right]) != 0:
                temp ^= nums[left]
                left += 1
            temp |= nums[right]
            res = max(res, right - left + 1)
        return res

        