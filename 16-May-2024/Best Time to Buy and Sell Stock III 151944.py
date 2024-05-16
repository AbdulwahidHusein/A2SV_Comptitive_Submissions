# Problem: Best Time to Buy and Sell Stock III - https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    if not prices:
        return 0

    buy1, buy2 = float('inf'), float('inf')
    sell1, sell2 = 0, 0

    for price in prices:
        buy1 = min(buy1, price)
        sell1 = max(sell1, price - buy1)
        buy2 = min(buy2, price - sell1)
        sell2 = max(sell2, price - buy2)
        #print(buy1, sell1, buy2, sell2)

    return sell2