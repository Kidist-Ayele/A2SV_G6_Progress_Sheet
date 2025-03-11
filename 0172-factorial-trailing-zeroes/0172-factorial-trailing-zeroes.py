class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        if n < 5:
            return ans
        else:
            ans = n//5
            return ans + self.trailingZeroes(n//5)

        return self.trailingZeroes(n)

        