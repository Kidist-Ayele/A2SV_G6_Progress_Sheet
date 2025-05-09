class Solution:
    def longestIncreasingPath(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        matrix = [[0] * (m + 2) for _ in range(n + 2)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                matrix[i][j] = grid[i - 1][j - 1]
        
        directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

        outdegree = [[0] * (m + 2) for _ in range(n + 2)]
        
        for i in range(1, n + 1):
            for j in range(1, m + 1):

                for dx, dy in directions:
                    x = i + dx
                    y = j + dy

                    if matrix[i][j] < matrix[x][y]:
                        outdegree[i][j] += 1
        
        leaves = deque()

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if outdegree[i][j] == 0:
                    leaves.append((i, j))

        height = 0
        while leaves:
            height += 1

            new_leaves = deque()
            for i, j in leaves:
                for dx, dy in directions:
                    x = i + dx
                    y = j + dy

                    if matrix[x][y] < matrix[i][j]:
                        outdegree[x][y] -= 1
                        if outdegree[x][y] == 0:
                            new_leaves.append((x, y))
            leaves = new_leaves
        
        return height
                    
