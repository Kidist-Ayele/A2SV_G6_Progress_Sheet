class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        ans = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j] and not ((i * j) % k):
                    ans += 1
        

        return ans

        