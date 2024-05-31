# Problem: Minimum Score Triangulation of Polygon - https://leetcode.com/problems/minimum-score-triangulation-of-polygon/

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:
        n = len(values)
        dp = [[0]*n for _ in range(n)]
        
        for i in range(2,n):
            for start in range(n-i):
                end = start  +i
                dp[start][end] = float("inf")
                for k in range(start+1,end):
                    dp[start][end] = min(dp[start][end], values[start]*values[k]*values[end] + dp[start][k] + dp[k][end])
        return dp[0][n-1]
		