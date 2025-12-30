# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        ans = 0
        while left <= right:
            mid = (right + left) // 2
            if isBadVersion(mid):
                ans = mid
                right -= 1
            else:
                left += 1
        return ans

