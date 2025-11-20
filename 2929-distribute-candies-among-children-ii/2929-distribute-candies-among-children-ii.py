class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        res = 0
        for b in range(min(limit, n) + 1):
            if n - b <= 2 * limit:
                res += min(n - b, limit) - max(0, n - b - limit) + 1
        return res