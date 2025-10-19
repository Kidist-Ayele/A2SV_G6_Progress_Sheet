class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left, right = 0, n
        res = []
        while right < 2*n:
            res.append(nums[left])
            res.append(nums[right])
            left += 1
            right += 1
        return res

        