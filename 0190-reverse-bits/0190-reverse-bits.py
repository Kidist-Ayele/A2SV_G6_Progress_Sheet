class Solution:
    def reverseBits(self, n: int) -> int:
        num_bit = [num for num in bin(n)]
        res = ''.join(num_bit[2:])
        res = (32 - len(res)) * "0" + res
        res = res[::-1]
        print(res)
        return int(res, 2)        