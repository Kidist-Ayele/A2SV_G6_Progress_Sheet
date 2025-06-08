class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_num = max(nums)
        count = 0
        left = 0
        max_found = 0
        n = len(nums)

        for right in range(n):
            if nums[right] == max_num:
                max_found += 1

            while max_found == k:
                count += n - right
                if nums[left] == max_num:
                    max_found -= 1
                left += 1

        return count