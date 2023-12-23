class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        ans = [0]*(52)

        for l, r in ranges:
            ans[l] += 1
            ans[r+1] -= 1
        for i in range(1, 52):
            ans[i] += ans[i-1]
        for j in range(left, right+1):
            if ans[j] < 1:
                return False
        return True