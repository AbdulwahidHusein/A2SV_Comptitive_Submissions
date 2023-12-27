class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        #transpose and flip

        for i in range(n):
            for j in range(i, n):
                matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i] = matrix[i][::-1]
        """
        Do not return anything, modify matrix in-place instead.
        """
        