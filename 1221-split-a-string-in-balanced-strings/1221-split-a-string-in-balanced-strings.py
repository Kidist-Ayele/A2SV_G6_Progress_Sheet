class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        ans = 0

        for char in s:
            if char == 'R':
                count += 1
            else:
                count -= 1
            if count == 0:
                ans += 1
        return ans

        