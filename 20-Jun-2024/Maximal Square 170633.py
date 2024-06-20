# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        for i in range(rows):
            if matrix[i][0] == "1":
                dp[i][0] = 1
        for j in range(cols):
            if matrix[0][j] == "1":
                dp[0][j] = 1
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == "1":
                    m =  min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1])
                    dp[i][j] = (int(sqrt(m)) + 1) ** 2
        
        return max([max(r) for r in dp])