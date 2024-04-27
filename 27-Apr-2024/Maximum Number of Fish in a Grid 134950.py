# Problem: Maximum Number of Fish in a Grid - https://leetcode.com/problems/maximum-number-of-fish-in-a-grid/

class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        dirs = [(0,1), (1, 0), (0, -1), (-1, 0)]
        def inbound(x,y):
            return 0 <= x < len(grid) and 0 <= y < len(grid[0])
        ans = 0
        def dfs(x,y):
            nonlocal ans
            if grid[x][y] == 0:
                return 0
            sp = grid[x][y]
            grid[x][y] = 0
            for dx, dy in dirs:
                nx = x+dx
                ny = y+dy
                if inbound(nx, ny):
                    sp += dfs(nx, ny)
            ans = max(ans, sp)
            return sp

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    dfs(i, j) 
        return ans