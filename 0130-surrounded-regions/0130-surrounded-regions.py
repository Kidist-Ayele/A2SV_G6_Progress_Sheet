class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = {(0, 1), (1, 0), (-1, 0), (0, -1)}
        visited = set()

        def inbound(row, col):
            return (0 <= row < len(board)) and (0 <= col < len(board[0]))
        
        def border(row, col):
            return (0 == row or row == len(board) - 1 or 0 == col or col == len(board[0]) - 1)

        def dfs(row, col):
            visited.add((row, col))

            in_border = border(row, col)

            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy

                if inbound(new_row, new_col) and board[new_row][new_col] == "O":
                    if (new_row, new_col) not in visited:
                        cur_border = dfs(new_row, new_col)
                        in_border |= cur_border

            return in_border

        def dfs2(row, col):
            board[row][col] = "X"

            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy

                if inbound(new_row, new_col) and board[new_row][new_col] == "O":
                        dfs2(new_row, new_col)

        in_border = False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O" and (i, j) not in visited: 
                    in_border = dfs(i, j)
                    if not in_border:
                        dfs2(i, j)