class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        ps = [0]
        candles = []
        ans = []
        for i in range(n):
            if s[i] == "*":
                ps.append(ps[-1] + 1)
            else:
                candles.append(i)
                ps.append(ps[-1])
        for start, end in queries:
            l = bisect_left(candles, start)
            r = bisect_left(candles, end)
            if r==len(candles) or candles[r]!=end:
                r -= 1
            if l == len(candles) or start == end:
                ans.append(0)
                continue
            lidx = candles[l]
            ridx = candles[r]
            if ridx > lidx:
                ans.append(ps[ridx] - ps[lidx+1])
            else:
                ans.append(0)
        return ans
        


        