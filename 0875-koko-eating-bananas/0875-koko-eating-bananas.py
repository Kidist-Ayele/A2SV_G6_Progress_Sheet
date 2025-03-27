class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isValid(bananas):
            count = 0
            for num in piles:
                count += ceil(num/bananas)

            return count <= h
        
        left, right = 1, sum(piles)

        while left < right:
            mid = left + (right - left) // 2

            if isValid(mid):
                right = mid
            else:
                left = mid + 1
        return left


        