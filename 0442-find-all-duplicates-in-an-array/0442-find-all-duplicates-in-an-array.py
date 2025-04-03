class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0

        while i < n:
            current_pos = nums[i] - 1
            if nums[current_pos] != nums[i]:
                nums[i], nums[current_pos] = nums[current_pos], nums[i]
            else:
                i += 1
                
        duplicates = []
        for i in range(n):
            if nums[i] != i + 1:
                duplicates.append(nums[i])

        return duplicates
        