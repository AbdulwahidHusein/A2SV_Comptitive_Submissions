class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        #condition 1 i nust be <= its order
        n = len(flips)
        ans = n
        curr = 1
        for i in range(1, n+1):
            curr = max(curr, flips[i-1])
            if curr > i:
                ans -= 1
        return ans