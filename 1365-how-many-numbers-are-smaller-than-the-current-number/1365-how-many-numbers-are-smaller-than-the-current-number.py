class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]: 
        arr = []
        n = len(nums)
        for i in range(n):
            cnt_small = 0
            curr_num = nums[i]
            for j in range(0, n):
                if nums[j] < curr_num:
                    cnt_small += 1
            arr.append(cnt_small)
        return arr


        
        