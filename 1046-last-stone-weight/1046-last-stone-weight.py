class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for num in stones:
            heappush(heap, -num)
        while heap:
            if len(heap) == 1:
                return -heap[0]
            
            y = -heappop(heap)
            x = -heappop(heap)

            if x != y:
                heappush(heap, -(y - x))
        return 0

        