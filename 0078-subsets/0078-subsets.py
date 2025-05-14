class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        for num in range(2 ** len(nums)):
            temp = []
            for i in range(32):
                if num & (1 << i) != 0:
                    # print(num & (1 << i))
                    temp.append(nums[i])
            res.append(temp)
        return res

        