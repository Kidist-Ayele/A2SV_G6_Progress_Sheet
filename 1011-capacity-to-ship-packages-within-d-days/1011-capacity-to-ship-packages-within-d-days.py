class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        def check(mid):
            total, count = 0, 1
            
            for num in weights:
                if total + num > mid:
                    total = num
                    count += 1
                else:
                    total += num
            return count <= days
        
        while left < right:
            mid = left + (right - left) // 2

            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left

        