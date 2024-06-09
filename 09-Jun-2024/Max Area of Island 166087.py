# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs= [(0, 1), (1, 0), (-1, 0), (0, -1)]

        ans = 0
        def inbound(x, y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])
        def dfs(i, j):
            if grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            res = 1
            for dx, dy in dirs:
                x = i + dx
                y = j + dy
                if inbound(x, y):
                    res += dfs(x, y)
            return res
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i, j))
        return ans
