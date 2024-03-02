class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        r = range(1, n+1)
        ans = []
        def backtrack(curr, _sum, start):
            nonlocal ans, r
            if len(curr) > k:
                return
            if _sum == n and len(curr) == k:
                ans.append(curr[:])
                return
            if _sum > n:
                return
            for i in range(start, len(r)):
                if r[i] < 10:
                    curr.append(r[i])
                    _sum += r[i]
                    backtrack(curr, 
                    _sum, i+1)
                    curr.pop()
                    _sum -= r[i]
        backtrack([], 0, 0)
        return ans