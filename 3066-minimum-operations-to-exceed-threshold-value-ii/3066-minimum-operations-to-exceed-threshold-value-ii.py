class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, num)
        count = 0
        
        while heap[0] < k:
            if len(heap) >= 2:
                x = heappop(heap)
                y = heappop(heap)

                new_num = min(x, y) * 2 + max(x, y)
                heappush(heap, new_num)
            count += 1
        return count