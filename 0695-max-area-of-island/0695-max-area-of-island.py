class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = {(0, 1), (1, 0), (-1, 0), (0, -1)}
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        def inbound(row, col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))
        
        def dfs(row, col):
            visited[row][col] = True

            area = 1

            for dx, dy in directions:
                new_row = dx + row
                new_col = dy + col

                if inbound(new_row, new_col) and grid[new_row][new_col]:
                    if not visited[new_row][new_col]:
                        area += dfs(new_row, new_col)
            return area

        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] and not visited[i][j]:
                    area = dfs(i, j)
                    total = max(total, area)
        return total