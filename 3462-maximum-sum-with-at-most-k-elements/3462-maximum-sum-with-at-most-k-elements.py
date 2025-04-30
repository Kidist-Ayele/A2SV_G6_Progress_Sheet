class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        max_heap = []
        for i in range(len(grid)):
            rows = []
            for j in range(len(grid[0])):
                grid[i][j] = -grid[i][j]
                heappush(rows, grid[i][j])

            grid[i] = rows
            heappush(max_heap, (rows[0], i))

        total = 0
        while k > 0:
            x, index = heappop(max_heap)
            if limits[index] > 0 and grid[index]:
                heappop(grid[index])
                limits[index] -= 1
                total += -x
                k -= 1
                if grid[index]:
                    heappush(max_heap, (grid[index][0], index))

        return total 




        

        

        