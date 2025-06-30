class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        nums = [1] * numOnes
        nums += [0] * numZeros
        nums += [-1] * numNegOnes

        i = 0
        ans = 0
        while k and i < len(nums):
            ans += nums[i]
            k -= 1
            i += 1
        return ans

        