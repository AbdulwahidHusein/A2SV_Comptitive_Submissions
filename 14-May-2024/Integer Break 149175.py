# Problem: Integer Break - https://leetcode.com/problems/integer-break/

class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * 60
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(2, i):
                dp[i] = max(dp[i], max(j*(i-j), dp[j]* (i - j)))
        return dp[n]