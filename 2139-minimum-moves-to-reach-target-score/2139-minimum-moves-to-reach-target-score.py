class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        if target == 1:
            return 0
        ans = 0
       
        while maxDoubles and target:
            if target % 2:
                target -= 1
            else:
                target //= 2
                maxDoubles -= 1
            
            ans += 1
            if target == 1:
                break

        if target > 1:
            ans += target - 1
        return ans

        