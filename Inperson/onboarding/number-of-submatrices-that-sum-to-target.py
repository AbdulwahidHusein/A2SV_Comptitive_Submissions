class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        row = len(matrix)
        col = len(matrix[0])

        pref_sum = [[0 for _ in range(col+1)] for _ in range(row+1)]

        for i in range(1, row+1):
            for j in range(1, col+1):
                pref_sum[i][j] = matrix[i-1][j-1] + pref_sum[i][j-1] + pref_sum[i-1][j] - pref_sum[i-1][j-1]

        ans = 0
        for i in range(row+1):
            for j in range(col+1):
                for k in range(i):
                    for z in range(j):
                        sub_sum = pref_sum[i][j] - pref_sum[i][z] - pref_sum[k][j] + pref_sum[k][z]
                        if sub_sum == target:
                            ans += 1
        return ans