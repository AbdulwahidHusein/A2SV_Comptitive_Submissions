class Solution:
    def myPow(self, x: float, n: int) -> float:
        neg = False
        if n < 0:
            neg = True
        n = abs(n)
        def pow(x, n):
            if n == 1:
                return x
            if n == 0:
                return 1
            if n%2 == 0:
                return self.myPow(x*x, n//2)
            else:
                return self.myPow(x, n-1) * x
        if neg:
            return 1/pow(x, n)
        else:
            return pow(x, n)