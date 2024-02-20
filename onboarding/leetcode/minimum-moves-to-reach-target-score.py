class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        oprs = 0
        while target > 1:
            if maxDoubles > 0 and target % 2 == 0:
                target //= 2
                maxDoubles -= 1
            elif maxDoubles == 0:
                return oprs + target - 1
            else:
                target -= 1   
            oprs += 1
        return oprs