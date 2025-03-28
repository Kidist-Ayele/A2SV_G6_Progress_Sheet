class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def check(capacity):
            index = count = 0

            while index < len(nums):
                if nums[index] <= capacity:
                    count += 1
                    index += 1
                index += 1
            return count >= k

        left, right = min(nums), max(nums)
        ans = float('inf') 
        while left <= right:
            mid = left + (right - left) // 2

            if check(mid):
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
                
        return ans


        