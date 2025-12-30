class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1, -1]
        def first(target):
            left, right = 0, len(nums) - 1
            
            while left <= right:
                mid = (right + left) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    result[0] = mid
                    right = mid - 1

        def last(target):
            left, right = 0, len(nums) - 1
            
            while left <= right:
                mid = (right + left) // 2
                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    result[1] = mid
                    left = mid + 1
        first(target)
        last(target)
        return result