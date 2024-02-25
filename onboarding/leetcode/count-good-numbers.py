class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod = (10**9+7)
        if n%2==0:
            val = n//2
        else:
            val=n//2+1
        even_ways = pow(5,val,10**9+7)
        odd_ways = pow(4,n-val,10**9+7)
        return (even_ways*odd_ways)%mod
        