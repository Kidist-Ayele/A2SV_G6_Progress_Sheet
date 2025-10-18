class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        num, s = x ^ y, 0
        while num > 0:
            s += num & 1
            num = num >> 1
        return s