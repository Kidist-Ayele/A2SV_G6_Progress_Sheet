class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        directions = {(0, 1), (1, 0), (-1, 0), (0, -1)}
        queue = deque()
        fresh = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    queue.append((i, j))
        
        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

        ans = 0
        while queue and fresh > 0:

            for _ in range(len(queue)):
                row, col = queue.popleft()

                for dx, dy in directions:
                    new_row = dx + row
                    new_col = dy + col

                    if inbound(new_row, new_col) and grid[new_row][new_col] == 1:
                        grid[new_row][new_col] = 2
                        fresh -= 1
                        queue.append((new_row, new_col))
            
            ans += 1
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    return -1

        return ans if fresh == 0 else -1
