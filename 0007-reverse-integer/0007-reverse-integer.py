class Solution:
    def reverse(self, x: int) -> int:
        flag = True
        if x < 0:
            flag = False
            x = abs(x)
        nums = x
        y = 0
        while nums > 0:
            y = (y * 10) + nums % 10
            nums //= 10
        if y > 2**31 - 1 or y < -2**31:
                return 0
        if flag :
            return int(y)
        return int(-y)
        
        