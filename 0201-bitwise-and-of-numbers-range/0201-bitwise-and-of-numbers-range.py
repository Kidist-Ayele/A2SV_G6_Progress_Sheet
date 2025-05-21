class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        length = right.bit_length()
        ans = 0
        for i in range(length, -1, -1):
            if left & (1 << i) == right & (1 << i):
                ans |= left & (1 << i)
            else:
                break
        return ans
        