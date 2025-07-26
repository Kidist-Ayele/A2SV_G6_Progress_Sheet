class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        def inbound(row, col):
            return (0 <= row < len(mat) and 0 <= col < len(mat[0]))

        direct = {(0, 1), (1, 0), (-1, 0), (0, -1)}
        dis = [[-1]*len(mat[0]) for _ in range(len(mat))]

        queue = deque()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    dis[i][j] = 0
                    queue.append((i, j))

        while queue:
            row, col = queue.popleft()
            for dx, dy in direct:
                new_row = row + dx
                new_col = col + dy

                if inbound(new_row, new_col) and dis[new_row][new_col] == -1:
                    dis[new_row][new_col] = dis[row][col] + 1
                    queue.append((new_row, new_col))
        
        return dis
            