class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        ans = -float("inf")
        for i in range(row-2):
            for j in range(col-2):
                up = grid[i][j] + grid[i][j+1] + grid[i][j+2]
                center = grid[i+1][j+1]
                down = grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2]
                ans = max(ans, up+center+down)
                
        return ans
