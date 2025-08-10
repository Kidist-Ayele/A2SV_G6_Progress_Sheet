class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        pairs = defaultdict(int)
        n = len(nums)
        ans = 0
        for left in range(n):
            for right in range(left + 1, n):
                product = nums[left] * nums[right]
                pairs[product] += 1

        for key, val in pairs.items():
            if val >= 2: 
                ans += (val * (val - 1) // 2) * 8 
        
        return ans

        