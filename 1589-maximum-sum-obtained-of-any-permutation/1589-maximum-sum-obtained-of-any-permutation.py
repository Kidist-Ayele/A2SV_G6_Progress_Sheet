class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)
        # Contract prefix sum of requests
        for start, end in requests:
            prefix[start] += 1
            prefix[end + 1] -= 1

       
        for i in range(1, n+1):
            prefix[i] += prefix[i - 1]

        # Sort prefix and nums to maximize the answer
        nums.sort()
        prefix.sort()

        result = 0
        for i in range(n):
            result += nums[i] * prefix[i+1]

        return result % (10**9 + 7)
        

