# Problem: IPO - https://leetcode.com/problems/ipo/

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        can_work = []
        cant_work = []
        for i in range(n):
            if capital[i] > w:
                heappush(cant_work, (capital[i], profits[i]))
            else:
                heappush(can_work, -profits[i])
        budget = w
        while k and can_work:
            budget += -heappop(can_work)
            while cant_work and cant_work[0][0] <= budget:
                heappush(can_work, -heappop(cant_work)[1])
            k -= 1
            
        return budget 
