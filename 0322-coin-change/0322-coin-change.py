class Solution:
    def __init__(self):
        self.memo = {}
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        
        min_count = float('inf')

        if amount not in self.memo:
            for coin in coins:
                res = self.coinChange(coins, amount - coin)
                if res != -1:
                    min_count = min(min_count, 1 + res)
        
            self.memo[amount] = min_count if min_count != float('inf') else -1
        return self.memo[amount]
        