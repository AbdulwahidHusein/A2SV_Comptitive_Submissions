# Problem: Stone Game - https://leetcode.com/problems/stone-game/

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # return True
        # n = len(piles)
        # ps = [0]
        # rs = 0
        # for i in range(n):
        #     rs += piles[i]
        #     ps.append(rs)
        # memo = [[-1 for _ in range(n)] for _ in range(n)]

        # def game(i, j):
        #     if i == j:
        #         return piles[i]
        #     if i + 1 == j:
        #         return max(piles[i], piles[j])
        #     # if memo[i][j] != -1:
        #     #     return memo[i][j]
        #     left_sum = ps[j+1] - ps[i+1]
        #     right_sum = ps[j] - ps[i]

        #     return   max(
        #         piles[i] + right_sum - game(i+1, j), piles[j] + left_sum - game(i, j-1)
        #     )
        #     # return memo[i][j]

        # alice = game(0, n-1)
        # if alice > sum(piles) / 2:
        #     return True
        # return False
        n = len(piles)
        pref_sum = [0] * (n+1)
        for i in range(1, n+1):
            pref_sum[i] += piles[i-1] + pref_sum[i-1]
        memo = {}
        def game(i, j):
            if i == j:
                return piles[i]
            if i == j-1:
                return max(piles[i], piles[j])
            if (i,j) not in memo:
                memo[(i,j)] = max(
                piles[i] + pref_sum[j+1] - pref_sum[i+1] - game(i+1, j),
                piles[j] + pref_sum[j] - pref_sum[i] - game(i, j-1)
            )
            return memo[(i,j)]
        score =  game(0, n-1)
        if pref_sum[-1] / 2 < score:
            return True
        return False