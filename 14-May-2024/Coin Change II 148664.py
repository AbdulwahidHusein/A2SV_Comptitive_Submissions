# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n  = len(coins)
        dp = [[0 for _ in range(amount+1)] for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 1
        for i in range(1, n+1):
            for j in range(1, amount+1):
                dp[i][j] =  dp[i-1][j]
    
                if j >= coins[i-1]: 
                    dp[i][j] += dp[i][j - coins[i-1]] 

        return dp[-1][-1]