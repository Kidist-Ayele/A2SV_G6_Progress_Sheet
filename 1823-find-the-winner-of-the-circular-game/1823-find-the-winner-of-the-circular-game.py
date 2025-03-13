class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        nums = [i for i in range(1, n + 1)]
        losser = 0
        def winner(nums, losser):
            if len(nums) == 1:
                return nums[0]

            losser =  (losser + k - 1) % len(nums)
            nums.pop(losser)
            
            return winner(nums, losser)

        return winner(nums, losser)
        