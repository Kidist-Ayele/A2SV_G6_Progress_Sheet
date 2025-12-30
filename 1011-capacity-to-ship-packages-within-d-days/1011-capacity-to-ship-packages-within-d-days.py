class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(k):
            temp = 0
            count = 0
            for num in weights:
                temp += num
                if temp > k:
                    temp = num
                    count += 1
            return count + 1 <= days

        ans = 0
        left, right = max(weights), sum(weights)
        while left <= right:
            mid = (right + left) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans        