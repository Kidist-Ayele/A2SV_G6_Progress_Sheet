class NumMatrix:

    def __init__(self, matrix: List[List[int]]):

        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]

        for row in range(1, rows + 1):
            for col in range(1, cols + 1):
                self.prefix[row][col] = (self.prefix[row - 1][col] 
                + self.prefix[row][col - 1] 
                - self.prefix[row-1][col-1] 
                + matrix[row - 1][col - 1])
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1 , row2 , col1 , col2 = row1 + 1 , row2 + 1 , col1 + 1 , col2 + 1

        result = (self.prefix[row2][col2] 
        - self.prefix[row2][col1 - 1] 
        - self.prefix[row1 - 1][col2] 
        + self.prefix[row1 - 1][col1 - 1])

        return result
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)