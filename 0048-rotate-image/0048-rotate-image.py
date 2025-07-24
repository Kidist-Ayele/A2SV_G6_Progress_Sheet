class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        for row in range(rows):
            for col in range(row, cols):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]
        for r in range(rows):
            matrix[r].reverse()
        