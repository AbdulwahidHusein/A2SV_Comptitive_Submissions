# Problem: Best Time to Buy and Sell Stock with Cooldown - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution:
        def maxProfit(self, prices: List[int]) -> int:    
            if len(prices) == 1:
                return 0
            dp = [[0 for i in range(len(prices) + 2)] for x in range(2)]
            dp[0][0] = -prices[0]#0 buy
            dp[0][1] = -min(prices[0], prices[1])
            for i in range(1, len(prices)):
                if i > 1:
                    dp[0][i] = max(-prices[i] + dp[1][i - 2], dp[0][i - 1])
                dp[1][i] = max(prices[i] + dp[0][i - 1], dp[1][i - 1])

            return dp[1][-3]