class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n):
            if n == 0:
                return 1
            if n < 0:
                return 1/ pow(x, -n)
                
            if not n % 2:
                half = pow(x, n//2)
                return half * half
            else:
                return x * pow(x, n - 1)

        
        return pow(x, n)
        
        