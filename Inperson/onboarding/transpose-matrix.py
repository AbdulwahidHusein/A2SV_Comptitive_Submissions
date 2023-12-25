class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row = len(matrix)
        col = len(matrix[0])
        ret = [[0 for i in range(row)] for _ in range(col)]
        for i in range(row):
            for j in range(col):
                ret[j][i] = matrix[i][j]

        return ret