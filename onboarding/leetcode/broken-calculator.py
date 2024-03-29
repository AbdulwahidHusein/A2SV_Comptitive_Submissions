class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        ans = 0
        def rec(s, e):
            nonlocal ans
            if s >= e:
                ans += s - e
                return
            ans += 1
            if e %2 == 0:
                rec(s, e//2)
            else:
                rec(s, e+1)
        rec(startValue, target)
        return ans