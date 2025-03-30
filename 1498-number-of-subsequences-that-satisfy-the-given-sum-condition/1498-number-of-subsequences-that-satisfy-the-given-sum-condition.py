class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10 ** 9 + 7
        ans = 0

        # Precompute power array to get the number of subsquence in O(1) time
        power = [1] * len(nums)

        for i in range(1,len(nums)):
            power[i] = power[i - 1] * 2

        for left in range(len(nums)):
            right = self.upper_bound(nums, left, target - nums[left])
            if right >= left:
                ans = (ans + power[right - left]) % mod
        return ans

    def upper_bound(self, nums, left, target):
        left, right = left, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return right



        