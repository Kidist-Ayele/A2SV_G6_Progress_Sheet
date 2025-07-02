class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = ""
        while a or b:
            t = z = 0
            while a and t < 2:
                ans += 'a'
                t += 1
                a -= 1
            while b and z < 2:
                ans += 'b'
                z += 1
                b -= 1
        return ans
            
        