class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = {(0, 1), (1, 0), (-1, 0), (0, -1)}
        # visited = [[False for i in range(len(grid[0]))] for j in range(len(grid))]

        def inbound(row, col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))

        def dfs(row, col):
            grid[row][col] = "0"

            for dx, dy in directions:
                new_row = dx + row
                new_col = dy + col

                if inbound(new_row, new_col) and grid[new_row][new_col] == "1":  
                    dfs(new_row, new_col)

        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count += 1
                    dfs(row, col)
        return count

                

        