class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:

        row = len(mat)
        col = len(mat[0])
        ans = [[] for i in range(row+col-1)]

        for x in range(row):
            for y in range(col):
                ans[x+y].append(mat[x][y])

        cands = [ans[i][::-1] if i%2==0 else ans[i] for i in range(len(ans))]
        res = []
        for row in cands:
            res.extend(row)
        return res