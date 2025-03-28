class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Merge Sort
        
        def merge(left_side, right_side):
            n, m = len(left_side), len(right_side)
            left, right = 0, 0
            merged = []

            while left < n and right < m:
                if left_side[left] < right_side[right]:
                    merged.append(left_side[left])
                    left += 1
                else:
                    merged.append(right_side[right])
                    right += 1
            while left < len(left_side):
                merged.append(left_side[left])
                left += 1
            while right < len(right_side):
                merged.append(right_side[right])
                right += 1

            return merged

        def merge_sort(left, right, nums):
            if left == right:
                return [nums[left]]
            mid = left + (right - left) // 2

            left_val = merge_sort(left, mid, nums)
            right_val = merge_sort(mid + 1, right, nums)

            return merge(left_val, right_val)

        ans = merge_sort(0, len(nums) - 1, nums)

        return ans

        