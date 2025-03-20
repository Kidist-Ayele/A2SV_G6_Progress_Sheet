class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        if len(s) < 2:
            return ""

        set_s = set(s)

        for i, char in enumerate(s):
            if char.swapcase() not in set_s:
                left = self.longestNiceSubstring(s[:i])
                right = self.longestNiceSubstring(s[i+1:])
                # return max(s1, s2, key = len)
                if len(left) >= len(right):
                    return left
                else:
                    return right
        return s
            

        