class Solution:
    def punishmentNumber(self, n: int) -> int:

        def backtrack(index, target, s):
            if index == len(s):
                if target == 0:
                    return True
                return False
            
            for i in range(index + 1, len(s) + 1):
                cur = int(s[index: i])

                if backtrack(i, target - cur, s):
                    return True

            return False

        ans = 0
        for i in range(1, n + 1):
            s = str(i * i)
            if backtrack(0, i, s):
                ans += i * i 
                
        return ans
        
        