class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        ice_creams = 0
        n = len(costs)
        i = 0
        while coins > 0 and i < n:
            if coins >= costs[i]:
                coins -= costs[i]
                ice_creams += 1
                i += 1
            else:
                break
        return ice_creams