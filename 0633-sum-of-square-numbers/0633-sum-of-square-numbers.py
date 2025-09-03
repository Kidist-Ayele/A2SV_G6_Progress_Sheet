class Solution(object):
    def judgeSquareSum(self, c):
        left, right = 0, int(sqrt(c))
        while left <= right:
            if (left ** 2 + right ** 2) == c:
                return True
            elif (left ** 2 + right ** 2) > c:
                right -= 1
            else:
                left += 1
        return False