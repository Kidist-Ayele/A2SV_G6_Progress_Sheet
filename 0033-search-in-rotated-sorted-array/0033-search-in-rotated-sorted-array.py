class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            left_most = max(mid-1,left)
            right_most = min(mid + 1, right)

            if nums[left] <= nums[left_most]:
                if target >= nums[left] and target <= nums[left_most]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if target >= nums[right_most] and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
                
        return -1

        