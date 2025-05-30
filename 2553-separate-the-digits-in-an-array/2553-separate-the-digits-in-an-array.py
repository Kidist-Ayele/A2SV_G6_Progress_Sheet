class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        string = []
        for num in nums:
            string.extend([char for char in num])
        return [int(char) for char in string]
        