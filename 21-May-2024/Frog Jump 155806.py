# Problem: Frog Jump - https://leetcode.com/problems/frog-jump/

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        if stones[0] + 1 != stones[1]:
            return False
        n = len(stones)
        idx = defaultdict(lambda : -1)
        for i in range(n):
            idx[stones[i]] = i
        dp = defaultdict(bool)
        dp[(stones[0], 0)] = True
        dp[(stones[1], 1)] = True

        for i in range(1, n):
            for step in range(1, n+1):
                if dp[(stones[i]), step]:
                    if idx[stones[i] + step] != -1:
                        dp[(stones[i] + step, step)] = True
                    if idx[stones[i] + step+1] != -1:
                        dp[(stones[i] + step +1, step+1)] = True
                    if idx[stones[i] + step -1] != -1:
                        dp[(stones[i] + step - 1, step - 1)] = True
        res = False
        for i in range(n+1):
            res = res or dp[(stones[-1], i)]
        return res
                    


