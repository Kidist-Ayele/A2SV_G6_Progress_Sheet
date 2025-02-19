class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        n = len(nums)
        prefix = [0] * n

        # Contract prefix sum of requests
        for start, end in requests:
            prefix[start] += 1
            if end + 1 < n:
                prefix[end + 1] -= 1

        cur_sum = 0
        for i in range(1, n):
            prefix[i] += prefix[i - 1]

        # Sort prefix and nums to maximize the answer
        nums.sort()
        prefix.sort()

        result = 0
        for i in range(n):
            result += nums[i] * prefix[i]

        return result
        

