class Solution:
    def totalMoney(self, n: int) -> int:
        ans = 0
        mondays = 1
        
        while n > 0:
            for day in range(min(n, 7)):
                ans += mondays + day
            n -= 7
            mondays += 1
        return ans