class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Cyclic Sort
        
        i = 0 
        n = len(nums)

        while i < n:
            correct_pos = nums[i] - 1

            if nums[i] != nums[correct_pos]:
                nums[i], nums[correct_pos] = nums[correct_pos], nums[i]
            else:
                i += 1

        ans = []
        for i in range(n):
            if nums[i] != i + 1:
                ans.append(i + 1)
        return ans


        