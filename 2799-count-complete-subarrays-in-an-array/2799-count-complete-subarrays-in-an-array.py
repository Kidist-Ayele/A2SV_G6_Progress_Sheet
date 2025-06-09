class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        totalDistinct = len(set(nums))
        n = len(nums)
        count = 0
        
        for i in range(n):
            visited = set()
            for j in range(i, n):
                visited.add(nums[j])
                if len(visited) == totalDistinct:
                    count += n - j
                    break
        return count