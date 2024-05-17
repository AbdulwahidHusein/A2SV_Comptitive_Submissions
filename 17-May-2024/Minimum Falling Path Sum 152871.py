# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])

        dp = matrix

        for r in range(1, row):
            for c in range(col):
                cand = [dp[r-1][c]]
                if c > 0:
                    cand.append(dp[r-1][c-1])
                if c < col-1:
                    cand.append(dp[r-1][c+1])
                dp[r][c] += min(cand)

        return min(dp[-1])
