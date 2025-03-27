class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(nums):
            left, right = 0, len(nums)

            while left < right:
                mid = left + (right - left) // 2

                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid
            return left

        def upper_bound(nums):
            left, right = 0, len(nums)

            while left < right:
                mid = left + (right - left) // 2

                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid
            return left

        ans = [-1, -1]
        left_idx = lower_bound(nums)
        right_idx = upper_bound(nums) - 1

        if left_idx < len(nums) and nums[left_idx] == target:
            ans[0] = left_idx 
        if 0 <= right_idx and nums[right_idx] == target:
            ans[1] = right_idx 
        return ans
        
        