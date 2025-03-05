class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        rows_building = defaultdict(int)
        cols_building = defaultdict(int)

        for row in range(n):
            for col in range(n):
                rows_building[row] = max(rows_building[row], grid[row][col])
                cols_building[col] = max(cols_building[col], grid[row][col])
                
        
        result = 0
        for row in range(n):
            for col in range(n):
                val = min(rows_building[row], cols_building[col])
                result += val - grid[row][col]
                
        return result

        