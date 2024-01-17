class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        row = len(matrix)
        col = len(matrix[0])

        self.pref_matrix = [[0 for _ in range(col+1)] for _ in range(row+1)]
        for i in range(1, row+1):
            for j in range(1, col+1):
                self.pref_matrix[i][j] = matrix[i-1][j-1] -self.pref_matrix[i-1][j-1] + self.pref_matrix[i][j-1] + self.pref_matrix[i-1][j]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pref_matrix[row2+1][col2+1] - self.pref_matrix[row2+1][col1] - self.pref_matrix[row1][col2+1] + \
        self.pref_matrix[row1][col1]



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)