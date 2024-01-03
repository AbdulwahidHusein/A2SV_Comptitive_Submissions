class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        count = 0
        ptr = 0
        for n in s:
            if ptr<len(g) and g[ptr] <= n:
                count += 1
                ptr += 1

        return count