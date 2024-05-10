# Problem: Best Time to Buy and Sell Stock - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left =0
        right =1
        p = 0
        while right < len(prices):
            curp = prices[right] - prices[left] 

            if curp >0:
                p = max(curp, p) 
            else:
                left = right
            right += 1
        return p