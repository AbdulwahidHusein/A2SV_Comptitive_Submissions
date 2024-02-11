class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.n=len(grid)
        self.m=len(grid[0])

        moves=[(1,-1),(1,0),(1,1)]
        memo=[[[-1 for _ in range(self.m)] for q_ in range(self.m)] for _ in range(self.n)]


        def dp(i,j,y):
            if j<0 or j>=self.m or i>=self.n or y<0 or y>=self.m or y==j:
                return 0

            if(grid[i][j]==-1 or grid[i][y]==-1):
                return 0

        
            if memo[i][j][y]!=-1:
                return memo[i][j][y]

            t1=grid[i][j]
            grid[i][j]=-1
            t2=grid[i][y]
            grid[i][y]=-1
            ans=0
            for p,q in moves:
                for s,t in moves:
                    ans=max(ans,dp(i+p,j+q,y+t)+t1+t2)
            grid[i][j]=t1
            grid[i][y]=t2

            memo[i][j][y]=ans
            

            return ans


        return dp(0,0,self.m-1)
            

        