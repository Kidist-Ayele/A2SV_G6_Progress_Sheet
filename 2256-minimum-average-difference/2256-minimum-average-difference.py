class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0] * (n + 1)

        for i in range(1, n + 1):
            prefix[i] = prefix[i - 1] + nums[i - 1]

        ans = float('inf')
        index = 0

        for i in range(1, n):

            left_avg = prefix[i] // i
            right_avg = (prefix[n] - prefix[i]) // (n - i) if (n - i) > 0 else 0

            cur = abs(right_avg - left_avg)

            if ans > cur:
                ans = cur
                index = i - 1

        if (prefix[n] // n) < ans:
            index = n - 1
        return index
            
        