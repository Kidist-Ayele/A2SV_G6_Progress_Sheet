class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        temp1 = temp2 = 0
        n, m = len(nums1), len(nums2)
        if n % 2 == 0 and m % 2 == 0:
            return 0
        
        for num in nums1:
            temp1 ^= num
        for num in nums2:
            temp2 ^= num
        print(temp1, temp2)
        if n % 2 == 0:
            return temp1
        if m % 2 == 0:
            return temp2
        if m % 2 and n % 2:
            return temp1 ^ temp2

       
        