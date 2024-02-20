class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        largest_rowi = [max(grid[i]) for i in range(n)]
        largest_coli = [0]* n
        for i in range(n):
            for j in range(n):
                largest_coli[j] = max(largest_coli[j], grid[i][j])
        #print(largest_coli)
        ans = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] < largest_rowi[i] and grid[i][j] < largest_coli[j]:
                    ans += min(largest_rowi[i],  largest_coli[j]) - grid[i][j]

        return ans