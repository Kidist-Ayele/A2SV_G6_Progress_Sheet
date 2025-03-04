class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count_5 = count_10 = 0
        for birr in bills:
            if birr == 5:
                count_5 += 1
            elif birr == 10 and count_5 > 0:
                count_10 += 1
                count_5 -= 1

            elif birr == 20 and count_10 > 0 and count_5 > 0:
                count_10 -= 1
                count_5 -= 1
            elif birr == 20 and count_10 == 0 and count_5 > 2:
                count_5 -= 3
            else:
                return False
        return True


        