class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        for i in range(0, n, 3):
            if i + 2 < n and nums[i + 2] - nums[i] <= k:
                result.append(nums[i:i + 3])
            else:
                return [] 
        return result
