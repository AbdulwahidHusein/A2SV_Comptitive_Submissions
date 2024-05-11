# Problem: Best Time to Buy and Sell Stock with Transaction Fee - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        n = len(prices)
        buy = [0] * n
        sell = [0] * n
        buy[0] = -prices[0]

        for i in range (1, n):
            buy[i] = max(buy[i-1], sell[i-1] - prices[i])
            sell[i] = max(sell[i-1], buy[i-1] +prices[i] - fee )

        return max(buy[-1], sell[-1])