class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0

        def check(candy):
            count = 0
            for num in candies:
                count += num // candy

            return count >= k

            
        left, right = 1, max(candies)
        ans = 0
        while left <= right:
            mid = left + (right - left) // 2

            if check(mid):
                ans = max(ans, mid)
                left = mid + 1
            else:
                right = mid - 1
        return ans


        