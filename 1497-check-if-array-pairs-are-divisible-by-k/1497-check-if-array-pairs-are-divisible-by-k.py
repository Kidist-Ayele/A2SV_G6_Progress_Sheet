class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        total = 0
        for num in arr:
            total += num % k
        return total % k == 0
        