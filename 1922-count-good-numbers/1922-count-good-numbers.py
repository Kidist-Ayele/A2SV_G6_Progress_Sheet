class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = 10**9 + 7
        ans = 1
        def power(base, exp):
            if exp == 0:
                return 1
            
            half = power(base, exp//2)
            half *= half

            if exp % 2:
                half *= base

            return half % MOD
        odd_index = ceil(n/2)
        even_index = n//2

        return (power(5, odd_index) * power(4, even_index)) % MOD

        
            


        