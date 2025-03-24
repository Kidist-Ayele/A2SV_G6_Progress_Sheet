class Solution:
    def mySqrt(self, x: int) -> int:
        left, right = 0, x
        while left <= right:
            mid = left + (right - left) // 2
            val = mid * mid
            if val > x:
                right = mid - 1
            else:
                left = mid + 1
        return right