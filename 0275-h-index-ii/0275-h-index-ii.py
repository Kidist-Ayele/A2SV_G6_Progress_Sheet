class Solution:
    def hIndex(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        n = len(nums)

        while left <= right:
            mid = left + (right - left) // 2
            h = n - mid
            if nums[mid] < h:
                left = mid + 1
            else:
                right = mid - 1
        return n - left

        