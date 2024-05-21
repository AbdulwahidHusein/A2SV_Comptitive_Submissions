# Problem: Triangle - https://leetcode.com/problems/triangle/

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = []
        for i in range(n):
            curr = []
            for j in range(i+1):
                curr.append(0)
            dp.append(curr)
        dp[0][0] = triangle[0][0]

        for i in range(1, n):
            for j in range(i+1):
                dp[i][j] = triangle[i][j]
                l = r = float("inf")
                if j >0:
                    l = dp[i-1][j-1]
                if j < len(dp[i-1]):
                    r = dp[i-1][j] 
                dp[i][j] += min(l, r)
                
        return min(dp[-1])
