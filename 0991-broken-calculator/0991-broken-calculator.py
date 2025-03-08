class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        num = target
        count = 0

        while num > startValue:
            if num % 2 == 0:
                num //= 2
            else:
                num += 1
            count += 1
            
        return count + (startValue - num)
        