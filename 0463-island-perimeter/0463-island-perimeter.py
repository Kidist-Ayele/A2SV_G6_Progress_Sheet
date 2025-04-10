class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        directions = {(0, 1), (1, 0), (0, -1), (-1, 0)}
        visited = [[False] * len(grid[0]) for _ in range(len(grid))]

        def inbound(row, col):
            return (0 <= row < len(grid)) and (0 <= col < len(grid[0]))

        perimeter = 0
        def dfs(row, col):
            nonlocal perimeter

            visited[row][col] = True
            
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy
                if inbound(new_row, new_col) and grid[new_row][new_col]:
                    if not visited[new_row][new_col]:
                        dfs(new_row, new_col)
                else:
                    perimeter += 1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] and not visited[row][col]:
                    dfs(row,col)
        return perimeter


        
        