class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left, right = max(nums), sum(nums)

        def check(mid):
            count = 1
            total = 0
            for num in nums:
                if total + num > mid:
                    total = num
                    count += 1
                else:
                    total += num
            return count <= k

        ans = float('inf')
        while left <= right:
            mid = left + (right - left) // 2

            if check(mid):
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
                
        return ans



        