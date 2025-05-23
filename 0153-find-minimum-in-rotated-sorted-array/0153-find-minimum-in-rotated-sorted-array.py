class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        ans = float('inf')

        while left <= right:
            mid = left + (right - left) // 2
            ans = min(ans, nums[mid])
            if nums[mid] < nums[right]:
                right = mid - 1
            else:
                left = mid + 1
        return ans
        