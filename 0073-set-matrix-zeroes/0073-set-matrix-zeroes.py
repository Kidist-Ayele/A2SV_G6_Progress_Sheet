class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_dict = defaultdict(bool)
        cols_dict = defaultdict(bool)

        rows = len(matrix)
        cols = len(matrix[0])

        for row in range(rows):
            for col in range(cols):
                if matrix[row][col] == 0:
                    rows_dict[row] = True
                    cols_dict[col] = True
        
        for row in range(rows):
            for col in range(cols):
                if rows_dict[row] or cols_dict[col]:
                    matrix[row][col] = 0
                    
        return matrix