class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        maximum = max(nums)
        minimum = abs(min(nums)) 
        n = len(nums)
        count = [0] * (maximum + minimum + 1)

        for num in nums:
            count[num + minimum] += 1

        index = 0
        for res, freq in enumerate(count):
            for i in range(freq):
                nums[index] = res - minimum
                index += 1
            
        return nums 

        