class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        min_heap = []
        prev_h = heights[0]

        for i in range(1, len(heights)):
            if heights[i] > prev_h:
                heappush(min_heap, heights[i] - prev_h)

            if len(min_heap) > ladders:
                x = heappop(min_heap)
                bricks -= x
                
            if bricks < 0:
                return i - 1
            prev_h = heights[i]

        return len(heights) - 1



        