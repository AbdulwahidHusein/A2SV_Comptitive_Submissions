# Problem: Coin Change - https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        n = len(coins)
        dp = [[float("inf") for _ in range (amount+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 0
            if coins[i-1] <= amount:  
                dp[i][coins[i-1]] = 1 
        for i in range(1, n+1):
            for j in range(1, amount+1): 
                dp[i][j] = dp[i-1][j]
                if j >= coins[i-1]:
                    dp[i][j] = min(dp[i][j - coins[i-1]]+1, dp[i][j])
        return dp[-1][-1] if dp[-1][-1] != float("inf") else -1
        