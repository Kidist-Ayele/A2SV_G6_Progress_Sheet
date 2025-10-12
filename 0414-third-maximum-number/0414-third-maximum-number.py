class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        max_num = max(nums)
        heap = []
        for num in nums:
            heappush(heap, -num)
            
        num_set = set()
        while heap:
            x = heappop(heap)
            num_set.add(x)
            if len(num_set) > 2:
                return - x
        return max_num