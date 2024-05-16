# Problem: Dungeon Game - https://leetcode.com/problems/dungeon-game/

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        rows, cols = len(dungeon), len(dungeon[0])
        dp = [[float('inf')] * (cols + 1) for _ in range(rows + 1)]

        dp[rows][cols-1] = dp[rows-1][cols] = 1 #to get started

        for i in range(rows-1, -1, -1):
            for j in range(cols-1, -1, -1):
                health_req = min(dp[i+1][j], dp[i][j+1]) - dungeon[i][j]
                dp[i][j] = max(1, health_req)

        return dp[0][0]