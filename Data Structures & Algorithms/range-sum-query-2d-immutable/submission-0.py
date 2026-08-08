class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows = len(matrix)
        cols = len(matrix[0])

        self.matrix = [[0] * cols for _ in range(rows)]

        for r in range(len(self.matrix)):
            rowPrefix = 0
            for c in range(len(self.matrix[0])):
                rowPrefix += matrix[r][c]
                colPrefix = self.matrix[r-1][c] if r != 0 else 0
                self.matrix[r][c] = rowPrefix + colPrefix
        
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        total = self.matrix[row2][col2]
        total -= self.matrix[row1-1][col2] if (row1-1) >= 0 else 0
        total -= self.matrix[row2][col1-1] if (col1-1) >= 0 else 0
        total += self.matrix[row1-1][col1-1] if (row1-1) >= 0 and (col1-1) >= 0 else 0

        return total



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)