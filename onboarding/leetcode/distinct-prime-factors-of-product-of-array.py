class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        p = 1
        for n in nums:
            p *= n
        distnicts = set()
        d=2
        while d*d<p:
            while p%d==0:
                distnicts.add(d)
                p//=d
            d += 1
        if p>1:
            distnicts.add(p)
        return len(distnicts)
            