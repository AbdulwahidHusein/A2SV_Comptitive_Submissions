# Problem: Minimum Cost For Tickets - https://leetcode.com/problems/minimum-cost-for-tickets/

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        n = len(days)
        dp = {i: float('inf') for i in range(n)}
        dp[-1] = 0
        dp[0] = min(costs)
        for i in range(1, n):
            svn_back = one_back = th_back = i
            while svn_back >= 0 and days[i] - 7 < days[svn_back]:
                svn_back -= 1
            while th_back >= 0 and days[i] - 30 < days[th_back]:
                th_back -= 1
            dp[i] = min( dp[i-1] + costs[0], dp[svn_back] + costs[1], dp[th_back] + costs[2])
        return dp[n-1]
 
                
            
