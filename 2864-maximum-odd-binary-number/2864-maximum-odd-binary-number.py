class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count_one = s.count('1')
        result = ['0'] * len(s)

        for i in range(count_one - 1):
            result[i] = '1'

        if count_one > 0:
            result[-1] = '1'
            
        return ''.join(result)
        