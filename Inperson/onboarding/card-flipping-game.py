from collections import defaultdict

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        n = len(backs)
        union = set(fronts) | set(backs)
        for i in range(n):
            if fronts[i] == backs[i]:
                if fronts[i] in union:
                    union.remove(fronts[i])
        if union:
            return min(union)
        return 0
        # ans = 2001
        # valids = set()
        # invalids = set()
        # for i in range(n):
        #     if fronts[i] == backs[i]:
        #         invalids.add(backs[i])
        #         if fronts[i] in valids:
        #             valids.remove(fronts[i])
        #         if valids:
        #             ans =  min(valids)
        #     else:
        #         valids.add(fronts[i])
        #         valids.add(backs[i])
        #         if not fronts[i] in invalids:
        #             ans = min(ans, fronts[i])
        #         if not backs[i] in invalids:
        #             ans = min(ans, backs[i])
        # if ans == 2001:
        #     return 0
        # return ans