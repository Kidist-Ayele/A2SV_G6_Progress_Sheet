class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        seive = [True] * n
        seive[0] = seive[1] = False

        for i in range(2, n):
            if seive[i] == True:
                for j in range(i * i, n, i):
                    seive[j] = False
        count = 0
        for bl in seive:
            if bl:
                count += 1
        return count
        