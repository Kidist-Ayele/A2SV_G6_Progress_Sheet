class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        '''
        objective: maximize perimeter
        decision variable: the side of triangle
        constraint:  side of a triangle is always shorter than the sum of the lengths of the other two sides of the triangle and the area must be greater than 0
        if the side of triangle are a, b and c
        a < b + c
        b < a + b
        c < a + b
        '''
        n = len(nums)
        nums.sort()
        max_val = 0

        right = 2
        for right in range(2, n):
            a, b, c = nums[right - 2], nums[right - 1], nums[right]
            if a < b + c and b < a + b and c < a + b:
                max_val = max(max_val, a + b + c)
        
        return max_val
        




        