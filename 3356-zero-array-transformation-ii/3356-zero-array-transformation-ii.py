class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        
        def canBeZero(k):
            diff = [0] * (len(nums) + 1)

            for i in range(k):
                start, end, val = queries[i]
                diff[start] += val
                if end + 1 < len(diff):
                    diff[end + 1] -= val

            current = 0
            for i in range(len(nums)):
                current += diff[i]
                if nums[i] - current > 0:
                    return False

            return True

        left, right = 0, len(queries)
        ans = float('inf')

        while left <= right:
            mid = left + (right -left) // 2

            if canBeZero(mid):
                ans = min(ans, mid)
                right = mid - 1
            else:
                left = mid + 1
        return ans if ans != float('inf') else -1


        