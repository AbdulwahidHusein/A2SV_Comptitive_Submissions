class Solution:
    def hasGroupsSizeX(self, deck: List[int]) -> bool:
        c = Counter(deck)
        minc = min(c.values())
        for n in c:
            g = gcd(c[n], minc)
            if  g == 1:
                return False
            minc = g
        return True